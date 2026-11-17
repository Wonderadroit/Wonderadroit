"""Small, standard-library-only detector for synthetic authentication events.

This is an educational batch detector, not a production SIEM.
"""
from __future__ import annotations

import ipaddress
import json
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {"event_id", "timestamp", "source_ip", "username", "event_type"}
ALLOWED_EVENT_TYPES = {"authentication_failure", "authentication_success"}
DEFAULT_FAILURE_THRESHOLD = 5
DEFAULT_WINDOW_SECONDS = 600


def parse_event(raw: dict[str, Any], line_number: int) -> dict[str, Any]:
    """Validate and normalise one event. Invalid events raise ValueError."""
    if not isinstance(raw, dict):
        raise ValueError("event must be a JSON object")

    missing = REQUIRED_FIELDS - raw.keys()
    if missing:
        raise ValueError(f"missing required fields: {', '.join(sorted(missing))}")

    for field in ("event_id", "timestamp", "source_ip", "username", "event_type"):
        if not isinstance(raw[field], str) or not raw[field].strip():
            raise ValueError(f"{field} must be a non-empty string")

    event_type = raw["event_type"]
    if event_type not in ALLOWED_EVENT_TYPES:
        raise ValueError(f"unsupported event_type: {event_type}")

    try:
        source_ip = str(ipaddress.ip_address(raw["source_ip"]))
    except ValueError as exc:
        raise ValueError("source_ip must be a valid IPv4 or IPv6 address") from exc

    try:
        timestamp = datetime.fromisoformat(raw["timestamp"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp must be ISO 8601") from exc

    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")

    event = dict(raw)
    event["source_ip"] = source_ip
    event["username"] = raw["username"].strip()
    event["_time"] = timestamp.astimezone(timezone.utc)
    event["_line"] = line_number
    return event


def load_events(path: str | Path) -> tuple[list[dict[str, Any]], list[str], int]:
    """Load JSONL events, skipping malformed and duplicate event IDs.

    Returns (valid_events, diagnostics, duplicate_count). The first occurrence
    of an event_id is retained; later occurrences are treated as duplicates.
    """
    events: list[dict[str, Any]] = []
    diagnostics: list[str] = []
    seen_ids: set[str] = set()
    duplicate_count = 0

    with Path(path).open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                raw = json.loads(line)
                event = parse_event(raw, line_number)
                event_id = event["event_id"]
                if event_id in seen_ids:
                    duplicate_count += 1
                    diagnostics.append(
                        f"line {line_number}: duplicate event_id {event_id!r}; skipped"
                    )
                    continue
                seen_ids.add(event_id)
                events.append(event)
            except (json.JSONDecodeError, ValueError) as exc:
                diagnostics.append(f"line {line_number}: invalid event; skipped ({exc})")

    events.sort(key=lambda item: (item["_time"], item["_line"]))
    return events, diagnostics, duplicate_count


def detect(
    events: list[dict[str, Any]],
    failure_threshold: int = DEFAULT_FAILURE_THRESHOLD,
    window_seconds: int = DEFAULT_WINDOW_SECONDS,
) -> list[dict[str, Any]]:
    """Detect failure bursts followed by success for the same user and source IP."""
    if failure_threshold < 1:
        raise ValueError("failure_threshold must be at least 1")
    if window_seconds < 1:
        raise ValueError("window_seconds must be at least 1")

    failures: dict[tuple[str, str], deque[datetime]] = defaultdict(deque)
    brute_force_alerted: set[tuple[str, str]] = set()
    alerts: list[dict[str, Any]] = []

    ordered = sorted(events, key=lambda item: item["_time"])

    for event in ordered:
        key = (event["source_ip"], event["username"])
        event_time = event["_time"]
        recent_failures = failures[key]

        cutoff = event_time.timestamp() - window_seconds
        while recent_failures and recent_failures[0].timestamp() < cutoff:
            recent_failures.popleft()

        if event["event_type"] == "authentication_failure":
            recent_failures.append(event_time)
            if len(recent_failures) < failure_threshold:
                brute_force_alerted.discard(key)
            elif key not in brute_force_alerted:
                alerts.append(
                    {
                        "rule": "FRONTIER-AUTH-002",
                        "event_id": event["event_id"],
                        "source_ip": event["source_ip"],
                        "username": event["username"],
                        "failed_attempts": len(recent_failures),
                        "window_seconds": window_seconds,
                        "successful_login": False,
                        "timestamp": event["timestamp"],
                        "severity": "MEDIUM",
                    }
                )
                brute_force_alerted.add(key)
            continue

        if event["event_type"] == "authentication_success":
            if len(recent_failures) >= failure_threshold:
                alerts.append(
                    {
                        "rule": "FRONTIER-AUTH-001",
                        "event_id": event["event_id"],
                        "source_ip": event["source_ip"],
                        "username": event["username"],
                        "failed_attempts": len(recent_failures),
                        "window_seconds": window_seconds,
                        "successful_login": True,
                        "timestamp": event["timestamp"],
                        "severity": "HIGH",
                    }
                )
            # A successful authentication closes both correlation sequences.
            recent_failures.clear()
            brute_force_alerted.discard(key)

    return alerts


def main() -> int:
    log_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("events.jsonl")
    try:
        events, diagnostics, duplicate_count = load_events(log_path)
    except OSError as exc:
        print(f"Unable to read {log_path}: {exc}", file=sys.stderr)
        return 2

    alerts = detect(events)

    print(f"Valid events processed: {len(events)}")
    print(f"Duplicate events skipped: {duplicate_count}")
    print(f"Invalid records skipped: {len(diagnostics) - duplicate_count}")
    print(f"Alerts generated: {len(alerts)}")

    for diagnostic in diagnostics:
        print(f"INPUT WARNING: {diagnostic}")

    for alert in alerts:
        print("\nSECURITY ALERT")
        print(json.dumps(alert, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

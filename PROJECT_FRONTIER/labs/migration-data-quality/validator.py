"""Synthetic-only migration data quality validator (v0.2).

This module validates fictional event records against the Project Frontier
contract. It is not an operational immigration or identity system.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
import json
import re
from typing import Iterable

REQUIRED = {
    "record_id", "event_type", "event_at", "ingested_at", "source_system",
    "source_record_id", "origin_country", "destination_country", "transport_mode",
}
ALLOWED = REQUIRED
ID_RE = re.compile(r"^SYN-[A-Z0-9-]{1,60}$")
SOURCE_RECORD_ID_RE = re.compile(r"^SRC-[A-Z0-9-]{1,60}$")
COUNTRY_RE = re.compile(r"^[A-Z]{2}$")
RFC3339_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]+)?(?:Z|[+-][0-9]{2}:[0-9]{2})$")
# Deliberately bounded fixture allowlist; this is not a complete ISO registry.
COUNTRY_CODES = frozenset({
    "NG", "GH", "BJ", "NE", "CM", "GB", "US", "FR", "DE", "CA",
    "ZA", "KE", "SN", "CI", "TG", "TD", "SD", "LY", "MA", "EG",
})
EVENT_TYPES = {"entry", "exit", "transit"}
SOURCE_SYSTEMS = {"SYNTH-A", "SYNTH-B", "SYNTH-C"}
TRANSPORT_MODES = {"air", "land", "sea", "unknown"}
FUTURE_TOLERANCE = timedelta(hours=24)


def _timestamp(value: object) -> datetime | None:
    if not isinstance(value, str) or not RFC3339_RE.fullmatch(value):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def parse_rfc3339(value: object) -> datetime | None:
    """Parse an RFC 3339 timestamp with an explicit offset into UTC."""
    return _timestamp(value)


def _issue(issues: list[str], code: str) -> None:
    if code not in issues:
        issues.append(code)


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    """Reject duplicate JSON object keys instead of silently keeping the last value."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def _reject_nonfinite_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON numeric constant: {value}")


def _canonical(record: dict) -> str:
    """Canonicalise key order only; values remain lexically/structurally exact."""
    return json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def validate_records(
    lines: Iterable[str], reference_time: datetime
) -> tuple[list[dict], list[dict], dict]:
    """Return (accepted, diagnostics, summary) with deterministic ordering."""
    if reference_time.tzinfo is None or reference_time.utcoffset() is None:
        raise ValueError("reference_time must be timezone-aware")
    reference_utc = reference_time.astimezone(timezone.utc)

    parsed_rows: list[dict] = []
    diagnostics: list[dict] = []
    issue_counts: Counter[str] = Counter()
    missing_by_field: Counter[str] = Counter()
    object_record_count = 0
    ingestion_lags: list[float] = []
    for row_number, raw in enumerate(lines, start=1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw, object_pairs_hook=_unique_object,
                            parse_constant=_reject_nonfinite_constant)
        except (json.JSONDecodeError, TypeError, ValueError):
            diagnostics.append({"row_number": row_number, "record_id": None,
                                "issue_codes": ["MALFORMED_JSON"], "disposition": "rejected"})
            issue_counts["MALFORMED_JSON"] += 1
            continue
        if not isinstance(obj, dict):
            diagnostics.append({"row_number": row_number, "record_id": None,
                                "issue_codes": ["NON_OBJECT_RECORD"], "disposition": "rejected"})
            issue_counts["NON_OBJECT_RECORD"] += 1
            continue

        object_record_count += 1
        issues: list[str] = []
        missing = REQUIRED - obj.keys()
        extra = obj.keys() - ALLOWED
        if missing:
            _issue(issues, "MISSING_REQUIRED_FIELD")
        if extra:
            _issue(issues, "UNEXPECTED_FIELD")
        for key in REQUIRED:
            value = obj.get(key)
            if key not in obj or value is None or (isinstance(value, str) and not value.strip()):
                missing_by_field[key] += 1
                _issue(issues, "EMPTY_REQUIRED_FIELD")

        rid = obj.get("record_id")
        if not isinstance(rid, str) or not ID_RE.fullmatch(rid):
            _issue(issues, "INVALID_RECORD_ID")
        for key, allowed, issue_code in (
            ("event_type", EVENT_TYPES, "INVALID_EVENT_TYPE"),
            ("source_system", SOURCE_SYSTEMS, "INVALID_SOURCE_SYSTEM"),
            ("transport_mode", TRANSPORT_MODES, "INVALID_TRANSPORT_MODE"),
        ):
            if not isinstance(obj.get(key), str) or obj.get(key) not in allowed:
                _issue(issues, issue_code)

        for key in ("origin_country", "destination_country"):
            value = obj.get(key)
            if not isinstance(value, str) or not COUNTRY_RE.fullmatch(value) or value not in COUNTRY_CODES:
                _issue(issues, "INVALID_COUNTRY_CODE")
        if obj.get("origin_country") == obj.get("destination_country"):
            _issue(issues, "SAME_ORIGIN_DESTINATION")

        source_record_id = obj.get("source_record_id")
        if not isinstance(source_record_id, str) or not SOURCE_RECORD_ID_RE.fullmatch(source_record_id):
            _issue(issues, "INVALID_SOURCE_RECORD_ID")

        event_at = _timestamp(obj.get("event_at"))
        ingested_at = _timestamp(obj.get("ingested_at"))
        if event_at is None:
            _issue(issues, "INVALID_EVENT_TIMESTAMP")
        if ingested_at is None:
            _issue(issues, "INVALID_INGESTION_TIMESTAMP")
        if event_at is not None and ingested_at is not None:
            lag = (ingested_at - event_at).total_seconds()
            if lag < 0:
                _issue(issues, "INGESTION_BEFORE_EVENT")
            else:
                ingestion_lags.append(lag)
        if event_at is not None and event_at > reference_utc + FUTURE_TOLERANCE:
            _issue(issues, "EVENT_TOO_FAR_IN_FUTURE")

        parsed_rows.append({
            "row_number": row_number,
            "record": obj,
            "record_id": rid if isinstance(rid, str) and ID_RE.fullmatch(rid) else None,
            "issues": issues,
            "event_at_utc": event_at,
            "ingested_at_utc": ingested_at,
        })

    # Duplicate/provenance checks cover every parseable JSON object row,
    # including rows with other validation issues. See v0.2 metric definitions.
    by_id: dict[str, list[dict]] = defaultdict(list)
    by_source: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in parsed_rows:
        record = row["record"]
        if isinstance(row["record_id"], str) and ID_RE.fullmatch(row["record_id"]):
            by_id[row["record_id"]].append(row)
        source, source_id = record.get("source_system"), record.get("source_record_id")
        # A provenance collision is meaningful only when both linked record IDs
        # are valid synthetic identifiers; malformed IDs must not create a
        # duplicate-source alert against an otherwise valid record.
        if (row["record_id"] is not None
                and isinstance(source, str) and source in SOURCE_SYSTEMS
                and isinstance(source_id, str) and SOURCE_RECORD_ID_RE.fullmatch(source_id)):
            by_source[(source, source_id)].append(row)

    exact_duplicate_rows = 0
    conflict_groups = 0
    for group in by_id.values():
        if len(group) < 2:
            continue
        canonical = {_canonical(row["record"]) for row in group}
        if len(canonical) == 1:
            exact_duplicate_rows += len(group) - 1
            for row in group[1:]:
                _issue(row["issues"], "EXACT_DUPLICATE")
        else:
            conflict_groups += 1
            for row in group:
                _issue(row["issues"], "RECORD_ID_CONFLICT")

    for group in by_source.values():
        if len(group) > 1 and len({row["record_id"] for row in group}) > 1:
            for row in group:
                _issue(row["issues"], "DUPLICATE_SOURCE_REFERENCE")

    accepted: list[dict] = []
    for row in parsed_rows:
        issues = sorted(row["issues"])
        for code in issues:
            issue_counts[code] += 1
        disposition = "accepted" if not issues else "rejected"
        if disposition == "accepted":
            clean = dict(row["record"])
            clean["event_at"] = row["event_at_utc"].isoformat().replace("+00:00", "Z")
            clean["ingested_at"] = row["ingested_at_utc"].isoformat().replace("+00:00", "Z")
            accepted.append(clean)
        diagnostics.append({
            "row_number": row["row_number"],
            "record_id": row["record_id"],
            "issue_codes": issues,
            "disposition": disposition,
        })

    diagnostics.sort(key=lambda item: item["row_number"])
    summary = {
        "input_records": len(diagnostics),
        "accepted_records": len(accepted),
        "rejected_records": sum(d["disposition"] == "rejected" for d in diagnostics),
        "exact_duplicate_rows": exact_duplicate_rows,
        "record_id_conflict_groups": conflict_groups,
        "object_records_assessed": object_record_count,
        "missingness_by_field": {
            key: {"missing_count": missing_by_field[key],
                  "denominator": object_record_count,
                  "rate": (missing_by_field[key] / object_record_count if object_record_count else None)}
            for key in sorted(REQUIRED)
        },
        "ingestion_lag_seconds": {
            "count": len(ingestion_lags),
            "min": min(ingestion_lags) if ingestion_lags else None,
            "max": max(ingestion_lags) if ingestion_lags else None,
            "mean": (sum(ingestion_lags) / len(ingestion_lags) if ingestion_lags else None),
        },
        "issue_counts": dict(sorted(issue_counts.items())),
    }
    return accepted, diagnostics, summary

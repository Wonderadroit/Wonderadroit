import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from detector import detect, load_events


class AuthenticationDetectorTests(unittest.TestCase):
    def setUp(self):
        self.start = datetime(2026, 11, 17, 2, 0, tzinfo=timezone.utc)

    def event(self, event_id, offset_seconds, event_type,
              source_ip="192.0.2.10", username="admin"):
        timestamp = self.start + timedelta(seconds=offset_seconds)
        return {
            "event_id": event_id,
            "timestamp": timestamp.isoformat().replace("+00:00", "Z"),
            "source_ip": source_ip,
            "username": username,
            "event_type": event_type,
            "_time": timestamp,
        }

    def scenario(self, failures, success_offset, source_ip="192.0.2.10",
                 failure_username="admin", success_username="admin"):
        events = [
            self.event(
                f"fail-{index}", index * 30, "authentication_failure",
                source_ip, failure_username
            )
            for index in range(failures)
        ]
        events.append(
            self.event(
                "success", success_offset, "authentication_success",
                source_ip, success_username
            )
        )
        return events

    def test_five_failures_then_success_within_window_alerts(self):
        alerts = detect(self.scenario(5, 240))
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["failed_attempts"], 5)
        self.assertEqual(alerts[0]["rule"], "FRONTIER-AUTH-001")

    def test_three_failures_do_not_alert(self):
        self.assertEqual(len(detect(self.scenario(3, 240))), 0)

    def test_success_after_window_does_not_alert(self):
        self.assertEqual(len(detect(self.scenario(5, 900))), 0)

    def test_different_username_does_not_correlate(self):
        events = self.scenario(5, 240, failure_username="alice",
                               success_username="admin")
        self.assertEqual(len(detect(events)), 0)

    def test_different_source_ip_does_not_correlate(self):
        events = self.scenario(5, 240)
        events[-1]["source_ip"] = "192.0.2.11"
        self.assertEqual(len(detect(events)), 0)

    def test_out_of_order_events_are_sorted(self):
        events = list(reversed(self.scenario(5, 240)))
        self.assertEqual(len(detect(events)), 1)

    def test_exact_window_boundary_is_included(self):
        events = [
            self.event(f"fail-{i}", i * 30, "authentication_failure")
            for i in range(5)
        ]
        events.append(
            self.event("success", 600, "authentication_success")
        )
        self.assertEqual(len(detect(events)), 1)

    def test_success_closes_the_previous_failure_sequence(self):
        events = self.scenario(5, 240)
        events.extend([
            self.event("later-success", 300, "authentication_success")
        ])
        self.assertEqual(len(detect(events)), 1)

    def test_duplicate_event_ids_are_skipped(self):
        original = {
            "event_id": "same-id",
            "timestamp": "2026-11-17T02:00:00Z",
            "source_ip": "192.0.2.10",
            "username": "admin",
            "event_type": "authentication_failure",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text(
                json.dumps(original) + "\n" + json.dumps(original) + "\n",
                encoding="utf-8",
            )
            events, diagnostics, duplicate_count = load_events(path)

        self.assertEqual(len(events), 1)
        self.assertEqual(duplicate_count, 1)
        self.assertEqual(len(diagnostics), 1)

    def test_malformed_and_invalid_records_are_skipped(self):
        valid = {
            "event_id": "valid",
            "timestamp": "2026-11-17T02:00:00Z",
            "source_ip": "192.0.2.10",
            "username": "admin",
            "event_type": "authentication_failure",
        }
        invalid = dict(valid, event_id="invalid", source_ip="not-an-ip")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text(
                "{not-json}\n"
                + json.dumps(invalid) + "\n"
                + json.dumps(valid) + "\n",
                encoding="utf-8",
            )
            events, diagnostics, duplicate_count = load_events(path)

        self.assertEqual(len(events), 1)
        self.assertEqual(len(diagnostics), 2)
        self.assertEqual(duplicate_count, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

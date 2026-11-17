import json
import unittest
from datetime import datetime, timezone

from validator import validate_records


REFERENCE = datetime(2026, 11, 17, 12, 0, tzinfo=timezone.utc)


def record(**changes):
    value = {
        "record_id": "SYN-0001",
        "event_type": "entry",
        "event_at": "2026-11-16T10:00:00Z",
        "ingested_at": "2026-11-16T10:05:00+00:00",
        "source_system": "SYNTH-A",
        "source_record_id": "SRC-001",
        "origin_country": "GH",
        "destination_country": "NG",
        "transport_mode": "air",
    }
    value.update(changes)
    return value


def run_rows(*rows):
    return validate_records([json.dumps(row) for row in rows], REFERENCE)


class ValidatorTests(unittest.TestCase):
    def test_valid_record_accepted_and_timestamp_normalised(self):
        accepted, diagnostics, summary = run_rows(record())
        self.assertEqual(len(accepted), 1)
        self.assertEqual(accepted[0]["event_at"], "2026-11-16T10:00:00Z")
        self.assertEqual(diagnostics[0]["disposition"], "accepted")
        self.assertEqual(summary["accepted_records"], 1)

    def test_equivalent_offsets_are_valid(self):
        accepted, _, _ = run_rows(record(event_at="2026-11-16T11:00:00+01:00"))
        self.assertEqual(accepted[0]["event_at"], "2026-11-16T10:00:00Z")

    def test_missing_and_empty_fields_rejected(self):
        bad = record()
        del bad["source_record_id"]
        bad["source_system"] = " "
        _, diagnostics, _ = run_rows(bad)
        self.assertIn("MISSING_REQUIRED_FIELD", diagnostics[0]["issue_codes"])
        self.assertIn("EMPTY_REQUIRED_FIELD", diagnostics[0]["issue_codes"])

    def test_unexpected_field_rejected(self):
        _, diagnostics, _ = run_rows(record(extra_personal_data="must-not-be-accepted"))
        self.assertIn("UNEXPECTED_FIELD", diagnostics[0]["issue_codes"])

    def test_invalid_json_does_not_stop_later_rows(self):
        accepted, diagnostics, summary = validate_records(
            ['{"broken":', json.dumps(record(record_id="SYN-0002"))], REFERENCE
        )
        self.assertEqual(len(accepted), 1)
        self.assertEqual(diagnostics[0]["issue_codes"], ["MALFORMED_JSON"])
        self.assertEqual(summary["input_records"], 2)

    def test_non_object_json_rejected(self):
        _, diagnostics, _ = validate_records(["[]"], REFERENCE)
        self.assertEqual(diagnostics[0]["issue_codes"], ["NON_OBJECT_RECORD"])

    def test_naive_timestamp_rejected(self):
        _, diagnostics, _ = run_rows(record(event_at="2026-11-16T10:00:00"))
        self.assertIn("INVALID_EVENT_TIMESTAMP", diagnostics[0]["issue_codes"])

    def test_ingestion_before_event_rejected(self):
        _, diagnostics, _ = run_rows(record(ingested_at="2026-11-15T10:00:00Z"))
        self.assertIn("INGESTION_BEFORE_EVENT", diagnostics[0]["issue_codes"])

    def test_future_event_beyond_tolerance_rejected(self):
        _, diagnostics, _ = run_rows(record(event_at="2026-11-19T13:00:00Z"))
        self.assertIn("EVENT_TOO_FAR_IN_FUTURE", diagnostics[0]["issue_codes"])

    def test_same_country_rejected(self):
        _, diagnostics, _ = run_rows(record(destination_country="GH"))
        self.assertIn("SAME_ORIGIN_DESTINATION", diagnostics[0]["issue_codes"])

    def test_exact_duplicate_retains_first_only(self):
        accepted, diagnostics, summary = run_rows(record(), record())
        self.assertEqual(len(accepted), 1)
        self.assertEqual(diagnostics[1]["issue_codes"], ["EXACT_DUPLICATE"])
        self.assertEqual(summary["exact_duplicate_rows"], 1)

    def test_conflicting_duplicate_rejects_all_members(self):
        accepted, diagnostics, summary = run_rows(
            record(), record(transport_mode="land")
        )
        self.assertEqual(accepted, [])
        self.assertTrue(all("RECORD_ID_CONFLICT" in d["issue_codes"] for d in diagnostics))
        self.assertEqual(summary["record_id_conflict_groups"], 1)

    def test_duplicate_source_reference_across_record_ids(self):
        accepted, diagnostics, _ = run_rows(
            record(), record(record_id="SYN-0002")
        )
        self.assertEqual(accepted, [])
        self.assertTrue(all("DUPLICATE_SOURCE_REFERENCE" in d["issue_codes"] for d in diagnostics))

    def test_distinct_sources_do_not_collide(self):
        accepted, _, _ = run_rows(
            record(source_system="SYNTH-A"),
            record(record_id="SYN-0002", source_system="SYNTH-B"),
        )
        self.assertEqual(len(accepted), 2)

    def test_summary_reconciles(self):
        _, _, summary = run_rows(record(), record(record_id="SYN-0002", origin_country="NG"))
        self.assertEqual(summary["input_records"],
                         summary["accepted_records"] + summary["rejected_records"])

    def test_outputs_are_deterministic(self):
        lines = [json.dumps(record()), json.dumps(record(record_id="SYN-0002"))]
        first = validate_records(lines, REFERENCE)
        second = validate_records(lines, REFERENCE)
        self.assertEqual(first, second)

    def test_reference_time_must_be_aware(self):
        with self.assertRaises(ValueError):
            validate_records([json.dumps(record())], datetime(2026, 11, 17))

    def test_non_string_controlled_value_is_rejected_not_crashing(self):
        _, diagnostics, _ = run_rows(record(event_type=[]))
        self.assertIn("INVALID_EVENT_TYPE", diagnostics[0]["issue_codes"])

    def test_missingness_and_ingestion_lag_metrics_have_denominators(self):
        bad = record()
        del bad["source_record_id"]
        _, _, summary = run_rows(record(), bad)
        self.assertEqual(summary["object_records_assessed"], 2)
        self.assertEqual(summary["missingness_by_field"]["source_record_id"]["missing_count"], 1)
        self.assertEqual(summary["missingness_by_field"]["source_record_id"]["denominator"], 2)
        self.assertEqual(summary["ingestion_lag_seconds"]["count"], 2)
        self.assertEqual(summary["ingestion_lag_seconds"]["mean"], 300.0)

    def test_empty_input_has_unavailable_rates_and_lag_metrics(self):
        _, _, summary = validate_records([], REFERENCE)
        self.assertEqual(summary["input_records"], 0)
        self.assertIsNone(summary["missingness_by_field"]["record_id"]["rate"])
        self.assertIsNone(summary["ingestion_lag_seconds"]["mean"])


if __name__ == "__main__":
    unittest.main()

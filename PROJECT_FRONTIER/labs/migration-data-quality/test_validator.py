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

    def test_timestamp_must_use_rfc3339_separator_and_offset(self):
        _, diagnostics, _ = run_rows(record(event_at="2026-11-16 10:00:00+00:00"))
        self.assertIn("INVALID_EVENT_TIMESTAMP", diagnostics[0]["issue_codes"])

    def test_exact_future_tolerance_boundary_is_accepted(self):
        accepted, _, _ = run_rows(
            record(event_at="2026-11-18T12:00:00Z", ingested_at="2026-11-18T12:01:00Z")
        )
        self.assertEqual(len(accepted), 1)

    def test_invalid_record_id_is_not_echoed_in_diagnostics(self):
        _, diagnostics, _ = run_rows(record(record_id="user@example.invalid"))
        self.assertIsNone(diagnostics[0]["record_id"])

    def test_overlong_record_id_rejected_and_not_echoed(self):
        _, diagnostics, _ = run_rows(record(record_id="SYN-" + "A" * 61))
        self.assertIn("INVALID_RECORD_ID", diagnostics[0]["issue_codes"])
        self.assertIsNone(diagnostics[0]["record_id"])

    def test_unknown_two_letter_country_code_rejected(self):
        _, diagnostics, _ = run_rows(record(origin_country="ZZ"))
        self.assertIn("INVALID_COUNTRY_CODE", diagnostics[0]["issue_codes"])


    def test_null_empty_and_whitespace_for_every_required_field(self):
        for field in sorted(record()):
            for value in (None, "", "   "):
                with self.subTest(field=field, value=value):
                    _, diagnostics, _ = run_rows(record(**{field: value}))
                    self.assertIn("EMPTY_REQUIRED_FIELD", diagnostics[0]["issue_codes"])

    def test_each_controlled_vocabulary_rejects_unknown_string(self):
        cases = {"event_type": "arrival", "source_system": "REAL-SYSTEM",
                 "transport_mode": "rail"}
        expected = {"event_type": "INVALID_EVENT_TYPE",
                    "source_system": "INVALID_SOURCE_SYSTEM",
                    "transport_mode": "INVALID_TRANSPORT_MODE"}
        for field, value in cases.items():
            with self.subTest(field=field):
                _, diagnostics, _ = run_rows(record(**{field: value}))
                self.assertIn(expected[field], diagnostics[0]["issue_codes"])

    def test_lowercase_and_malformed_country_codes_rejected(self):
        for value in ("ng", "NGA", "N1", "ZZ"):
            with self.subTest(value=value):
                _, diagnostics, _ = run_rows(record(origin_country=value))
                self.assertIn("INVALID_COUNTRY_CODE", diagnostics[0]["issue_codes"])

    def test_source_record_id_length_boundaries(self):
        for length, expected_count in ((1, 1), (64, 1), (0, 0), (65, 0)):
            with self.subTest(length=length):
                accepted, diagnostics, _ = run_rows(record(source_record_id="S" * length))
                self.assertEqual(len(accepted), expected_count)
                if expected_count == 0:
                    self.assertIn("INVALID_SOURCE_RECORD_ID", diagnostics[0]["issue_codes"])

    def test_distinct_valid_rows_preserve_input_order(self):
        rows = [record(record_id=f"SYN-{i:04d}", source_record_id=f"SRC-{i:04d}") for i in (2, 1, 3)]
        accepted, diagnostics, _ = run_rows(*rows)
        self.assertEqual([r["record_id"] for r in accepted], ["SYN-0002", "SYN-0001", "SYN-0003"])
        self.assertEqual([d["row_number"] for d in diagnostics], [1, 2, 3])

    def test_conflicting_duplicate_is_rejected_under_both_input_orders(self):
        first = record(transport_mode="air")
        second = record(transport_mode="land")
        for rows in ((first, second), (second, first)):
            with self.subTest(order=rows[0]["transport_mode"]):
                accepted, diagnostics, summary = run_rows(*rows)
                self.assertEqual(accepted, [])
                self.assertTrue(all("RECORD_ID_CONFLICT" in d["issue_codes"] for d in diagnostics))
                self.assertEqual(summary["record_id_conflict_groups"], 1)

    def test_issue_count_keys_are_sorted(self):
        _, _, summary = run_rows(record(destination_country="GH"), record(event_at="bad"))
        keys = list(summary["issue_counts"])
        self.assertEqual(keys, sorted(keys))

    def test_reference_time_changes_future_validity(self):
        future = record(event_at="2026-11-18T00:01:00Z", ingested_at="2026-11-18T00:02:00Z")
        early = datetime(2026, 11, 17, 0, 0, tzinfo=timezone.utc)
        late = datetime(2026, 11, 19, 0, 0, tzinfo=timezone.utc)
        _, early_diag, _ = validate_records([json.dumps(future)], early)
        accepted, late_diag, _ = validate_records([json.dumps(future)], late)
        self.assertIn("EVENT_TOO_FAR_IN_FUTURE", early_diag[0]["issue_codes"])
        self.assertNotIn("EVENT_TOO_FAR_IN_FUTURE", late_diag[0]["issue_codes"])
        self.assertEqual(len(accepted), 1)


    def test_duplicate_json_object_keys_are_rejected(self):
        raw = '{"record_id":"SYN-0001","record_id":"SYN-0002"}'
        _, diagnostics, _ = validate_records([raw], REFERENCE)
        self.assertEqual(diagnostics[0]["issue_codes"], ["MALFORMED_JSON"])

    def test_nonstandard_json_numeric_constant_is_rejected(self):
        raw = '{"record_id":"SYN-0001","event_type":NaN}'
        _, diagnostics, _ = validate_records([raw], REFERENCE)
        self.assertEqual(diagnostics[0]["issue_codes"], ["MALFORMED_JSON"])


if __name__ == "__main__":
    unittest.main()

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from run_lab import load_input, main


class InputReaderTests(unittest.TestCase):
    def test_invalid_utf8_is_rejected_without_repair(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.jsonl"
            path.write_bytes(b'{"record_id":"SYN-1"}' + bytes([255]))
            with self.assertRaises(UnicodeDecodeError):
                load_input(path)


class CliTests(unittest.TestCase):
    def invoke(self, input_path, output_dir, reference="2026-11-17T12:00:00Z"):
        stdout = io.StringIO()
        with patch("sys.argv", ["run_lab.py", "--input", str(input_path),
                                "--output-dir", str(output_dir),
                                "--reference-time", reference]):
            with contextlib.redirect_stdout(stdout):
                code = main()
        return code, stdout.getvalue()

    def test_empty_input_creates_empty_outputs_and_null_metrics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "empty.jsonl"
            source.write_text("", encoding="utf-8")
            output = root / "out"
            code, _ = self.invoke(source, output)
            self.assertEqual(code, 0)
            self.assertEqual((output / "accepted.jsonl").read_text(), "")
            self.assertEqual((output / "diagnostics.jsonl").read_text(), "")
            summary = json.loads((output / "summary.json").read_text())
            self.assertEqual(summary["input_records"], 0)
            self.assertIsNone(summary["ingestion_lag_seconds"]["mean"])

    def test_invalid_reference_time_fails_without_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.jsonl"
            source.write_text("", encoding="utf-8")
            output = root / "out"
            with self.assertRaises(SystemExit) as error:
                self.invoke(source, output, "2026-11-17T12:00:00")
            self.assertEqual(error.exception.code, 2)
            self.assertFalse(output.exists())

    def test_console_prints_aggregate_only_not_record_identifiers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.jsonl"
            record = {
                "record_id": "SYN-PRIVATE-MARKER",
                "event_type": "entry",
                "event_at": "2026-11-16T10:00:00Z",
                "ingested_at": "2026-11-16T10:05:00Z",
                "source_system": "SYNTH-A",
                "source_record_id": "SRC-001",
                "origin_country": "GH",
                "destination_country": "NG",
                "transport_mode": "air",
            }
            source.write_text(json.dumps(record) + chr(10), encoding="utf-8")
            _, stdout = self.invoke(source, root / "out")
            self.assertNotIn("SYN-PRIVATE-MARKER", stdout)
            self.assertIn('"input_records": 1', stdout)

    def test_cli_outputs_are_byte_for_byte_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.jsonl"
            source.write_text(json.dumps({
                "record_id": "SYN-0001", "event_type": "entry",
                "event_at": "2026-11-16T10:00:00Z",
                "ingested_at": "2026-11-16T10:05:00Z",
                "source_system": "SYNTH-A", "source_record_id": "SRC-001",
                "origin_country": "GH", "destination_country": "NG",
                "transport_mode": "air"
            }) + chr(10), encoding="utf-8")
            first, second = root / "first", root / "second"
            self.invoke(source, first)
            self.invoke(source, second)
            for name in ("accepted.jsonl", "diagnostics.jsonl", "summary.json"):
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())


if __name__ == "__main__":
    unittest.main()

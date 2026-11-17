import tempfile
import unittest
from pathlib import Path

from run_lab import load_input


class InputReaderTests(unittest.TestCase):
    def test_invalid_utf8_is_rejected_without_repair(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.jsonl"
            path.write_bytes(b'{"record_id":"SYN-1"}\xff')
            with self.assertRaises(UnicodeDecodeError):
                load_input(path)


if __name__ == "__main__":
    unittest.main()

"""Command-line runner for the synthetic-only migration data quality lab."""
import argparse
from datetime import datetime
import json
from pathlib import Path

from validator import validate_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Synthetic JSONL input")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--reference-time", required=True,
                        help="Fixed RFC3339 timestamp with explicit UTC offset")
    args = parser.parse_args()

    try:
        reference_time = datetime.fromisoformat(args.reference_time.replace("Z", "+00:00"))
        if reference_time.tzinfo is None or reference_time.utcoffset() is None:
            raise ValueError("reference time must include an explicit UTC offset")
        raw_text = args.input.read_bytes().decode("utf-8", errors="strict")
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        parser.error(str(exc))

    accepted, diagnostics, summary = validate_records(raw_text.splitlines(), reference_time)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "accepted.jsonl": "".join(json.dumps(row, sort_keys=True) + "\n" for row in accepted),
        "diagnostics.jsonl": "".join(json.dumps(row, sort_keys=True) + "\n" for row in diagnostics),
        "summary.json": json.dumps(summary, indent=2, sort_keys=True) + "\n",
    }
    for name, content in outputs.items():
        (args.output_dir / name).write_text(content, encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Migration Data Quality Laboratory

A small Python-standard-library demonstration for validating **fictional** migration-event records against the Project Frontier **v0.2** data contract.

## Scope

This is a data-quality teaching lab, not an immigration product, operational border system, migration statistics source, identity verifier or risk-scoring tool. It accepts no personal identity fields and uses no real traveller, passport, NIN, biometric, personnel or government operational data.

## Current version and documents

The current implementation and regression suite are v0.2:
- [Data Contract v0.2](DATA_CONTRACT_v0.2.md)
- [Test Plan v0.2](TEST_PLAN_v0.2.md)
- [Independent Review Request](REVIEW_REQUEST.md)

The unversioned `DATA_CONTRACT.md` and `TEST_PLAN.md` are retained as historical v0.1 documents; they do not describe every v0.2 rule.

## Run

From this directory, using Python 3.11 or newer:

```sh
python -m unittest discover -v
python run_lab.py --input fixtures/synthetic_events.jsonl --output-dir build --reference-time 2026-11-17T12:00:00Z
```

The runner writes:
- `accepted.jsonl`: records passing all hard checks;
- `diagnostics.jsonl`: one disposition and stable issue codes per non-empty input line;
- `summary.json`: aggregate counts and issue frequencies.

Outputs are deterministic for the same input and explicit reference time. The sample fixture is intentionally small and includes an exact duplicate and an invalid same-country record.

## Important limitations

- The country-code allowlist is deliberately small and fixture-oriented; it is not a complete or authoritative ISO registry.
- Passing validation means only that a record conforms to this narrow synthetic contract. It does not prove that an event happened, that data is truthful, or that a dataset is representative.
- Ingestion lag and other metrics must not be interpreted as operational performance without validated context.
- No fuzzy matching, person resolution, enforcement inference, external network calls or live data integrations are implemented.
- Invalid UTF-8 input is rejected at the file-reader boundary; it is not silently repaired.
- The `source_record_id` token pattern is a format constraint, not proof that a record is synthetic. Only generated fictional fixtures may be used.

The v0.2 implementation passed 45 regression tests and its synthetic CLI fixture in GitHub Actions run 44176377842 on Python 3.12. This validates only the tested cases, not production readiness or real-world data quality. Independent human review remains outstanding.

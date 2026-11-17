# Migration Data Quality Laboratory — Test Plan v0.2

**Status:** The first v0.2 CI run (44175844227) passed the carried-forward 41-test suite, but it ran before the three new v0.2 regression methods were committed. The latest three-test additions are awaiting their own CI result. Independent review remains open.

## Test philosophy

Tests establish deterministic contract behaviour before any dashboard or analytical interpretation. Every fixture is fictional. Tests use a fixed reference timestamp and assert dispositions and stable issue codes.

## Carried-forward v0.1 coverage

The previous suite had 41 passing tests in run 44174686867. It covers valid acceptance, UTC normalisation, strict RFC 3339 parsing, required fields, unexpected fields, malformed and non-object JSON, duplicate JSON keys, non-standard numeric constants, controlled vocabularies, country-code rules, timestamp ordering/future tolerance, duplicate/conflict behaviour, deterministic outputs, metrics, invalid UTF-8 and CLI behaviour.

## v0.2 regression additions

- `source_record_id` must match `SRC-[A-Z0-9-]{1,60}`; email-like, phone-like, whitespace-padded, lowercase and non-ASCII lookalike values are rejected.
- Synthetic source identifier minimum and maximum lengths are tested.
- Exact duplicate comparison canonicalises object-key order only; equivalent timestamp instants expressed with different offsets are conflicting payloads when they share a record ID.
- Duplicate/conflict checks include all parseable JSON object rows, including rows with other validation defects.
- Metric denominators and duplicate counts are defined in DATA_CONTRACT_v0.2.md.

## Independent review still required

A reviewer should inspect:
1. Whether the source identifier pattern meaningfully enforces the synthetic-only boundary.
2. Duplicate grouping and first-seen exact-duplicate policy.
3. RFC 3339 parsing and explicit reference-time boundary.
4. Missingness and ingestion-lag denominators.
5. Privacy-minimised diagnostics and unexpected-field rejection.
6. Contract/documentation consistency and output reproducibility.
7. Policy-source interpretation in the research brief.

A successful workflow establishes only the listed synthetic contract cases. It does not establish real-world data accuracy, truth, representativeness or operational suitability. Independent review remains a separate gate.

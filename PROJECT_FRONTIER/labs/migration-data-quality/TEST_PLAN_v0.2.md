# Migration Data Quality Laboratory — Test Plan v0.2

**Status:** Automated v0.2 regression and fixture gate passed. GitHub Actions run **44176377842**, commit `c13c1f85fe677227e194f9ee18968d37ca3de653`, Python 3.12: **45 tests passed** and the synthetic CLI fixture completed successfully. Independent review remains open.

## Test philosophy

Tests establish deterministic contract behaviour before any dashboard or analytical interpretation. Every fixture is fictional. Tests use a fixed reference timestamp and assert dispositions and stable issue codes.

## Coverage

The 45-test suite covers:
- Valid record acceptance and UTC timestamp normalisation.
- Strict RFC 3339 shape, explicit offsets, ASCII digits and future-time boundary behaviour.
- Required-field completeness, unexpected fields and controlled vocabularies.
- Malformed/non-object JSON, duplicate JSON object keys and non-standard numeric constants.
- Country-code fixture allowlist and origin/destination consistency.
- Synthetic record and source-record identifier format and boundaries.
- Exact duplicates, conflicting record IDs, both input orders and duplicate source references.
- Equivalent timestamp instants expressed with different offsets are classified as conflicting payloads under the lexical duplicate policy.
- Duplicate/conflict grouping includes parseable JSON objects with other validation defects.
- Invalid record IDs do not create duplicate-source-reference findings against otherwise valid records.
- Missingness and ingestion-lag denominators, summary reconciliation and empty-input null metrics.
- Deterministic output ordering and explicit reference-time handling.
- Privacy-minimised diagnostics and invalid UTF-8 handling at the CLI reader boundary.

## v0.2 decisions

- `source_record_id` must match `SRC-[A-Z0-9-]{1,60}`; free text, email-like, phone-like, whitespace-padded, lowercase and non-ASCII lookalike values are rejected. This is a format constraint, not cryptographic proof of synthetic origin; only repository-generated fixtures are permitted.
- Exact duplicate comparison canonicalises object-key ordering only. Timestamp strings are not semantically normalised before comparison.
- Duplicate/conflict checks include parseable JSON object rows even when they have other validation defects.
- Provenance collision checks are limited to rows with valid synthetic record IDs and valid synthetic source references.
- Metric denominators and duplicate counts are defined in `DATA_CONTRACT_v0.2.md`.

## Independent review still required

A reviewer should inspect:
1. Whether the source identifier convention and fixture-generation controls are adequate for the synthetic-only boundary.
2. Duplicate grouping and first-seen exact-duplicate policy.
3. RFC 3339 parsing and explicit reference-time boundary.
4. Missingness and ingestion-lag denominators.
5. Privacy-minimised diagnostics and unexpected-field rejection.
6. Contract/documentation consistency and output reproducibility.
7. Policy-source interpretation in the research brief.

A successful workflow establishes only the listed synthetic contract cases. It does not establish real-world data accuracy, truth, representativeness or operational suitability. Independent review remains a separate gate.

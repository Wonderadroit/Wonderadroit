# Migration Data Quality Laboratory — Test Plan v0.1

**Status:** Partial executable coverage; remaining cases are explicitly deferred below.

## Test philosophy

Tests establish deterministic contract behaviour before any dashboard or analytical interpretation. Every fixture is fictional. Tests use a fixed reference timestamp and assert dispositions and stable issue codes.

## Implemented coverage (26 passing tests)

- Valid record acceptance and UTC timestamp normalisation.
- Equivalent timestamp offsets and strict RFC 3339 syntax.
- Missing required field, whitespace-only required value and unexpected field.
- Invalid JSON continuation and non-object JSON.
- Invalid, overlong and privacy-minimised record identifiers.
- Non-string controlled values are rejected without crashing.
- Unknown country code and same-origin/destination rejection.
- Naive timestamp, ingestion-before-event and future-tolerance rejection; exact future boundary acceptance.
- Exact duplicate retention, conflicting record-ID groups and duplicate source provenance.
- Distinct source systems do not collide.
- Summary reconciliation, field missingness denominators, ingestion-lag metrics and empty-input null metrics.
- Deterministic repeated validation.
- Invalid UTF-8 rejected at the file-reader boundary.

Latest evidence: GitHub Actions run 44172650451, Python 3.12, 26 tests passed; the synthetic CLI fixture also completed.

## Deferred coverage

The following items remain open before calling the v0.1 test plan fully satisfied:

1. Explicit null, empty-string and whitespace-only cases for every required field (current suite samples representative cases).
2. Unsupported string values for each controlled vocabulary independently.
3. Lowercase and malformed country-code variants.
4. Source-record identifier lower/upper length boundaries.
5. Multiple distinct valid rows preserve input order in both accepted and diagnostics outputs.
6. Exact duplicate classification under permutations of input order.
7. Summary issue-count ordering and byte-for-byte CLI output determinism across separate executions.
8. CLI output-file behaviour for empty input and invalid reference-time strings.
9. Console output contains only aggregate summary and never a full input record.
10. Explicit change-of-reference-time test proving only time-dependent outcomes change.

## Acceptance gate

The first prototype is implemented and has a passing CI suite, but this plan is not fully closed until deferred coverage is addressed and an independent review checks duplicate semantics, timestamp parsing, denominator arithmetic and privacy boundaries.

A green workflow alone does not establish real-world data accuracy or operational suitability.

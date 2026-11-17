# Migration Data Quality Laboratory — Test Plan v0.1

**Status:** Executable regression coverage complete for the documented v0.1 acceptance cases; independent review remains open.

## Test philosophy

Tests establish deterministic contract behaviour before any dashboard or analytical interpretation. Every fixture is fictional. Tests use a fixed reference timestamp and assert dispositions and stable issue codes.

## Implemented coverage (38 passing tests)

- Valid record acceptance and UTC timestamp normalisation.
- Equivalent timestamp offsets and strict RFC 3339 syntax.
- Null, empty-string and whitespace-only values for every required field.
- Missing required fields and unexpected fields.
- Invalid JSON continuation and non-object JSON.
- Invalid, overlong and privacy-minimised record identifiers.
- Each controlled vocabulary independently rejects unsupported values and non-string values do not crash validation.
- Unknown, lowercase and malformed country-code values; same-origin/destination rejection.
- Source-record identifier lower and upper length boundaries.
- Naive timestamps, ingestion-before-event, future-tolerance rejection and exact future boundary acceptance.
- Exact duplicate retention, conflicting record-ID groups under both input orders and duplicate source provenance.
- Distinct source systems do not collide; distinct valid records preserve input order.
- Summary reconciliation, sorted issue-code keys, field missingness denominators, ingestion-lag metrics and empty-input null metrics.
- Deterministic repeated validation and byte-for-byte CLI output determinism using a valid synthetic record.
- Invalid UTF-8 rejected at the file-reader boundary.
- Empty-input CLI output, invalid reference-time rejection, aggregate-only console output and reference-time-dependent future validation.

Latest evidence: GitHub Actions run 44173904566, Python 3.12, 38 tests passed; synthetic CLI fixture completed successfully.

## Independent review still required

The executable v0.1 cases are covered, but the lab is not approved as production software. A reviewer should inspect:
1. Duplicate grouping and first-seen exact-duplicate policy.
2. RFC 3339 parsing and the explicit reference-time boundary.
3. Missingness and ingestion-lag denominators.
4. Privacy-minimised diagnostics and unexpected-field rejection.
5. Contract/documentation consistency and output reproducibility.

## Acceptance gate

The v0.1 implementation/test gate is satisfied for the listed synthetic contract cases. The independent-review gate remains open. Any material schema or semantic change requires a version increment and new tests.

A green workflow does not establish real-world data accuracy, truth, representativeness or operational suitability.

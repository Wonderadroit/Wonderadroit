# Migration Data Quality Laboratory — Test Plan v0.1

**Status:** Test design; no implementation claim.

## Test philosophy

Tests must establish deterministic contract behaviour before any dashboard or analytical interpretation. Every fixture is fictional. Each test uses a fixed reference timestamp and asserts both disposition and stable issue code(s).

## Required positive cases

1. A fully conforming record is accepted and UTC-normalised.
2. Equivalent timestamps with different explicit offsets compare as the same instant.
3. Multiple distinct valid records preserve input order in outputs.
4. An event within the allowed 24-hour future tolerance is handled according to the declared boundary.

## Required negative cases

1. Missing required field.
2. Null, empty and whitespace-only required values.
3. Unexpected field.
4. Invalid JSON line while later valid lines continue processing.
5. Invalid record ID pattern and overlong identifier.
6. Unsupported event type, source label or transport mode.
7. Lowercase, malformed and unknown country code.
8. Naive timestamp without offset.
9. Malformed timestamp.
10. Ingestion timestamp earlier than event timestamp.
11. Event beyond the explicit future tolerance.
12. Origin and destination country are equal.
13. Non-object JSON value.
14. Invalid UTF-8 handling is explicit and tested at the file-reader boundary.

## Duplicate and provenance cases

1. Repeated record ID with identical canonical payload: first retained, later rows marked exact duplicate.
2. Repeated record ID with differing payload: every member of the group is marked conflict; none is accepted.
3. Same source provenance key with different record IDs: duplicate-source-reference issue is emitted.
4. Same source record ID from different source systems is not treated as a collision.
5. Duplicate classification is independent of input ordering except for the documented first-row retention rule for exact duplicates.

## Metrics and determinism cases

1. Summary totals reconcile: input rows = accepted + rejected/dispositioned rows, with duplicate/conflict categories explicitly accounted for.
2. Missingness rates use the correct denominator.
3. Empty input produces valid empty outputs and null/unavailable rates where appropriate.
4. Re-running the same input with the same reference time produces byte-identical outputs.
5. Changing only the reference time changes only time-dependent outcomes.
6. Issue counts are stable and sorted deterministically.
7. No full input record or unexpected field value is written to routine console output.

## Acceptance gate

Implementation is not complete until:
- every test above has an executable assertion;
- CI runs the suite successfully on the documented Python version;
- fixture outputs are manually inspected;
- a second review checks duplicate semantics, time handling, denominator arithmetic and privacy boundaries;
- the README documents limitations and reproducible commands.

A green workflow alone does not establish real-world data accuracy or operational suitability.

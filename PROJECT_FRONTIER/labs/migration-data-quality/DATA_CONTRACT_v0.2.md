# Migration Data Quality Laboratory — Data Contract v0.2

**Status:** v0.2 implementation candidate; automated verification and independent-review gates remain open.  
**Data classification:** Synthetic demonstration data only.

## Safety and scope

This is an educational data-quality exercise, not an NIS system, operational border tool, migration-statistics source or risk-scoring product. Every record and identifier must be fictional and generated for this repository. No personal identity, traveller, government, immigration or border operational data is permitted. No live integrations or testing of government/third-party systems.

One row represents one fictional movement-event record, not a verified person.

## Record model

| Field | Type | Required | Rule |
|---|---|---:|---|
| record_id | string | yes | Synthetic stable ID; `SYN-[A-Z0-9-]{1,60}` |
| event_type | string | yes | `entry`, `exit`, or `transit` |
| event_at | string | yes | RFC 3339 timestamp with explicit UTC offset; normalise to UTC |
| ingested_at | string | yes | RFC 3339 timestamp with explicit UTC offset; normalise to UTC |
| source_system | string | yes | `SYNTH-A`, `SYNTH-B`, or `SYNTH-C` |
| source_record_id | string | yes | Synthetic token only; `SRC-[A-Z0-9-]{1,60}`; no whitespace or free text |
| origin_country | string | yes | Uppercase code from the deliberately limited fixture allowlist |
| destination_country | string | yes | Uppercase code from the deliberately limited fixture allowlist |
| transport_mode | string | yes | `air`, `land`, `sea`, or `unknown` |

No other fields are accepted. Unknown fields are rejected.

## Validation semantics

- Required fields must exist and must not be null, empty or whitespace-only.
- Timestamps require RFC 3339 syntax, an explicit offset and ASCII digits. They are normalised to UTC in accepted output.
- `ingested_at < event_at` is rejected.
- Events more than 24 hours after the explicit caller-supplied reference time are rejected.
- The country-code allowlist is intentionally small and is not a complete or authoritative ISO registry.
- The validator rejects malformed JSON, duplicate JSON object keys, non-standard numeric constants, non-object JSON and invalid UTF-8 at the reader boundary.
- Diagnostics contain row number, a record ID only when it matches the synthetic ID pattern, issue codes and disposition; raw payloads are not copied.

## Duplicate policy

- Exact duplicate means equality of all parsed JSON field values after object-key ordering is canonicalised.
- Timestamp strings are not semantically normalised before duplicate comparison. Equivalent instants written with different offsets are different payloads and therefore conflict when they share a record ID.
- Same record ID and identical canonical payload: retain the first row; later rows receive `EXACT_DUPLICATE`.
- Same record ID with different canonical payloads: all rows in the group receive `RECORD_ID_CONFLICT`; no winner is selected.
- Same valid `(source_system, source_record_id)` attached to different valid record IDs receives `DUPLICATE_SOURCE_REFERENCE`.
- Duplicate/conflict grouping runs over all parseable JSON object rows, even when they have other validation defects. This is a diagnostic classification, not a claim that those rows are valid.
- Invalid rows remain in diagnostics and are excluded from clean output. No fuzzy matching or probabilistic entity resolution.

## Metrics

- `input_records`: all non-empty input lines receiving a disposition, including malformed and non-object lines.
- `object_records_assessed`: parseable JSON objects; denominator for each field-missingness metric.
- `issue_counts`: issue occurrences across parseable objects plus malformed/non-object line-level issues. Duplicate/conflict counts include parseable objects with other validation defects.
- `record_id_conflict_groups`: groups, not rows.
- `exact_duplicate_rows`: later rows dropped under first-seen retention.
- Ingestion lag includes parseable timestamp pairs with non-negative lag, even if other row checks fail; its count is the denominator.
- A zero denominator produces null/unavailable, not zero.

A high pass rate does not prove truth, real-world completeness, representativeness or suitability for operational decisions. The pipeline validates conformance to this narrow synthetic contract only.

## Implementation constraints

Python standard library only; JSONL; UTF-8; deterministic output; fixed explicit reference time; no network calls, external services, databases or secrets. Do not log or print entire records.

## Versioning

v0.2 tightens source-local identifier constraints and explicitly defines duplicate and metric semantics. Future schema or semantic changes require a version increment and regression tests. Sensitive fields, biometrics, person-level matching and operational integrations are out of scope and require separate safety review.

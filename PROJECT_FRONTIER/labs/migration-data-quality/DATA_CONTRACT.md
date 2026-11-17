# Migration Data Quality Laboratory — Data Contract v0.1

**Status:** v0.1 prototype implemented; test and independent-review gates remain open.  
**Data classification:** Synthetic demonstration data only.

## 1. Research question

Can a small, reproducible validation pipeline identify common completeness, validity, consistency, uniqueness, timeliness and provenance defects in fictional migration-event records without collecting or inferring personal identity?

This lab is an educational data-quality exercise. It is not an NIS system, operational border tool, migration-statistics source or risk-scoring product.

## 2. Safety boundary

- Every record and identifier must be fictional and generated for this repository.
- No names, dates of birth, passport numbers, NINs, visa numbers, biometrics, phone numbers, addresses, personnel identifiers or free-text notes.
- No real traveller-level, government, immigration or border operational data.
- No person-level risk score, watchlist, enforcement recommendation or prediction.
- Do not connect to NIS, government or third-party systems.
- Do not publish operational routes, facility details or security procedures.
- Country and route fields in fixtures are illustrative synthetic values, not claims about actual movement volumes or routes.

## 3. Record model

One row represents one fictional movement-event record. It does not represent a verified person.

| Field | Type | Required | Rule |
|---|---|---:|---|
| record_id | string | yes | Synthetic stable ID; 1–64 chars; pattern `SYN-[A-Z0-9-]+` |
| event_type | string | yes | One of `entry`, `exit`, `transit` |
| event_at | string | yes | RFC 3339 timestamp with explicit UTC offset; normalise to UTC |
| ingested_at | string | yes | RFC 3339 timestamp with explicit UTC offset; normalise to UTC |
| source_system | string | yes | Controlled synthetic source label: `SYNTH-A`, `SYNTH-B`, or `SYNTH-C` |
| source_record_id | string | yes | Synthetic source-local identifier; 1–64 chars |
| origin_country | string | yes | Uppercase ISO 3166-1 alpha-2 code from the deliberately limited v0.1 fixture allowlist |
| destination_country | string | yes | Uppercase ISO 3166-1 alpha-2 code |
| transport_mode | string | yes | One of `air`, `land`, `sea`, `unknown` |

No other fields are accepted in v0.1. Unknown fields are rejected rather than silently retained.

## 4. Time and provenance semantics

- Timestamps must parse as RFC 3339/ISO 8601 values with an explicit offset; naive local timestamps are invalid.
- The pipeline does not copy raw record payloads into diagnostics. It emits only the input row number, a record ID when it matches the synthetic ID pattern, stable issue codes and disposition; accepted output contains UTC-normalised timestamps.
- `event_at` is when the fictional event is said to have occurred.
- `ingested_at` is when the fictional source says it entered that source's dataset.
- `ingested_at < event_at` is a temporal consistency error.
- An event more than 24 hours in the future relative to a caller-supplied reference time is invalid. The reference time must be explicit and fixed in tests; the pipeline must not silently depend on wall-clock time.
- Source provenance is the pair `(source_system, source_record_id)`.

## 5. Quality dimensions and v0.1 rules

1. **Completeness:** required fields exist and are not null, empty or whitespace-only.
2. **Validity:** field types, controlled vocabularies, identifier pattern, country-code syntax and timestamps conform.
3. **Uniqueness:** repeated `record_id` values are classified as exact duplicates or conflicting duplicates.
4. **Consistency:** origin and destination differ; event and ingestion times are ordered; field combinations obey the declared contract.
5. **Timeliness:** future events beyond the explicit 24-hour tolerance are rejected; report ingestion lag as a descriptive metric, not a quality verdict by itself.
6. **Provenance:** source label is allow-listed and source-local identifier is present; duplicate provenance keys are surfaced.
7. **Auditability:** every input row receives a deterministic row number and one or more stable issue codes; summaries are reproducible from the same input and reference time.

### Duplicate policy

- Same `record_id` and identical canonical payload: retain the first row; classify later rows as `EXACT_DUPLICATE`.
- Same `record_id` but different canonical payload: classify all rows sharing that ID as a conflict group; do not choose a winner automatically.
- Same `(source_system, source_record_id)` attached to different `record_id` values: emit `DUPLICATE_SOURCE_REFERENCE`; do not merge records.
- Invalid rows remain in diagnostics and are excluded from the clean output.
- No silent overwrite, fuzzy matching or probabilistic entity resolution.

## 6. Expected outputs

The first implementation should produce:
- a clean JSONL file containing only rows that pass all hard validation rules and are not duplicate/conflict cases;
- a row-diagnostics JSONL file with input row number, record ID when safely parseable, issue codes and disposition;
- a summary JSON document with input count, accepted count, rejected count, exact-duplicate count, conflict-group count, issue counts by code and aggregate ingestion-lag statistics;
- deterministic output ordering by input row number.

No dashboard is required.

## 7. Metrics and interpretation

Report counts and rates with denominators. If the denominator is zero, report the metric as unavailable/null, not zero. Report missingness by field with an explicit object-record denominator, validation failures by issue code, duplicate classes, and ingestion-lag count/min/max/mean for rows with parseable, non-negative lag. Do not imply statistical representativeness. The v0.1 country-code allowlist is intentionally small and is not a complete or authoritative ISO registry.

A high pass rate does not prove that records are true, complete in the real world, representative or fit for operational decisions. The pipeline validates conformance to this contract only.

## 8. Determinism and implementation constraints

- Python standard library only for v0.1.
- JSON Lines input; UTF-8; one JSON object per non-empty line.
- Stable issue codes and deterministic JSON output.
- Reference time supplied as an explicit argument.
- No network calls, external services, databases or runtime secrets.
- Malformed JSON, duplicate object keys and non-standard numeric constants are diagnosed per line; processing continues. Duplicate keys are rejected rather than silently collapsed by the parser.
- Do not log or print entire records by default.

## 9. Versioning

A schema change requires a version increment and tests for backward/forward behaviour. v0.1 is intentionally narrow. Any proposal to add sensitive fields, person-level matching, biometrics or operational integration is out of scope and requires a separate safety review.

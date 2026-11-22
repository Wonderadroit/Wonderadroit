# Migration Data Quality Lab v0.2 — Evidence Traceability and Gap Review

**Review date:** 2026-11-22  
**Scope inspected:** `PROJECT_FRONTIER/labs/migration-data-quality/` on branch `project-frontier/migration-data-quality-lab`; implementation, both test modules, v0.2 contract and v0.2 test plan.  
**Purpose:** Map what the existing synthetic validator actually tests against the research evaluation dimensions. This is a desk review of repository artefacts, not an independent review or a new test execution.

## 1. Evidence baseline

The v0.2 test plan records GitHub Actions run **44176377842**, commit `c13c1f85fe677227e194f9ee18968d37ca3de653`, Python 3.12, with **45 tests passed** and a synthetic CLI fixture completed. This document did not rerun that workflow. The 45 tests are 40 tests in `test_validator.py` and 5 in `test_run_lab.py`.

Implementation files inspected:
- `validator.py`: record parsing, validation, duplicate/provenance grouping, metrics and diagnostics.
- `run_lab.py`: strict UTF-8 file reader, reference-time parsing, CLI output writing and aggregate console output.
- `test_validator.py`: 40 unit tests.
- `test_run_lab.py`: 5 reader/CLI tests.

Contract limits are explicit: one row is a fictional movement-event record, not a verified person; only nine named fields are accepted; identifiers and country codes use narrow fixture-oriented allowlists; no live integration or personal/operational data is permitted.

## 2. Evaluation-dimension traceability

| Research evaluation dimension | Implemented rule / observable behaviour | Exact tests (file: test name) | Assessment and boundary |
|---|---|---|---|
| **Completeness — required-field presence** | All nine contract fields required; missing, null, empty and whitespace-only values are rejected. Per-field missingness count and denominator are reported. | `test_validator.py`: `test_missing_and_empty_fields_rejected`; `test_null_empty_and_whitespace_for_every_required_field`; `test_missingness_and_ingestion_lag_metrics_have_denominators`; `test_empty_input_has_unavailable_rates_and_lag_metrics` | **Tested at record/field level.** Does not establish completeness of an underlying population, completeness of a source extract, or whether expected events are absent entirely. |
| **Validity — schema and allowed values** | Unknown fields rejected; event type, source system, transport mode and country code constrained to enumerations/allowlists; same origin/destination rejected. | `test_validator.py`: `test_unexpected_field_rejected`; `test_non_string_controlled_value_is_rejected_not_crashing`; `test_each_controlled_vocabulary_rejects_unknown_string`; `test_same_country_rejected`; `test_unknown_two_letter_country_code_rejected`; `test_lowercase_and_malformed_country_codes_rejected` | **Tested against the lab's narrow contract.** The country allowlist is deliberately incomplete and not authoritative. The same-country rule is a chosen fixture rule, not a universal migration-data truth. |
| **Validity — timestamp syntax and temporal rules** | RFC 3339 shape, explicit offset, ASCII digits, parseability, ingestion not before event, and a 24-hour future tolerance against explicit reference time. Accepted timestamps normalised to UTC. | `test_validator.py`: `test_valid_record_accepted_and_timestamp_normalised`; `test_equivalent_offsets_are_valid`; `test_naive_timestamp_rejected`; `test_ingestion_before_event_rejected`; `test_future_event_beyond_tolerance_rejected`; `test_timestamp_must_use_rfc3339_separator_and_offset`; `test_exact_future_tolerance_boundary_is_accepted`; `test_reference_time_must_be_aware`; `test_reference_time_changes_future_validity`; `test_rfc3339_rejects_non_ascii_digits` | **Tested for these boundaries.** Not a validation of source clock accuracy, time-zone correctness, event chronology, or a domain-justified 24-hour threshold. |
| **Consistency — within-record constraints** | Event/ingestion chronology and origin/destination inequality are enforced. Summary accepted/rejected totals reconcile to input dispositions. | `test_validator.py`: `test_ingestion_before_event_rejected`; `test_same_country_rejected`; `test_summary_reconciles` | **Narrow internal consistency only.** No cross-record event-sequence, itinerary, referential-integrity, or multi-source semantic consistency is tested. |
| **Uniqueness and conflict handling** | Exact duplicate compares canonical JSON with key ordering sorted but values unchanged; first exact duplicate retained; same ID/different payload rejects all group members; source reference collisions across distinct valid record IDs are flagged. | `test_validator.py`: `test_exact_duplicate_retains_first_only`; `test_conflicting_duplicate_rejects_all_members`; `test_duplicate_source_reference_across_record_ids`; `test_distinct_sources_do_not_collide`; `test_conflicting_duplicate_is_rejected_under_both_input_orders`; `test_equivalent_timestamp_offsets_with_same_record_id_are_conflicts`; `test_invalid_record_id_does_not_trigger_duplicate_source_reference`; `test_duplicate_metrics_include_parseable_objects_with_other_errors` | **Well-defined deterministic policy.** Lexical timestamp differences representing the same instant intentionally conflict. First-seen retention is order-dependent for exact duplicates. No fuzzy matching, probabilistic entity resolution or cross-dataset identity resolution. |
| **Timeliness — ingestion lag** | Non-negative ingestion lag is computed where both timestamps parse; count/min/max/mean reported. Negative lag is separately rejected. | `test_validator.py`: `test_missingness_and_ingestion_lag_metrics_have_denominators`; `test_empty_input_has_unavailable_rates_and_lag_metrics`; `test_ingestion_before_event_rejected` | **Basic descriptive metric tested.** No service-level threshold, latency distribution analysis, freshness requirement, delayed-feed detection or operational timeliness benchmark is defined. |
| **Provenance — source references** | Source system is from a synthetic enumeration; source record ID must match `SRC-[A-Z0-9-]{1,60}`; duplicate source references across distinct valid record IDs are flagged. | `test_validator.py`: `test_duplicate_source_reference_across_record_ids`; `test_distinct_sources_do_not_collide`; `test_source_record_id_length_boundaries`; `test_source_record_id_requires_synthetic_prefix_and_ascii_token`; `test_invalid_record_id_does_not_trigger_duplicate_source_reference` | **Identifier format and collision behaviour only.** The code itself states the token pattern is not cryptographic proof of synthetic origin. No source authentication, chain of custody, signed provenance, source-system audit, transformation lineage or accountable data-owner metadata. |
| **Privacy minimisation — diagnostics and console** | Unexpected fields rejected; diagnostics expose only row number, valid-pattern record ID, issue codes and disposition; malformed IDs are not echoed; CLI console prints aggregate summary rather than record identifiers. | `test_validator.py`: `test_unexpected_field_rejected`; `test_invalid_record_id_is_not_echoed_in_diagnostics`; `test_overlong_record_id_rejected_and_not_echoed`; `test_run_lab.py`: `test_console_prints_aggregate_only_not_record_identifiers` | **Limited output minimisation tested.** Not a privacy impact assessment, anonymisation guarantee, re-identification analysis, access-control test, retention policy, encryption test or legal compliance assessment. |
| **Reproducibility — deterministic behaviour** | Fixed explicit timezone-aware reference time; stable output ordering and issue-key ordering; deterministic JSONL/summary bytes for identical inputs. | `test_validator.py`: `test_outputs_are_deterministic`; `test_distinct_valid_rows_preserve_input_order`; `test_issue_count_keys_are_sorted`; `test_reference_time_changes_future_validity`; `test_run_lab.py`: `test_cli_outputs_are_byte_for_byte_deterministic`; `test_invalid_reference_time_fails_without_outputs` | **Determinism tested for same code/input/reference time.** Does not prove independent reproduction on a second implementation/environment or reproducibility of real-world measurements. |
| **Input robustness / reader boundary** | Malformed JSON, non-object JSON, duplicate object keys, non-standard numeric constants and invalid UTF-8 are rejected; later valid rows continue after malformed JSON lines. | `test_validator.py`: `test_invalid_json_does_not_stop_later_rows`; `test_non_object_json_rejected`; `test_duplicate_json_object_keys_are_rejected`; `test_nonstandard_json_numeric_constant_is_rejected`; `test_run_lab.py`: `test_invalid_utf8_is_rejected_without_repair`; `test_run_lab.py`: `test_empty_input_creates_empty_outputs_and_null_metrics` | **Input handling is tested.** No resource-exhaustion, very-large-file, deeply nested JSON, filesystem-permission, partial-write or crash-recovery test is evidenced here. |

## 3. Full test inventory (45)

### `test_validator.py` — 40 tests

1. `test_valid_record_accepted_and_timestamp_normalised`
2. `test_equivalent_offsets_are_valid`
3. `test_missing_and_empty_fields_rejected`
4. `test_unexpected_field_rejected`
5. `test_invalid_json_does_not_stop_later_rows`
6. `test_non_object_json_rejected`
7. `test_naive_timestamp_rejected`
8. `test_ingestion_before_event_rejected`
9. `test_future_event_beyond_tolerance_rejected`
10. `test_same_country_rejected`
11. `test_exact_duplicate_retains_first_only`
12. `test_conflicting_duplicate_rejects_all_members`
13. `test_duplicate_source_reference_across_record_ids`
14. `test_distinct_sources_do_not_collide`
15. `test_summary_reconciles`
16. `test_outputs_are_deterministic`
17. `test_reference_time_must_be_aware`
18. `test_non_string_controlled_value_is_rejected_not_crashing`
19. `test_missingness_and_ingestion_lag_metrics_have_denominators`
20. `test_empty_input_has_unavailable_rates_and_lag_metrics`
21. `test_timestamp_must_use_rfc3339_separator_and_offset`
22. `test_exact_future_tolerance_boundary_is_accepted`
23. `test_invalid_record_id_is_not_echoed_in_diagnostics`
24. `test_overlong_record_id_rejected_and_not_echoed`
25. `test_unknown_two_letter_country_code_rejected`
26. `test_null_empty_and_whitespace_for_every_required_field`
27. `test_each_controlled_vocabulary_rejects_unknown_string`
28. `test_lowercase_and_malformed_country_codes_rejected`
29. `test_source_record_id_length_boundaries`
30. `test_distinct_valid_rows_preserve_input_order`
31. `test_conflicting_duplicate_is_rejected_under_both_input_orders`
32. `test_issue_count_keys_are_sorted`
33. `test_reference_time_changes_future_validity`
34. `test_duplicate_json_object_keys_are_rejected`
35. `test_nonstandard_json_numeric_constant_is_rejected`
36. `test_rfc3339_rejects_non_ascii_digits`
37. `test_source_record_id_requires_synthetic_prefix_and_ascii_token`
38. `test_equivalent_timestamp_offsets_with_same_record_id_are_conflicts`
39. `test_invalid_record_id_does_not_trigger_duplicate_source_reference`
40. `test_duplicate_metrics_include_parseable_objects_with_other_errors`

### `test_run_lab.py` — 5 tests

1. `test_invalid_utf8_is_rejected_without_repair`
2. `test_empty_input_creates_empty_outputs_and_null_metrics`
3. `test_invalid_reference_time_fails_without_outputs`
4. `test_console_prints_aggregate_only_not_record_identifiers`
5. `test_cli_outputs_are_byte_for_byte_deterministic`

## 4. Important gaps — what the 45 tests do not establish

These are not necessarily defects in a deliberately narrow synthetic teaching lab. They are limits that must be stated and considered before designing a research paper.

1. **Population completeness and coverage:** no known expected-event denominator, missing-event detection, source-feed completeness or representativeness test.
2. **Truth and factual validity:** a syntactically valid fictional record can still describe an event that never happened. No ground-truth comparison exists.
3. **External reference integrity:** no authoritative country-code registry, transport code source, source-system registry or versioned reference-data process.
4. **Cross-record domain integrity:** no parent/child relationships, sequence logic, impossible travel/event ordering, cross-border route plausibility or multi-source reconciliation.
5. **Provenance assurance:** no cryptographic source authentication, signature verification, audit trail, lineage, source ownership or evidence of how a record was generated.
6. **Metric fitness:** missingness denominator is parseable JSON objects, while input disposition denominator includes malformed/non-object lines. This is documented, but a research protocol must explain why each denominator answers its intended question. Ingestion lag excludes negative values and includes rows with other defects; that is a specific descriptive choice, not a universal quality standard.
7. **Timeliness thresholds:** no justified acceptable-lag threshold or service-level objective; mean alone can hide skew and tails.
8. **Privacy/security controls:** no threat model, access control, encryption, retention/deletion, re-identification assessment, logging review beyond tested outputs, or formal legal assessment.
9. **Scale and resilience:** no load, performance, memory, streaming, concurrency, interruption, crash recovery or large-file tests.
10. **Independent reproduction:** the recorded CI pass is one project workflow result. No second reviewer or independent implementation has reproduced the results.
11. **Cross-version and interoperability:** no migration between contract versions, schema evolution, mapping across source schemas, or exchange with another implementation.
12. **Fairness and rights impact:** the lab has no person-level data or decision logic, so it cannot evaluate disparate impact, due process or operational effects. It must not be repurposed into person-level risk or enforcement scoring.

## 5. Literature interpretation — what this means for Frontier

The literature reviewed so far changes the framing:

- IOM's ECOWAS migration-data harmonisation guidance (2019) and Nigeria assessment (2013) establish that regional harmonisation and Nigerian migration-data management are not new topics. The 2013 assessment is historical and cannot be used to describe current systems.
- IOM's 2026 *Essentials of Migration Data* provides a current broad reference for migration definitions, sources, lifecycle, governance, sharing, protection and analysis. It is not a direct evaluation of this validator.
- Ibor et al. (2025) distinguish identity proofing, authentication, secure data exchange and receiving-side authorisation. This lab implements none of those identity/interoperability mechanisms; it is a record-contract validator only.
- Uzomah (2024) and Iwuoha's work on biometric border technologies show why governance, rights, mobility and institutional context cannot be reduced to technical validation metrics. The lab contains no empirical evidence about those impacts.
- ECOWAS's May 2026 public announcement about harmonised migration governance and integrated border management is a lead for documentary research. It is not the formal strategy or technical architecture and cannot substantiate system design claims.

Consequently, this lab can be described as a **synthetic contract-validation demonstrator**. It cannot yet be described as a migration-data quality framework validated for operational use, a test of Nigerian or ECOWAS systems, or evidence that the project has solved a regional data-governance problem.

## 6. Recommended research decision

Do **not** add more features yet. First seek independent technical review of:
- the nine-field contract and its domain rationale;
- timestamp parser and 24-hour tolerance;
- duplicate grouping and first-seen policy;
- denominator choices and metric interpretation;
- synthetic identifier boundary and privacy-minimised diagnostics;
- test sufficiency and the gaps listed above.

Separately obtain policy/data-governance review of the selected migration-data dimensions and their relevance to ECOWAS/Nigeria. Do not treat technical review as policy review.

A defensible initial paper, if the reviews support it, would evaluate the **design, contract, test coverage, deterministic behaviour and limitations of a synthetic migration-event validator**. It should not claim to measure real migration-data quality. A stronger empirical contribution would require a carefully authorised, ethically reviewed and legally assessed data source; that is not part of this lab's current scope.

## 7. Source register for this mapping

- Project Frontier, `DATA_CONTRACT_v0.2.md`, `TEST_PLAN_v0.2.md`, `validator.py`, `run_lab.py`, `test_validator.py`, `test_run_lab.py` (repository branch noted above).
- IOM, *Guidelines for the Harmonization of Migration Data Management in the ECOWAS Region* (2019): https://publications.iom.int/books/guidelines-harmonization-migration-data-management-ecowas-region
- IOM, *Enhancing Migration Data Management in Nigeria: Assessment and Recommendations* (2013): https://publications.iom.int/books/enhancing-migration-data-management-nigeria-assessment-and-recommendations
- IOM, *The Essentials of Migration Data* (2026): https://publications.iom.int/books/essentials-migration-data-emd-iom-guide-migration-data-and-statistics
- Ibor et al. (2025), *Considerations for trustworthy cross-border interoperability of digital identity systems in developing countries*: https://pmc.ncbi.nlm.nih.gov/articles/PMC12078359/
- Uzomah (2024), *European Union border technology in Africa: Experiences en route*: https://onlinelibrary.wiley.com/doi/abs/10.1002/psp.2824
- Iwuoha & Doevenspeck (2023 online / 2025 issue), *Dilemmas of ‘biometric nationality’*: https://doi.org/10.1080/21622671.2023.2205885
- ECOWAS Commission (10 May 2026), *Interior Ministers ... Commit to Harmonized Migration Governance and Integrated Border Management*: https://www.ecowas.int/interior-ministers-from-ecowas-member-states-commit-to-harmonized-migration-governance-and-integrated-border-management/

**Review status:** AI-assisted desk mapping only. Not independent peer review, not a legal opinion, not an operational assessment, and not a new test result.

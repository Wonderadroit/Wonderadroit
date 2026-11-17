# Internal Self-Review — Migration Data Quality Laboratory

**Date:** 17 November 2026  
**Scope:** Static inspection of validator, CLI, regression tests, v0.2 contract and test plan.  
**Review type:** Internal assistant self-review. **Not independent assurance.**

## Original v0.1 findings and v0.2 disposition

### Finding 1 — Source-local identifier accepted arbitrary text

**Original severity:** High for the stated synthetic-only boundary.  
**Disposition:** Mitigated by a versioned v0.2 format constraint and regression coverage; not independently closed.

v0.1 accepted any non-empty `source_record_id` up to 64 characters. v0.2 requires `SRC-[A-Z0-9-]{1,60}` and rejects email-like, phone-like, whitespace-padded, lowercase and non-ASCII lookalike values. The accepted-output and diagnostic boundaries remain narrow.

**Residual limitation:** A prefix/character pattern cannot prove that an identifier was generated synthetically; someone could still place meaningful digits after the prefix. The repository must use generated fictional tokens only, and the field must never be populated from real source data. An independent reviewer should assess whether the format and fixture-generation controls are adequate.

### Finding 2 — Duplicate canonicalisation is lexical, not semantic

**Original severity:** Medium.  
**Disposition:** Semantics made explicit and regression-tested; independent review remains open.

Exact duplicates are defined as equality of parsed JSON field values after object-key ordering is canonicalised. Timestamp strings are not normalised before duplicate comparison. Therefore equivalent timestamp instants expressed with different offsets are different payloads and conflict when sharing a record ID. A dedicated regression test asserts this decision.

This is a deliberate strict-payload policy, not a claim that equivalent timestamp instants are different events.

### Finding 3 — Duplicate grouping and validation are separate layers

**Original severity:** Low / clarification.  
**Disposition:** Metric semantics documented and regression-tested; independent review remains open.

Duplicate/conflict grouping is intentionally run across all parseable JSON objects, including records with other validation defects. The denominator and issue-count interpretation are documented in `DATA_CONTRACT_v0.2.md`, with a regression test for a malformed-but-parseable conflicting record.

A further implementation defect was found during continuation: duplicate provenance grouping previously allowed an invalid record ID to participate in a source-reference collision. The implementation now requires a valid synthetic record ID before adding a row to the provenance grouping, and a regression test confirms an invalid record ID does not create a duplicate-source-reference issue.

## Checks observed in code and regression suite

- Duplicate JSON keys and non-standard JSON numeric constants are rejected at parse time.
- Invalid UTF-8 is rejected at the CLI file-reader boundary.
- Timestamp parsing requires an explicit offset and ASCII RFC 3339-shaped syntax, then normalises to UTC.
- The reference time must be timezone-aware and is supplied explicitly.
- Diagnostics do not copy raw payloads or source-record identifiers; invalid record IDs are not echoed.
- Missingness rates expose their object-record denominator and return null for a zero denominator.
- CLI summary output is aggregate-only in the tested path.
- Output ordering is deterministic for a fixed input and reference time.
- Provenance collision grouping now requires valid synthetic record IDs and source references.

These are observations from internal inspection and tests, not proof of correctness or a substitute for an independent reviewer.

## Verification evidence

GitHub Actions run **44176377842** on commit `c13c1f85fe677227e194f9ee18968d37ca3de653` completed successfully on Python 3.12:
- 45 regression tests passed.
- Synthetic CLI fixture completed and produced accepted, diagnostics and summary outputs.

This validates only the cases exercised by the synthetic suite. It does not establish real-world accuracy, truth, representativeness, production readiness or operational suitability.

## Remaining independent-review checklist

1. Assess whether the synthetic source identifier convention and fixture-generation controls adequately protect the synthetic-only boundary.
2. Review duplicate grouping, first-seen retention and conflict semantics.
3. Review RFC 3339 parsing, offset handling and explicit reference-time boundaries.
4. Review missingness and ingestion-lag denominators.
5. Review diagnostic minimisation and unexpected-field rejection.
6. Reconcile contract, tests, README and CLI behaviour.
7. Independently verify the official policy sources and interpretation in the NBMS 2027–2031 research brief.

## Disposition

- Internal v0.2 remediation is implemented and the 45-test CI gate passed.
- No independent-review gate is closed by this document.
- The NBMS research brief still requires independent source and interpretation review.
- Keep the pull request draft and unmerged until review and acceptance criteria are satisfied.

# Internal Self-Review — Migration Data Quality Laboratory v0.1

**Date:** 17 November 2026  
**Scope:** Static inspection of `validator.py`, `run_lab.py`, the 41-test suite, data contract, test plan and README.  
**Review type:** Internal assistant self-review. **Not independent assurance.**

## Finding 1 — Provenance identifier does not enforce synthetic-only format

**Severity:** High for the lab's stated privacy boundary  
**Location:** `validator.py`, validation of `source_record_id`

The current validator accepts any non-empty string of up to 64 characters. Accepted records preserve this value in `accepted.jsonl`. Consequently, arbitrary text such as an email-like value, phone-like value or name can pass the field-level rule even though the contract says identifiers must be synthetic.

**Required correction:** In a versioned contract revision, require a narrow synthetic token format (for example, a fixed `SRC-` prefix followed only by uppercase ASCII letters, digits and hyphens, with explicit length bounds). Add negative tests for email-like, phone-like, whitespace-padded, lowercase and overlong values. Keep raw values out of diagnostics. This finding should be closed by a test-backed commit, not by documentation alone.

## Finding 2 — Duplicate canonicalisation is lexical, not semantic

**Severity:** Medium  
**Location:** `_canonical()` and exact-duplicate grouping

Exact duplicates are identified by serialising the raw parsed object with sorted keys. Two records with equivalent timestamps expressed using different valid offsets normalise to the same UTC instant for accepted output, but their raw payloads differ and the same `record_id` is classified as a conflict. This may be a defensible strict-payload policy, but the contract's phrase “identical canonical payload” does not clearly state whether timestamp equivalence is semantic or lexical.

**Required correction:** Ask the independent reviewer to decide and document whether exact duplicate means byte/field-value equivalence or equality after field normalisation. Add a test that presents the same event timestamp in equivalent offsets and asserts the chosen policy. Do not silently change duplicate semantics without a versioned decision.

## Finding 3 — Validation and duplicate classification are separate layers

**Severity:** Low / clarification  
**Location:** duplicate/provenance grouping after row validation

Duplicate grouping includes object rows even when they already have other field-validation issues. This is deterministic and does not cause invalid rows to enter accepted output, but issue counts can include duplicate classifications for already-invalid rows. The metric definitions should state whether duplicate rates cover all parseable object records or only otherwise-valid records.

**Required correction:** Document the denominator and add a fixture/test for a malformed-but-parseable record participating in a duplicate group. Independent reviewer to assess whether this is appropriate.

## Checks that appeared sound in this inspection

- Duplicate JSON keys and non-standard JSON numeric constants are rejected at parse time.
- Invalid UTF-8 is rejected at the CLI file-reader boundary.
- Timestamp parsing requires an explicit offset and ASCII RFC 3339-shaped syntax, then normalises to UTC.
- The reference time must be timezone-aware and is supplied explicitly.
- Diagnostics do not copy raw payloads or source-record identifiers; invalid record IDs are not echoed.
- Missingness rates expose their object-record denominator and return null for a zero denominator.
- CLI summary output is aggregate-only in the tested path.
- Output ordering is deterministic for a fixed input and reference time.

These are observations from static inspection and existing tests, not proof of correctness or a substitute for an independent reviewer.

## Disposition

- No independent-review gate is closed by this document.
- Finding 1 should be addressed in a versioned revision before the lab is used as a portfolio demonstration of synthetic-only provenance controls.
- Findings 2 and 3 should be resolved through explicit semantic decisions and regression tests.
- The research brief still needs independent source/interpretation review.

# Project Frontier — Status

**Last reviewed:** 2026-11-17  
**Current phase:** Phase 1 — First reproducible synthetic data-quality prototype  
**Overall state:** IN PROGRESS

## Verified starting assets

- Public Python security-engineering and automation work exists across CYDRA Web2 and Web3.
- CYDRA Web2 documents an evidence-led web security research loop, scope controls, provenance, differential testing, and replay requirements.
- CYDRA Web3 documents an authorization-focused Solidity research engine, explicit execution boundaries, causal verification, and evidence requirements.
- The broader CYDRA repository contains a substantial Python reasoning system, tests, and GitHub Actions workflows.
- A public portfolio site has Playwright browser regression checks.

These are repository-level indicators of software engineering practice. They do **not** independently prove mastery of networking, Linux administration, enterprise cybersecurity, digital forensics, migration policy, biometrics, or operational border systems.

## Initial assessment

| Domain | Evidence-based starting assessment | Next validation |
|---|---|---|
| Python/software engineering | Strong project-level evidence | Independent implementation and explanation |
| Software architecture | Strong project-level evidence | Architecture walkthrough and trade-off review |
| Testing/CI | Strong practical evidence | Design a test plan and diagnose seeded failures |
| Security research methodology | Strong documented evidence | Reproduce a safe local control experiment |
| Networking | Not established by repository evidence reviewed | IP/subnet/DNS/TCP/HTTP practical assessment |
| Linux | Not established by repository evidence reviewed | Shell, permissions, processes, packages and logs |
| SQL/data analysis | Partial / not yet established | Reproducible public-data analysis |
| Defensive cybersecurity | Working hypothesis only | Threat model and isolated defensive lab |
| Digital forensics | Not established | Offline evidence-handling exercise |
| Digital identity | Research interest; competence not established | Standards review and synthetic identity flow |
| Migration/border governance | Initial NIS strategic-alignment note grounded in official public sources | Page/section-level policy brief and independent source review |
| Professional English | Not formally assessed | Reviewed 800–1,000 word brief |
| French | Starting level not assessed | CEFR-aligned placement baseline |

## Completed

- [x] Project charter and safety boundaries drafted.
- [x] Evidence-first operating rules and phase gates defined.
- [x] Initial public-repository inventory reviewed.
- [x] Initial primary-source register created with official NIS, ECOWAS and NIST materials.
- [x] Initial research question proposed for Nigeria's 2027–2031 National Border Management Strategy.
- [x] Initial NIS strategic-alignment note added, mapping public NIS priorities to safe Frontier portfolio capabilities.
- [x] Digital Identity Laboratory scope, draft data contract and initial threat model created using synthetic-only assumptions.
- [x] Migration Data Quality Laboratory v0.1 data contract and executable test plan documented.
- [x] Migration Data Quality Laboratory v0.1 validator, CLI, synthetic fixtures and regression suite implemented; 41 tests passed in GitHub Actions run 44174686867.
- [x] First source-checked research brief drafted for the 2027–2031 National Border Management Strategy, distinguishing official facts, recommendations and unknowns.
- [x] First synthetic-only validator and command-line runner implemented.
- [x] Synthetic fixture and deterministic accepted/diagnostics/summary outputs added.
- [x] GitHub Actions regression suite passed on Python 3.12; synthetic fixture run succeeded.

## Active

- [ ] Independent review of duplicate/conflict semantics, field typing, time handling, metrics and privacy boundaries.
- [x] Add strict invalid-UTF-8 file-reader test and identifier/country-code boundary tests.
- [x] Address the internal v0.1 provenance and duplicate-semantics findings through a versioned v0.2 change and regression tests; independent review remains open.
- [ ] Complete practical networking/Linux/Python/data baseline.
- [ ] Review Nigerian legal and policy sources relevant to identity data, privacy and border management.
- [ ] Obtain independent review of the Migration Data Quality Laboratory and research brief; reconcile any substantive review findings.
- [ ] Obtain a successful CI run and complete independent code/test review for the Digital Identity Laboratory.
- [ ] Review Security Monitoring Lab false-positive boundaries before extending detection logic.

## Current prototype decisions

### Digital Identity Laboratory

The Digital Identity Laboratory is a local educational verifier for fictional credentials only. It is designed to demonstrate strict schema validation, a configured demo issuer, payload-integrity checks, expiry checks, duplicate-presentation handling and privacy-minimised audit events.

A first verifier and unit-test suite have been committed. It uses Ed25519, strict schema checks, UTC validity checks, in-memory duplicate detection and allow-listed audit events. The GitHub Actions workflow has been added, but a successful run has not yet been observed; implementation is therefore not yet validated. No real passport, national-ID, biometric, traveller or government data will be used. A successful lab check will not be represented as proof of a presenter's identity, legal status or eligibility.

### Migration Data Quality Laboratory

The v0.1 prototype is under PROJECT_FRONTIER/labs/migration-data-quality/. It accepts a narrow fictional movement-event schema with no personal identity fields. It validates required fields, controlled values, timestamp offsets/order, a bounded country-code fixture allowlist, duplicate record IDs, conflicting record IDs and duplicate source references. It emits accepted JSONL, row-level diagnostics and a summary with issue counts, field missingness denominators/rates and ingestion-lag count/min/max/mean.

The v0.1 CI run on Python 3.12 passed 41 unit tests and executed the synthetic fixture (run 44174686867). The v0.2 implementation subsequently passed 45 tests and the synthetic CLI fixture in run 44176377842 (commit `c13c1f85fe677227e194f9ee18968d37ca3de653`). The fixture produced 3 input object records, 1 accepted record and 2 rejected dispositions (one exact duplicate and one same-origin/destination record). This proves only the tested contract behaviour on synthetic inputs. It does not establish real-world migration data quality, truth, representativeness or operational suitability.

The country-code allowlist is intentionally limited and is not a complete or authoritative ISO registry. The documented v0.1 executable test cases include strict rejection of duplicate JSON keys and non-standard numeric constants, ASCII-only RFC 3339 timestamps and strict CLI reference-time parsing; independent review remains outstanding.

An internal self-review identified a gap in v0.1 provenance validation. v0.2 now constrains `source_record_id` to a synthetic token pattern, adds negative regression cases, and limits duplicate provenance grouping to valid synthetic record IDs. The token pattern is a format constraint, not proof of synthetic origin. This is an internal finding and remediation, not an independent review.

## Security Monitoring Laboratory

The authentication detector is a separate defensive workstream under labs/security-monitoring/auth-detection/. Verified v0.2 CI run 44143393201 completed successfully on commit d239b46f882f78f2bbce63624b12262f9290b741; its suite ran 17 tests and the synthetic fixture generated the expected two alerts. This validates only the listed synthetic cases, not production readiness or real-world detection effectiveness. No production SIEM capability is claimed.

## Blockers / constraints

- Android phone is the current primary device; prefer browser/cloud-compatible and lightweight Python work.
- No assumption of access to government systems, data, or internal training channels.
- No live integrations or testing of government/third-party systems without explicit written authorisation.
- Any future NIS-related career opportunity must be verified through official channels and actual published requirements.

## Next action

Obtain an independent review of the v0.2 Migration Data Quality Laboratory and the NBMS research brief. Resolve substantive findings, then produce a compact synthetic demonstration dataset and reproducible quality report. Do not build a broad dashboard.

## Decision rule

A phase is not complete because code was written or a workflow turned green. It is complete only when the stated deliverables, tests, provenance, limitations, and review criteria are satisfied.


## v0.2 continuation update — 17 November 2026

The internal provenance finding has been addressed in code: `source_record_id` now requires the narrow token format `SRC-[A-Z0-9-]{1,60}`. This is a format constraint, not proof of synthetic origin; repository fixtures must remain generated fictional data. Regression cases reject email-like, phone-like, whitespace-padded, lowercase and non-ASCII lookalike values and test identifier boundaries.

The duplicate policy is now explicit: exact duplicate comparison canonicalises JSON object-key order only; timestamp strings are not semantically normalised before comparison. Equivalent instants written with different offsets therefore count as conflicting payloads under the same record ID. Duplicate/conflict grouping covers all parseable JSON objects, including rows with other validation defects; metric denominators are documented in `DATA_CONTRACT_v0.2.md`.

Versioned files:
- `labs/migration-data-quality/DATA_CONTRACT_v0.2.md`
- `labs/migration-data-quality/TEST_PLAN_v0.2.md`

The v0.2 code and tests have been committed. GitHub Actions run 44176377842 completed successfully on Python 3.12 with 45 regression tests passed and the synthetic CLI fixture completed. Subsequent commits update documentation only. Independent review of the lab and the NIS strategy research brief remains outstanding. The earlier v0.1 contract and test-plan files are retained as historical artifacts.


## v0.2 verification update — 17 November 2026

- [x] Tighten the source-local identifier format and add negative tests for email-like, phone-like, whitespace-padded, lowercase and non-ASCII values.
- [x] Define lexical duplicate semantics, including equivalent timestamp offsets, and document duplicate/metric denominators.
- [x] Correct provenance collision grouping so invalid record IDs do not create duplicate-source-reference findings.
- [x] GitHub Actions run **44176377842** passed **45 tests** on Python 3.12 and completed the synthetic CLI fixture. Run URL: https://github.com/Wonderadroit/Wonderadroit/actions/runs/44176377842
- [ ] Independent review of the code, test semantics and NBMS research brief remains outstanding.

The successful v0.2 run proves only the tested synthetic contract behaviour. It does not prove real-world accuracy, truth, representativeness, operational suitability or production readiness.


## Independent-review preparation update — 17 November 2026

- [x] Added `labs/migration-data-quality/REVIEW_REQUEST.md` with two distinct human-review tracks: implementation/data-quality semantics and NBMS policy-source interpretation.
- [x] The request specifies reviewer independence/conflict disclosure, exact commit/version, evidence-backed findings, test execution, limitations and acceptance criteria.
- [x] Reconciled the lab README to identify v0.2 as current and the unversioned contract/test-plan files as historical v0.1 artefacts. The review request now asks reviewers to verify consistency across the README, v0.2 documents, implementation and tests.
- [ ] No independent reviewer has yet been identified or confirmed.
- [ ] No independent review has been completed. PR #3 remains draft and unmerged.

The review package is preparation for human review, not the review itself. Do not start the compact demonstration dataset/report or dashboard work until both review tracks have been addressed and substantive findings reconciled.


## Documentation reconciliation update — 17 November 2026

- [x] Updated `labs/migration-data-quality/README.md` to describe v0.2 and link to the versioned v0.2 contract and test plan.
- [x] Explicitly labelled `DATA_CONTRACT.md` and `TEST_PLAN.md` as retained historical v0.1 documents.
- [x] Updated `REVIEW_REQUEST.md` so independent reviewers assess consistency across the current README, v0.2 contract/test plan, implementation and tests rather than a discrepancy that has now been corrected.
- [ ] Independent technical review and independent NBMS policy-source review remain outstanding. Documentation correction does not close either review gate.



## Research direction update — 22 November 2026

The research identity and scope are now drafted in `RESEARCH_SCOPE.md`, with three candidate studies and a literature map in `RESEARCH_AGENDA.md`.

**Proposed research identity:** Project Frontier investigates how data governance, digital identity and cybersecurity practices can support trustworthy, rights-respecting and interoperable migration and border-management systems in West Africa.

**Priority 1:** Prepare a methods paper on the synthetic Migration Data Quality Laboratory v0.2. This is not yet a publication-ready paper. Independent technical review and separate policy-source review remain prerequisites.

**Priority 2:** Conduct a structured literature review on digital identity and border technology in West Africa, beginning with the identified work by Ngozi Louis Uzomah and Victor Chidubem Iwuoha.

**Priority 3:** Develop a documentary and synthetic-architecture study of secure, accountable interoperability.

Completed in this update:
- [x] Drafted research identity and scope.
- [x] Defined three candidate research questions, methods, evidence boundaries and publication gates.
- [x] Added a preliminary literature map and source links for Uzomah, Iwuoha and ICMPD.
- [x] Updated the project README/navigation to reflect the focused research identity.

Still open:
- [ ] Verify the proposed scope against the full existing source register and legal/policy brief.
- [ ] Read and annotate full papers, not only abstracts or institutional profiles.
- [ ] Identify and obtain independent reviewers for the technical lab and policy brief.
- [ ] Complete the first paper's traceability matrix and manuscript after review.

The literature map is preliminary, not an exhaustive systematic review. The three questions are candidates, not claims of originality. No independent reviewer, institutional partnership or endorsement is recorded.

# Independent Review Request — Migration Data Quality Lab v0.2 and NBMS Research Brief

**Repository:** Wonderadroit/Wonderadroit  
**Branch:** `project-frontier/migration-data-quality-lab`  
**Pull request:** #3 (draft; intentionally unmerged)  
**Review requested:** Independent human review; no review is claimed complete by this document.

## Purpose

Project Frontier is an independent learning and applied-research portfolio. This request seeks critical review of a small, synthetic-only migration-event data-quality prototype and a public-source policy research brief. The work is not an NIS product, government system, operational border tool, or representation of an unpublished government strategy.

Please identify defects and unsupported claims, not merely confirm that tests pass.

## Review track A — Python implementation and data-quality semantics

**Suggested reviewer:** Python engineer, data-quality engineer, software tester, or privacy/security reviewer with relevant experience.

### Files in scope

- `PROJECT_FRONTIER/labs/migration-data-quality/validator.py`
- `PROJECT_FRONTIER/labs/migration-data-quality/run_lab.py`
- `PROJECT_FRONTIER/labs/migration-data-quality/test_validator.py`
- `PROJECT_FRONTIER/labs/migration-data-quality/test_run_lab.py`
- `PROJECT_FRONTIER/labs/migration-data-quality/DATA_CONTRACT_v0.2.md`
- `PROJECT_FRONTIER/labs/migration-data-quality/TEST_PLAN_v0.2.md`
- `PROJECT_FRONTIER/labs/migration-data-quality/README.md`

### Questions requiring independent judgement

1. Is the synthetic-only boundary credible? In particular, does the `SRC-[A-Z0-9-]{1,60}` format constraint provide a useful guardrail, and what does it fail to guarantee? Are fixture-generation and review controls sufficient?
2. Are duplicate semantics correct and internally consistent: object-key-order canonicalisation, lexical timestamp comparison, first-seen retention for exact duplicates, and rejection of all members of conflicting record-ID groups?
3. Is it appropriate that duplicate/conflict grouping includes all parseable JSON objects with other validation defects, while provenance collisions require valid synthetic record IDs and valid source references?
4. Are the RFC 3339 parser, UTC normalisation, future tolerance, explicit reference-time handling, and ingestion-lag calculations correct at boundaries?
5. Are missingness and ingestion-lag denominators correctly defined and labelled? Do issue counts and record counts reconcile?
6. Are malformed JSON, duplicate object keys, non-standard numeric constants, invalid UTF-8, unexpected fields, diagnostics, and CLI outputs handled safely and deterministically?
7. Are tests sufficient? Identify missing boundary, adversarial, property-based, or regression cases that materially affect correctness.
8. Are the contract, test plan, README and implementation consistent?

### Documentation versioning note

The README was reconciled on 17 November 2026 to identify v0.2 as the current implementation and to label the unversioned `DATA_CONTRACT.md` and `TEST_PLAN.md` as historical v0.1 documents. Please still verify that the README, versioned v0.2 contract/test plan, implementation and tests are mutually consistent. The documentation correction is not an independent review finding or approval.

### Evidence requested

Please provide:
- Review date and the exact commit SHA reviewed.
- Relevant experience and any relationship/conflict that could affect independence.
- Findings with severity, file/line or test references, impact, and recommended correction.
- Any tests or commands independently executed and their results.
- Explicit statement of what was not reviewed.

Do not provide an approval based only on the green CI run. The recorded v0.2 CI result is 45 tests passed in GitHub Actions run 44176377842 on Python 3.12; this is evidence of those automated cases only.

## Review track B — NBMS policy-source and interpretation review

**Suggested reviewer:** Nigerian migration/border-governance researcher, public-policy analyst, lawyer, or subject-matter expert familiar with institutional and regional policy sources.

### File in scope

- `PROJECT_FRONTIER/research/NBMS_2027_2031_TECHNICAL_CAPABILITIES_BRIEF.md`

### Primary sources cited by the brief

- NIS workshop report: https://immigration.gov.ng/nis-iom-review-strategic-framework-for-effective-border-management/
- NIS organisational structure: https://immigration.gov.ng/nis-structure/
- NIS core mandate: https://immigration.gov.ng/our-core-mandate/
- Nigeria Data Protection Act 2023: https://ndpc.gov.ng/wp-content/uploads/2024/03/Nigeria_Data_Protection_Act_2023.pdf
- ECOWAS regional border-management report: https://www.ecowas.int/interior-ministers-from-ecowas-member-states-commit-to-harmonized-migration-governance-and-integrated-border-management/

### Questions requiring independent judgement

1. Do the cited primary sources support each institutional, legal and regional-policy statement attributed to them?
2. Are the dates, institutional names, strategy-cycle references and descriptions of the NIS workshop accurately represented?
3. Does the brief correctly distinguish publicly reported priorities from the complete final 2027–2031 strategy, which it says was not reproduced in the public report reviewed?
4. Are the Data Protection Act references (including sections 24, 28, 37, 39–41) accurately characterised, with appropriate qualifications and without overclaiming exemptions or obligations?
5. Does the ECOWAS discussion distinguish a regional strategy/interoperability proposal from completed Nigerian implementation?
6. Are recommendations clearly labelled as Project Frontier recommendations rather than NIS policy, and are any claims about actual operational gaps unsupported?
7. What important primary sources, legal qualifications or context are missing?

### Evidence requested

Please provide:
- Review date and the exact brief version/commit reviewed.
- Reviewer expertise and any relevant relationship/conflict.
- Claim-by-claim corrections with source URL, page/section/paragraph locator and exact supported interpretation.
- Any additional primary sources consulted.
- Explicit statement of limitations and what was not reviewed.

## Safety and scope boundaries

- Use public sources and repository code only.
- Do not request, upload, or use real traveller, passport, NIN, biometric, personnel, immigration or government operational data.
- Do not scan, test, access or integrate with government or third-party systems.
- Do not infer operational readiness, real-world migration-data quality, or NIS endorsement from this portfolio.
- A review is independent only when performed by a suitably qualified person other than the author, with relevant independence/conflicts disclosed.

## Acceptance gate

The review gate is complete only when both tracks have written findings, the exact reviewed commit/version is recorded, substantive findings are resolved or explicitly accepted with rationale, and the status document is updated. A request sent, a reviewer assigned, or a CI pass does not close the gate.

**Current status: review requested in principle; no independent reviewer or completed review is recorded.**

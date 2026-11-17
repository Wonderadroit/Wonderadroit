# Project Frontier — Status

**Last reviewed:** 2026-11-17  
**Current phase:** Phase 0 — Baseline and research design  
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
| Migration/border governance | No source-checked portfolio item yet | Primary-source policy brief |
| Professional English | Not formally assessed | Reviewed 800–1,000 word brief |
| French | Starting level not assessed | CEFR-aligned placement baseline |

## Completed

- [x] Project charter and safety boundaries drafted.
- [x] Evidence-first operating rules and phase gates defined.
- [x] Initial public-repository inventory reviewed.
- [x] Initial primary-source register created with official NIS, ECOWAS and NIST materials.
- [x] Initial research question proposed for Nigeria's 2027–2031 National Border Management Strategy.
- [x] Digital Identity Laboratory scope, draft data contract and initial threat model created using synthetic-only assumptions.
- [x] Security Monitoring Lab regression suite executed successfully in GitHub Actions (10 tests; synthetic fixture produced the expected alert).

## Active

- [ ] Complete practical networking/Linux/Python/data baseline.
- [ ] Review Nigerian legal and policy sources relevant to identity data, privacy and border management.
- [ ] Draft the first research brief with page/section-level citations and limitations.
- [x] Review and freeze the first implementation profile for the Digital Identity Laboratory (Ed25519, fixed demo issuer, strict synthetic schema).
- [ ] Obtain a successful CI run and complete independent code/test review for the Digital Identity Laboratory.
- [x] Execute and review the Security Monitoring Lab regression suite in GitHub Actions.

## Current prototype decision

The Digital Identity Laboratory is being designed as a local educational verifier for fictional credentials only. It will demonstrate strict schema validation, a configured demo issuer, payload-integrity checks, expiry checks, duplicate-presentation handling and privacy-minimised audit events.

A first verifier and unit-test suite have been committed. It uses Ed25519, strict schema checks, UTC validity checks, in-memory duplicate detection and allow-listed audit events. The GitHub Actions workflow has been added, but a successful run has not yet been observed; implementation is therefore not yet validated. No real passport, national-ID, biometric, traveller or government data will be used. A successful lab check will not be represented as proof of a presenter's identity, legal status or eligibility.

### Security Monitoring Laboratory

A separate defensive lab has been added under `labs/security-monitoring/auth-detection/`. It contains a standard-library Python batch detector, synthetic JSONL authentication events, regression tests and a GitHub Actions workflow.

The initial Termux prototype produced one expected alert from seven synthetic events in a manually observed positive test. The repository implementation is a stricter revision: it validates event fields and IP addresses, requires timezone-aware timestamps, skips malformed and duplicate event IDs, sorts out-of-order records, and correlates by both username and source IP. Detection Engine v0.2 adds `FRONTIER-AUTH-002`, a medium-severity brute-force heuristic that alerts on five failures in ten minutes without requiring a subsequent successful login. It suppresses repeat alerts within a burst and resets on success or expiry of the rolling window. Six additional regression tests were added for thresholding, key isolation, suppression, expiry/re-arming and reset behavior.

**Verified CI evidence for v0.1:** GitHub Actions run `44141356573` completed successfully. Its regression step ran 10 tests and reported `OK`; the synthetic fixture step processed seven valid events and generated the expected single alert. The tested workflow commit was `554e2cb70b4f89944d3e8e93a7531d3c0eccfccf`. Later commits on the branch added v0.2 brute-force logic and six regression tests. **v0.2 is not yet CI-verified**; do not treat the earlier 10-test run as evidence for the new rule. This lab does not establish production readiness or real-world detection effectiveness. No production SIEM capability is claimed.

## Blockers / constraints

- Android phone is the current primary device; prefer browser/cloud-compatible and lightweight Python work.
- No assumption of access to government systems, data, or internal training channels.
- No live integrations or testing of government/third-party systems without explicit written authorisation.
- Any future NIS-related career opportunity must be verified through official channels and actual published requirements.

## Next action

Run the expanded 16-test Security Monitoring Lab suite in GitHub Actions and inspect the full job output. Resolve any failures before claiming v0.2 validated. Then review false-positive boundaries and event semantics before considering privileged-account monitoring. Continue the practical networking/Linux baseline and primary-source legal review. Do not build a broad dashboard.

## Decision rule

A phase is not complete because code was written or a workflow turned green. It is complete only when the stated deliverables, tests, provenance, limitations, and review criteria are satisfied.

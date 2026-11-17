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
| Migration/border governance | Initial NIS strategic-alignment note grounded in official public sources | Page/section-level policy brief and independent source review |
| Professional English | Not formally assessed | Reviewed 800–1,000 word brief |
| French | Starting level not assessed | CEFR-aligned placement baseline |

## Completed

- [x] Project charter and safety boundaries drafted.
- [x] Evidence-first operating rules and phase gates defined.
- [x] Initial public-repository inventory reviewed.
- [x] Initial primary-source register created with official NIS, ECOWAS and NIST materials.
- [x] Initial research question proposed for Nigeria's 2027–2031 National Border Management Strategy.\n- [x] Initial NIS strategic-alignment note added, mapping public NIS priorities to safe Frontier portfolio capabilities.
- [x] Digital Identity Laboratory scope, draft data contract and initial threat model created using synthetic-only assumptions.

## Active

- [ ] Complete practical networking/Linux/Python/data baseline.
- [ ] Review Nigerian legal and policy sources relevant to identity data, privacy and border management.\n- [ ] Convert the NIS 2027–2031 alignment note into a source-checked policy brief; the new note is a planning baseline, not a completed research brief.
- [ ] Draft the first research brief with page/section-level citations and limitations.
- [x] Review and freeze the first implementation profile for the Digital Identity Laboratory (Ed25519, fixed demo issuer, strict synthetic schema).
- [ ] Obtain a successful CI run and complete independent code/test review.

## Current prototype decision

The Digital Identity Laboratory is being designed as a local educational verifier for fictional credentials only. It will demonstrate strict schema validation, a configured demo issuer, payload-integrity checks, expiry checks, duplicate-presentation handling and privacy-minimised audit events.

A first verifier and unit-test suite have been committed. It uses Ed25519, strict schema checks, UTC validity checks, in-memory duplicate detection and allow-listed audit events. The GitHub Actions workflow has been added, but a successful run has not yet been observed; implementation is therefore not yet validated. No real passport, national-ID, biometric, traveller or government data will be used. A successful lab check will not be represented as proof of a presenter's identity, legal status or eligibility.

## Blockers / constraints

- Android phone is the current primary device; prefer browser/cloud-compatible and lightweight Python work.
- No assumption of access to government systems, data, or internal training channels.
- No live integrations or testing of government/third-party systems without explicit written authorisation.
- Any future NIS-related career opportunity must be verified through official channels and actual published requirements.

## Next action

Use the NIS 2027–2031 alignment note to guide the next deliverables: first, a source-checked policy brief; second, a synthetic migration-data quality lab with a documented data contract and measurable tests. Continue the authentication detector and digital identity verifier as supporting technical workstreams. Complete the networking/Linux baseline and primary-source legal review. Do not build a broad dashboard.

## Decision rule

A phase is not complete because code was written or a workflow turned green. It is complete only when the stated deliverables, tests, provenance, limitations, and review criteria are satisfied.

# Research Portfolio Architecture: CYDRA and Project Frontier

**Status:** Working portfolio note  
**Last reviewed:** 22 November 2026

## Purpose

CYDRA and Project Frontier are complementary but independent research programmes. They share an evidence-first discipline, but they answer different questions and must retain separate scopes, repositories, methods, safety rules and claims.

The relationship is:

- **CYDRA asks:** Does a software system enforce its security properties under a defined, reproducible test?
- **Project Frontier asks:** What evidence, governance requirements and technical safeguards are needed for trustworthy, rights-respecting digital systems in migration and border-management contexts?

CYDRA supplies a technical research discipline and selected reusable lessons. Frontier applies its own multidisciplinary research method to a distinct policy and technology domain. Frontier is not a CYDRA deployment or an operational extension of it.

## Shared research principles

Both programmes follow these principles:

1. State a narrow, answerable question before implementation.
2. Freeze the source, version, assumptions and test conditions.
3. Distinguish observed facts, hypotheses, interpretations and unknowns.
4. Use deterministic methods and reproducible artefacts wherever possible.
5. Preserve negative results, blocked experiments and limitations.
6. Require independent reproduction or review before strong claims.
7. Keep human operators accountable for interpretation and external decisions.
8. Never infer real-world readiness from a prototype or a green CI run.

The common engineering maxim is **“LLMs propose. Tools test. Evidence decides.”**

For Frontier's documentary and policy research, the corresponding rule is **“Sources frame. Methods test. Evidence decides. Humans interpret and remain accountable.”**

## Separation of responsibilities

| Dimension | CYDRA Web3 | Project Frontier |
|---|---|---|
| Primary domain | Solidity/EVM application security | Migration data governance, digital identity, border technology and cyber resilience |
| Initial research problem | Missing or ineffective authorization on externally callable state-changing contract operations | What claims can bounded synthetic data-quality and digital-system experiments support in a rights-respecting governance context? |
| Main methods | Source modelling, authorization hypotheses, local executable experiments, paired controls, causal differential and reproduction | Primary-source and literature review, requirements traceability, threat modelling, synthetic laboratories and independent technical/policy review |
| Evidence objects | Pinned source revisions, model provenance, test traces, raw execution artefacts, control outcomes | Cited sources, page-level notes, research protocols, synthetic contracts/fixtures, test reports and traceability matrices |
| Safety boundary | Explicitly authorised bounty or local test scope; no unapproved live asset interaction | Public sources and synthetic-only data; no real traveller or government operational data; no unauthorised system testing |
| Output type | Bounded technical security evidence and carefully qualified findings | Research papers, policy/technical briefs and narrowly scoped synthetic demonstrations |
| Human responsibility | Operator verifies scope, impact and any disclosure | Researcher interprets evidence, rights implications and policy context |

## What can transfer between projects

The following are transferable as methods, not as automatic evidence:

- Explicit status vocabulary: confirmed, rejected, blocked, unmeasurable, not selected and not run.
- Exact version and provenance tracking.
- Paired positive and negative controls where appropriate.
- Fail-closed handling of missing preconditions.
- Separation of workflow success from research conclusion.
- Reproducible artefacts and transparent limitations.
- A disciplined distinction between a hypothesis and a supported claim.

A CYDRA test result does not validate a Frontier data-governance claim. A Frontier policy source does not establish a CYDRA vulnerability. Each programme must earn its own conclusions.

## Researcher development pathway

Together, the programmes can build a coherent portfolio across:

1. Software security engineering and authorization analysis.
2. Secure data handling, identity assurance and interoperability concepts.
3. Research design, literature synthesis and requirements traceability.
4. Reproducible testing, evidence evaluation and technical communication.
5. Privacy, rights, governance and accountable human review.

These are development objectives, not claims that all competencies have already been independently assessed.

## Portfolio presentation rules

- Keep the repositories separate and link to each other only where useful.
- Do not describe Frontier as a government, immigration or international-organisation project.
- Do not describe CYDRA as a general autonomous vulnerability scanner or claim unverified detection performance.
- Label prototypes, historical CI runs, current branch state and independent reviews accurately.
- Do not add features solely to make either repository look larger.
- Prefer a small number of well-documented, reproducible contributions over commit volume.

## Current portfolio priorities

### CYDRA
1. Resolve the open capability-integration work through regression evidence.
2. Keep the status document aligned with the actual merged baseline and open draft PRs.
3. Demonstrate held-out unfamiliar-target performance only when the full experiment and controls support it.
4. Improve the public README so it accurately describes the current codebase and maturity.

### Project Frontier
1. Finish the requirements-to-evidence comparison for the existing v0.2 synthetic validator.
2. Complete outstanding literature and primary-source reading.
3. Obtain separate independent technical and policy/data-governance reviews.
4. Do not expand the lab until review and requirements justify a change.
5. Prepare a paper only after its contribution and limitations survive those checks.

## Review status

This document is an internal portfolio-architecture note. It does not claim external recognition, independent review, institutional partnership, scholarship eligibility or professional certification. It should be revised when either project's scope or evidence base materially changes.

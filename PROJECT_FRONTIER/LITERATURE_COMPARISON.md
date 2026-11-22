# Project Frontier — Preliminary Literature Comparison

**Version:** 0.1  
**Review date:** 22 November 2026  
**Status:** Exploratory comparison, not a systematic review and not a novelty finding.

## 1. Purpose

This note compares selected migration-data, digital-identity, border-technology and data-governance sources against Frontier's proposed work. It is intended to prevent duplicate effort and unsupported novelty claims. Search coverage is selective; full-text review remains incomplete for some sources.

## 2. Comparison matrix

| Source | Scope and contribution established by the source | Relevance to Frontier | What it does not establish for Frontier |
|---|---|---|---|
| IOM, *Guidelines for the Harmonization of Migration Data Management in the ECOWAS Region* (2019) | Regional guidance on migration concepts, data sources, collection, analysis, dissemination, sharing and coordination; includes an action plan. | Direct regional baseline. Frontier's data contract and quality dimensions should be mapped to the guideline's concepts and data lifecycle. | It does not validate Frontier's software or establish current implementation across ECOWAS states. |
| IOM, *Enhancing Migration Data Management in Nigeria: Assessment and Recommendations* (2013) | Country assessment describing migration data sources and agency processes, with recommendations on data use, sharing and quality. | Nigeria-specific historical baseline; important comparator before describing any Nigerian data-management problem as new. | It is a 2013 assessment and cannot establish the present state of agency systems. |
| IOM, *The Essentials of Migration Data* (2026) | Consolidated guide covering migration statistics, concepts, data sources, governance, data lifecycle, sharing, protection and analysis. | Current broad reference for terminology and migration-data lifecycle; use it to check the first paper's scope and definitions. | A guide is not a direct evaluation of Frontier's prototype and does not prove implementation outcomes. |
| IOM, *Harnessing Data Innovation for Migration Policy* (2023) | Practitioner handbook on non-traditional data, methods, data access, collaboration, ethics, security and protection. | Helps bound future use of novel data sources and reinforces ethics and access constraints. | Frontier's first synthetic study does not use non-traditional real-world sources. |
| Uzomah (2024), *European Union border technology in Africa: Experiences en route* | Scholarly study of technology-enabled border governance and mobility/rights consequences in African contexts, including Nigeria-related material in its abstract. | Governance and rights context; technical design must be evaluated alongside social and institutional consequences. | It is not a benchmark of Frontier's software or a general measurement of system performance. Full-text annotation remains incomplete. |
| Iwuoha & Doevenspeck (2023 online; 2025 issue), *Dilemmas of 'biometric nationality'* | Qualitative scholarship on biometric identity, migration control and political mobilisation in West Africa. | Requires Frontier to distinguish biometric enrolment, identity claims, nationality and legal status, and to consider political and rights risks. | It does not provide a technical performance evaluation of a data-quality validator. Full-text annotation remains incomplete. |
| Iwuoha (2025), *European Biometric Borders and (Im)Mobilities in West Africa* | Examines biometric border practices, mobility and migrant strategies in West African settings. | Strong critical context for the second research theme; warns against technology-only accounts. | Its geography and qualitative arguments should not be generalised to every ECOWAS country or treated as a technical audit. |
| Ibor et al. (2025), *Considerations for trustworthy cross-border interoperability of digital identity systems in developing countries* | Examines cross-border foundational identity interoperability, trust relationships, governance, legal and technical requirements, and compares approaches including eIDAS and X-Road. | Direct comparator for identity federation, trust frameworks, data exchange, privacy, security and institutional accountability. | It is not a migration-event data quality study and does not establish that any particular national system meets the proposed requirements. |
| ECOWAS Commission (10 May 2026), MIDWA ministerial meeting announcement | Reports endorsement of a Border Management Strategy and Action Plan and priorities including linking systems such as MIDAS and PISCES; reports ENBIC deployment statements. | Current policy context for interoperability and border management; provides specific public claims to verify against formal strategy documents. | A press release is not the strategy text, technical architecture, independent evaluation or proof of operational interoperability. |
| Nigeria Data Protection Act 2023 and NDPC GAID 2025 | Primary Nigerian legal/regulatory materials governing personal-data processing and implementation. | Must inform any future real-data proposal, synthetic-data boundary and governance-control mapping. | Mentioning the law does not prove a design is compliant; applicability depends on facts, roles and processing. Obtain qualified legal review for compliance claims. |

## 3. Preliminary findings

### Finding 1 — Migration-data harmonisation is established work

ECOWAS/IOM regional guidance has already addressed migration definitions, data sources, collection, analysis, dissemination and sharing. IOM also published a Nigeria-specific assessment in 2013 and a broad migration-data guide in 2026.

**Consequence:** Frontier must not present migration data quality or harmonisation as a newly discovered problem. The first paper must identify a narrow technical question not already answered by those guides, and explain how its experiment relates to the established migration-data lifecycle.

### Finding 2 — Digital identity interoperability is an established African research topic

Ibor et al. (2025) directly address trustworthy cross-border identity interoperability in developing-country/African settings, including trust frameworks and technical, institutional and legal requirements.

**Consequence:** Frontier's second theme cannot claim novelty merely by proposing secure digital identity interoperability in Africa. It needs a more precise question, perhaps a comparative assessment of specific assurance, provenance, access-control or accountability requirements against defined ECOWAS instruments—subject to a fuller review.

### Finding 3 — Border technology must be analysed as governance, not just engineering

Uzomah and Iwuoha's scholarship shows that biometric and digital border technologies raise questions about mobility, rights, political use, identity and institutional power.

**Consequence:** A technically correct validator or identity verifier is not, by itself, evidence of a trustworthy or legitimate border system. Rights and governance constraints must shape the research question and evaluation criteria from the beginning.

### Finding 4 — The 2026 ECOWAS policy announcement makes interoperability timely, but not a licence to speculate

The ECOWAS Commission reported ministerial endorsement of a Border Management Strategy and Action Plan, with a proposed integrated platform linking systems such as MIDAS and PISCES.

**Consequence:** This creates a timely documentary-research lead. Frontier must obtain and examine the formal strategy/action plan and distinguish official commitments, proposals, deployments and demonstrated operational outcomes. Do not infer architecture or security weaknesses from a press release.

## 4. Revised assessment of Frontier's possible contribution

At this stage, **no defensible research gap or originality claim has been established**.

The existing Migration Data Quality Laboratory may support a useful applied methods paper, but its current scope is a narrow synthetic record validator. Before treating it as a research contribution, we must establish:

1. Which migration-data quality requirements are already specified in IOM/ECOWAS guidance and the 2026 IOM guide.
2. Which requirements are measurable at the record level and which require source-level, institutional or population-level evidence unavailable to a synthetic lab.
3. Whether the prototype tests add reproducible value beyond ordinary schema validation.
4. Whether its provenance and duplicate/conflict diagnostics are conceptually sound and transparently reported.
5. Whether the test suite includes counterexamples, boundary cases and false-assurance tests.
6. Whether independent reviewers agree that the experiment answers a worthwhile, bounded question.

A defensible initial framing is therefore:

> **A reproducible design-and-evaluation study of a privacy-minimising synthetic validator for a narrowly defined migration-event data contract.**

This is a description of the work, not a novelty claim. The paper should be submitted only if the traceability matrix and independent review show a meaningful contribution.

## 5. Recommended technical evaluation matrix for the first paper

| Dimension | Research question for the lab | Evidence required | Known limitation |
|---|---|---|---|
| Completeness | Does the validator detect missing required fields under the declared contract? | Requirement-to-test mapping and positive/negative fixtures. | Does not show whether a real source captured all events. |
| Validity | Does it reject values outside declared types, formats and controlled sets? | Boundary tests, malformed values and documented allowlists. | A valid value may still be factually false. |
| Consistency | Does it detect defined internal contradictions and timestamp-order violations? | Explicit rules and counterexample fixtures. | Cannot establish consistency across agencies without linked source data. |
| Uniqueness/conflict | Does it distinguish exact duplicates from conflicting reuse of identifiers as specified? | Canonicalisation rules, duplicate and collision fixtures. | Does not prove source identifiers are globally unique. |
| Timeliness | Are ingestion-lag calculations correct against a declared reference time? | Fixed-clock tests, timezone cases, metric denominator. | Synthetic timestamps do not estimate operational reporting delays. |
| Provenance | Are source references syntactically validated and diagnostics traceable to input records? | Provenance contract, malformed token cases, traceability tests. | A token pattern is not proof of source authenticity or chain of custody. |
| Privacy minimisation | Does the contract avoid unnecessary direct identifiers and does output avoid leaking disallowed fields? | Field inventory, adversarial fixtures, output inspection. | Synthetic data does not itself prove legal compliance or privacy safety in deployment. |
| Reproducibility | Can another reviewer repeat the same run and reconcile outputs? | Frozen commit, environment, commands, deterministic fixtures and hashes. | Reproducibility does not establish external validity. |

## 6. Immediate research actions

1. Obtain and read the complete IOM ECOWAS guidelines (2019), Nigeria assessment (2013), and IOM Essentials of Migration Data (2026), extracting page-level requirements relevant to data quality, definitions, administrative sources, sharing and protection.
2. Read the full Ibor et al. (2025) paper and finish the full-text annotations for Uzomah and Iwuoha & Doevenspeck.
3. Obtain the formal ECOWAS Border Management Strategy and Action Plan referenced in the May 2026 announcement; do not substitute the press release for the strategy.
4. Map every current v0.2 validator rule and test to the IOM/ECOWAS concepts and the proposed evaluation matrix.
5. Identify what the prototype cannot test and remove any claim that overreaches those limits.
6. Request independent technical review only after the exact implementation, contract, tests and traceability matrix are frozen.
7. Keep the first paper on hold until the review identifies a worthwhile and supportable contribution.

## 7. Source register

- IOM (2019), *Guidelines for the Harmonization of Migration Data Management in the ECOWAS Region*: https://publications.iom.int/books/guidelines-harmonization-migration-data-management-ecowas-region
- IOM (2013), *Enhancing Migration Data Management in Nigeria: Assessment and Recommendations*: https://publications.iom.int/books/enhancing-migration-data-management-nigeria-assessment-and-recommendations
- IOM (2026), *The Essentials of Migration Data*: https://publications.iom.int/books/essentials-migration-data-emd-iom-guide-migration-data-and-statistics
- IOM (2023), *Harnessing Data Innovation for Migration Policy*: https://publications.iom.int/books/harnessing-data-innovation-migration-policy-handbook-practitioners
- Uzomah (2024), *European Union border technology in Africa: Experiences en route*: https://doi.org/10.1002/psp.2824
- Iwuoha & Doevenspeck (2023/2025), *Dilemmas of 'biometric nationality'*: https://doi.org/10.1080/21622671.2023.2205885
- Iwuoha (2025), *European Biometric Borders and (Im)Mobilities in West Africa*: https://doi.org/10.1111/polp.12653
- Ibor et al. (2025), *Considerations for trustworthy cross-border interoperability of digital identity systems in developing countries*: https://doi.org/10.1007/s00146-024-02008-9
- ECOWAS Commission (10 May 2026), *Interior Ministers from ECOWAS Member States Commit to Harmonized Migration Governance and Integrated Border Management*: https://www.ecowas.int/interior-ministers-from-ecowas-member-states-commit-to-harmonized-migration-governance-and-integrated-border-management/
- Nigeria Data Protection Commission, *Nigeria Data Protection Act 2023 / General Application and Implementation Directive 2025*: https://ndpc.gov.ng/wp-content/uploads/2025/03/NDP-ACT-GAID-2025-MARCH-20TH.pdf

## 8. Review caveat

This is a selective preliminary comparison based on the source material listed above. It is not a systematic review, legal opinion, security assessment, or evidence of any agency's current system condition. Claims about implementation, operational performance, legal compliance or novelty require further primary evidence and qualified independent review.


## 9. Full-text reading note — Ibor et al. (2025)

**Source:** Ibor, A., Hooper, M., Maple, C., Crowcroft, J. & Epiphaniou, G. (2025). *Considerations for trustworthy cross-border interoperability of digital identity systems in developing countries*. AI & Society, 40, 2729–2750. DOI: 10.1007/s00146-024-02008-9. Open full text inspected via PubMed Central.

### Research purpose and method visible in the paper

The authors examine requirements and challenges for trustworthy cross-border interoperability of foundational identity systems in developing-country/African settings. They compare two existing interoperability approaches—Estonia's X-Road and the EU's eIDAS—and propose a process-based way to scope requirements across identity-management stages. The paper is a conceptual/technical requirements analysis, not an empirical evaluation of ECOWAS or Nigerian operational systems.

### Important distinctions for Frontier

1. **Data exchange is not identity proofing.** The paper explicitly notes that X-Road does not verify or validate end-user identity data; it provides a secure data-exchange layer. Frontier must not conflate a secure connection or interoperable message with proof that an identity claim is true.
2. **Organisational access is not end-user authorisation.** The paper explains that X-Road's infrastructure addresses organisational-level access, while the service client remains responsible for end-user authorisation inside its own information system. This is a useful design distinction for Frontier's security-control matrix.
3. **Trust is sociotechnical and legal.** The paper discusses bilateral agreements, differing laws, dispute resolution, certification compatibility, assurance levels and trust relationships, in addition to cryptographic controls.
4. **Auditability and accountability matter.** Its discussion of signed, timestamped message exchange provides a comparator for evidence of data exchange, while warning that trust-service configuration and certificate-status differences can affect assurance.
5. **Interoperability does not remove privacy risk.** The authors identify risks where a partner organisation's weak internal access management could expose shared data. This supports least-privilege, purpose-bound access, logging and partner accountability as requirements to investigate—not as controls already proven by Frontier.

### Direct implications for the Frontier workstreams

- The digital identity verifier should make a strictly limited claim about the integrity and validation of a fictional credential under its configured rules. It must not claim to prove a person's real identity or legal status.
- The secure-interoperability study should separate at least four layers: identity proofing/credential issuance; authentication and assertions; secure message/data exchange; and authorisation within the receiving organisation.
- A synthetic architecture experiment could test whether an event exchange records the sender, recipient, purpose, timestamp, schema version and access decision without exposing unnecessary identity data. This is a possible future experiment, not yet designed or validated.
- A governance matrix should include trust agreements, assurance levels, revocation/status checking, end-user authorisation, dispute handling, audit evidence and privacy safeguards.

### Limitations

The paper compares X-Road and eIDAS and proposes requirements for African settings; it does not establish the actual architecture, legal basis, security posture or operational performance of Nigeria's or ECOWAS's systems. Its broad African framing should not be treated as uniform evidence across countries. The paper itself notes that other interoperability solutions were not considered.

**Reading status:** Full-text page reviewed, including introduction, X-Road/eIDAS comparison, challenges, trust relationships and assurance-level sections. A final manuscript-quality annotation should still capture the conclusion and references in full.


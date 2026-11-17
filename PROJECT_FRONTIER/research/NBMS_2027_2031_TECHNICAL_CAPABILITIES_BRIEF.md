# Research Brief 01 — Technical Capabilities for Nigeria's 2027–2031 National Border Management Strategy

**Project:** Project Frontier — International Border Security, Technology & Intelligence Initiative  
**Version:** 0.1 — evidence-led discussion draft  
**Research cut-off:** 17 November 2026  
**Status:** Independent portfolio research; not an NIS document, official recommendation, or statement of the final 2027–2031 strategy.

## Executive summary

The Nigeria Immigration Service (NIS) reports that it and the International Organization for Migration (IOM), with European Union support, reviewed the 2019–2023 National Border Management Strategy in a 27–30 September 2026 workshop to prepare for the 2027–2031 policy cycle. The NIS account identifies three priorities for the next cycle: **credible migration data, effective implementation mechanisms, and sustained inter-agency collaboration**. It also says the workshop outcomes and proposed strategic direction were reviewed through an NIS Executive Management Endorsement Session. The public report does not reproduce the complete final 2027–2031 strategy or its detailed action plan. This brief therefore treats the three priorities as publicly reported strategic signals, not as a complete approved policy text.

A practical technology programme should connect those priorities rather than treat cybersecurity, data quality, digital identity and interoperability as isolated IT projects. The recommended sequence is: establish accountable data governance; define shared data and exchange contracts; protect systems and information; provide trustworthy identity/document assurance; and measure implementation outcomes with privacy, rights and human review built in.

## 1. What the public evidence establishes

### 1.1 National policy signal

The NIS public account says the next strategy should be anchored on credible migration data, effective implementation mechanisms and sustained inter-agency collaboration. The same report says the review considered emerging border-management and security challenges, implementation priorities, financing options and an integrated border-management direction. It does **not** publish the full final strategy, a complete list of workstreams, approved budgets, performance baselines or agency-level responsibilities.

### 1.2 NIS mandate and organisational context

The NIS describes its statutory functions as controlling persons entering and leaving Nigeria, issuing travel documents and residence permits, conducting border surveillance and patrol, and enforcing laws within its mandate. Its published organisational structure includes directorates for Border Management, Migration, Investigation and Compliance, ICT and Cyber Security, Passport and Other Travel Documents, Visa and Residency, and Planning, Research and Statistics. This supports a cross-functional approach: border processes depend on operational, technical, analytical, legal and service-delivery capabilities working together. It does not establish that any particular directorate owns every recommendation in this brief.

### 1.3 Regional interoperability signal

In May 2026, ECOWAS reported that Ministers responsible for interior, immigration and border management endorsed a regional Border Management Strategy and Action Plan. The ECOWAS account describes priority actions including an integrated platform to link border-management information systems such as MIDAS and PISCES, and regional work toward mutual acceptance of the ECOWAS National Biometric Identity Card at air, land and sea borders. These are regional policy developments; they should not be presented as proof that a specific Nigerian national integration has already been completed or that all technical/legal arrangements are settled.

### 1.4 Data protection and rights obligations

The Nigeria Data Protection Act 2023 sets principles for personal-data processing including fairness, lawfulness and transparency; specified purposes; data minimisation; retention limits; accuracy; and appropriate security. Sections 24 and 39 address processing principles and security, integrity and confidentiality. Section 28 provides for a data privacy impact assessment where processing is likely to create high risk to individuals' rights and freedoms. Section 37 addresses decisions based solely on automated processing that produce legal or similarly significant effects and provides safeguards including human intervention, the ability to express a point of view and contest the decision. Section 41 governs transfers of personal data outside Nigeria. The Act contains specific exemptions and qualifications; any operational application requires legal review of the facts and applicable provisions, not a blanket assumption that national-security work is either wholly exempt or wholly unrestricted.

## 2. Recommended capability framework

The following are **Project Frontier recommendations for consideration and validation**, not claims about what the unpublished final NBMS already contains.

### Capability A — Trusted migration data governance

Establish a common data-governance model before expanding analytics or dashboards.

Recommended components:
- A shared data dictionary defining event types, field meanings, allowed values, time semantics and provenance.
- Named data owners and stewards for each authoritative dataset, with documented correction and escalation routes.
- Validation rules for completeness, validity, consistency, uniqueness, timeliness and provenance.
- Reconciliation procedures for duplicate, conflicting and late-arriving records; preserve source lineage and never silently overwrite conflicts.
- Versioned schemas, controlled change management and documented data-quality limitations.
- Published aggregate statistics only where disclosure risk, methodology and representativeness have been assessed.

Potential measures (establish baselines before setting targets):
- Completeness rate by field and dataset, with denominators.
- Duplicate and conflict rates, separated by category.
- Share of records with valid source provenance and timestamps.
- Ingestion-lag distributions, with median and upper percentiles once sample size and method are defensible.
- Reconciliation backlog and time to resolve material data-quality defects.

**Frontier link:** the synthetic Migration Data Quality Laboratory demonstrates a narrow set of validation and audit concepts. Its fictional records do not measure Nigeria's actual migration data quality.

### Capability B — Secure and accountable interoperability

Inter-agency collaboration needs more than a shared platform. It needs governed exchange.

Recommended components:
- A documented inventory of systems, datasets, owners, purposes and legal authority for each exchange.
- Data-sharing agreements that specify purpose, minimum fields, permitted recipients, retention, onward disclosure, incident handling, correction and audit responsibilities.
- Common data definitions and versioned machine-readable interfaces; validate message schemas before exchange.
- Strong service identity, least-privilege access, mutual authentication where appropriate, encryption in transit and at rest, and auditable access logs.
- Segmented environments, controlled integration gateways, rate limits, monitoring, tested recovery and documented failure handling.
- A non-production conformance environment using synthetic data before any live interconnection.

Interoperability should not mean unrestricted pooling. Each receiving agency should receive only the fields necessary for its lawful function. A technical connection does not itself establish lawful authority to disclose or process personal data.

### Capability C — Cybersecurity and operational resilience

Treat border-management information systems as critical public-service systems whose confidentiality, integrity and availability all matter.

Recommended components:
- Asset and data-flow inventories; documented system owners and security responsibilities.
- Identity and access management, multi-factor authentication where feasible, privileged-access controls and periodic access recertification.
- Secure configuration, vulnerability and patch management, endpoint protection, network segmentation and secure software-development practices.
- Centralised, time-synchronised security logging with access controls, retention rules and incident-response procedures.
- Tested backup, restoration and continuity plans for outages, cyber incidents and infrastructure disruption.
- Tabletop exercises involving ICT, operational, legal, communications and partner-agency roles.

Measures should include service availability, recovery-test results, patch exposure, privileged-account review completion, incident detection/response times and lessons closed. Avoid claiming that a SIEM, dashboard or number of alerts is a security outcome by itself.

### Capability D — Digital identity and travel-document assurance

Identity assurance should verify a specific claim for a defined purpose; it should not turn a biometric match or document scan into an unreviewable determination of a person's legal status.

Recommended components:
- Document and credential authenticity checks, issuer validation and certificate/key lifecycle management.
- Clear handling for expired, revoked, damaged, unreadable or inconsistent credentials.
- Separation of identity proofing, authentication, travel-document validity and immigration-status decisions.
- Human review and accessible escalation for false matches, system outages and disputed records.
- Privacy and security assessment before any biometric processing, including purpose limitation, minimisation, retention, access, accuracy, redress and breach response.
- Interoperability testing that respects the legal and technical conditions for cross-border data transfer.

The ECOWAS report makes regional identity interoperability a relevant policy consideration. It does not remove the need for national legal authority, safeguards, technical conformance and human accountability.

### Capability E — Implementation, workforce and performance governance

The public NIS workshop report explicitly refers to implementation mechanisms, financing options and inter-agency collaboration. A credible action plan should translate policy into accountable delivery.

Recommended components:
- A delivery matrix: objective, lead agency, supporting agencies, accountable senior owner, dependencies, budget, milestones and evidence of completion.
- A governance forum with decision rights, escalation paths, documented minutes and a process for resolving cross-agency data and technology disputes.
- Workforce mapping and role-based training across border operations, ICT, data governance, legal/privacy, research and incident response.
- Procurement and vendor governance: security requirements, data ownership, audit rights, exit plans, portability and incident obligations.
- Periodic independent assurance and public reporting of suitable aggregate progress indicators.

A training attendance count is an input, not proof of competence. Use practical assessments, exercises and post-training performance evidence.

## 3. Sequencing proposal

| Phase | Priority | Minimum evidence before moving forward |
|---|---|---|
| 1. Baseline | Map mandates, datasets, systems, owners, data flows, legal bases, risks and current performance | Approved inventory, gap register, baseline metrics and accountable owners |
| 2. Governance | Agree data dictionary, quality rules, sharing principles, retention and escalation | Signed governance artefacts and tested synthetic examples |
| 3. Secure foundations | Strengthen identity/access, logging, segmentation, backups and incident processes | Access review, incident exercise, recovery test and remediation record |
| 4. Controlled interoperability | Pilot one bounded exchange in a non-production environment before live deployment | Interface contract, legal approval, security assessment, audit evidence and rollback plan |
| 5. Assurance and scale | Evaluate outcomes, rights impacts, cost, reliability and workforce capability | Independent review, measurable benefits, unresolved-risk disclosure and explicit scale decision |

The phases are a proposed sequence, not a statement of the NIS's current implementation plan.

## 4. Rights, privacy and accountability safeguards

At minimum, any future programme involving personal data should:
1. Identify and document the lawful basis and specific purpose before collection or exchange.
2. Collect the minimum data needed and define retention and deletion rules.
3. Assess accuracy, correction mechanisms and the consequences of erroneous records.
4. Conduct a DPIA where the Act requires it; assess necessity, proportionality, risks and safeguards.
5. Restrict access by role and purpose; log access and review misuse.
6. Provide human review, a route to challenge significant automated outcomes, and a way to correct disputed data where applicable.
7. Assess cross-border transfers under the Act before personal data is transferred outside Nigeria.
8. Test breach response, restoration and accountability arrangements.

These are design recommendations informed by the Act, not legal advice or a substitute for the responsible agency's legal and data-protection review.

## 5. Evidence gaps and research questions

The following remain unknown from the public sources reviewed:
- The complete approved 2027–2031 NBMS and its final action plan, budgets and indicators.
- The current baseline quality, coverage and interoperability of Nigerian migration datasets.
- The actual system architecture, interfaces, security controls and operational performance of NIS or partner-agency platforms.
- The formal legal instruments and data-sharing arrangements for each inter-agency or cross-border exchange.
- The detailed procurement, workforce and implementation constraints.

Next research should seek publicly available final strategy and action-plan documents, relevant legislation and regulations, published programme evaluations, and official regional interoperability specifications. Do not infer operational gaps from the absence of public detail.

## 6. Project Frontier application

Project Frontier can responsibly demonstrate transferable skills without access to government systems:

- **Migration Data Quality Laboratory:** synthetic schema validation, duplicate/conflict classification, provenance, missingness and reproducible metrics.
- **Security Monitoring Laboratory:** defensive detection logic and alert-quality testing using synthetic logs.
- **Digital Identity Laboratory:** fictional credential validation, issuer trust, expiry/revocation concepts and privacy-minimised audit.
- **Research portfolio:** source-checked policy briefs, evidence registers and transparent limitations.

No lab should use real traveller, passport, NIN, biometric, personnel or government operational data. No government or third-party system should be scanned, tested or integrated without explicit written authorisation.

## 7. Conclusion

The public policy signal is clear but bounded: NIS has identified credible migration data, implementation and sustained inter-agency collaboration as priorities for the 2027–2031 strategy cycle. The regional ECOWAS agenda reinforces the importance of interoperable border systems, while Nigeria's data-protection framework requires careful attention to purpose, minimisation, accuracy, security, accountability and safeguards around significant automated decisions.

The practical recommendation is to build trustworthy foundations first. Better data governance and secure, auditable exchange should precede sophisticated analytics. Digital identity assurance should remain purpose-specific and reviewable. Progress should be judged by verified outcomes, not by the existence of platforms or dashboards.

---

## Source register

All sources below are official institutional or legal sources. Accessed 17 November 2026.

| ID | Source | Date / locator | Claims supported | Limitation |
|---|---|---|---|---|
| S1 | Nigeria Immigration Service, [NIS, IOM Review Strategic Framework for Effective Border Management](https://immigration.gov.ng/nis-iom-review-strategic-framework-for-effective-border-management/) | 1 Oct 2026; workshop held 27–30 Sep 2026 | Preparation for 2027–2031 policy cycle; three publicly stated priorities; workshop review and endorsement process | Does not reproduce the full final strategy/action plan |
| S2 | Nigeria Immigration Service, [Organisational Structure](https://immigration.gov.ng/nis-structure/) | Official web page; accessed 17 Nov 2026 | Public directorate structure including Border Management, Migration, ICT and Cyber Security, and Planning, Research and Statistics | Structure page does not establish project-level ownership or internal system architecture |
| S3 | Nigeria Immigration Service, [Our Core Mandate](https://immigration.gov.ng/our-core-mandate/) | Official web page; accessed 17 Nov 2026 | Public description of statutory functions | For legal interpretation, consult the Act itself and qualified counsel |
| S4 | Federal Republic of Nigeria, [Nigeria Data Protection Act 2023](https://ndpc.gov.ng/wp-content/uploads/2024/03/Nigeria_Data_Protection_Act_2023.pdf) | Act No. 37, 12 Jun 2023; especially ss. 24, 28, 37, 39–41 | Data-processing principles, DPIA, safeguards for significant solely automated decisions, security and cross-border transfers | Specific application depends on facts, lawful basis, exemptions and other applicable law |
| S5 | ECOWAS Commission, [Interior Ministers Commit to Harmonized Migration Governance and Integrated Border Management](https://www.ecowas.int/interior-ministers-from-ecowas-member-states-commit-to-harmonized-migration-governance-and-integrated-border-management/) | 10 May 2026; MIDWA ministerial meeting 29 Apr 2026 | Regional strategy/action-plan endorsement, MIDAS/PISCES interoperability proposal, ENBIC and regional training priorities | Regional policy signal; not proof of completed national technical integration |

## Research method and confidence

- Prioritised primary official sources and the enacted statute.
- Distinguished reported institutional facts from Project Frontier recommendations.
- Did not infer system vulnerabilities, data-quality deficiencies, implementation status or operational performance.
- Confidence is **high** for what the cited sources explicitly state; **moderate** for the capability implications derived from those statements; **low / unknown** for current operational baselines and implementation gaps because public evidence reviewed does not establish them.

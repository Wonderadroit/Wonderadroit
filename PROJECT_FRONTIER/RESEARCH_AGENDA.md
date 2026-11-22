# Project Frontier — Initial Research Agenda

**Version:** 0.1  
**Date:** 22 November 2026  
**Status:** Candidate questions; not yet approved as completed studies

This agenda narrows the programme-level question in `RESEARCH_SCOPE.md` into three studies. Each study must distinguish what public sources establish from what Frontier proposes or tests.

## Research Question 1 — Migration-event data quality (first technical paper)

**Proposed title:** *A Reproducible, Privacy-Minimising Approach to Migration-Event Data Quality Testing: Design and Evaluation of a Synthetic Laboratory.*

**Question:** Can a narrowly specified, reproducible validation pipeline identify defined completeness, validity, consistency, uniqueness, timeliness and provenance defects in fictional migration-event records while minimising personal data exposure and preserving diagnostic traceability?

**Why first:** Frontier already has a working synthetic Migration Data Quality Laboratory v0.2, a documented data contract and test plan, deterministic CLI outputs, 45 passing regression tests in a recorded Python 3.12 CI run, and a review request. This gives us a real artefact to evaluate rather than an abstract proposal.

**Method:**
1. Freeze the exact code commit, contract and test-plan versions under review.
2. Obtain independent review of implementation semantics, test adequacy, privacy boundaries and metric denominators.
3. Build a test-to-requirement traceability matrix.
4. Report test coverage by quality dimension and documented edge cases.
5. Run the fixed synthetic fixture and additional explicitly described synthetic cases.
6. Report failures, false assurances, limitations and what the experiment cannot establish.

**Evidence boundary:** The study can evaluate the behaviour of the prototype against its declared synthetic contract. It cannot estimate the quality of Nigerian migration data, establish the existence of operational data defects, validate an agency's systems or demonstrate operational readiness.

**Publication gate:** Independent technical review completed; substantive findings resolved or transparently accepted; reproducible commands and artefacts identified; policy claims checked separately by a qualified reviewer.

## Research Question 2 — Digital identity and border technology in West Africa

**Proposed title:** *Digital Identity at West African Borders: Interoperability, Identity Assurance, Data Protection and Mobility Governance.*

**Question:** What technical, legal and governance conditions are necessary for digital identity and biometric border technologies to support reliable identity assurance and legitimate regional mobility without creating avoidable exclusion, privacy or accountability harms?

**Why it matters:** Published research by Victor Chidubem Iwuoha examines biometric identity, border securitisation, migration control and mobility in West Africa. Ngozi Louis Uzomah's research examines cross-border mobility, forced displacement, return and reintegration, border technologies and migration justice/data ethics. Frontier should engage this scholarship critically rather than assume that technology is inherently beneficial.

**Method:**
- Structured review of peer-reviewed studies and official ECOWAS, Nigerian and international sources.
- Define terms carefully: identity proofing, authentication, biometric matching, document verification, interoperability and identity resolution are not interchangeable.
- Compare stated system objectives with documented legal, institutional and rights safeguards.
- Identify where evidence is contested or geographically limited.
- Produce a governance and technical-control matrix; do not test real identity systems.

**Evidence boundary:** A documentary study can identify arguments, documented cases, standards and governance requirements. It cannot independently establish the performance or current deployment status of Nigerian border systems without reliable direct evidence.

## Research Question 3 — Secure and accountable interoperability

**Proposed title:** *Beyond Connectivity: Security, Data Governance and Accountability Requirements for Interoperable Border-Management Information Systems in West Africa.*

**Question:** What minimum governance and cybersecurity controls should be addressed before migration or border-management information systems exchange data across agencies or jurisdictions?

**Why it matters:** Regional policy discussions include interoperability, shared information platforms and cooperation. A technical connection alone does not establish lawful authority, data quality, security or accountability.

**Method:**
- Analyse public regional and national policy sources.
- Map data-sharing lifecycle risks: purpose, authority, minimisation, identity and access management, authentication, encryption, logging, retention, correction, incident response and oversight.
- Use a synthetic architecture and threat model to test design assumptions.
- Produce a control matrix that distinguishes mandatory legal requirements, standards-based recommendations and Frontier proposals.

**Evidence boundary:** The study will be a documentary and synthetic architecture analysis. It will not connect to, scan or test NIS, ECOWAS, police, government or partner systems.

## Priority and sequencing

| Priority | Study | Reason |
|---|---|---|
| 1 | Migration-event data quality | Existing code and test evidence make it the most concrete first paper; independent review is the immediate gate. |
| 2 | Digital identity and border technology | Builds directly on relevant West African scholarship and Frontier's digital identity workstream. |
| 3 | Secure interoperability | Integrates data governance, cybersecurity and institutional cooperation after the first two studies establish stronger foundations. |

## Initial literature and source map

### A. Ngozi Louis Uzomah

Institutional profile: Toronto Metropolitan University, Bridging Divides, Visiting Fellows.

The profile describes research on cross-border mobility, forced displacement, return and reintegration policies in West Africa, EU border technologies in Africa, ECOWAS border-region trade and Lake Chad displacement. It also identifies a collaborative research interest in digital technologies, cross-border movement, mobility governance, migration justice and data ethics.

Selected starting publications listed by the profile:
- Uzomah and Madu (2025), *Reassessing return migration governance: insights on Nigeria's return migration infrastructures*, GAPs Country Dossier WP3.
- Uzomah, Madu, Ajaero and Ezea (2024), *Navigating the complexities of return migration and reintegration: challenges and opportunities for Nigerian migrants from North Africa in the context of EU policies*, GAPs Working Paper.

Research use: useful for the migration-governance, return/reintegration and mobility-justice context. Do not assume his work is primarily cybersecurity engineering.

### B. Victor Chidubem Iwuoha

Institutional profile: University of Bayreuth / Bayreuth Academy of Advanced African Studies.

Selected starting publications:
- Iwuoha and Doevenspeck (2023; journal issue 2025), “Dilemmas of ‘biometric nationality’: migration control, biometric ID technology and political mobilisation of migrants in West Africa,” *Territory, Politics, Governance*.
- Iwuoha (2025), “European Biometric Borders and (Im)Mobilities in West Africa: Reflections on Migrant Strategies for Border Circumvention and Subversion,” *Politics and Policy*.
- Iwuoha (2025), “European Biometric ID Program in West Africa: Between European External Border Securitization and ECOWAS Free Movement,” *African Security*.
- Iwuoha (2026), “European Migration Control and the Migrant Smuggling Enterprise in West Africa: Using the Concept of Biometricycle to Explain the ‘Corporate Smuggling’ Dimensions,” *Society*.

Research use: essential critical scholarship for biometric border systems, identity, securitisation, mobility and unintended consequences. Treat the author's claims and conceptual frameworks as scholarly arguments to analyse, not as automatically established facts or as a complete technical assessment of system performance.

### C. Institutional and policy research comparators

- ICMPD Research Unit: policy-oriented, empirical, interdisciplinary and international migration research. Its 2025 working paper *Advances in Border Management: Digitalisation Trends and Emerging Technologies* is directly relevant to the technology/governance intersection.
- Nigeria Immigration Service: primary source for its public mandate, directorate structure and publicly reported strategic-planning statements.
- ECOWAS Commission: primary source for regional free-movement and border-management policy statements.
- Nigeria Data Protection Commission / Nigeria Data Protection Act 2023: primary legal and regulatory materials for privacy, processing, security and rights safeguards.
- IOM and UNODC: institutional sources for migration data, migration management, trafficking and migrant-smuggling context; use specific reports rather than broad institutional descriptions.

## Reading protocol

For each selected paper:
1. Read the abstract and research question.
2. Identify theoretical framework and key definitions.
3. Record geography, period, sample/data and methods.
4. Separate empirical findings from interpretation and normative argument.
5. Record limitations and what the study does not claim.
6. Note technical questions the study leaves unanswered.
7. Compare with at least one primary policy or legal source.
8. Record how Frontier's proposed work adds evidence without claiming novelty prematurely.

## Source links

- Uzomah institutional profile: https://www.torontomu.ca/bridging-divides/people/visiting-fellows/future-leaders-fellows/ngozi-uzomah/
- Uzomah research profile: https://migrationresearch.com/experts/ngozi-l-uzomah/2340
- Iwuoha institutional profile: https://www.bayreuth-academy.uni-bayreuth.de/en/people/Fellows-list/24Victor-Chidubem-Victor/index.php
- Iwuoha (2023/2025), *Dilemmas of biometric nationality*: https://doi.org/10.1080/21622671.2023.2205885
- Iwuoha (2025), *European Biometric Borders and (Im)Mobilities in West Africa*: https://doi.org/10.1111/polp.12653
- Iwuoha (2025), *European Biometric ID Program in West Africa*: https://doi.org/10.1080/19392206.2025.2491206
- Iwuoha (2026), *European Migration Control and the Migrant Smuggling Enterprise in West Africa*: https://doi.org/10.1007/s12115-026-01169-1
- ICMPD Research: https://www.icmpd.org/our-work/policy-and-research/research
- ICMPD Research publications: https://research.icmpd.org/publications/

## Immediate next actions

1. Confirm this research scope against the existing charter and NIS technical-capabilities brief.
2. Read at least two full papers by Iwuoha and the relevant Uzomah working paper(s), taking structured notes.
3. Identify a suitable independent technical reviewer and policy reviewer; do not count the author or an AI-generated critique as independent review.
4. Prepare the first paper only after the review gate and traceability matrix are complete.
5. Contact researchers with a concise, specific request for scholarly feedback—not an implied request for endorsement or employment.


---

## Preliminary literature analysis — first reading pass

**Reading date:** 22 November 2026  
**Status:** Preliminary source-based notes. These are not a systematic review and do not substitute for reading every section, checking cited evidence, or obtaining author clarification.

### Study A — Uzomah (2024)

**Citation:** Uzomah, N. L. (2024). *European Union border technology in Africa: Experiences en route*. Population, Space and Place, 30(8), e2824. https://doi.org/10.1002/psp.2824

**Source inspected:** Publisher article page, abstract and visible reference list.

**Research purpose and scope:** Examines the effects of technology-enabled border governance associated with EU externalisation in Africa. The abstract identifies MIDAS deployment in Nigeria, risk-analysis cells in Niger and biometric registration in Mauritania.

**Method reported:** Non-participant observation, informal/instant interactions and 78 semi-structured interviews with migrants, cross-border traders, government officials, civil-society organisations, motorists, residents and media along two routes: Nigeria–Niger and Mauritania–Western Sahara (Morocco).

**Reported argument/findings:** The author argues that the examined technology interventions affected migrants' mobility and rights, and that data sharing across European digital platforms can contribute to migration-control and deportation processes. These are the author's reported findings and interpretation; Frontier must not present them as independently verified operational facts without examining the full study and corroborating sources.

**Relevance to Frontier:**
- The article directly connects to Nigeria and technology-enabled migration management.
- It demonstrates that technical deployments must be evaluated alongside data governance, mobility outcomes, rights and institutional power.
- It cautions against assuming that digitisation or biometric collection automatically improves security or governance.
- It provides a basis for investigating system purpose, data flows, access, sharing, retention, oversight and redress.

**Questions for full-text reading:**
1. How were the 78 interview participants selected, and how are the two routes and countries represented?
2. What specific evidence supports each claim about data sharing and the use of collected data?
3. How does the paper distinguish observed practices, participant accounts and the author's interpretation?
4. What limitations does the author identify concerning access, sample, time period and generalisability?
5. What technical details of MIDAS and other systems are documented, and which remain outside the study's scope?

### Study B — Iwuoha and Doevenspeck (2023 online; journal issue 2025)

**Citation:** Iwuoha, V. C., & Doevenspeck, M. (2025 issue; published online 26 May 2023). *Dilemmas of ‘biometric nationality’: migration control, biometric ID technology and political mobilisation of migrants in West Africa*. Territory, Politics, Governance, 13(3), 279–304. https://doi.org/10.1080/21622671.2023.2205885

**Source inspected:** Publisher abstract and bibliographic information.

**Research purpose:** Examines how biometric ID technology intersects with migration control and political mobilisation of migrants in West Africa.

**Method reported in abstract:** Qualitative in-depth study involving migrants from Chad, Niger, Benin, Cameroon and Togo in Nigeria.

**Reported argument/findings:** The authors identify regional migration regimes, state identity politics/policies, monetary inducement and biometric ID technology as structures facilitating migration instrumentalisation for electoral purposes. They argue that biometric systems can be used in ways that complicate claims to political belonging and nationality.

**Relevance to Frontier:**
- Identity assurance is not the same as determining nationality or legal status.
- Biometric enrolment and identity systems operate within legal, political and institutional contexts.
- Technical design must not silently convert a biometric match, enrolment record or identifier into a conclusion about citizenship or entitlement.
- Data quality and identity resolution errors can have consequences beyond ordinary database defects.

**Questions for full-text reading:**
1. What is the precise relationship the authors establish between biometric enrolment, NIN/e-ID issuance and claims of nationality?
2. What evidence supports the four identified structures?
3. How are the participants and locations selected?
4. Which legal provisions and institutional practices are analysed?
5. What safeguards or alternative institutional designs are discussed, if any?

### Study C — Iwuoha (2025)

**Citation:** Iwuoha, V. C. (2025). *European Biometric Borders and (Im)Mobilities in West Africa: Reflections on Migrant Strategies for Border Circumvention and Subversion*. Politics & Policy, 53(1), e12653. https://doi.org/10.1111/polp.12653

**Source inspected:** Open-access publisher full-text page, including abstract, introduction, conceptual framing and conclusion.

**Research purpose and scope:** Uses Niger and the Burkina Faso–Niger border context to examine how European biometric installations and border securitisation shape migration and mobility.

**Conceptual contribution:** The author introduces “biometric reborderization” and “agentic deborderization” to describe, respectively, the reconfiguration of border control through biometric infrastructure and migrants' efforts to negotiate or circumvent its effects.

**Reported argument:** The author argues that biometric border processes can interact with identity conflicts and social exclusion, and that migrants may respond through alternative mobility strategies. The article questions whether security interventions achieve their stated aims when they produce unintended effects.

**Relevance to Frontier:**
- A border technology system must be evaluated as a socio-technical system, not only as software or hardware.
- Security effectiveness, lawful mobility, inclusion, privacy and accountability can conflict; these trade-offs should be made explicit.
- System performance cannot be inferred from installation, enrolment volume or data capture alone.
- Frontier's technical work should avoid designing circumvention guidance or operational route intelligence. Its contribution should remain at the level of governance analysis, defensive architecture, synthetic testing and rights-aware evaluation.

**Questions for full-text reading:**
1. What field evidence supports the concepts introduced, and how are they operationalised?
2. What are the limits of transferring findings from Niger to Nigeria or other ECOWAS states?
3. Which claims concern system design, which concern implementation, and which concern broader political outcomes?
4. What alternative explanations or counter-evidence are considered?
5. What measurable technical or governance criteria could future research use without reproducing the harms identified?

### Cross-paper synthesis: what this changes in Frontier's approach

These studies establish that the digitalisation of borders is already a substantial research field. Frontier must not claim novelty merely because it combines migration, biometrics and cybersecurity.

The strongest contribution available to Frontier at this stage is narrower and more defensible:

**Develop reproducible, privacy-minimising technical methods for examining data quality, provenance, access control and accountability in synthetic migration-information workflows, while situating those methods in the documented legal, institutional and human consequences of border technologies.**

This suggests five design requirements for all Frontier laboratories:

1. **Purpose limitation:** define why each data field exists and what decisions it must never determine.
2. **Provenance and contestability:** record where data came from, how it changed, and how errors can be corrected.
3. **Separation of identity concepts:** distinguish identifier, identity proofing, authentication, biometric match, nationality and legal status.
4. **Access and accountability:** model who may access or share data, under what authority, for what purpose, and with what audit trail.
5. **Rights-aware evaluation:** test not only whether a pipeline accepts or rejects records, but also whether errors, missing data and uncertainty are surfaced without automated adverse conclusions.

These are proposed Frontier design principles informed by the literature, not claims that the cited authors endorse Frontier or that the principles are already implemented in every laboratory.

### Research gap: current assessment

A defensible gap has **not yet been established**. The reviewed studies focus substantially on migration governance, biometric border practices, political identity, mobility and rights. Frontier's proposed technical laboratory work may complement this literature, but a claim that there is little or no technical work in this area would require a broader search across computer science, information systems, public administration, data governance and digital identity research.

Before claiming a contribution, compare Frontier's proposed methods with:
- Existing migration-data quality frameworks and data-quality measurement research.
- IOM's published MIDAS documentation and data-protection materials.
- Public biometric identity and digital public infrastructure standards.
- Nigerian data-protection and identity-management legal frameworks.
- Existing research on interoperability, access control, auditability and algorithmic accountability in migration systems.

### Current reading status and next gate

- [x] Publisher abstract and bibliographic details reviewed for Uzomah (2024).
- [x] Publisher abstract and bibliographic details reviewed for Iwuoha & Doevenspeck (2023/2025).
- [x] Open-access full-text page reviewed for Iwuoha (2025), including introduction and conclusion.
- [ ] Read and annotate the complete Uzomah article.
- [ ] Obtain and read the complete Iwuoha & Doevenspeck article.
- [ ] Verify cited legal and institutional claims against primary sources.
- [ ] Compare Frontier's laboratory design with existing technical standards and research.
- [ ] Revise research questions only after the literature comparison.

**Important:** These notes are a first reading pass based on publisher-visible material. They are not a substitute for complete full-text reading of all three papers, and they do not establish a novel research gap.

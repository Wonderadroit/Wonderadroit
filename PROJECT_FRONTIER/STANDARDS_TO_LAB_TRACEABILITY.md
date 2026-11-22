# Standards-to-Laboratory Traceability — Migration Data Quality Lab v0.2

**Date:** 22 November 2026  
**Status:** AI-assisted documentary comparison; not a conformity assessment, certification, legal opinion or independent review.  
**Artefact assessed:** v0.2 contract and test-plan claims on branch project-frontier/migration-data-quality-lab. This comparison did not rerun tests or independently inspect every implementation line.

## 1. Purpose

This compares the narrow synthetic validator with publicly inspectable data-quality, statistical-quality, provenance and privacy/security guidance. A mapping to a standards concept does **not** mean the lab conforms to that standard. Enterprise data quality, statistical production, provenance, organisational privacy risk and information-system controls have different scopes.

## 2. Sources inspected

1. **ISO 8000-1:2022, Data quality — Part 1: Overview.** ISO says the series establishes principles for information/data quality and describes the series' structure. Public material discusses syntactic, semantic and pragmatic characteristics and systemic data-quality management.  
   https://www.iso.org/standard/81745.html  
   https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso%3Ats%3A8000%3A-230%3Aed-1%3Av1%3Aen

2. **ISO/TS 8000-82:2022, Data quality assessment: Creating data rules.** Its published abstract concerns expressing requirements as processable rules for identifiers, dates/times, codes, keys and other data types, and the role of profiling. It does not prescribe rules for a particular dataset.  
   https://www.iso.org/standard/78707.html

3. **ISO/IEC 25024:2015, Measurement of data quality.** ISO describes measures for characteristics defined in ISO/IEC 25012 and guidance for applying measures and defining organisation-specific measures.  
   https://www.iso.org/standard/35749.html

4. **ISO 8000-8:2015, Information and data quality: Concepts and measuring.** Public preview stresses documented methods, tailoring to intended requirements, prerequisites, and reporting which information was not checked.  
   https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso%3A8000%3A-8%3Aed-1%3Av1%3Aen

5. **UN Statistics Division, Handbook on Management and Organization of National Statistical Systems (2025), Chapter 8.** Its discussion of the IMF Data Quality Assessment Framework identifies integrity, methodological soundness, accuracy/reliability, serviceability and accessibility, plus prerequisites such as legal/institutional environment, resources and quality awareness. It distinguishes this framework from the UN National Quality Assurance Framework and European Statistics Code of Practice.  
   https://unstats.un.org/capacity-development/handbook/chapters/Chapter8_Handbook_2025A_202505.pdf

6. **NIST Privacy Framework 1.1 guidance.** NIST describes privacy-risk management, accountability, traceability between privacy requirements and controls, and understanding data-processing ecosystem relationships. This is organisational guidance, not a record-level validator specification.  
   https://www.nist.gov/privacy-framework/using-privacy-framework-11

7. **NIST SP 800-53 Rev. 5, Security and Privacy Controls.** Includes organisational and system control families such as Audit and Accountability. It is not a data-quality standard.  
   https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf

8. **W3C PROV-O.** An ontology for representing entities, activities and agents and relationships such as derivation, usage, generation and attribution. Provenance representation does not itself prove truth or source authenticity.  
   https://www.w3.org/TR/prov-o/

This comparison uses public abstracts/previews and public framework guidance. Full ISO standards were not inspected clause by clause; no formal conformity assessment is claimed.

## 3. Requirement-to-evidence matrix

| Concern | Reference concept | v0.2 evidence | Assessment and boundary |
|---|---|---|---|
| Syntactic validity | ISO 8000; ISO/TS 8000-82 data rules | Required fields, controlled values, RFC 3339 shape/offset, ASCII digits, strict JSON, duplicate-key rejection, invalid UTF-8 boundary | **Partially addressed** for this fixed synthetic schema. Not general semantic correctness. |
| Semantic validity | ISO 8000 syntactic/semantic/pragmatic distinction | Event type, transport mode, limited country-code allowlist; ingested_at before event_at rejected | **Narrowly addressed.** Rules and allowlist are project-defined; no authoritative external registry or domain validation. |
| Completeness | ISO 8000 / ISO/IEC 25012 family; statistical quality concepts | Required-field checks and missingness counts with stated denominator | **Schema completeness only.** Does not establish population, event, source, route or time-period completeness. |
| Accuracy / truth | ISO/IEC 25012; statistical quality frameworks | No independent reference dataset or ground truth | **Not measured.** Valid fictional records may still be false or unrealistic. |
| Consistency | Data-quality frameworks; ISO rule concepts | Timestamp order; same-country origin/destination check; record-ID conflict grouping | **Partially addressed.** No cross-dataset reconciliation, referential integrity or longitudinal consistency. |
| Uniqueness | Data-quality measurement concepts | Exact duplicate, record-ID conflict and duplicate source-reference checks | **Explicit but policy-dependent.** First-seen retention and lexical timestamp comparison need reviewer justification; they are not universal requirements. |
| Timeliness / currency | Statistical quality and data-quality concepts | Ingestion-lag summary; explicit reference time; future tolerance | **Limited interval metric.** No service-level target, punctuality requirement or proof timestamps reflect actual event times. |
| Provenance | W3C PROV-O; ISO governance concepts | Synthetic source labels and token-shaped source_record_id; duplicate source-reference diagnostics | **Very limited.** Token format is not provenance evidence, source authentication or chain of custody. No PROV-O entity/activity/agent graph. |
| Methodological soundness | IMF DQAF / statistical quality assurance | Fixed schema and documented rules; 45 historical regression tests | **Not established.** No sampling, collection methodology, estimation method, bias assessment or validated statistical process. |
| Reliability / reproducibility | ISO 8000-8 documented measurement/reporting | Deterministic output for same input/reference time; fixture; recorded CI result | **Partially addressed.** Historical CI supports tested cases, not independent reproduction or deployment reliability. |
| Accessibility / serviceability | Statistical quality frameworks | JSONL and JSON outputs | **Not assessed.** Machine-readable output alone does not establish accessibility, metadata quality or serviceability. |
| Privacy minimisation | NIST Privacy Framework | No personal identity fields; unexpected fields rejected; diagnostics omit raw payloads | **Design constraint with limited test evidence.** No privacy impact or re-identification assessment, access governance or real-world processing review. |
| Security / accountability | NIST SP 800-53; NIST Privacy Framework | Local standard-library tool; no network calls/secrets; deterministic diagnostics | **Not a security-control assessment.** No authentication, authorisation, access logging, key management, secure deployment or incident response assessment. |
| Governance / institutional prerequisites | IMF DQAF; NIST Privacy Framework | None at institutional level | **Not addressed.** No mandate, roles, data-sharing agreement, legal basis, stewardship or inter-agency governance model. |

## 4. Interpretation

### 4.1 A data-rule demonstrator, not a statistical quality framework

The implementation expresses a small set of record-level rules and produces deterministic dispositions. This aligns conceptually with ISO/TS 8000-82's idea of capturing requirements as processable data rules. It does not implement a full data-quality management process, statistical production framework or enterprise quality measurement system.

### 4.2 A pass rate is not accuracy

The accepted-record fraction measures conformance to the current synthetic contract. It is not the fraction of true records, complete events or correct migration statistics. The prototype has no independent ground truth.

### 4.3 Token format is not provenance assurance

The SRC token pattern prevents arbitrary free text under this contract. It does not prove a source exists, created the record, that the record was not altered, or that the source is trustworthy. A future provenance study would need explicit entities, activities, agents, timestamps, derivation links and integrity protection, justified by a research requirement.

### 4.4 Privacy-by-schema is not a privacy programme

Excluding personal fields and omitting raw payloads from diagnostics reduce exposure in this educational fixture. They do not establish lawful processing, appropriate retention, access control, rights handling, re-identification resistance or organisational accountability.

## 5. Consequences

1. Do not label v0.2 ISO compliant, NIST compliant, statistically validated or migration-data quality assured.
2. Retain the narrow claim: it checks selected fictional records against a versioned synthetic contract and reports deterministic dispositions.
3. In any paper, define intended use and quality requirements before selecting measures; explain why each measure is appropriate.
4. Report unchecked dimensions explicitly, especially truth, population completeness, representativeness, methodological soundness, provenance authenticity, security controls, governance and rights impacts.
5. Treat ISO/IEC 25012/25024 as candidate sources for measurement vocabulary, not proof that this validator covers the full model.
6. Do not expand the code yet. Obtain human data-quality review of rules/denominators and separate migration-statistics/policy review of contextual relevance.

## 6. Candidate research question

> How transparently can a synthetic record-validation demonstrator report the scope, measurement rules and untested assumptions of its data-quality checks when assessed against selected international data-quality and privacy-governance guidance?

This is a candidate methods question, not a claim of a literature gap. It may be too modest or already covered by existing work. Further literature review and independent judgement must decide that.

## 7. Review limitations

- AI-assisted desk comparison based on public standards abstracts/previews and framework guidance.
- Full paid ISO standards were not inspected clause by clause.
- The validator implementation and full tests were not re-read line by line in this pass; this assessment uses the v0.2 contract/test plan and prior documented 45-test inventory.
- No test suite was executed.
- No independent technical, statistical, privacy or policy reviewer participated.
- No real migration data or government system was accessed.

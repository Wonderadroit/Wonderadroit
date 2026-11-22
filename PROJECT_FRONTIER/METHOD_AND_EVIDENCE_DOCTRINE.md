# Project Frontier — Method and Evidence Doctrine

**Version:** 0.1  
**Date:** 22 November 2026  
**Status:** Proposed operating doctrine for review

## 1. The principle inherited from CYDRA

CYDRA's operating principle is:

> **LLMs propose. Tools test. Evidence decides.**

Project Frontier should inherit this discipline, but adapt it to research rather than copy it mechanically.

Frontier's corresponding doctrine is:

> **Sources frame. Methods test. Evidence decides. Humans interpret and remain accountable.**

A shorter public-facing formulation is:

> **Sources support. Methods test. Limitations qualify. Humans decide.**

These are complementary, not competing slogans. The first states the evidence hierarchy; the second describes the research workflow and the role of human judgement.

## 2. What the doctrine means in Frontier

| Stage | Permitted role | What it must not do |
|---|---|---|
| Research question | LLMs may help generate and narrow candidate questions. | Treat a plausible question as proof of a research gap. |
| Source discovery | Search tools and researchers locate primary law, official policy, standards and scholarship. | Treat search ranking, abstracts or institutional prestige as proof. |
| Source interpretation | Researchers extract claims, methods, geography, dates, limitations and competing explanations. LLMs may assist with summaries that are checked against the source. | Invent quotations, findings, citations or details not present in the source. |
| Technical experiment | Reproducible scripts, tests and synthetic datasets examine explicitly declared properties. | Use synthetic outputs to claim facts about real migrants, agencies, borders or operational systems. |
| Analysis | Compare observed results with predeclared expectations and alternative explanations. | Convert a passing test or single paper into a broad conclusion. |
| Conclusion | State only what the evidence supports, including uncertainty and unresolved questions. | Inflate the claim to sound more important, novel or policy-relevant. |
| Decision and publication | A named human author/reviewer takes responsibility for interpretation, ethics and publication. | Delegate accountability to an LLM, tool, test suite or institution that has not endorsed the work. |

## 3. Research evidence hierarchy

Frontier should identify the type and strength of evidence behind each material claim:

1. **Primary legal and policy material:** enacted laws, official regulations, published government/ECOWAS instruments and formal institutional documents. These establish what a source says or requires; they do not by themselves prove implementation.
2. **Primary empirical material:** transparently collected and ethically obtained observations, interviews, datasets or system documentation. Frontier currently has no access to non-public operational migration data.
3. **Peer-reviewed research:** valuable for methods, empirical findings and scholarly interpretations. Record the authors' geography, period, sample and limitations.
4. **Technical standards and implementation guidance:** useful for control requirements and terminology. A standard's existence does not prove an organisation implements it.
5. **Secondary reporting and institutional summaries:** useful for discovery and context, but trace consequential claims back to primary sources where possible.
6. **LLM-generated synthesis:** a drafting and reasoning aid only; never an independent evidence source.

Evidence quality is claim-specific. A primary source may be authoritative about its own policy but weak evidence of real-world outcomes. A peer-reviewed qualitative study may support a contextual interpretation but not a technical performance claim.

## 4. Five mandatory research controls

- **Traceability:** every important factual claim should be traceable to a source, page/section, dataset or reproducible output.
- **Reproducibility:** methods, versions, assumptions, test cases and metric denominators should be stated clearly enough for another person to repeat the work.
- **Falsifiability:** define what result would contradict the hypothesis or show that the method does not work.
- **Scope discipline:** distinguish Nigeria-specific evidence from West African regional evidence and from findings in other regions.
- **Human accountability:** disclose uncertainty, conflicts, ethical considerations and the limits of automation; humans retain responsibility for interpretation and decisions.

## 5. What makes this useful — and what does not make it unique

This doctrine can make Frontier's work more disciplined, auditable and credible. It is not, by itself, a novel research method or proof that Frontier is unique. Evidence-led, reproducible and human-accountable research practices already exist across science, software assurance, data governance and security engineering.

Frontier's potential distinctiveness must come from the combination of:
- a clearly bounded Nigeria/ECOWAS migration-governance problem;
- technically testable questions about data quality, provenance, access and accountability;
- reproducible, privacy-minimising synthetic experiments;
- careful engagement with migration scholarship and legal/policy sources; and
- independent review by people with relevant technical and policy expertise.

The combination is a research direction to investigate, not a novelty claim to announce before a structured literature review.

## 6. Initial source-grounded implications

The literature reviewed so far reinforces why the doctrine matters:

- IOM's 2019 *Guidelines for the Harmonization of Migration Data Management in the ECOWAS Region* describe a regional need for reliable migration evidence, shared concepts, data collection/analysis and responsible dissemination. This is a strong regional policy comparator; it is not evidence that regional data systems currently meet those aims.
- The Nigeria Data Protection Act 2023 and the NDPC's General Application and Implementation Directive provide primary Nigerian privacy and data-protection materials. Legal requirements must be mapped to the exact processing activity and lawful basis; a generic claim that a prototype is “compliant” would be unjustified.
- O'Sullivan et al. (2025), on provenance tracking in Trusted Research Environments, demonstrates that provenance capture, processing traceability and audit support are already active technical research areas. The paper describes a prototype developed in a Scottish health-data environment, not a migration or border system. Frontier must compare methods rather than claim to have invented provenance-based quality assurance.
- Ibor et al. (2025), on trustworthy cross-border interoperability of foundational identity systems in developing countries, makes African identity-system trust, institutional dynamics, privacy and security relevant comparators.
- Research on MIDAS and biometric border technologies in Nigeria and West Africa shows that technical systems must be analysed alongside institutional power, mobility, rights and governance. Technical functionality alone cannot establish social legitimacy or beneficial outcomes.

## 7. Mandatory claim labels

When writing briefs, papers and public updates, use clear labels where ambiguity is possible:

- **Source fact:** what a primary source explicitly states.
- **Author finding:** an empirical result reported by a named study.
- **Author interpretation:** the explanation or argument advanced by its author.
- **Frontier observation:** what a documented Frontier experiment directly produced.
- **Frontier interpretation:** the explanation Frontier offers for those observations.
- **Proposal:** a recommended design or control not yet validated.
- **Unknown:** a question for which adequate evidence has not been found.

Never silently convert one category into another.

## 8. First-paper consequence

The first Migration Data Quality paper should not be framed as “a new migration data quality system” or as a discovery about Nigeria's migration records.

It should be framed as a bounded design-and-evaluation study of a synthetic laboratory:
- freeze the exact implementation, contract and test plan;
- map each requirement to tests and outputs;
- test declared quality dimensions and failure cases;
- assess whether diagnostics and provenance are reproducible and interpretable;
- document false assurances and limitations;
- obtain independent technical review and separate policy review.

A successful experiment supports a claim about the tested synthetic contract and implementation only. It does not establish operational suitability, real-world prevalence, or the quality of any agency's data.

## 9. Review status

This doctrine is proposed. It should be reviewed alongside the research scope and agenda. It does not replace the existing project charter, ethics boundaries, source register or independent-review gates.

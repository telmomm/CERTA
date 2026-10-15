---
title: "Systematic review protocol"
subtitle: "How the test of analog circuits is designed and how its diagnostic coverage is justified"
author: "Telmo Miguel-Medina"
date: today
doctype: "Protocol"
reference: "WP0 · T0.1"
---

# Summary {-}

A systematic mapping review in Scopus, Web of Science and IEEE Xplore with two search blocks: S1, on how the test of analog circuits is designed (what to measure and what to apply), and S2, on how the diagnostic coverage of analog hardware is computed or justified for the functional safety standards. Each included study is coded against seven gap criteria. A rule fixed before screening (milestone G0) decides whether some work already reaches a coverage target at minimum hardware cost, with risk weighting and statistical certification, at board level.

# Aim and type of review

To map how the literature decides what to measure and what to apply in order to detect and locate faults in analog circuits, and how the diagnostic coverage of analog hardware is computed or justified against IEC 61508 and ISO 26262. To check, with the rule of the last section, whether any work already combines embedded hardware cost, risk weighting and statistical certification at board level.

Systematic mapping review, without meta-analysis, reported according to PRISMA 2020 and PRISMA-S. What the standards themselves require (metric, target per safety level) is not part of the review: it is T0.8.

# Questions

| Id | Question |
| --- | ------------------------------------------------------------ |
| RQ1 | What is decided when the test is designed (nodes, stimuli, measurements), and jointly or separately? |
| RQ2 | How are the cost and the limitations of the measuring hardware modelled? |
| RQ3 | What objective is optimised? Is a coverage target a constraint? Are faults weighted by probability or severity, and are false alarms controlled? |
| RQ4 | How are tolerances treated, and with what statistical support are detection and coverage figures reported? |
| RQ5 | What is each method compared against, on which circuits, and how reproducible is the comparison? |
| RQ6 | How is the diagnostic coverage of analog parts obtained for a safety standard (computed, measured or credited from tables), and with which metric (DC, SFF, SPFM, LFM)? |
| RQ7 | Does any work reach a coverage target at minimum embedded hardware cost, with risk weighting and statistical certification, at board level? |

# Sources and search

Scopus, Web of Science Core Collection and IEEE Xplore (metadata only), with no date limit. The strings are in [search-strings.md](search-strings.md).

| Block | What it retrieves | Answers |
| -------------------- | ------------------------------------------------------------ | ------- |
| S1 · Test design | Selection of test points, stimuli and measurements; testability and ambiguity groups; analog test generation | RQ1–RQ5 |
| S2 · Safety coverage | Diagnostic, fault or defect coverage of analog and mixed-signal hardware for functional safety; FMEDA; safety mechanisms | RQ6 |

Both blocks are merged and deduplicated into one corpus (T0.2). They are complemented in T0.4 with author searches and with backward and forward citation tracking of the works in [control_set.csv](control_set.csv) and of the included studies that meet three or more gap criteria. No grey literature: standards, application notes and vendor material go to T0.8.

# Eligibility

A study is included if it meets I1 to I4 and no exclusion reason applies. The first applicable reason is recorded.

| Id | Inclusion |
| --- | ------------------------------------------------------------ |
| I1 | Analog electronic circuit, or the analog part of a mixed-signal circuit |
| I2 | (a) Selects, orders or optimises test points, stimuli, measurements or specification tests; or analyses testability or ambiguity groups; or is an in-field self-test of an analog board that decides what to measure. (b) Or computes, estimates or demonstrates, by simulation, fault injection or measurement, the coverage of the diagnostics of an analog part with respect to a safety standard |
| I3 | Primary study with a method applied to at least one circuit |
| I4 | Full text in English or Spanish |

| Id | Exclusion |
| --- | ------------------------------------------------------------ |
| E1 | Digital only |
| E2 | Diagnosis without selection: features and a classifier on fixed measurements, with no coverage computed against a safety standard |
| E3 | Other domain |
| E4 | Test technique, structure or tool (BIST, DfT, simulation or fault models) that neither decides what to measure nor computes a coverage against a safety standard |
| E5 | Not a primary study (reviews are tagged separately) |
| E6 | Redundant version: the most complete one is kept |
| E7 | Language |
| E8 | Full text not available |

Boundary cases are in [screening-criteria.md](screening-criteria.md).

# Selection

Deduplication with the T0.2 notebook; screening by title and abstract (include, exclude or doubt; a doubt goes to full text); full-text screening; PRISMA diagram, with the records of each block.

An AI assistant makes a first pass of the title and abstract screening with the criteria in force, which is stored separately (`screening_ai.csv`). The decision that counts is the human one, taken with that proposal in view; the agreement between both is reported and the use of AI is declared in the paper.

# Extraction and synthesis

One row per included study, following [extraction-form.md](extraction-form.md). The synthesis is descriptive: counts by family, year, level and block; a matrix of studies against the gap criteria; the distribution of Monte Carlo runs; how coverage is obtained and with which metric; and a table of published figures for WP1.

# Gap criteria and G0 rule

Each included study is coded as yes, partial or no:

| Id | Criterion | "Yes" means |
| --- | --------------- | ------------------------------------------------------------ |
| C1 | Joint selection | At least two of {node, stimulus, measurement} are decided in the same optimisation |
| C2 | Hardware cost | The cost distinguishes physical resources, or the model includes the limits of the instrument |
| C3 | Risk | Faults are weighted by probability or severity, or false alarms or test escapes are constrained |
| C4 | Certification | Detection or coverage figures carry confidence intervals, or the sample size is justified |
| C5a | Reference | The result is compared with an exact optimum or with the limit set by the ambiguity groups |
| C5b | Openness | Code or data sufficient to repeat the experiment are published |
| C6 | Safety metrics | Coverage is computed as a metric of a safety standard (DC, SFF, SPFM, LFM) or checked against the target of a safety level. "Partial": the standard is cited but its metric is not computed |

| Outcome | Condition | Consequence |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| G0 passed | No study has C2, C3 and C4 as "yes" or "partial" at the same time | The proposal stands |
| Passed with repositioning | Some study combines C2, C3 and C4, but on an integrated circuit or with one of them as "partial"; or some study has C4 and C6 as "yes" | It becomes the main comparator |
| Not passed | Some study has C2, C3 and C4 as "yes" at board level | The benchmark and the certification become the main contribution |

# Limitations

Screening by a single reviewer; IEEE Xplore by metadata only; English and Spanish only; no grey literature, although much of the industrial practice on diagnostic coverage is published as standards and vendor material (covered by T0.8). S2 was defined after S1 had been run; both blocks are screened with the same criteria.

# References {-}

- M. J. Page et al., *The PRISMA 2020 statement: an updated guideline for reporting systematic reviews*, BMJ 372:n71, 2021. doi:10.1136/bmj.n71
- M. L. Rethlefsen et al., *PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews*, Systematic Reviews 10:39, 2021. doi:10.1186/s13643-020-01542-z

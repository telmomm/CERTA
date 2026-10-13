# Systematic review protocol

Selection of points, stimuli and measurements for the test of analog circuits.

## 1. Aim and type of review

To map how the literature decides what to measure and what to apply in order to detect and locate faults in analog circuits, and to check with a rule fixed in advance whether any work already combines embedded hardware cost, risk weighting and statistical certification at board level (milestone G0).

Systematic mapping review, without meta-analysis, reported according to PRISMA 2020 and PRISMA-S.

## 2. Questions

| Id | Question |
| --- | --- |
| RQ1 | What is decided when the test is designed (nodes, stimuli, measurements), and jointly or separately? |
| RQ2 | How are the cost and the limitations of the measuring hardware modelled? |
| RQ3 | What objective is optimised? Are faults weighted by probability or severity, and are false alarms controlled? |
| RQ4 | How are tolerances treated, and with what statistical support are the metrics reported? |
| RQ5 | What is each method compared against, on which circuits, and how reproducible is the comparison? |
| RQ6 | Does any work combine embedded cost, risk and statistical certification at board level? |

## 3. Sources

Scopus, Web of Science Core Collection and IEEE Xplore (metadata only), with no date limit, using the strings in [search-strings.md](search-strings.md). They are complemented in T0.4 with author searches and with backward and forward citation tracking of the works in [control_set.csv](control_set.csv) and of the included studies that meet three or more gap criteria. No grey literature.

## 4. Eligibility

A study is included if it meets I1 to I4 and no exclusion reason applies. The first applicable reason is recorded.

| Id | Inclusion |
| --- | --- |
| I1 | Analog electronic circuit, or the analog part of a mixed-signal circuit |
| I2 | Selects, orders or optimises test points, stimuli, measurements or specification tests; or analyses testability or ambiguity groups; or is an in-field self-test of an analog board that decides what to measure |
| I3 | Primary study with a method applied to at least one circuit |
| I4 | Full text in English or Spanish |

| Id | Exclusion |
| --- | --- |
| E1 | Digital only |
| E2 | Diagnosis without selection: features and a classifier on fixed measurements |
| E3 | Other domain |
| E4 | Test technique, structure or tool (BIST, DfT, simulation or fault models) that does not decide what to measure |
| E5 | Not a primary study (reviews are tagged separately) |
| E6 | Redundant version: the most complete one is kept |
| E7 | Language |
| E8 | Full text not available |

Boundary cases are in [screening-criteria.md](screening-criteria.md).

## 5. Selection

Deduplication with the T0.2 notebook; screening by title and abstract (include, exclude or doubt; a doubt goes to full text); full-text screening; PRISMA diagram.

An AI assistant makes a first pass of the title and abstract screening, which is stored separately (`screening_ai.csv`). The decision that counts is the human one, taken with that proposal in view; the agreement between both is reported and the use of AI is declared in the paper.

## 6. Extraction and synthesis

One row per included study, following [extraction-form.md](extraction-form.md). The synthesis is descriptive: counts by family, year and level, a matrix of studies against criteria, the distribution of Monte Carlo runs and a table of published figures for WP1.

## 7. Gap criteria and G0 rule

Each included study is coded as yes, partial or no:

| Id | Criterion | "Yes" means |
| --- | --- | --- |
| C1 | Joint selection | At least two of {node, stimulus, measurement} are decided in the same optimisation |
| C2 | Hardware cost | The cost distinguishes physical resources, or the model includes the limits of the instrument |
| C3 | Risk | Faults are weighted by probability or severity, or false alarms or test escapes are constrained |
| C4 | Certification | Confidence intervals are given, or the sample size is justified |
| C5a | Reference | The result is compared with an exact optimum or with the limit set by the ambiguity groups |
| C5b | Openness | Code or data sufficient to repeat the experiment are published |

| Outcome | Condition | Consequence |
| --- | --- | --- |
| G0 passed | No study has C2, C3 and C4 as "yes" or "partial" at the same time | The proposal stands |
| Passed with repositioning | Some study combines them, but on an integrated circuit or with one of them as "partial" | It becomes the main comparator |
| Not passed | Some study has C2, C3 and C4 as "yes" at board level | The benchmark and the certification become the main contribution |

## 8. Expected limitations

Screening by a single reviewer; IEEE Xplore by metadata only; English and Spanish only; no grey literature.

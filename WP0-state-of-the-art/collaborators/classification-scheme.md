---
title: "Classification scheme"
subtitle: "Data extraction form for the included studies"
author: "Telmo Miguel-Medina"
---

One row per included study, filled in from the full text.

Codes: `y` yes, `p` partial, `n` no, `ns` not stated. Lists are separated with semicolons. Every `y` or `p` in block K is backed by the literal sentence and the page where it appears.

# 1. Extraction form

| Block | Field | Values |
|:-------------|:------------------------|:-----------------------------------------|
| A. Context | Reference, DOI, research group | text |
| | Level | integrated circuit, board, both, ns |
| | Stage | production, maintenance, in-field, design, ns |
| | Validation | simulation, hardware, both |
| | Circuits; size of the largest | list; number of components |
| B. Selection | Selects nodes / stimuli / measurements | y, n (one field each) |
| | Type of stimulus | DC, AC, transient, other |
| | Coupling of the decisions | joint, sequential, single |
| | Number of candidate tests | integer or ns |
| C. Faults | Fault type | catastrophic, parametric, both |
| | Multiple faults; number of faults | y, n; integer or ns |
| D. Objective | Objective | detection, isolation, identification, specification compliance |
| | Multi-objective | y, n |
| | Weighting by fault probability | y, p, n |
| | Weighting by fault severity | y, p, n |
| | False alarms controlled | y, p, n |
| E. Cost | Cost model | none, count of tests, abstract, time, hardware |
| | Model of the instrument (noise, resolution, range) | y, p, n |
| | Node accessibility considered | y, n |
| F. Tolerances | Treatment of tolerances | ignored, threshold, parametric, Monte Carlo |
| | Monte Carlo runs per fault; distribution | integer or ns; normal, uniform, other, ns |
| | Confidence intervals reported | y, n |
| G. Algorithm | Family | exhaustive, greedy, graph search, metaheuristic, exact, machine learning, reinforcement learning, symbolic, other |
| | Optimality or approximation guarantee | y, n |
| H. Comparison | Compared with an exact optimum | y, n |
| | Compared with the ambiguity-group limit | y, n |
| | Baseline methods | list |
| J. Reproducibility | Netlist given; fault list given; parameters given | y, p, n (one field each) |
| | Code; data | URL or n |
| K. Cross-cutting criteria | C1, C2, C3, C4, C5a, C5b | y, p, n (defined below) |
| | Notes | text |

# 2. Cross-cutting criteria

They summarise blocks B to J into six properties, so that the studies can be compared in a single matrix.

| Id | Criterion | "Yes" means |
|:--|:------------------|:---------------------------------------------------|
| C1 | Joint selection | At least two of {node, stimulus, measurement} are decided in the same optimisation |
| C2 | Hardware cost | The cost distinguishes physical resources, or the model includes the limits of the instrument |
| C3 | Risk | Faults are weighted by probability or severity, or false alarms or test escapes are constrained |
| C4 | Statistical certification | Confidence intervals are given, or the sample size is justified |
| C5a | Reference | The result is compared with an exact optimum or with the limit set by the ambiguity groups |
| C5b | Openness | Code or data sufficient to repeat the experiment are published |

"Partial" is used when the property is present but incomplete; for example, C2 when the cost is the test time on a production tester, or C4 when the number of Monte Carlo runs is discussed but no interval is given.

# 3. Published figures

A separate table, one line per study and circuit, records the results reported for the most common benchmark circuits, so that they can be compared across studies.

Fields: study, circuit, tests selected, number of tests, metric, value, table or figure of origin.

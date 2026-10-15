---
title: "Extraction form"
subtitle: "Columns and codes of the extraction matrix"
author: "Telmo Miguel-Medina"
date: today
doctype: "Protocol annex"
reference: "WP0 · T0.1"
---

# Matrix {-}

Columns of `matrix.csv` (T0.5), one row per included study.

Codes: `y` yes, `p` partial, `n` no, `ns` not stated. Lists are separated with semicolons. Every `y` or `p` in block L carries, in its `_quote` column, the literal sentence and the page.

| Block | Column | Values |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| A. Context | `id`, `citation`, `doi`, `group` | text |
| | `level` | `ic`, `board`, `both`, `ns` |
| | `stage` | `production`, `maintenance`, `field`, `design`, `ns` |
| | `validation` | `simulation`, `hardware`, `both` |
| | `circuits`, `n_components` | list; integer for the largest circuit |
| B. Selection | `sel_node`, `sel_stimulus`, `sel_measurement` | `y`, `n` |
| | `stimulus_type` | `dc`, `ac`, `transient`, `other` |
| | `coupling` | `joint`, `sequential`, `single` |
| | `n_candidates` | integer or `ns` |
| C. Faults | `fault_type` | `catastrophic`, `parametric`, `both` |
| | `multiple_faults`, `n_faults` | `y`, `n`; integer or `ns` |
| D. Objective | `objective` | `detection`, `isolation`, `identification`, `specification` |
| | `multiobjective` | `y`, `n` |
| | `coverage_target` | `y` if a coverage target is a constraint or is checked, `n` |
| | `weight_probability`, `weight_severity`, `false_alarms` | `y`, `p`, `n` |
| E. Cost | `cost` | `none`, `count`, `abstract`, `time`, `hardware` |
| | `instrument_model` | `y`, `p`, `n` |
| | `accessibility` | `y`, `n` |
| F. Tolerances | `tolerances` | `ignored`, `threshold`, `parametric`, `montecarlo` |
| | `mc_runs`, `mc_distribution` | integer or `ns`; `normal`, `uniform`, `other`, `ns` |
| | `intervals` | `y`, `n` |
| G. Algorithm | `family` | `exhaustive`, `greedy`, `graph`, `metaheuristic`, `exact`, `ml`, `rl`, `symbolic`, `other` |
| | `guarantee` | `y`, `n` |
| H. Comparison | `cmp_optimum`, `cmp_bound` | `y`, `n` |
| | `baselines` | list of methods, by `id` if they are in the corpus |
| J. Reproducibility | `rep_netlist`, `rep_faults`, `rep_parameters` | `y`, `p`, `n` |
| | `code`, `data` | URL or `n` |
| K. Safety | `safety_standard` | list of `iec61508`, `iso26262`, `iec60601`, `ieee2427`, `other`; or `n` |
| | `safety_metric` | list of `dc`, `sff`, `spfm`, `lfm`, `defect_coverage`, `other`; or `n` |
| | `coverage_source` | `computed`, `measured`, `credited` (from tables), `n` |
| | `failure_rates` | `standard` (IEC 61709, SN 29500), `handbook`, `assumed`, `n` |
| L. Gap | `C1_joint`, `C2_hw_cost`, `C3_risk`, `C4_certification`, `C5a_reference`, `C5b_openness`, `C6_safety` | `y`, `p`, `n` (definitions in the protocol, "Gap criteria and G0 rule") |
| | `g0_candidate` | `y` if C2, C3 and C4 are `y` or `p` |
| | `notes` | text |

# I. Published figures {-}

A separate file, `figures.csv`, with one line per study and circuit. It is the input of experiment E1 of WP1.

Columns: `id`, `circuit`, `selected_tests`, `n_tests`, `metric`, `value`, `table_or_figure`.

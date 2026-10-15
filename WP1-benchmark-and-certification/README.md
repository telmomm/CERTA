# WP1 · Benchmark and certification

Notes on the contents of this folder. The tasks and their estimated duration are in [ROADMAP.md](../ROADMAP.md).

## Objective

To build the open benchmark on which every method is compared: benchmark circuits and fault universe in spicefault, enumeration of candidate tests, the coverage metrics of the safety standards (DC and SFF of IEC 61508, SPFM and LFM of ISO 26262) with confidence intervals, adaptive Monte Carlo and reimplemented baselines. It also defines the lead demonstrator and the two secondary cases (circuit, specifications, measurement hardware, safety goal with its target level and fault table with severities) that WP2 and WP4 use. It ends at milestone G1: the baselines reproduce the published figures, or the discrepancy is documented.

## Status

T1.1 started ahead of milestone G0 (WP0): the benchmark circuits are already fixed in GUIDE.md and do not depend on the outcome of the review.

## Folders

| Folder | What goes inside |
| --- | --- |
| `T1.1-benchmark-circuits` | `circuits.md` (source, values, tolerances and faults of each circuit), `netlists/`, the notebook `01_benchmark_circuits.ipynb` and its outputs: `fault_universe.csv` and `starting_simulations.csv` |

## Notes

- Simulations use spicefault (pinned in `requirements.txt`) and ngspice, which is installed separately (`brew install ngspice` on macOS).


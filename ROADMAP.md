# ROADMAP

Durations are part-time estimates and are not tied to calendar dates. The duration of a package is shorter than the sum of its tasks when some of them run in parallel.

## WP0 · STATE OF THE ART

About 3 months. Ends at milestone G0: nobody has combined embedded cost, risk and certification at board level.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T0.1 | Protocol: review questions, search strings per database, inclusion and exclusion criteria, extraction form | `protocol.md` | 2 weeks |
| T0.2 | Search in Scopus, IEEE Xplore and WoS; deduplication | Corpus and counts per database | 2 weeks |
| T0.3 | Screening by title and abstract, then at full text, with the exclusion reason recorded | `screening.csv` and PRISMA diagram | 4 weeks |
| T0.4 | Citation tracking and author searches | Records added, tagged by origin | 1 week |
| T0.5 | Data extraction from the included studies | `matrix.csv` | 4 weeks |
| T0.6 | In-depth reading of Chakrabarti, Huang, Zilch and Tang | One sheet per work: what it formulates, what it assumes, what it lacks | 3 weeks, in parallel with T0.5 |
| T0.7 | G0 report and skeleton of P1 | Reasoned decision and reusable state-of-the-art text | 4 weeks |

## WP1 · BENCHMARK AND CERTIFICATION

About 5 months. Requires G0. Ends at milestone G1: the baselines reproduce the published figures, or the discrepancy is documented.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T1.1 | Benchmark circuits (Sallen-Key, biquad and leapfrog) in spicefault, with tolerances and fault universe | Netlists and starting simulations | 3 weeks |
| T1.2 | `candidates` module: enumerate tests (node × stimulus × feature) from the netlist and the accessible nodes | Module with tests | 3 weeks |
| T1.3 | `metrics` module: detection, false alarms, ambiguity sets and Clopper–Pearson intervals | Module with tests | 3 weeks |
| T1.4 | Adaptive Monte Carlo: runs until the interval falls below a target width | Stopping rule built into `metrics` | 2 weeks |
| T1.5 | Reimplemented baselines: Starzyk's entropy, genetic algorithm and fault-pair table with Bhattacharyya and KDE | Baselines in `select` | 6 weeks, in parallel with T1.3 and T1.4 |
| T1.6 | Experiment E1: do the baselines reproduce the published figures? | Table of published versus reproduced figures | 3 weeks |
| T1.7 | Experiment E5: runs needed and stability of the rankings with small samples | Interval width and stability curves | 3 weeks |
| T1.8 | G1 report, first public release of `spicefault.testdesign` with a DOI and skeleton of P2 | Reasoned decision, release on Zenodo | 3 weeks |

## WP2 · FORMULATION AND ALGORITHMS

About 6 months. Requires G1. Ends at milestone G2: the greedy stays close to the optimum and risk weighting changes the selection.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T2.1 | `costmodel` module: cost per node and per measurement; ADC noise, resolution and range | Module and model of a specific microcontroller | 3 weeks |
| T2.2 | `faultprior` module: probabilities per component type (IEC 61709 or SN 29500) and severity per fault or per specification violation | Module and rate tables | 3 weeks, in parallel with T2.1 |
| T2.3 | Metrics of the formulation: risk-weighted coverage and residual uncertainty about the fault | Extension of `metrics` | 3 weeks |
| T2.4 | Greedy by information gain per unit cost and Pareto front per budget | `select.pareto` | 3 weeks |
| T2.5 | Exact optimum by integer linear programming on small instances | Reference solution in `select` | 4 weeks |
| T2.6 | `bounds` module: sensitivity matrix and ambiguity groups by SVD | Theoretical bound and testability gap | 4 weeks, in parallel with T2.5 |
| T2.7 | `bench` module and experiments E2 (greedy versus optimum), E3 (joint versus sequential) and E4 (with and without risk), with sensitivity analysis to the weights | Tables and Pareto fronts | 6 weeks |
| T2.8 | G2 report, release with a DOI and skeleton of P3 | Reasoned decision, release on Zenodo | 3 weeks |

## WP3 · BOARD VALIDATION

About 7 months. Board design can start while the WP2 experiments are being closed. Ends at milestone G3: the simulated test ranking holds on the board.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T3.1 | Specification of the two boards (Sallen-Key and ECG front end): faults to inject, accessible nodes and microcontroller | Specification document | 3 weeks |
| T3.2 | Schematic and PCB design with fault injection by relays or jumpers | Manufacturing files | 6 weeks |
| T3.3 | Manufacturing, assembly and bring-up | Two working boards | 4 weeks, plus manufacturing lead time |
| T3.4 | Firmware (ESP32 or STM32) that runs the self-test plan exported as JSON | Firmware and plan format | 5 weeks, in parallel with T3.2 and T3.3 |
| T3.5 | Characterisation of the measurement chain (ADC and DAC) and adjustment of `costmodel` | Measured noise and resolution parameters | 2 weeks |
| T3.6 | Experiment E6: measurement campaign with fault injection | Raw measurement data | 4 weeks |
| T3.7 | Measured versus simulated coverage and G3 report | Reasoned decision and simulation-to-reality gap | 3 weeks |
| T3.8 | Release with a DOI and skeletons of P4 and P5 | Release on Zenodo | 3 weeks |

## WP4 · BIOMEDICAL APPLICATION

About 8 months. Requires G2; the data part requires the WP3 measurements.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T4.1 | spicefault models of the ECG front end and the Howland current source, with their specifications | Netlists and fault universe | 4 weeks |
| T4.2 | Risk analysis: severity of each fault according to IEC 60601 and ISO 14971 | Table of faults, effects and severities | 4 weeks, in parallel with T4.1 |
| T4.3 | Experiments E3 and E4 on the biomedical circuits | Pareto fronts and coverage of severe faults | 5 weeks |
| T4.4 | Bridge or thermistor conditioning as a generic industrial case | Results on a non-biomedical circuit | 3 weeks |
| T4.5 | Self-test plan exportable from the web GUI starting from a netlist | Feature in the GUI | 5 weeks |
| T4.6 | Dataset of simulations and measurements with fixed splits, and skeleton of P6 | Deposit with a DOI | 3 weeks |
| T4.7 | Skeleton of P7 | Starting text of the paper | 3 weeks |
| T4.8 | Fault diagnosis exercises for teaching, generated from the GUI | Collection of exercises | 3 weeks |

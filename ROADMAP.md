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
| T1.2 | Definition of the three application cases (battery measurement chain, ECG front end, bridge sensor conditioning): candidate circuit, specifications, measurement hardware and fault table with severities | One sheet per case | 3 weeks, in parallel with T1.1 |
| T1.3 | `candidates` module: enumerate tests (node × stimulus × feature) from the netlist and the accessible nodes | Module with tests | 3 weeks |
| T1.4 | `metrics` module: detection, false alarms, ambiguity sets and Clopper–Pearson intervals | Module with tests | 3 weeks |
| T1.5 | Adaptive Monte Carlo: runs until the interval falls below a target width | Stopping rule built into `metrics` | 2 weeks |
| T1.6 | Reimplemented baselines: Starzyk's entropy, genetic algorithm and fault-pair table with Bhattacharyya and KDE | Baselines in `select` | 6 weeks, in parallel with T1.4 and T1.5 |
| T1.7 | Experiment E1: do the baselines reproduce the published figures? | Table of published versus reproduced figures | 3 weeks |
| T1.8 | Experiment E5: runs needed and stability of the rankings with small samples | Interval width and stability curves | 3 weeks |
| T1.9 | G1 report, first public release of `spicefault.testdesign` with a DOI and skeleton of P2 | Reasoned decision, release on Zenodo | 3 weeks |

## WP2 · FORMULATION AND ALGORITHMS

About 6 months. Requires G1. Ends at milestone G2: the greedy stays close to the optimum and risk weighting changes the selection.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T2.1 | `costmodel` module: cost per node and per measurement; ADC noise, resolution and range | Module and model of a specific microcontroller | 3 weeks |
| T2.2 | `faultprior` module: probabilities per component type (IEC 61709 or SN 29500) and severity per fault, taken from the case sheets of T1.2, or per specification violation | Module and rate tables | 3 weeks, in parallel with T2.1 |
| T2.3 | Metrics of the formulation: risk-weighted coverage and residual uncertainty about the fault | Extension of `metrics` | 3 weeks |
| T2.4 | Greedy by information gain per unit cost and Pareto front per budget | `select.pareto` | 3 weeks |
| T2.5 | Exact optimum by integer linear programming on small instances | Reference solution in `select` | 4 weeks |
| T2.6 | `bounds` module: sensitivity matrix and ambiguity groups by SVD | Theoretical bound and testability gap | 4 weeks, in parallel with T2.5 |
| T2.7 | `bench` module and experiments E2 (greedy versus optimum), E3 (joint versus sequential) and E4 (with and without risk) on the benchmark circuits and on one application circuit, with sensitivity analysis to the weights | Tables and Pareto fronts | 6 weeks |
| T2.8 | G2 report, release with a DOI and skeleton of P3 | Reasoned decision, release on Zenodo | 3 weeks |

## WP3 · BOARD VALIDATION

About 6 months. Board design can start while the WP2 experiments are being closed. Ends at milestone G3: the simulated test ranking holds on the board.

The boards carry typical analog blocks (Sallen-Key, biquad and similar) and are kept deliberately simple: the aim is to validate the method, not an application.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T3.1 | Specification of the validation boards with benchmark circuits (Sallen-Key, biquad and similar): faults to inject, accessible nodes and microcontroller | Specification document | 3 weeks |
| T3.2 | Schematic and PCB design with fault injection by relays or jumpers | Manufacturing files | 4 weeks |
| T3.3 | Manufacturing, assembly and bring-up | Working boards | 4 weeks, plus manufacturing lead time |
| T3.4 | Firmware (ESP32 or STM32) that runs the self-test plan exported as JSON | Firmware and plan format | 5 weeks, in parallel with T3.2 and T3.3 |
| T3.5 | Characterisation of the measurement chain (ADC and DAC) and adjustment of `costmodel` | Measured noise and resolution parameters | 2 weeks |
| T3.6 | Experiment E6: measurement campaign with fault injection | Raw measurement data | 4 weeks |
| T3.7 | Measured versus simulated coverage and G3 report | Reasoned decision and simulation-to-reality gap | 3 weeks |
| T3.8 | Release with a DOI and skeletons of P4 and P5 | Release on Zenodo | 3 weeks |

## WP4 · APPLICATIONS

About 7 months. Requires G2 and the case sheets of T1.2.

Three cases, each with a different kind of risk. The specific circuits are refined in T1.2 and at the start of each task.

| Case | Kind of risk |
| --- | --- |
| Cell voltage and current measurement chain of a battery management system | Functional safety: an error that hides an overvoltage is far worse than one that only reduces availability |
| ECG front end | Patient safety (IEC 60601, ISO 14971) |
| Bridge sensor conditioning (strain gauge or thermistor) in an unattended measurement node | Data integrity: an undetected drift corrupts the record without anyone noticing |

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T4.1 | Battery measurement chain: spicefault model, specifications and fault table with severities | Netlist, fault universe and risk table | 5 weeks |
| T4.2 | ECG front end: spicefault model, specifications and fault table with severities | Netlist, fault universe and risk table | 5 weeks, in parallel with T4.1 |
| T4.3 | Bridge sensor conditioning: spicefault model, specifications and fault table with severities | Netlist, fault universe and risk table | 4 weeks |
| T4.4 | Self-test plan for each case: Pareto fronts and risk-weighted coverage with intervals, with and without risk weighting | Plan and coverage per case | 6 weeks |
| T4.5 | Comparison across cases: what the kind of risk changes in the selected tests | Cross-case tables and guidelines | 3 weeks |
| T4.6 | Hardware check of one case, if a board is available from a collaborator | Measured versus simulated coverage on a real board | 6 weeks, optional |
| T4.7 | Skeleton of P7 | Starting text of the paper | 3 weeks |

## WP5 · TOOL AND DISSEMINATION

About 4 months, in parallel with WP4. Requires G2; the dataset requires the WP3 measurements.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T5.1 | Self-test plan exportable from the web GUI starting from a netlist | Feature in the GUI | 5 weeks |
| T5.2 | Documentation with a worked example from netlist to firmware | User guide | 3 weeks |
| T5.3 | Dataset of simulations and measurements with fixed splits, and skeleton of P6 | Deposit with a DOI | 3 weeks |
| T5.4 | Fault diagnosis exercises for teaching, generated from the GUI | Collection of exercises | 3 weeks |
| T5.5 | Final release of `spicefault.testdesign` with a DOI | Release on Zenodo | 2 weeks |

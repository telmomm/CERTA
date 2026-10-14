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
| T0.8 | Requirements of the safety standards on the diagnostic coverage of analog parts (IEC 61508, ISO 26262, IEC 60601-1 with ISO 14971, IEEE 2427): which metric, which target per safety level and how it is justified today | `standards-mapping.md` | 2 weeks, in parallel with T0.5 |

## WP1 · BENCHMARK AND CERTIFICATION

About 5 months. Requires G0. Ends at milestone G1: the baselines reproduce the published figures, or the discrepancy is documented.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T1.1 | Benchmark circuits (Sallen-Key, biquad and leapfrog) in spicefault, with tolerances and fault universe | Netlists and starting simulations | 3 weeks |
| T1.2 | Definition of the lead demonstrator (measurement chain of a battery management system) and of the two secondary cases (ECG front end, bridge sensor conditioning): circuit, specifications, measurement hardware, safety goal with its target level and fault table with severities | One sheet per case | 3 weeks, in parallel with T1.1 |
| T1.3 | `candidates` module: enumerate tests (node × stimulus × feature) from the netlist and the accessible nodes | Module with tests | 3 weeks |
| T1.4 | `metrics` module: detection, false alarms, ambiguity sets and the coverage metrics of the standards (DC and SFF of IEC 61508, SPFM and LFM of ISO 26262), all with Clopper–Pearson intervals | Module with tests | 4 weeks |
| T1.5 | Adaptive Monte Carlo: runs until the interval falls below a target width | Stopping rule built into `metrics` | 2 weeks |
| T1.6 | Reimplemented baselines: Starzyk's entropy, genetic algorithm and fault-pair table with Bhattacharyya and KDE | Baselines in `select` | 6 weeks, in parallel with T1.4 and T1.5 |
| T1.7 | Experiment E1: do the baselines reproduce the published figures? | Table of published versus reproduced figures | 3 weeks |
| T1.8 | Experiment E5: runs needed and stability of the rankings with small samples | Interval width and stability curves | 3 weeks |
| T1.9 | G1 report, first public release of `spicefault.testdesign` with a DOI and skeleton of P2 | Reasoned decision, release on Zenodo | 3 weeks |

## WP2 · FORMULATION AND ALGORITHMS

About 6 months. Requires G1. Ends at milestone G2: the greedy stays close to the optimum and risk weighting changes the selection.

The central problem is to reach a coverage target, set by the safety level, at minimum hardware cost, where the target is checked against the lower bound of the confidence interval and not against the point estimate.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T2.1 | `costmodel` module: cost per node and per measurement; ADC noise, resolution and range | Module and model of a specific microcontroller | 3 weeks |
| T2.2 | `faultprior` module: failure rates per component type (IEC 61709 or SN 29500), split into safe and dangerous failure modes, and severity per fault taken from the case sheets of T1.2 | Module and rate tables | 3 weeks, in parallel with T2.1 |
| T2.3 | Metrics of the formulation: risk-weighted coverage, its lower confidence bound and residual uncertainty about the fault | Extension of `metrics` | 3 weeks |
| T2.4 | Greedy for minimum cost subject to a coverage target, and Pareto front of cost against coverage | `select.pareto` | 3 weeks |
| T2.5 | Exact optimum by integer linear programming on small instances | Reference solution in `select` | 4 weeks |
| T2.6 | `bounds` module: sensitivity matrix and ambiguity groups by SVD | Theoretical bound and testability gap | 4 weeks, in parallel with T2.5 |
| T2.7 | `bench` module and experiments E2 (greedy versus optimum), E3 (joint versus sequential) and E4 (with and without risk) on the benchmark circuits and on the lead demonstrator, with sensitivity analysis to the weights | Tables and Pareto fronts | 6 weeks |
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

## WP4 · SAFETY DEMONSTRATOR AND APPLICATIONS

About 8 months. Requires G2 and the case sheets of T1.2; the hardware demonstrator requires G3. Ends at milestone G4: in the lead demonstrator, the computed coverage meets the safety target with less diagnostic hardware than the table-based FMEDA.

| Case | Role | Kind of risk |
| --- | --- | --- |
| Cell voltage and current measurement chain of a battery management system | Lead demonstrator, ideally co-designed with an industrial partner | Functional safety (ISO 26262 in vehicles, IEC 61508 for industrial and stationary batteries) |
| ECG front end | Secondary case | Patient safety (IEC 60601-1, ISO 14971) |
| Bridge sensor conditioning (strain gauge or thermistor) in an unattended measurement node | Secondary case | Data integrity |

The specific circuits are refined in T1.2.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T4.1 | Lead demonstrator: spicefault model, safety goal, target level and table-based FMEDA as the industry would do it today | Netlist, fault universe and reference FMEDA | 5 weeks |
| T4.2 | Self-test plan that reaches the target coverage at minimum cost, with its interval | Plan, coverage and cost | 4 weeks |
| T4.3 | Experiment E7: mock safety assessment, table-based FMEDA against CERTA (coverage claimed, diagnostic hardware needed, evidence produced) | Comparison report | 4 weeks |
| T4.4 | Hardware demonstrator: the plan running on the partner's board or, failing that, on a board built as in WP3 | Measured versus predicted coverage | 6 weeks, in parallel with T4.5 and T4.6 |
| T4.5 | Secondary case, ECG front end: model, fault table with severities and self-test plan | Plan and coverage | 5 weeks |
| T4.6 | Secondary case, bridge sensor conditioning: model, fault table with severities and self-test plan | Plan and coverage | 4 weeks |
| T4.7 | G4 report and skeleton of P7 | Reasoned decision and starting text of the paper | 3 weeks |

## WP5 · TOOL AND EXPLOITATION

About 4 months, in parallel with WP4. Requires G2; the dataset requires the WP3 measurements.

| Id | Task | Deliverable | Estimated duration |
| --- | --- | --- | --- |
| T5.1 | `fmeda` module: export of the coverage per failure mode, with its interval, to the spreadsheet format used in safety analyses | Module and template | 4 weeks |
| T5.2 | Self-test plan and coverage report from the web GUI starting from a netlist | Feature in the GUI | 5 weeks |
| T5.3 | Documentation with a worked example from netlist to firmware and FMEDA, and a short training course for industry | User guide and course material | 4 weeks |
| T5.4 | Dataset of simulations and measurements with fixed splits, and skeleton of P6 | Deposit with a DOI | 3 weeks |
| T5.5 | Fault diagnosis exercises for teaching, generated from the GUI | Collection of exercises | 3 weeks |
| T5.6 | Final release of `spicefault.testdesign` with a DOI | Release on Zenodo | 2 weeks |

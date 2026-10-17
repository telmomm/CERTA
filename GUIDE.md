# Certified self-test for analog electronics: state of the art, gap and proposal

Oct 12, 2026 · @TelmoMM

## Summary

Functional safety standards require every safety-related product to declare the diagnostic coverage of its hardware. For analog parts that figure is taken today from generic tables, with conservative margins and no uncertainty. CERTA computes it instead: it chooses what an embedded system should measure to reach the coverage that the safety level requires at minimum hardware cost, and it reports that coverage with a confidence interval that can be used as evidence in the safety analysis.

On the research side there is a gap, but not in the optimiser: it is in the formulation. Analog test point selection has been studied for 40 years and is now saturated with metaheuristics and reinforcement learning applied to the same benchmark filters. What nobody brings together is a test design that (1) optimises nodes, stimuli and type of measurement at the same time, (2) with a realistic cost model of what a microcontroller can measure in the field, (3) weighted by the probability and severity of the fault instead of "isolating every class", (4) with statistically certified coverage, aligned with the metrics of the standards, and (5) compared against the theoretical bound of the ambiguity groups.

Proposal: a test design module in spicefault that solves that problem for discrete circuits at board level and exports its result to the FMEDA, with an open benchmark of reimplemented baselines, validation on simple boards and a lead demonstrator, the measurement chain of a battery management system, taken through a mock safety assessment against the table-based FMEDA. Natural targets: IEEE Transactions on Reliability, Reliability Engineering & System Safety or IEEE Transactions on Instrumentation and Measurement.

## Motivation: diagnostic coverage in functional safety

Safety standards turn the detection of faults into a number that decides whether a product can be certified:

| Standard | Field | Coverage metric | Targets |
| --- | --- | --- | --- |
| IEC 61508 | Industrial, generic | Diagnostic coverage DC and safe failure fraction SFF | DC low ≥ 60 %, medium ≥ 90 %, high ≥ 99 %; SFF and hardware fault tolerance set the achievable SIL |
| ISO 26262 | Road vehicles, including traction batteries | Single-point fault metric SPFM and latent fault metric LFM | ASIL B: SPFM ≥ 90 %, LFM ≥ 60 %; ASIL C: ≥ 97 %, ≥ 80 %; ASIL D: ≥ 99 %, ≥ 90 % |
| IEC 60601-1 with ISO 14971 | Medical electrical equipment | No single coverage figure: safety under single fault condition and risk control measures | Each hazardous fault must be detected or made safe |

For digital logic, coverage can be computed by fault simulation. For analog parts the usual practice is to credit each diagnostic technique (a range check, a comparison between two channels, a test pulse) with the coverage that the tables of the standard allow it, low, medium or high, without simulating what the technique actually detects in that circuit. The result is conservative and unverifiable: designs add diagnostic hardware to reach a figure that nobody has measured. IEEE 2427 points in the right direction, coverage computed by simulation as a statistical estimate, but for integrated circuits.

## State of the art

The literature falls into seven families. The first four tackle the problem directly; the last three come from neighbouring areas and provide the missing pieces.

### 1. Test point selection by fault dictionary (1985–2018)

This is the classical core. Hochwald and Bastian introduced ambiguity sets with a threshold of 0.7 V (one diode drop) to build the integer-coded dictionary ([Ma et al., 2018](https://onlinelibrary.wiley.com/doi/full/10.1155/2018/9714206)). On that basis came Starzyk's entropy index, heuristic graph search and the genetic algorithms of Golonek and Rutkowski ([Application of Heuristic Graph Search](https://www.researchgate.net/publication/224348201_Application_of_Heuristic_Graph_Search_to_Test-Point_Selection_for_Analog_Fault_Dictionary_Techniques)).

The problem is known to be NP-hard ([Gao et al., 2014](https://www.researchgate.net/publication/270672050_Entropy_Based_Test_Point_Evaluation_and_Selection_Method_for_Analog_Circuit_Fault_Diagnosis)). Later improvements handle tolerance with fault-pair tables, similarity coefficients under a normal hypothesis or non-parametric tests, always with a Monte Carlo of about 50 runs per fault ([Ma et al., 2018](https://onlinelibrary.wiley.com/doi/10.1155/2018/9714206)).

### 2. Testability and ambiguity groups (symbolic analysis)

The Florence school (Fedi, Manetti, Piccirilli) with Starzyk determines which components are identifiable from the testability and the canonical ambiguity groups ([Fedi et al., 1999](https://flore.unifi.it/handle/2158/215337)). It was later made numerically robust with the SVD of the testability matrix ([Manetti and Piccirilli, 2003](https://flore.unifi.it/handle/2158/311262)).

It gives the theoretical limit of what can be diagnosed, but it is linear or linearised, depends on in-house symbolic tools and considers neither measurement cost nor realistic tolerances.

### 3. Design of stimuli and test frequencies

The excitation is optimised instead of the node: genetic algorithms with wavelet packets to reduce ambiguity under tolerances ([Int. J. Electronics, 2011](https://www.tandfonline.com/doi/abs/10.1080/00207217.2010.506839)) or frequencies selected with ARMA models ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1434841104702216)). It is nearly always solved separately from node selection.

### 4. Recent metaheuristics and machine learning (2021–2025)

This is the most active family and the most saturated:

- Selection based on a deep joint distribution, which considers multiple faults and dependencies between tests ([Zio et al., 2021](https://re.public.polimi.it/handle/11311/1181144)).
- Multi-objective selection with beluga whale optimization coupled to an SDAE classifier ([Electronics, 2025](https://www.mdpi.com/2079-9292/14/8/1528)).
- Deep reinforcement learning that poses the selection as a knapsack with dynamic cost ([Yang et al., 2025](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5338908)); the published version points out that many methods use static representations that ignore the accumulated cost ([EAAI, 2025](https://www.sciencedirect.com/science/article/abs/pii/S0952197625033251)).
- Bhattacharyya coefficient with KDE so as not to assume distributions ([Intelligence & Robotics, 2025](https://www.oaepublish.com/articles/ir.2025.21)).

### 5. Test compaction in integrated circuits

In IC production test, Biswas, Blanton and Stratigopoulos remove redundant specification tests with statistical learning, controlling defect escape and yield loss ([arXiv:0710.4719](https://arxiv.org/abs/0710.4719)). Stratigopoulos estimates those metrics with parts-per-million accuracy using Monte Carlo ([Fast Monte Carlo-Based Estimation](https://www.researchgate.net/publication/273393883_Fast_Monte_Carlo-Based_Estimation_of_Analog_Parametric_Test_Metrics)).

It provides what family 1 lacks: the criterion is meeting specifications, with type I and type II errors under control. But it is pass/fail in production, not localisation in the field.

### 6. Embedded in-field self-test

There are strategies that use only the resources of the microcontroller (ADC, internal operational amplifiers) to self-check configurable analog circuits, with errors attributable to the ADC itself ([Microelectronics Journal](https://www.sciencedirect.com/science/article/abs/pii/S0026269212001644)). They are ad hoc solutions: there is no general method to decide what to measure.

### 7. Standardisation of analog coverage

[IEEE 2427-2025](https://standards.ieee.org/ieee/2427/7233/) defines the defect universe, detectability and statistical coverage from simulation. Its working group justifies the standard by the lack of compatible definitions of coverage ([IEEE P2427 WG](https://sagroups.ieee.org/2427)). It is intended for ICs, not for boards with discrete components.

In functional safety, IEC 61508-2 (Annex A) and ISO 26262-5 (Annex D) list diagnostic techniques with the maximum coverage they can be credited with. They give an upper bound per technique, not a figure computed for a specific circuit.

## Comparison

No family covers more than two or three criteria at once; the proposal column is the only one that brings them together.

| Criterion | Dictionary (1) | Symbolic (2) | Stimuli (3) | ML / RL (4) | IC compaction (5) | Self-test (6) | Proposal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Selects nodes | Yes | Indirectly | No | Yes | No | Ad hoc | Yes |
| Selects stimulus and type of measurement | No | No | Yes | Rarely | Subset of specs | Ad hoc | Yes, jointly |
| Realistic measurement cost | Node count | No | No | Abstract cost | Tester time | Implicit | Embedded hardware model |
| Objective | Isolate classes | Identifiability | Separate classes | Isolate classes | Escape and yield loss | Detect | Coverage target of the safety level at minimum cost |
| Tolerances | Fixed threshold or normal | Ignored | Partial | Small Monte Carlo | Large Monte Carlo | Empirical | Large Monte Carlo |
| Confidence intervals | No | Not applicable | No | No | Yes (ppm) | No | Yes |
| Theoretical bound as reference | No | It is the bound | No | No | No | No | Yes (ambiguity groups) |
| Open code and data | No | In-house programs | No | No | Industrial data | No | Yes |
| Evaluation circuits | Benchmark filters | Small filters | Filters | Benchmark filters | ICs, MEMS | Specific MCU | Filters + safety demonstrator (battery management system) + two secondary cases |

## Identified gap

The gap is the combination of five shortcomings, each documented in the literature reviewed, plus one in industrial practice. Taken separately, some are solved in another field; together, and at board level, they are not.

1. **Nodes, stimuli and measurements are optimised separately in the recent literature.** Families 1 and 4 choose nodes with the stimulus fixed; family 3 chooses stimuli with the node fixed. An embedded system decides all three at once: which ADC channel, which signal its DAC injects and which feature it extracts.
2. **The cost does not reflect the hardware.** What is counted is the number of nodes or an abstract cost. In the field the cost is something else: a free ADC channel is almost free, a node that needs a switch or an extra pin is not, and the ADC resolution limits which differences are detectable.
3. **The objective is to isolate all classes equally.** A short circuit in the blocking capacitor of an applied part does not weigh the same as a 5 % drift in an anti-aliasing filter. Weighting by fault probability and severity of the effect is missing, as FMEDA and ISO 14971 do, as is including the false alarm rate, as IC test compaction does.
4. **The metrics carry no uncertainty.** With 50 to 120 Monte Carlo runs per fault, percentages are published without intervals. IEEE 2427 already requires coverage to be treated as a statistical estimate, but only for ICs.
5. **There is no theoretical reference and no reproducible comparison.** Data-driven methods ignore the bound given by the ambiguity groups, so nobody knows how far a solution is from the achievable optimum. And each paper compares against two or three methods on its own data, without code.
6. **In practice, analog diagnostic coverage is credited, not computed.** Safety analyses take it from the tables of the standards, so the research on test selection never reaches the FMEDA, and the FMEDA never benefits from it.

The gap is not "another optimiser". The defensible novelty is a new formulation of the problem plus an open tool that allows the existing optimisers to be compared within it.

## Check against Scopus

Screening the Scopus export (379 records, 1966–2026) confirms the gap, but forces shortcoming 1 to be qualified. No record brings together more than three of the seven criteria, and none combines risk weighting, an embedded hardware cost model and confidence intervals.

Automatic keyword screening on title, abstract and author keywords, then reviewed by hand. The counts are indicative: they count mentions, not contributions.

| Gap criterion | Records that mention it | Reading after manual review |
| --- | --- | --- |
| Core: selection of nodes, tests or testability | 163 | A broad field; most are fault dictionaries and DfT of integrated circuits |
| Node and stimulus optimised at once | 24 | It exists, but in old ATPG or board works; the recent ML wave abandons it |
| Risk, diagnostic coverage, false alarms or escapes | 20 | Almost all IC production test; none weights by probability and severity |
| Confidence intervals or sample size | 1 | The only result is not about circuits: shortcoming confirmed |
| Theoretical bound (ambiguity groups) | 18 | Symbolic school and Starzyk's; never used as a reference for data-driven methods |
| Board or biomedical | 12 | Only two relevant board works and one on ECG |

### Works to cite and to position against

| Work | What it already covers | What it lacks with respect to the proposal |
| --- | --- | --- |
| [Chakrabarti and Chatterjee, ICCAD 2000](https://doi.org/10.1109/ICCAD.2000.896532) | Transient stimulus, nodes and measurement instants at once; tolerances, measurement error and tester capabilities | Production test; no risk, no embedded cost, no intervals |
| [Huang and Cheng, ITC 1997](https://doi.org/10.1109/TEST.1997.639675) and [TCAS-II 2000](https://doi.org/10.1109/82.877140) | Unpowered boards: test points and stimuli; limited node access | Intended for an in-circuit tester, not for in-field self-test |
| [Tadeusiewicz and Hałgas, JETTA 2017](https://doi.org/10.1007/s10836-017-5650-4) | Excitation nodes, source values and measurement nodes by non-linear programming | No statistical tolerances and no cost |
| [Brosa and Figueras, ETW 1999](https://doi.org/10.1109/ETW.1999.804430) | Subset of tests that maximises coverage at minimum cost, as a covering problem | Abstract cost; no localisation |
| [Zilch, Lubaszewski and Balen, AICSP 2022](https://doi.org/10.1007/s10470-022-02039-6) | SPICE tool that sweeps DC, AC and transient stimuli per node and minimises test time | IC defects; detection only; no risk and no intervals |
| [Tang et al., IEEE TCAD 2018](https://doi.org/10.1109/TCAD.2017.2762647) | Simulation-based testability with KDE, false alarms and ambiguity groups | Does not select tests or model cost |
| [Spinks et al., JETTA 2004](https://doi.org/10.1023/B:JETT.0000009310.48706.b7) | Detection probability under process spread as a metric | Catastrophic IC faults only |
| [Grzechca, ECCTD 2011](https://doi.org/10.1109/ECCTD.2011.6043396) | Optimises the excitation of an ECG amplifier with simulated annealing | No cost and no risk; a single circuit |
| [Yang et al., EAAI 2026](https://doi.org/10.1016/j.engappai.2025.113294) and [Liu et al., IEEE TIM 2025](https://doi.org/10.1109/TIM.2025.3588964) | Same group: nodes with RL and dynamic cost; stimuli with bio-inspired optimisation | Nodes and stimuli in separate papers; benchmark filters |
| [Ankush et al. (CODA), ETS 2026](https://doi.org/10.1109/ETS69887.2026.11591724) | Adaptive test with confidence-based early stopping | Pass/fail in IC production |

Conclusion for the paper: joint optimisation of node and stimulus is not new in itself and this has to be acknowledged by citing Chakrabarti and Huang. The contribution rests on shortcomings 2 to 5 and on recovering the joint formulation that the recent ML literature has abandoned.

## Proposal: formulation

Self-test design is posed as reaching the coverage that the safety level requires at minimum hardware cost. The working title could be *Certified diagnostic coverage at minimum cost: risk-aware joint test design for in-field self-diagnosis of board-level analog circuits*.

### Elements

- **Fault universe** F = {f₀ (fault-free), f₁ … f\_K}: catastrophic faults (open and short) and parametric faults (several deviation levels), generated by spicefault. Each fault carries a prior probability p\_k, taken from component failure rates (IEC 61709 or SN 29500) split into failure modes, a classification as safe or dangerous, and a severity w\_k, which comes from the risk analysis or from whether the fault violates a specification or a safety goal.
- **Candidate tests** t = (s, n, m): a stimulus s (DC level, sine at a frequency, step), an accessible node n and a measured feature m (mean value, amplitude, phase, settling time, supply current).
- **Cost** with a shared part: accessing a node costs once (switch, pin, ADC channel) and each measurement adds time. ADC noise and resolution are included in the measurement model.
- **Tolerances** by large Monte Carlo, with distributions of the components and of the ADC.

### Metrics for a subset of tests Q

Risk-weighted detection coverage, analogous to the diagnostic coverage of FMEDA:

```latex
DC_w(Q) = \frac{\sum_{k=1}^{K} p_k \, w_k \, P(\text{alarm} \mid f_k, Q)}{\sum_{k=1}^{K} p_k \, w_k}
```

False alarm rate on fault-free circuits within tolerance, analogous to yield loss in IC test:

```latex
FA(Q) = P(\text{alarm} \mid f_0, Q)
```

Alignment with the standards. With w\_k = 1 and the sum restricted to dangerous faults, DC\_w is the diagnostic coverage of IEC 61508 for the element, DC = λ\_DD / λ\_D, where the dangerous detected rate of each fault is its dangerous rate times its detection probability. The other metrics follow from the same rates:

```latex
SFF = \frac{\lambda_S + \lambda_{DD}}{\lambda_S + \lambda_D}, \qquad
SPFM = 1 - \frac{\sum (\lambda_{SPF} + \lambda_{RF})}{\sum \lambda}, \qquad
LFM = 1 - \frac{\sum \lambda_{MPF,L}}{\sum (\lambda - \lambda_{SPF} - \lambda_{RF})}
```

The difference with current practice is that each detection probability is computed by simulation for the specific circuit and measurement hardware, with its interval, instead of being credited from a table.

Localisation capability as residual uncertainty about the fault, or as the expected size of the candidate set:

```latex
H(F \mid Y_Q) = -\sum_{k} \int p(f_k, y) \log p(f_k \mid y) \, dy
```

### Problem

```latex
\min_{Q} \; C(Q) \quad \text{s.t.} \quad \underline{DC}_w(Q) \ge DC^{*}, \;\; FA(Q) \le \alpha
```

where DC\* is the target set by the safety level (for example SPFM ≥ 97 % for ASIL C) and the underlined term is the lower bound of the confidence interval of the coverage, not its point estimate: the claim must hold with a stated confidence. Localisation, H(F | Y\_Q), is a secondary objective among the solutions of equal cost.

The general result is a Pareto front of cost against certified coverage: for each budget, which coverage can be claimed, and for each safety level, how much diagnostic hardware it costs.

### Algorithms

1. **Greedy by information gain per unit cost.** This is the main method. If the measurements were conditionally independent given the fault, mutual information would be submodular and the greedy would have an approximation guarantee of (1 − 1/e). With shared tolerances that hypothesis does not hold: how far it departs from the optimum will be measured empirically.
2. **Exact optimum by integer linear programming** on small instances, formulated as fault-pair covering with costs. It serves as ground truth.
3. **Reimplemented baselines**: Starzyk's entropy, genetic algorithm, fault-pair table with Bhattacharyya and KDE and, time permitting, a reinforcement learning variant.

### Theoretical bound

From the numerical sensitivity matrix of all candidate tests (SPICE sensitivity analysis or finite differences), the SVD gives the canonical ambiguity groups. That fixes the maximum resolution achievable with all the tests. The "testability gap" of a solution is the distance between its resolution and that bound.

### Statistical certification

Each detection probability is reported with a Clopper–Pearson interval. The number of Monte Carlo runs per fault is set adaptively until the interval falls below a target width, instead of using a fixed number. The lower bound of the aggregated coverage is obtained conservatively from the per-fault lower bounds, or by bootstrap when that is too pessimistic.

## Experimental methodology

Evaluation is on six circuits: three benchmark ones to compare with the literature, a lead demonstrator with a direct safety use and two secondary cases with other kinds of risk. The method is domain-neutral; the secondary cases show that risk weighting is general.

| Circuit | Role | Why |
| --- | --- | --- |
| Sallen-Key band-pass | Benchmark | It is the most used; it allows published figures to be reproduced |
| Four-op-amp biquad | Benchmark | Medium size, many ambiguity groups |
| Leapfrog low-pass | Benchmark | The largest of the usual ones |
| Battery management system measurement chain (cell voltage and current) | Lead demonstrator | Functional safety (ISO 26262 in vehicles, IEC 61508 for industrial and stationary batteries): an error that hides an overvoltage is far worse than one that only reduces availability |
| ECG front end | Secondary case | Patient safety (IEC 60601, ISO 14971); already modelled in the author's repository |
| Bridge sensor conditioning in an unattended node | Secondary case | Data integrity: an undetected drift corrupts the record without anyone noticing |

The specific application circuits are still to be refined. The Howland current source (bioimpedance) is kept in reserve as a second biomedical case.

### Experiments

| Id | Question | Expected result |
| --- | --- | --- |
| E1 | Do the reimplemented baselines reproduce the published figures? | Validation of the tool and of the benchmark |
| E2 | How far is the greedy from the exact optimum? | Gap to the optimum on small instances |
| E3 | What does optimising node, stimulus and measurement at once add? | Joint versus sequential Pareto front |
| E4 | Does the solution change when weighting by risk? | Coverage of severe faults with and without weighting |
| E5 | How many Monte Carlo runs are needed? | Interval width curves; instability of the rankings with small samples |
| E6 | Do the chosen tests hold in hardware? | Measured versus simulated coverage on a board with fault injection |
| E7 | What does computing the coverage change with respect to crediting it from tables? | In the lead demonstrator: coverage claimed, diagnostic hardware needed and evidence produced, table-based FMEDA against CERTA |

### Hardware validation

Simple boards with typical analog blocks (Sallen-Key, biquad and similar) and fault injection by relays or jumpers, measured with the ADC and DAC of a microcontroller (ESP32 or STM32). The boards are kept deliberately simple: the aim is to validate the method, not an application. A small number of faults per board is enough to check that the simulated test ranking is preserved.

E7 is the experiment that speaks to industry: if the computed coverage reaches the safety target with less diagnostic hardware than the table-based FMEDA, or shows that a tabulated claim does not hold, the method has a direct use.

E5 deserves special attention: if it is shown that with 50 runs the rankings of published methods are not stable, that alone calls part of the literature into question and reinforces the need to certify.

## Implementation in spicefault

A `spicefault.testdesign` subpackage is added that consumes the simulations spicefault already generates. The names are a proposal.

| Module | Function |
| --- | --- |
| `candidates` | Enumerates tests (node × stimulus × feature) from the netlist and a list of accessible nodes |
| `costmodel` | Cost per node and per measurement; ADC noise, resolution and range |
| `faultprior` | Probabilities per component type and severity per fault or per specification violation |
| `metrics` | DC\_w, FA, H(F\|Y), ambiguity sets, the metrics of the standards (DC, SFF, SPFM, LFM), Clopper–Pearson intervals |
| `bounds` | Sensitivity matrix and ambiguity groups by SVD |
| `select` | Cost-benefit greedy, exact ILP (PuLP or OR-Tools) and baselines |
| `bench` | Runs all methods on all circuits and generates tables and Pareto fronts |
| `fmeda` | Exports the coverage per failure mode, with its interval, to the spreadsheet format used in safety analyses |

A typical use would be to generate the candidates, load the cost model of the microcontroller, call `select.pareto(...)` with a coverage target, export the self-test plan (which channel, which stimulus, which thresholds) as JSON for the firmware and the coverage per failure mode to the FMEDA.

This layer also serves the web GUI: the user uploads a netlist and gets the test plan and its coverage.

## Phases and roadmap

The project takes about 26 months part-time (November 2026 to December 2028), in six phases that leave seven publications. The rule is to start writing each paper as soon as the experiment that supports it is closed, not at the end of the phase. The introduction and the state of the art of F0 are reused in all of them.

The main paper closes F2 and coincides with the start of the hardware phase.

### Phases and milestones

| Phase | Dates | Work | Experiments | Milestone to move on | If the milestone fails |
| --- | --- | --- | --- | --- | --- |
| F0 State of the art | Nov 2026 – Jan 2027 | Systematic search in Scopus, IEEE Xplore and Web of Science with a PRISMA protocol; in-depth reading of Chakrabarti, Huang, Zilch and Tang; mapping of the coverage requirements of the safety standards | — | G0: nobody has combined embedded cost, risk and certification at board level | The benchmark and the certification become the main contribution |
| F1 Benchmark and certification | Jan – May 2027 | `candidates` and `metrics` modules with the metrics of the standards, intervals and adaptive Monte Carlo, baselines; definition of the lead demonstrator and the two secondary cases; first public release of `spicefault.testdesign` with a DOI | E1, E5 | G1: the baselines reproduce the published figures, or the discrepancy is documented | The lack of reproducibility becomes the central result of P2 |
| F2 Formulation and algorithms | Jun – Nov 2027 | `costmodel`, `faultprior`, minimum cost for a coverage target (greedy and exact ILP), theoretical bound by SVD | E2, E3, E4 | G2: the greedy stays close to the optimum and risk weighting changes the selection | P3 focuses on the formulation and the benchmark; the greedy remains one more method |
| F3 Board validation | Oct 2027 – Apr 2028 | Simple boards with typical analog blocks (Sallen-Key, biquad and similar) and fault injection; firmware on ESP32 or STM32 that runs the test plan | E6 | G3: the simulated test ranking holds on the board | The simulation-to-reality gap is published and bounded |
| F4 Safety demonstrator and applications | May – Dec 2028 | Battery management system measurement chain taken to a mock safety assessment against a table-based FMEDA, on hardware; ECG front end and bridge sensor conditioning as secondary cases | E7; E3 and E4 on the application circuits | G4: the computed coverage meets the safety target with less diagnostic hardware than the table-based FMEDA | The result is reported as evidence that complements the FMEDA, and the cases where the tables overestimate become the contribution |
| F5 Tool and exploitation | In parallel with F4 | Export to FMEDA, web GUI, documentation and training for industry, dataset and teaching material | — | — | — |

F2 and F3 overlap by two months on purpose: board design starts while the F2 experiments are being closed.

### Publications and when to write them

| Id | Content | Written | Submitted | Possible venue | Supported by |
| --- | --- | --- | --- | --- | --- |
| P1 | Systematic review of node and stimulus selection for analog test (1966–2026) | Dec 2026 – Mar 2027 | Mar 2027 | JETTA or Measurement | F0 |
| P2 | Note: reproducibility of published methods and instability of rankings with small Monte Carlo | Apr – Jun 2027 | Jun 2027 | Test conference (ETS, LATS or IMSTW) or letter in JETTA | E1, E5 |
| P3 | Main paper: joint test design with embedded cost, risk and statistical certification | Sep 2027 – Jan 2028 | Jan 2028 | IEEE Transactions on Reliability or Reliability Engineering & System Safety | E1–E5 |
| P4 | Conference paper with the first board measurements | Jan – Feb 2028 | Feb 2028 | I2MTC or MeMeA | First results of E6 |
| P5 | Embedded self-test validated on a board | Mar – Jun 2028 | Jun 2028 | IEEE Transactions on Instrumentation and Measurement | Full E6 |
| P6 | Data descriptor: simulations and measurements with fixed splits | Jun – Jul 2028 | Jul 2028 | Data in Brief | F1, F3 and F5 |
| P7 | Computed versus table-based diagnostic coverage: a mock safety assessment of a battery management system, with two secondary cases | Aug – Nov 2028 | Nov 2028 | To be decided once the demonstrator is fixed (energy or safety journal) | F4 |

The tasks each paper requires, the alternative venues, five optional papers (P8–P12) and the intellectual property options are in the [dissemination plan](WP5-tool-and-exploitation/T5.7-dissemination-and-ip/plan.md), which is the reference when this table and the plan differ.

### Contributions without a paper

- spicefault releases with a DOI on Zenodo at the close of F1, F2 and F3, so that each paper cites the exact code it uses.
- The spicefault paper for IEEE TCAD can mention `testdesign` as work in progress.
- In F5, the web GUI generates fault diagnosis exercises for teaching.

### Open decisions

- **Journal for P3.** If the spicefault methodology paper goes to IEEE Transactions on Reliability, it is better to take P3 to Reliability Engineering & System Safety so as not to coincide in the same journal and dates.
- **Timing of P1.** The review makes the gap public before P3. It should be limited to mapping the field and pointing out directions, without anticipating the formulation.
- **Conference deadlines.** The dates of P2 and P4 are indicative; they have to be adjusted to the calls of ETS, LATS, I2MTC and MeMeA.

## Impact and exploitation

- **Who uses it.** Designers and safety engineers of products that must be certified: automotive and industrial electronics, battery management systems, medical equipment. The output enters a document they already produce, the FMEDA.
- **Technology readiness.** From level 2–3 (formulation and simulation) to level 4 (validation on laboratory boards, WP3), and level 5 with the lead demonstrator on a partner's board (WP4).
- **Measurable outcomes.** Coverage reported with a confidence interval of a stated width; diagnostic hardware needed to reach a given safety level, against the table-based FMEDA (E7); measured against predicted coverage on at least two boards (E6 and T4.4).
- **Partners sought.** A research group in energy electronics and battery management, a manufacturer of battery management systems or industrial electronics for the lead demonstrator, a functional safety expert and, if possible, a letter of support from a certification body.
- **Funding.** The project fits national and regional competitive calls for research projects and, with an industrial partner, public-private collaboration calls. In European programmes it fits better as a work package of a larger consortium in electronics or batteries.
- **Secondary impact.** Self-diagnosis that locates the faulty component supports repair instead of replacement and the qualification of second-life batteries.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| A reviewer reads it as "another node selection method" in a saturated field | Sell the formulation and the benchmark, not the optimiser; show that the existing methods are particular cases of the problem |
| The published baselines cannot be reproduced for lack of detail | Document it as a result (E1) and publish the reimplementations |
| The fault probabilities and severities look arbitrary | Take rates from reliability standards and severities from specifications; sensitivity analysis to those weights |
| The (1 − 1/e) guarantee does not hold with shared tolerances | Present it as a motivated heuristic and measure the gap to the ILP |
| The computational cost of the large Monte Carlo | The parallelisation spicefault already has and adaptive sampling |
| Hardware validation drags on | Limit it to simple boards with benchmark circuits and few faults; the main paper does not depend on it |
| A certification body does not accept coverage computed by simulation | Present it as evidence that complements the FMEDA, not as a replacement; back it with hardware fault injection (E6, T4.4) and with the confidence bounds |
| No industrial partner for the lead demonstrator | Build it on an open reference design of a battery management system, on a board made as in WP3 |
| The split of failure rates into modes is uncertain | Use published failure mode distributions and analyse the sensitivity of the coverage to them |

**Still to be checked:** this review is based on web search. Before writing, a systematic search in Scopus or IEEE Xplore is advisable, especially from 2023 to 2026 and for the groups of Stratigopoulos and Florence, in case one of them has already combined compaction with localisation at board level.

## Sources

- [Ma et al., 2018 — Test point selection based on similarity coefficient](https://onlinelibrary.wiley.com/doi/full/10.1155/2018/9714206)
- [Gao et al., 2014 — Entropy based test point evaluation and selection](https://www.researchgate.net/publication/270672050_Entropy_Based_Test_Point_Evaluation_and_Selection_Method_for_Analog_Circuit_Fault_Diagnosis)
- [Application of Heuristic Graph Search to Test-Point Selection](https://www.researchgate.net/publication/224348201_Application_of_Heuristic_Graph_Search_to_Test-Point_Selection_for_Analog_Fault_Dictionary_Techniques)
- [Fedi, Manetti, Piccirilli, Starzyk, 1999 — Optimum set of testable components](https://flore.unifi.it/handle/2158/215337)
- [Manetti and Piccirilli, 2003 — SVD approach for ambiguity groups](https://flore.unifi.it/handle/2158/311262)
- [Design of test stimuli and minimisation of ambiguity (Int. J. Electronics)](https://www.tandfonline.com/doi/abs/10.1080/00207217.2010.506839)
- [Selection of input stimulus using ARMA model](https://www.sciencedirect.com/science/article/abs/pii/S1434841104702216)
- [Joint distribution-based test selection under multiple faults (Zio et al., 2021)](https://re.public.polimi.it/handle/11311/1181144)
- [Multi-objective selection of measurement nodes (Electronics, 2025)](https://www.mdpi.com/2079-9292/14/8/1528)
- [Test point selection with deep reinforcement learning (SSRN, 2025)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5338908)
- [Test point selection with deep reinforcement learning (EAAI, 2025)](https://www.sciencedirect.com/science/article/abs/pii/S0952197625033251)
- [Extended fault-pair Boolean table with Bhattacharyya and KDE (2025)](https://www.oaepublish.com/articles/ir.2025.21)
- [Biswas et al. — Specification test compaction for analog circuits and MEMS](https://arxiv.org/abs/0710.4719)
- [Stratigopoulos — Fast Monte Carlo-based estimation of analog parametric test metrics](https://www.researchgate.net/publication/273393883_Fast_Monte_Carlo-Based_Estimation_of_Analog_Parametric_Test_Metrics)
- [Low-cost configurability test for an embedded analog circuit (MSP430)](https://www.sciencedirect.com/science/article/abs/pii/S0026269212001644)
- [IEEE 2427-2025 — Analog defect modeling and coverage](https://standards.ieee.org/ieee/2427/7233/)
- [IEEE P2427 Working Group](https://sagroups.ieee.org/2427)

* Scopus export of 12 October 2026 (379 records), screened in that session; the "Check against Scopus" table links the key works by DOI. Spinks et al., JETTA 2004: [10.1023/B:JETT.0000009310.48706.b7](https://doi.org/10.1023/B:JETT.0000009310.48706.b7)

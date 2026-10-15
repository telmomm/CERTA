# Benchmark circuits

The three benchmark circuits of WP1, as simulated by `01_benchmark_circuits.ipynb`. Netlists are in `netlists/`. Each sheet gives where the circuit comes from, what is taken as published and what is an assumption of CERTA. Faults are injected by spicefault, so the netlists carry no fault-emulation elements.

Common to all three:

- **Fault universe:** open (100 MΩ in series) and short (1 Ω in parallel) on every resistor and capacitor, plus a high and a low parametric fault on each of them. The faults used by the source paper are tagged `reference = y`.
- **Out of the universe:** op-amp faults and sources. Op-amps are treated as one part at board level; their failure modes come with the rates of T2.2.
- **Tolerances** are applied before the fault is injected, and a parametric fault acts on the drawn value.

## Sallen-Key band-pass

| | |
| --- | --- |
| Source | Aminian and Aminian, IEEE TCAS-II 47(2), 2000; Aminian, Aminian and Collins, IEEE TIM 51(3), 2002 |
| Values | R1 = 1 kΩ, R2 = 3 kΩ, R3 = 2 kΩ, R4 = R5 = 4 kΩ, C1 = C2 = 5 nF |
| Specification | Centre frequency 25 kHz |
| Op-amp | Single-pole macromodel, µA741-like (A0 = 2·10⁵, GBW = 1 MHz). Assumption |
| Tolerances | R ± 5 %, C ± 10 %, uniform. The distribution is an assumption |
| Reference faults | R2, R3, C1, C2 at ± 50 %: 8 fault classes plus fault-free |
| Accessible nodes | Output only in the source; `a`, `b` and `n` are candidates for T1.3 |

Notes:

- The values were transcribed from a secondary open-access source (Sci. Rep. 15, 2025, doi:10.1038/s41598-025-02596-6); they and the ± 50 % of the faults must be checked against the original papers. That source gives R4 = 2.8 kΩ and faults at ± 30 %: published reuses of this circuit do not agree, which is relevant to E1.
- The topology was checked by simulation: the response peaks at the published centre frequency.

## Four-op-amp biquad high-pass

| | |
| --- | --- |
| Source | Aminian, Aminian and Collins, IEEE TIM 51(3), 2002 |
| Values | R1 = R2 = R3 = 6.2 kΩ, R4 = 1.6 kΩ, R5 = R6 = 5.1 kΩ, R7 = R8 = R9 = 10 kΩ, R10 = 11.5 kΩ, C1 = C2 = 5 nF (secondary source as above) |
| Specification | Cut-off frequency 10 kHz |
| Tolerances | R ± 5 %, C ± 10 % |
| Reference faults | R1, R2, R3, R4, C1, C2 at ± 50 %: 12 fault classes plus fault-free |

**Pending:** the netlist. The node connections are only given in the figure of the original paper, which is not open access. It is written once the PDF is available, and is accepted only if it reproduces the 10 kHz cut-off.

## Leapfrog low-pass

| | |
| --- | --- |
| Source | ITC'97 benchmark (Kaminska et al., Proc. ITC 1997), with the fault model and tolerances of Kondagunturi, Bradley, Maggard and Stroud, Proc. IEEE Southeastcon 1999, pp. 217–220 |
| Netlist | The benchmark page of C. Stroud at Auburn University (archived), without its fault-emulation resistors |
| Values | R1–R13 = 10 kΩ, C1 = C4 = 10 nF, C2 = C3 = 20 nF |
| Op-amp | CMOS two-stage `Opamp2` of the benchmark, at transistor level, ± 15 V |
| Tolerances | Normal, σ = 2 % for R1–R13 and C1–C3, σ = 3 % for C4, truncated at 3σ |
| Reference faults | Open and short on every R and C (34) and parametric at ± 6σ (± 12 %, ± 18 % for C4) |

Notes:

- The benchmark also defines 120 transistor-level op-amp faults (20 per op-amp), which are left out.
- The source notes that the netlist has 13 resistors while the ITC'97 schematic shows 12. The netlist is followed.

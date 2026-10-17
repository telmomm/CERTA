---
title: "Screening criteria"
subtitle: "One-page sheet for screening titles and abstracts"
author: "Telmo Miguel-Medina"
date: today
doctype: "Guide"
reference: "WP0 · T0.1"
---

# What we are looking for {-}

Works on analog circuits of two kinds:

- **Test design:** works that decide **what to measure or which signal to apply** in order to detect or locate faults. We are interested in the choice of the test, not in the classifier that interprets the measurements.
- **Safety coverage:** works that **compute or demonstrate the coverage of the diagnostics** of an analog part with respect to a safety standard (IEC 61508, ISO 26262, IEC 60601, IEEE 2427), by simulation, fault injection or measurement.

# What has to be done {-}

The records are read one at a time, with their title and abstract, in the notebook of `T0.3-screening` or in the screening spreadsheet. For each one, choose one of these three decisions:

| Decision | When |
| --------- | ------------------------------------------------------------ |
| `include` | It meets the three questions below |
| `exclude` | It clearly fails one of them; the reason is recorded |
| `doubt` | The abstract is not enough to decide. When in doubt, `doubt`: it will be settled with the full text |

Indicative pace: one or two minutes per record. There is no need to open the paper.

# The three questions {-}

1. **Is it an analog electronic circuit**, or the analog part of a mixed-signal one?
2. **Does it choose, order or optimise** test points, nodes, stimuli, frequencies, measurements or specification tests, or analyse testability or ambiguity groups? **Or does it compute the coverage** of the diagnostics of an analog part against a safety standard?
3. **Does it propose a method and apply it** to at least one circuit?

Three yeses: `include`.

# Exclusion reasons {-}

Only the first one that applies is recorded.

| Code | Reason | Typical example |
| -------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| E1 | Digital only | Test point insertion in logic, scan chains, fault injection in a processor |
| E2 | Diagnosis without selection | "Fault diagnosis with wavelets and a neural network", always measuring the output |
| E3 | Other domain | Power networks, sensor placement in a plant, battery state of charge or cell faults |
| E4 | Test technique or structure without selection or coverage | A BIST architecture, a simulator or a fault model that neither discusses what to measure nor computes a safety coverage |
| E5 | Not a primary study | Editorial, tutorial, review (reviews are also tagged with `review` in `notes`) |

# Cases that tend to cause trouble {-}

- **"Feature selection".** If what is chosen are frequencies, nodes or sampling instants, `include`. If they are mathematical transformations of a signal already measured, `exclude` by E2.
- **Analog automatic test pattern generation (ATPG).** `include`.
- **System-level test selection** (dependency matrices): `include` only if the example is an analog circuit; if that is not known, `doubt`.
- **Integrated circuit or board.** It makes no difference: both are in scope.
- **A fixed safety mechanism whose coverage is computed** (a window comparator, a redundant channel, an analog BIST with its coverage under ISO 26262): `include`, even if it does not choose what to measure.
- **FMEDA or safety analysis that takes the coverage from tables**, without computing it: `exclude` by E4 and write `practice` in `notes`; T0.8 uses them.
- **Battery management systems.** Only the diagnostics of the analog measurement chain are in scope; state estimation and cell faults are E3.
- **English abstract of a paper in another language.** It is screened by the abstract all the same.

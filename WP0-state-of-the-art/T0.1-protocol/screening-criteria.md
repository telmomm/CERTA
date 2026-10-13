# Screening criteria: one-page sheet

For whoever screens titles and abstracts. Nothing else needs to be read.

## What we are looking for

Works on analog circuits that **decide what to measure or which signal to apply** in order to detect or locate faults. We are interested in the choice of the test, not in the classifier that interprets the measurements.

## What has to be done

The notebook of `T0.3-screening` shows the records one at a time, with title and abstract. For each one, choose one of these three decisions:

| Decision | When |
| --- | --- |
| `include` | It meets the three questions below |
| `exclude` | It clearly fails one of them; the reason is recorded |
| `doubt` | The abstract is not enough to decide. When in doubt, `doubt`: it will be settled with the full text |

Indicative pace: one or two minutes per record. There is no need to open the paper.

## The three questions

1. **Is it an analog electronic circuit**, or the analog part of a mixed-signal one?
2. **Does it choose, order or optimise** test points, nodes, stimuli, frequencies, measurements or specification tests? It also counts if it analyses testability or ambiguity groups, or if it is an in-field self-test of an analog board that decides what to measure.
3. **Does it propose a method and apply it** to at least one circuit?

Three yeses: `include`.

## Exclusion reasons

Only the first one that applies is recorded.

| Code | Reason | Typical example |
| --- | --- | --- |
| E1 | Digital only | Test point insertion in logic, scan chains |
| E2 | Diagnosis without selection | "Fault diagnosis with wavelets and a neural network", always measuring the output |
| E3 | Other domain | Power networks, sensor placement in a plant |
| E4 | Test technique or structure without selection | A BIST architecture, a simulator or a fault model that does not discuss what to measure |
| E5 | Not a primary study | Editorial, tutorial, review (reviews are also tagged with `review` in `notes`) |

## Cases that tend to cause trouble

- **"Feature selection".** If what is chosen are frequencies, nodes or sampling instants, `include`. If they are mathematical transformations of a signal already measured, `exclude` by E2.
- **Analog automatic test pattern generation (ATPG).** `include`.
- **System-level test selection** (dependency matrices): `include` only if the example is an analog circuit; if that is not known, `doubt`.
- **Integrated circuit or board.** It makes no difference: both are in scope.
- **English abstract of a paper in another language.** It is screened by the abstract all the same.

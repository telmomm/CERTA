<p align="center">
  <img src="docs/assets/banners/certa-banner-github.png" alt="CERTA: Certified, Embedded, Risk-aware Test design for Analog circuits" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-WP0%20in%20progress-00BFA5" alt="Status: WP0 in progress">
  <img src="https://img.shields.io/badge/project-research-0B2D4A" alt="Research project">
  <img src="https://img.shields.io/badge/python-%E2%89%A5%203.11-00AEEF" alt="Python 3.11 or later">
</p>

# CERTA

**Certified, Embedded, Risk-aware Test design for Analog circuits.** A research project on certified self-test for analog electronics: deciding what an embedded system should measure so that the diagnostic coverage required by functional safety standards is computed and demonstrated, not estimated from tables.

**Objective.** Given the schematic of a board, the measurement hardware it carries and the safety target it must meet, to obtain the self-test plan that reaches the diagnostic coverage required by IEC 61508 or ISO 26262 at minimum hardware cost, with a confidence interval on that coverage, and to show on real boards that the firmware detects the injected faults with the predicted coverage. The method is domain-neutral; the lead demonstrator is the measurement chain of a battery management system.

## The problem

Every manufacturer that certifies safety-related electronics (automotive, industrial, batteries, medical) has to declare the diagnostic coverage of its hardware: the fraction of dangerous faults that its diagnostics detect. For analog parts that figure is taken today from generic tables of diagnostic techniques, with conservative margins and no uncertainty, which leads to more diagnostic hardware than needed or to a lower safety rating than the design deserves.

On the research side, analog test point selection has been studied for forty years and is now saturated with metaheuristics applied to the same benchmark filters. The gap is not in the optimiser but in the formulation: nobody brings together the five pieces that an in-field self-test needs.

| | Shortcoming in the literature | What CERTA proposes |
| :---: | --- | --- |
| <img src="docs/assets/icons/test-box.png" width="40" alt=""> | Nodes, stimuli and measurements are optimised separately | Joint design of node, stimulus and measured feature |
| <img src="docs/assets/icons/embedded-box.png" width="40" alt=""> | Cost is a count of nodes | A cost model of the embedded hardware: channels, switches, ADC noise and resolution |
| <img src="docs/assets/icons/risk-box.png" width="40" alt=""> | All fault classes weigh the same | Coverage weighted by fault probability and severity, with a bounded false alarm rate |
| <img src="docs/assets/icons/certification-box.png" width="40" alt=""> | Coverage without uncertainty: 50 to 120 Monte Carlo runs in research, generic tables in safety analyses | Diagnostic coverage computed with confidence intervals and aligned with the metrics of IEC 61508 and ISO 26262 |
| <img src="docs/assets/icons/certification-box.png" width="40" alt=""> | No theoretical bound and no reproducible comparison | Gap to the ambiguity groups and an open benchmark of reimplemented baselines |

The expected outcome is a `spicefault.testdesign` module that, starting from a netlist, returns the self-test plan (which channel, which stimulus, which thresholds), its diagnostic coverage with a confidence interval and an export for the safety analysis (FMEDA). It is validated on boards and demonstrated on a battery management system, with two secondary cases. The motivation, the formulation and the full plan are in [GUIDE.md](GUIDE.md).

<p align="center"><img src="docs/assets/backgrounds/certa-divider.png" alt="" width="100%"></p>

## Work packages

| Package | What it does | Milestone | Status |
| --- | --- | --- | --- |
| [WP0 · State of the art](WP0-state-of-the-art/) | Systematic review in Scopus, IEEE Xplore and Web of Science; what the safety standards require of analog diagnostic coverage | G0: the gap exists | In progress |
| [WP1 · Benchmark and certification](WP1-benchmark-and-certification/) | Coverage metrics of the standards with intervals, adaptive Monte Carlo and reimplemented baselines; definition of the demonstrator and the cases | G1: the baselines reproduce the published figures | In progress |
| [WP2 · Formulation and algorithms](WP2-formulation-and-algorithms/) | Minimum hardware cost to reach a coverage target: cost model, risk weighting, greedy, exact ILP and theoretical bound | G2: the greedy stays close to the optimum and risk changes the selection | Pending |
| [WP3 · Board validation](WP3-board-validation/) | Simple boards with typical analog blocks (Sallen-Key, biquad), fault injection and self-test firmware | G3: the simulated ranking holds on the board | Pending |
| [WP4 · Safety demonstrator and applications](WP4-demonstrator-and-applications/) | Battery management system measurement chain taken to a mock safety assessment against a table-based FMEDA; ECG front end and bridge sensor conditioning as secondary cases | G4: computed coverage meets the safety target with less diagnostic hardware than the table-based FMEDA | Pending |
| [WP5 · Tool and exploitation](WP5-tool-and-exploitation/) | Export to FMEDA, web GUI, documentation and training for industry, dataset and teaching material | — | Pending |

The tasks of each package and their estimated duration are in [ROADMAP.md](ROADMAP.md).

## Repository structure

| Path | Contents |
| --- | --- |
| `WPn-…/` | One work package per folder, with its own `README.md` and one subfolder per task (`T0.1-protocol`…) |
| [GUIDE.md](GUIDE.md) | Starting document: state of the art, gap, formulation, experiments and planned publications |
| [ROADMAP.md](ROADMAP.md) | Tasks, deliverables and estimated duration |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to work in the repository: notebooks, data, documents and commits |
| [docs/assets/](docs/assets/) | Visual identity |
| [docs/templates/](docs/templates/) | Templates for documents, notebooks, Word and PowerPoint, with the project header, footer and logo |
| [web/](web/) | Project website, built with Quarto. Preview with `quarto preview web` |

## Getting started

Python 3.11 or later is required.

```bash
git clone https://github.com/telmomm/CERTA.git
cd CERTA
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Analyses are Jupyter notebooks inside the folder of each task and are committed executed. To re-run one, from its folder:

```bash
jupyter nbconvert --to notebook --execute --inplace 01_screening.ipynb
```

## Visual identity

The reference is [visual-identity.png](docs/assets/visual-identity.png). The PNGs in [docs/assets/](docs/assets/) are generated with `python3 docs/assets/generate.py` (requires `rsvg-convert` and the Avenir Next font); to change an asset, edit the script, not the PNG.

| Folder | Assets |
| --- | --- |
| `logo/` | Logo and logo mark for light and dark (`-dark`) backgrounds, with transparency, and `certa-favicon.png` |
| `banners/` | GitHub header (2560×800), social preview (1280×640) and square for announcements (1080×1080) |
| `icons/` | Certification, embedded, risk and test: navy line, white line (`-white`) and on a coloured box (`-box`) |
| `backgrounds/` | Dark and light slide backgrounds (1920×1080) and divider |

| | | | | |
| :---: | :---: | :---: | :---: | :---: |
| ![#0B2D4A](https://img.shields.io/badge/-0B2D4A-0B2D4A?style=flat-square) | ![#00BFA5](https://img.shields.io/badge/-00BFA5-00BFA5?style=flat-square) | ![#00AEEF](https://img.shields.io/badge/-00AEEF-00AEEF?style=flat-square) | ![#A7E3F7](https://img.shields.io/badge/-A7E3F7-A7E3F7?style=flat-square) | ![#E6EEF6](https://img.shields.io/badge/-E6EEF6-E6EEF6?style=flat-square) |
| Navy | Teal | Blue | Sky | Ice |

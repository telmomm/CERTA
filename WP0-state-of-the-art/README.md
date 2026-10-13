# WP0 · State of the art

Notes on the contents of this folder. The tasks and their estimated duration are in [ROADMAP.md](../ROADMAP.md).

## Objective

To establish, with a reproducible systematic review, whether the gap that motivates CERTA exists: that nobody has combined embedded hardware cost, risk weighting and statistical certification in test design for analog circuits at board level (milestone G0). Along the way, to leave ready the material used by the following phases: the reusable state of the art, the works to position against and the published figures that WP1 will try to reproduce.

## Scope

- **In:** literature on the selection of test points, stimuli and measurements, testability and self-test in analog and mixed-signal circuits, with no date limit; search in Scopus, Web of Science and IEEE Xplore, citation tracking and author searches; screening, data extraction, in-depth reading of the four key works, G0 report and skeleton of P1.
- **Out:** reimplementing methods (WP1), developing the formulation (WP2), diagnosis works that only classify on fixed measurements, digital test and the full writing of P1.
- **Estimated duration:** about 3 months.

## Folders

| Folder | What goes inside |
| --- | --- |
| `T0.1-protocol` | `protocol.md`, `search-strings.md` (the searches that were run), `control_set.csv` (works the search must find), `screening-criteria.md` (one-page sheet for screening), `extraction-form.md` |
| `T0.2-search-and-deduplication` | Raw exports per database, `search_log.csv`, the notebook `01_search_and_deduplication.ipynb` and its outputs: `corpus.csv` (2632 records to screen, including those from the T0.4 tracking) and `counts.csv` |
| `T0.3-screening` | The notebook `01_screening.ipynb`, `screening_ai.csv` (first pass made by AI) and `screening.csv` (human decisions) |
| `T0.4-citation-and-author-tracking` | The notebook `01_tracking.ipynb`, `backward_candidates.csv` (highly cited references missing from the corpus), the `query_*.txt` queries for Scopus and, in the folders of the same name, their exports |
| `T0.5-data-extraction` | The notebook `01_extraction.ipynb`, `matrix.csv` (filled in by hand from the full text) and `precoding_ai.csv` (first approximation made by AI from the abstracts). The notebook `02_full_texts.ipynb` maintains `full_texts.csv` (priority, DOI and availability of each PDF), `priority_pending.txt` and the `pdf/` folder, which is not committed |
| `T0.6-in-depth-reading` | One sheet per work (Chakrabarti, Huang, Zilch, Tang) |
| `T0.7-g0-report-and-p1-skeleton` | G0 decision report and skeleton of P1 |

The `collaborators` folder holds what is sent to prospective co-authors, each with its PDF: `protocol`, `classification-scheme` and `corpus-summary`. They are derived from T0.1 and from the counts of the notebooks; they do not include the G0 rule.

## Data

The raw exports and the abstracts in `corpus.csv` come from Scopus, Web of Science and IEEE Xplore and remain subject to the terms of those databases.

## Decisions

- **Database access:** full Scopus and WoS; IEEE Xplore with full text for some journals only (CRUE agreement).

## Notes


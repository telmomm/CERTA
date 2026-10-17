---
title: "Screening instructions"
subtitle: "What a reviewer has to do with the screening sheet of the CERTA review"
author: "Telmo Miguel-Medina"
date: today
doctype: "Guide"
reference: "WP0 · T0.3"
---

# Summary {-}

You are asked to decide, for each record of a spreadsheet, whether a paper should go on to the next stage of a systematic review: include, exclude or doubt. You decide from the title and the abstract only, without opening the paper and without consulting anyone. It takes one or two minutes per record and can be done in several sittings.

# What you receive

| File | Use |
| ------------------------ | ------------------------------------------------------------ |
| `screening-sheet.xlsx` | The records to screen, one per row, with three empty columns for your answers |
| `screening-criteria.pdf` | One page with everything needed to decide. Read it before starting and keep it at hand |

The review looks for two kinds of work on analog circuits: works that **decide what to measure or which signal to apply** to detect or locate faults, and works that **compute the coverage of the diagnostics** of an analog part against a safety standard (IEC 61508, ISO 26262, IEC 60601, IEEE 2427). The criteria sheet explains both, with the cases that tend to cause trouble.

# How to fill in the sheet

The first columns (`id`, `title`, `year`, `source`, `abstract`) are only to be read. Fill in the last three:

| Column | What to write |
| ---------- | ------------------------------------------------------------ |
| `decision` | `include`, `exclude` or `doubt`, from the drop-down list |
| `reason` | Only if `exclude`: the first reason that applies, `E1` to `E5` |
| `notes` | Optional. A few words when the decision was not obvious, `review` for a review paper, or `own` (see below) |

When the abstract is not enough to decide, choose `doubt`: those records are settled later with the full text. A `doubt` costs little; a wrong `exclude` loses the paper for good.

# Rules

- **Independently.** Do not consult the other reviewers, the project or any tool that classifies the papers for you.
- **Title and abstract only.** Do not look for the paper or its full text.
- **Your own group.** If a record is by you or your group, leave `decision` empty and write `own` in `notes`.
- **Keep the sheet intact.** Do not delete rows or change the `id` column. Sorting or filtering is fine.

# Returning the sheet

Save the file with your initials at the end of its name (`screening-sheet-XY.xlsx`) and return it by the date given in the message. Partial sheets are welcome if the deadline arrives before you finish.

Your decisions are compared with those of the main reviewer, the agreement between both is measured, and the records where you disagree are discussed with you before a final decision is taken.

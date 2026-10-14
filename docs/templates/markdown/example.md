---
title: "Writing CERTA documents"
subtitle: "How the document template works, shown with the template itself"
author: "Telmo Miguel-Medina"
date: today
doctype: "Guide"
reference: "docs/templates"
---

# Summary {-}

Every document of the project starts from [`document.md`](document.md): a front matter with title, subtitle, author, date, type and reference, followed by a fixed sequence of sections. The same file reads well on GitHub and exports to a PDF with the CERTA title block, the logo in the header and the page count in the footer. This guide is itself written with the template, so it doubles as an example of every element.

# Front matter

The fields at the top of the file fill the title block of the first page and the running header of the following ones.

| Field | Use | Example |
| --- | --- | --- |
| `title` | Title of the document | Writing CERTA documents |
| `subtitle` | One sentence that says what it is about | How the document template works |
| `author` | One name or a list of names | Telmo Miguel-Medina |
| `date` | A date, or `today` to use the export date | `today` |
| `doctype` | Kind of document, shown above the title | Report, Protocol, Guide, Minutes |
| `reference` | Work package and task it belongs to, shown in the header | WP0 · T0.8 |

`doctype` and `reference` are optional. A long title can be shortened in the header with `running-title`.

# Structure

The sections of the template follow the order in which a reader needs them:

1. **Summary**, unnumbered: the answer in three to five lines.
2. **Purpose and scope**: the question and what is left out.
3. **Method**: how the work was done, pointing to files instead of copying them.
4. **Results**: tables and figures, each introduced by a sentence.
5. **Conclusions and next steps**: what follows and which task does it.
6. **References**, unnumbered.

Sections that do not apply are removed rather than left empty. Headings are written without numbers; the export numbers them.

## Elements

Tables, lists, links, code and equations use plain Markdown. An equation is written in LaTeX between dollar signs, for example the risk-weighted coverage of the guide:

$$
DC_w(Q) = \frac{\sum_{k} p_k \, w_k \, P(\mathrm{alarm} \mid f_k, Q)}{\sum_{k} p_k \, w_k}
$$

Code and commands go in fenced blocks:

```bash
pandoc document.md -d docs/templates/pdf/certa-pdf.yaml -o document.pdf
```

Figures take a caption and a relative path:

![Certification icon of the project, from `docs/assets/icons`.](../../assets/icons/certification-box.png){width=18%}

# Export to PDF

From the repository root, with pandoc and a LaTeX distribution that includes XeLaTeX:

```bash
pandoc path/to/document.md -d docs/templates/pdf/certa-pdf.yaml -o path/to/document.pdf
```

The defaults file `pdf/certa-pdf.yaml` sets the paper, margins, font and colours, and applies the filter `certa.lua`, which builds the title block from the front matter and loads `certa-header.tex`, the LaTeX preamble that draws the header with the logo and the footer with the page count. The font is Avenir Next; on a system without it, change `mainfont` in the defaults file.

# Conclusions and next steps

The template gives every document the same look without extra work. The PDF of a document is regenerated whenever its Markdown changes and is committed next to it.

# References {-}

- Pandoc User's Guide, section "Defaults files". <https://pandoc.org/MANUAL.html#defaults-files>

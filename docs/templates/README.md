# Templates

Templates for every kind of document in the project, all with the CERTA identity. Each folder holds a template and an example made with it.

| Folder | Template | Example | Use it for |
| --- | --- | --- | --- |
| [`markdown/`](markdown/) | `document.md` | `example.md`, `example.pdf` | Reports, protocols and any document kept in the repository |
| [`notebook/`](notebook/) | `notebook.ipynb` | `example.ipynb`, `example.pdf` | Data analyses |
| [`word/`](word/) | `certa-template.docx` | `example.docx` | Documents that have to be edited in Word |
| [`powerpoint/`](powerpoint/) | `certa-template.pptx` | The template itself carries one example slide per layout | Presentations |
| [`pdf/`](pdf/) | — | — | The PDF export shared by Markdown documents and notebooks |

## Markdown

`document.md` has a front matter (title, subtitle, author, date, type and reference) and the standard sections: Summary, Purpose and scope, Method, Results, Conclusions and next steps, References. `example.md` explains the template using the template itself.

1. Copy `markdown/document.md` into the folder of the task and rename it.
2. Fill in the front matter and replace the sections; remove the ones that do not apply.
3. From the repository root, export it to PDF:

   ```bash
   pandoc path/to/document.md -d docs/templates/pdf/certa-pdf.yaml -o path/to/document.pdf
   ```

## Notebooks

`notebook.ipynb` has a raw first cell with the same front matter, a header cell with the logo, what the notebook reads and writes, a setup cell with the CERTA colours and the `table()` helper, numbered sections and the closing "Conclusions and notes" cell. `example.ipynb` applies it to the identification counts of T0.2.

1. Copy `notebook/notebook.ipynb` into the folder of the task, numbered (`01_….ipynb`).
2. Fill in the first cell (front matter) and the header cell with the same title and subtitle.
3. Show tables with `table(df)` or `table(df, bar="column")`: coloured in the notebook, as a LaTeX table in the PDF.
4. To export it, from the repository root with the `.venv` activated:

   ```bash
   docs/templates/notebook/notebook-to-pdf.sh path/to/notebook.ipynb
   ```

   The header cell (tag `pdf-skip`) and the code of the setup cell (tag `pdf-hide-code`) are left out of the PDF. The logo of the header cell is loaded from GitHub, so it needs a connection to show in the notebook.

## Word

| File | Contents |
| --- | --- |
| `certa-template.docx` | Styles (title, subtitle, headings, body, captions), header with the logo mark and the document title, footer with "Page X of Y", and the standard sections as a starting text |
| `certa-reference.docx` | The same styles, header and footer with an empty body, for pandoc |
| `example.docx` | `markdown/example.md` exported to Word with `certa-reference.docx` |

- **Writing directly in Word:** open `certa-template.docx`, save it with a new name and replace the text. The header picks up the title of the document by itself.
- **From Markdown:** from the repository root,

  ```bash
  pandoc path/to/document.md --reference-doc=docs/templates/word/certa-reference.docx -o path/to/document.docx
  ```

## PowerPoint

`certa-template.pptx` is 16:9 and has six layouts: Title, Section, Content, Two columns, Title only and Closing. Open it, save it with a new name, delete the example slides you do not need and add new ones from the layouts (Home › New slide). The footer, logo and slide number come from the layouts. The slide notes explain each layout.

## PDF export

| File | Contents |
| --- | --- |
| `certa-pdf.yaml` | Pandoc defaults: paper, margins, font, colours and the filter |
| `certa.lua` | Pandoc filter: builds the title block from the front matter, loads the preamble and resolves image paths relative to the document |
| `certa-header.tex` | LaTeX preamble: colours, headings, header with the logo and footer with the page count |

## Requirements

- **PDF export:** pandoc 3 and a LaTeX distribution with XeLaTeX. The font is Avenir Next; on a system without it, change `mainfont` in `pdf/certa-pdf.yaml`.
- **Office files:** Century Gothic for headings and Calibri for text, which ship with Office on Windows and macOS.

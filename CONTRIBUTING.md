# How to work in CERTA

## Structure

- One folder per work package (`WP0-state-of-the-art`…) and, inside it, one per task (`T0.1-protocol`…).
- The tasks and their estimated duration are in `ROADMAP.md`.
- Each package has a `README.md` with its objective, its scope and what each folder holds.
- `docs/` holds the visual identity and the document templates; `web/` holds the project website.

## Environment

Python 3.11 or later is required. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

On Windows, activation is `.venv\Scripts\activate`.

The `.venv` folder is not committed. If a notebook needs a new package, it is added to `requirements.txt` in the same commit.

## Notebooks

Every data analysis goes in a Jupyter notebook inside the folder of the task, numbered (`01_….ipynb`), so that it can be re-run and reviewed. New notebooks start from the template in `docs/templates/notebook/notebook.ipynb`.

- **In VS Code:** open the notebook and choose the `.venv` interpreter as the kernel.
- **From the terminal**, with the environment activated and from the folder of the notebook:

  ```bash
  jupyter nbconvert --to notebook --execute --inplace 01_screening.ipynb
  ```

Each notebook:

- uses paths relative to its own folder;
- states at the top what it reads, what it writes and how to re-run it;
- ends with a "Conclusions and notes" cell;
- gives the same result if it is run twice and does not overwrite manual work already saved (for example, the decisions in `screening.csv`).

They are committed executed, with their outputs.

## Data

- Raw database exports are not edited. If a search is repeated, the file is replaced and `search_log.csv` is updated.
- Derived files (`corpus.csv`, `counts.csv`) are written only by their notebook, never by hand.
- Record identifiers (`R0001`…) are stable: they are not renumbered.
- CSV files are UTF-8, with column names and coded values in English.

## Documents

- In English and brief.
- Written from the template in `docs/templates/markdown/document.md` and exported to PDF with `pandoc document.md -d docs/templates/pdf/certa-pdf.yaml -o document.pdf` when they are going to be sent.
- Only the version in force: no version numbers, edit dates, history or discarded variants. The trace is in git.
- Changes of method (criteria, search strings, the G0 rule) are made in `T0.1-protocol` before they are applied to the data, and the commit message explains the reason.

## Commits

- One commit per coherent change, with a message that says what changes and why.
- The data and the notebook that generates them go in the same commit.
- Before committing a notebook, run it in full so that the outputs match the code.

#!/usr/bin/env bash
# Exports a notebook to PDF with the CERTA template, next to the notebook.
# Usage, from the repository root and with the .venv activated:
#   docs/templates/notebook/notebook-to-pdf.sh path/to/notebook.ipynb
# Cells tagged "pdf-skip" (the header with the logo) are left out, and so is the code of
# cells tagged "pdf-hide-code" (the setup cell). The title block comes from the front
# matter in the first, raw cell.
set -euo pipefail
nb="$1"
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
jupyter nbconvert --to markdown --output-dir "$tmp" \
  --TagRemovePreprocessor.enabled=True \
  --TagRemovePreprocessor.remove_cell_tags='["pdf-skip"]' \
  --TagRemovePreprocessor.remove_input_tags='["pdf-hide-code"]' \
  --NbConvertBase.display_data_priority='["image/png","image/jpeg","text/latex","text/markdown","text/plain"]' \
  "$nb" >/dev/null 2>&1
# Notebook headings are "## 1. Load": promote them one level and keep their own numbers
pandoc "$tmp/$(basename "${nb%.ipynb}").md" -d "$here/../pdf/certa-pdf.yaml" \
  --shift-heading-level-by=-1 --number-sections=false -o "${nb%.ipynb}.pdf"
echo "${nb%.ipynb}.pdf"

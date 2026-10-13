#!/usr/bin/env python3
"""Copies to `web/assets/` the visual identity assets used by the website.

Quarto runs it before every render (`pre-render` in `_quarto.yml`). The source is
`docs/assets/`; the copy is not committed.
"""
import shutil
from pathlib import Path

WEB = Path(__file__).parent
SOURCE = WEB.parent / "docs" / "assets"

for folder in ("logo", "icons", "backgrounds", "banners"):
    shutil.copytree(SOURCE / folder, WEB / "assets" / folder, dirs_exist_ok=True)

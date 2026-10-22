#!/usr/bin/env python3
"""Generate Kodi-readable static download listing for FFK on GitHub Pages."""

from html import escape
from pathlib import Path
from urllib.parse import quote
import shutil

root = Path(__file__).resolve().parent
site = root / "_site"

if site.exists():
    shutil.rmtree(site)
site.mkdir()
(site / ".nojekyll").touch()

# Include all Kodi ZIP archives and TXT files (especially FF_Json.txt).
files = sorted(
    (
        entry
        for entry in root.iterdir()
        if entry.is_file()
        and entry.suffix.lower() in {".zip", ".txt"}
    ),
    key=lambda entry: entry.name.casefold(),
)

lines = [
    "<!DOCTYPE html>",
    '<html lang="pl">',
    '<head><meta charset="utf-8"><title>FFK - FanFilm Kodi Addons</title></head>',
    "<body>",
]
for entry in files:
    shutil.copy2(entry, site / entry.name)
    label = escape(entry.name)
    href = quote(entry.name, safe="")
    lines.append(f'<a href="{href}">{label}</a><br>')
lines.extend(["</body>", "</html>"])
(site / "index.html").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"FFK: generated {len(files)} links in _site/index.html")

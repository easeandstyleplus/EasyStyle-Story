#!/usr/bin/env python3
"""python rename_brand.py index.html [sortie.html]
Remplace "EasyStyle+" par "ES+ Make" partout (HTML, alt, title, dictionnaire JS)."""
import shutil, sys
from pathlib import Path

src = Path(sys.argv[1])
dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src

html = src.read_text(encoding="utf-8")
n = html.count("EasyStyle+")
html = html.replace("EasyStyle+", "ES+ Make")

if dst == src:
    shutil.copy(src, src.with_suffix(src.suffix + ".bak"))
dst.write_text(html, encoding="utf-8")
print(f"✔ {n} occurrence(s) de « EasyStyle+ » remplacée(s) par « ES+ Make »")
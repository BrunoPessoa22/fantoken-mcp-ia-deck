#!/usr/bin/env python3
"""Assemble the keynote deck: inline fonts + Chiliz logo into index.html."""
import pathlib

HERE = pathlib.Path(__file__).parent
ASSETS = HERE / "assets"

tpl = (HERE / "deck.tpl.html").read_text(encoding="utf-8")
fontface = (ASSETS / "fontface.css").read_text(encoding="utf-8")
chiliz = (ASSETS / "chiliz_datauri.txt").read_text().strip()
qr = (ASSETS / "qr_datauri.txt").read_text().strip()

out = (tpl.replace("/*__FONTFACE__*/", fontface)
          .replace("__CHILIZ__", chiliz)
          .replace("__QR__", qr))

for ph in ("__CHILIZ__", "__FONTFACE__", "__QR__"):
    assert ph not in out, f"placeholder left unfilled: {ph}"
(HERE / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written: {len(out):,} bytes")

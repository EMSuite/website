#!/usr/bin/env python3
"""Put a reviewed picture into the documentation: a WebP and a PNG fallback at a fixed width.

    python3 tools/docs_pictures.py SOURCE.png APP TUTORIAL NAME [--width 1600]

writes assets/docs/APP/TUTORIAL/NAME.webp and NAME.png (APP is 4dstem-studio or electron-microscopy-studio, NAME as
01-open) and prints the <figure> to paste into the page, with the picture's width and height filled in.

Only pictures someone has looked at go in: result figures from the agent door (get_result_image, get_pattern_image,
the figures File > Export writes) and window pictures from the release walk, in the dark appearance, from public data.
Development only (needs Pillow: pip install pillow); CI never runs it.
"""
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS = {"4dstem-studio", "electron-microscopy-studio"}
NAME = re.compile(r"^\d{2}-[a-z0-9-]+$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("app", choices=sorted(APPS))
    ap.add_argument("tutorial", help="the tutorial's file name without .md")
    ap.add_argument("name", help="two digits, a dash, a few words: 01-open")
    ap.add_argument("--width", type=int, default=1600, help="pixels; the page shows it at most 800 wide (2x)")
    a = ap.parse_args()
    if not NAME.match(a.name):
        sys.exit(f"error: the name is two digits, a dash and lower-case words, as 01-open, not {a.name!r}")
    from PIL import Image   # development only
    img = Image.open(a.source).convert("RGB")
    if img.width > a.width:
        img = img.resize((a.width, round(img.height * a.width / img.width)), Image.LANCZOS)
    out = ROOT / "assets" / "docs" / a.app / a.tutorial
    out.mkdir(parents=True, exist_ok=True)
    img.save(out / f"{a.name}.webp", "WEBP", lossless=True, method=6)
    img.save(out / f"{a.name}.png", "PNG", optimize=True)
    web = f"/assets/docs/{a.app}/{a.tutorial}/{a.name}"
    print(f"""<figure>
  <picture>
    <source srcset="{web}.webp" type="image/webp">
    <img src="{web}.png" alt="" width="{img.width}" height="{img.height}" loading="lazy">
  </picture>
  <figcaption></figcaption>
</figure>""")


if __name__ == "__main__":
    main()

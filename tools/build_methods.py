#!/usr/bin/env python3
"""Generate the Methods page of Electron Microscopy Studio from the app's parity table.

    python3 tools/build_methods.py --fetch [--tag v2.1.1]   # docs/parity.md of the app at its latest release tag
    python3 tools/build_methods.py --file PATH --tag v2.1.1  # a local copy of that file

The app's docs/parity.md lists every function the app computes itself: its Python reference with the pinned version
(and the paper where one defines the method) and the tolerance its parity test holds it to. This page keeps those three
columns of each section's table, under the section's heading; the test names and the development notes stay in the
file, which the page links. The output is docs-src/electron-microscopy-studio/methods.md; then run build_docs.py. Run
it after each app release (the page's applies_to follows the tag). Standard library only.
"""
import argparse, html, json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORG, REPO = "EMSuite", "Electron-Microscopy-Studio"
OUT = ROOT / "docs-src" / "electron-microscopy-studio" / "methods.md"
KEEP = ("Function", "Reference", "Tolerance")
OLD_NAME = re.compile(r"(?<![\w./-])mac(?:em|tem)(?![\w.-])", re.I)   # the app's own words in a cell keep its old name


def latest_tag():
    url = f"https://api.github.com/repos/{ORG}/{REPO}/releases/latest"
    return json.load(urllib.request.urlopen(url, timeout=30))["tag_name"]


def cells(line):
    """The cells of a Markdown table row; an escaped pipe stays in its cell."""
    parts = re.split(r"(?<!\\)\|", line.strip().strip("|") if not line.strip().endswith("\\|") else line.strip()[1:])
    return [c.strip() for c in parts]


def clean(cell):
    """A cell as the public page shows it: links into the app's repo become their text, the old app name the new."""
    cell = re.sub(r"\[([^\]]+)\]\((?!https?:)[^)]*\)", r"\1", cell)
    cell = re.sub(r"\s*\((?:#\d+|D-SEM-\d+)(?:,\s*(?:#\d+|D-SEM-\d+))*\)", "", cell)   # the repo's issue and decision ids
    cell = re.sub(r"[;,]\s*(?:#\d+|D-SEM-\d+)\b", "", cell)
    return OLD_NAME.sub("Electron Microscopy Studio", cell)


def sections(text):
    """[(heading, [rows of the kept columns])] for each ## section with a table that has the kept columns."""
    out, heading, lines, i = [], None, text.splitlines(), 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^## (.+)", line)
        if m:
            heading = re.sub(r"\s*\(figures? [^)]*\)", "", m.group(1)).strip()   # the app's internal figure ids
        elif line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i + 1]) and heading:
            head = cells(line)
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            if all(k in head for k in KEEP):
                idx = [head.index(k) for k in KEEP]
                kept = [[clean(r[j]) if j < len(r) else "" for j in idx] for r in rows]
                if out and out[-1][0] == heading:
                    out[-1][1].extend(kept)
                else:
                    out.append((heading, kept))
            continue
        i += 1
    return out


def inline(cell):
    """A cell as HTML: escaped, code spans kept as code."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(cell, quote=False))


def table(rows):
    """A section's rows as an HTML table in which long names wrap, so the tolerance stays on screen (build_docs puts
    every table in its scrolling panel)."""
    out = ['<table class="methods">',
           "<thead><tr><th>Function</th><th>Reference</th><th>Tolerance</th></tr></thead>", "<tbody>"]
    out += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows]
    return out + ["</tbody>", "</table>"]


def page(text, tag):
    ver = tag.lstrip("v")
    minor = ".".join(ver.split(".")[:2])
    parts = sections(text)
    n = sum(len(rows) for _, rows in parts)
    src = f"https://github.com/{ORG}/{REPO}/blob/{tag}/docs/parity.md"
    out = ["---", "title: Methods and their references", "nav: Methods",
           "description: Every number Electron Microscopy Studio computes itself, the Python package it is checked against, "
           "and the tolerance.", f"applies_to: {minor}", "---", "",
           f'<p class="lede">Each function the app computes itself, the reference it is checked against and how closely. '
           f"{n} functions in {len(parts)} groups, from the app's parity table at {ver}.</p>", "",
           "The rule is the same for every row: the app matches the pinned version of the Python package within the tolerance "
           "that package's own tests use, never stricter. Readers, indices and metadata match exactly. Where a method has a "
           "paper, the reference names it. The numbers of the kits the app is built on are listed on the "
           "[kits page](/suite/), each with its own parity table.", "",
           f"Generated from [docs/parity.md at {tag}]({src}), which also gives each row's test and notes. "
           "The page's tables leave those out.", ""]
    for heading, rows in parts:
        out += [f"## {heading}", ""] + table(rows) + [""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true", help="read docs/parity.md from GitHub at the tag")
    ap.add_argument("--file", type=Path, help="a local copy of the app's docs/parity.md at the tag")
    ap.add_argument("--tag", help="the release tag, as v2.1.1 (default with --fetch: the latest release)")
    a = ap.parse_args()
    if a.fetch:
        tag = a.tag or latest_tag()
        url = f"https://raw.githubusercontent.com/{ORG}/{REPO}/{tag}/docs/parity.md"
        text = urllib.request.urlopen(url, timeout=30).read().decode()
    elif a.file and a.tag:
        tag, text = a.tag, a.file.read_text()
    else:
        sys.exit("error: give --fetch, or --file and --tag")
    OUT.write_text(page(text, tag))
    print(f"methods: {OUT.relative_to(ROOT)} written from {tag}")


if __name__ == "__main__":
    main()

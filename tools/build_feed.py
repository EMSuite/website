#!/usr/bin/env python3
"""Build releases.atom, the site's release feed, from the releases the site already lists.

    python3 tools/build_feed.py           # write releases.atom
    python3 tools/build_feed.py --check   # exit 1 if releases.atom is not what the sources give (CI)

Sources: each app's update feed (appcast/*.xml, its newest release with the user notes) and the table of
suite/releases.html (each kit's and EMSuiteUI's latest tag and date). The update feeds and the table hold only the
latest release, so the entries already in releases.atom are kept and a new release is added beside them: the feed
grows by one entry per release, newest first, up to KEEP entries. Every page links it in its <head>; check_site
fails when one does not. Standard library only.
"""
import argparse, html, re, sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FEED = "releases.atom"
SITE = "https://mac4dstem.com"
ORG = "EMSuite"
KEEP = 50
ATOM = "{http://www.w3.org/2005/Atom}"
SPARKLE = "{http://www.andymatuschak.org/xml-namespaces/sparkle}"
# Each app's update feed and its page on this site.
APPS = {"appcast/mac4dstem.xml": "/", "appcast/macem.xml": "/electron-microscopy-studio/"}
LINK = '<link rel="alternate" type="application/atom+xml" title="EMSuite releases" href="/releases.atom">'


def app_entries(root):
    """The newest release of each app's update feed, as feed entries."""
    out = []
    for path, page in APPS.items():
        f = root / path
        if not f.is_file():
            continue
        channel = ET.parse(f).getroot().find("channel")
        item = channel.find("item")
        if item is None:
            continue
        ver = item.findtext(f"{SPARKLE}shortVersionString") or item.findtext(f"{SPARKLE}version")
        link = item.findtext(f"{SPARKLE}fullReleaseNotesLink") or f"{SITE}{page}"
        out.append({"id": link, "title": item.findtext("title"), "link": link,
                    "updated": parsedate_to_datetime(item.findtext("pubDate")).astimezone(timezone.utc),
                    "summary": (item.findtext("description") or "").strip(), "app": channel.findtext("title"),
                    "version": ver})
    return out


def kit_entries(root):
    """Each kit's and EMSuiteUI's latest tag from suite/releases.html, as feed entries."""
    f = root / "suite" / "releases.html"
    if not f.is_file():
        return []
    out = []
    for name, ver, date in re.findall(r"<tr><td>(\w+)</td><td>([\d.]+)</td><td>(\d{4}-\d{2}-\d{2})</td>", f.read_text()):
        link = f"https://github.com/{ORG}/{name}/releases/tag/{ver}"
        out.append({"id": link, "title": f"{name} {ver}", "link": link,
                    "updated": datetime.fromisoformat(date).replace(tzinfo=timezone.utc),
                    "summary": f"{name} {ver}: the changes are in its CHANGELOG "
                               f"(https://github.com/{ORG}/{name}/blob/{ver}/CHANGELOG.md).",
                    "app": None, "version": ver})
    return out


def kept_entries(root):
    """The entries releases.atom holds now."""
    f = root / FEED
    if not f.is_file():
        return []
    out = []
    for e in ET.parse(f).getroot().findall(f"{ATOM}entry"):
        cat = e.find(f"{ATOM}category")
        out.append({"id": e.findtext(f"{ATOM}id"), "title": e.findtext(f"{ATOM}title"),
                    "link": e.find(f"{ATOM}link").get("href"),
                    "updated": datetime.fromisoformat(e.findtext(f"{ATOM}updated").replace("Z", "+00:00")),
                    "summary": e.findtext(f"{ATOM}summary") or "",
                    "app": cat.get("term") if cat is not None else None,
                    "version": e.findtext(f"{ATOM}title").rsplit(" ", 1)[-1]})
    return out


def entries(root):
    """Every entry, the sources' newest ones replacing kept ones of the same id, newest first."""
    by_id = {e["id"]: e for e in kept_entries(root)}
    for e in app_entries(root) + kit_entries(root):
        by_id[e["id"]] = e
    return sorted(by_id.values(), key=lambda e: (e["updated"], e["id"]), reverse=True)[:KEEP]


def stamp(t):
    return t.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def render(items):
    esc = html.escape
    out = ['<?xml version="1.0" encoding="utf-8"?>',
           '<feed xmlns="http://www.w3.org/2005/Atom">',
           "  <title>EMSuite releases</title>",
           "  <subtitle>New versions of 4DSTEM Studio, Electron Microscopy Studio and the Swift kits they are built on.</subtitle>",
           f"  <id>{SITE}/{FEED}</id>",
           f'  <link rel="self" type="application/atom+xml" href="{SITE}/{FEED}"/>',
           f'  <link rel="alternate" type="text/html" href="{SITE}/suite/releases.html"/>',
           f"  <updated>{stamp(items[0]['updated']) if items else '1970-01-01T00:00:00Z'}</updated>",
           "  <author><name>EMSuite</name></author>"]
    for e in items:
        out += ["  <entry>",
                f"    <title>{esc(e['title'])}</title>",
                f'    <link rel="alternate" type="text/html" href="{esc(e["link"], quote=True)}"/>',
                f"    <id>{esc(e['id'])}</id>",
                f"    <updated>{stamp(e['updated'])}</updated>"]
        if e["app"]:
            out.append(f'    <category term="{esc(e["app"], quote=True)}"/>')
        out += [f"    <summary type=\"text\">{esc(e['summary'], quote=False)}</summary>", "  </entry>"]
    return "\n".join(out + ["</feed>", ""])


def newest_app_versions(text):
    """The version of the newest entry of each app in a feed's text: {app name: version}."""
    out = {}
    for e in ET.fromstring(text).findall(f"{ATOM}entry"):
        cat = e.find(f"{ATOM}category")
        if cat is not None and cat.get("term") not in out:
            out[cat.get("term")] = e.findtext(f"{ATOM}title").rsplit(" ", 1)[-1]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if releases.atom differs from what the sources give")
    a = ap.parse_args()
    text = render(entries(ROOT))
    f = ROOT / FEED
    if a.check:
        if not f.is_file() or f.read_text() != text:
            print(f"error: {FEED} is not what the update feeds and suite/releases.html give: run python3 tools/build_feed.py")
            sys.exit(1)
        print(f"feed: {FEED} checked")
        return
    f.write_text(text)
    print(f"feed: {FEED} written, {text.count('<entry>')} entries")


if __name__ == "__main__":
    main()

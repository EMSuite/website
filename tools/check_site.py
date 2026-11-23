#!/usr/bin/env python3
"""Check the site before it publishes: every internal link resolves, and the pages name the current releases.

    python3 tools/check_site.py             # links, then versions and download sizes against GitHub releases
    python3 tools/check_site.py --offline   # links and old app names only

Links: every href, src and srcset that points into the site must name a file in this repo, and every #fragment an id
on its page. Releases: each app page must give the latest release's version and its .dmg size wherever it states
them (the text and the JSON-LD), and the kits pages the latest tag of each kit and of EMSuiteUI. From mac4DSTEM 5.3.0 on,
the website download updates itself (Sparkle), so appcast/mac4dstem.xml must name that latest release: its version, and
its versioned DMG (4DSTEM-Studio-<version>.dmg from 5.4.3, mac4DSTEM-<version>.dmg before) on the release with the same length. Documentation: a page under docs-src/ that says which
version it applies to (applies_to in its front matter) must name the latest release's major.minor; moving the stamp says
the page was read against that version. CI runs it on every push
and once a day, so a new release turns it red until the pages follow. Standard library only; GITHUB_TOKEN is used
when set.
"""
import argparse, html.parser, json, os, re, sys, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
ORG = "EMSuite"
APPS = {"mac4DSTEM": "index.html", "macEM": "electron-microscopy-studio/index.html"}
# Pages that moved: the old address serves a forwarding page, and nothing in the site links to it any more.
MOVED = {"mactem/index.html": "/electron-microscopy-studio/"}
SITE = "https://mac4dstem.com"
# Each app's GitHub repo (renamed 2026-11-17); release assets keep the app names.
REPOS = {"mac4DSTEM": "4DSTEM-Studio", "macEM": "Electron-Microscopy-Studio"}
PACKAGES = ["FormatoKit", "ImagoKit", "DiffractoKit", "SpectroKit", "CuboKit", "SimulatoKit", "EMSuiteUI"]
SKIP = {".git", "datacube", "tools"}
# Each app's DMG file name from the release that renamed its download (4DSTEM-Studio#496, Electron-Microscopy-Studio#759);
# earlier releases carry the app's old name. A renamed release also carries <old name>.dmg, so old links keep working.
FILES = {"mac4DSTEM": ("4DSTEM-Studio", (5, 4, 3)), "macEM": ("Electron-Microscopy-Studio", (2, 1, 1))}


def dmg_base(app, ver):
    """The DMG's base name for this app at this version: the new name from the renaming release on, else the old one."""
    new, first = FILES[app]
    return new if tuple(int(n) for n in ver.split(".")) >= first else app


# Apps whose website download reads an update feed, the feed's path in this repo, and the first version that reads it.
FEEDS = {"mac4DSTEM": ("appcast/mac4dstem.xml", (5, 3, 0)), "macEM": ("appcast/macem.xml", (2, 1, 0))}
# The app name a docs section carries in docs-src/nav.json, for each app.
DOCS_APPS = {"mac4DSTEM": "4DSTEM Studio", "macEM": "Electron Microscopy Studio"}
SPARKLE = "{http://www.andymatuschak.org/xml-namespaces/sparkle}"


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs = set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "name" in a:
            self.ids.add(a["name"])
        for key in ("href", "src"):
            if a.get(key):
                self.refs.append(a[key])
        if a.get("srcset"):
            self.refs += [part.split()[0] for part in a["srcset"].split(",") if part.strip()]


# Old app names (mac4DSTEM, macEM, macTEM) must not appear in what a reader sees. Text is joined across inline tags, so a
# wordmark split by markup (mac<em>4D</em>STEM) is caught; alt, title, aria-label and meta descriptions count too.
# File and domain names keep the old names: mac4dstem.com, mac4DSTEM.dmg, mac4DSTEM-5.4.1.dmg, .mac4dstem.h5, /mactem/.
OLD_NAME = re.compile(r"(?<![\w./-])mac(?:4dstem|em|tem)(?![\w.-])", re.I)
INLINE = {"a", "abbr", "b", "bdi", "bdo", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "s", "samp",
          "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr"}
META = {"description", "og:title", "og:description", "og:site_name", "twitter:title", "twitter:description",
        "application-name", "apple-mobile-web-app-title"}


class Text(html.parser.HTMLParser):
    """The text a reader sees (or a screen reader or a link preview reads), with inline markup joined."""
    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style") and a.get("type") != "application/ld+json":
            self.skip += 1
        if tag not in INLINE:
            self.parts.append(" ")
        for key in ("alt", "title", "aria-label"):
            if a.get(key):
                self.parts.append(f" {a[key]} ")
        if tag == "meta" and (a.get("name") or a.get("property")) in META and a.get("content"):
            self.parts.append(f" {a['content']} ")

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
        if tag not in INLINE:
            self.parts.append(" ")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def text(self):
        return re.sub(r"\s+", " ", "".join(self.parts))


def old_names(source):
    """Each old app name in a page's visible text, with a little context."""
    t = Text()
    t.feed(source)
    s = t.text()
    return [s[max(0, m.start() - 30):m.end() + 30].strip() for m in OLD_NAME.finditer(s)]


def check_names():
    errors = []
    for page in pages():
        for hit in old_names(page.read_text()):
            errors.append(f"{page.relative_to(ROOT)}: old app name in the page text: …{hit}…")
    return errors


def pages():
    return sorted(p for p in ROOT.rglob("*.html") if not SKIP & set(p.relative_to(ROOT).parts))


def parse(path):
    p = Page()
    p.feed(path.read_text())
    return p


def target(page, ref, root=None):
    """The file a site-internal reference names, or None for an external one."""
    root = root or ROOT
    u = urlsplit(ref)
    if u.scheme or u.netloc or ref.startswith(("mailto:", "tel:", "data:")):
        return None
    if not u.path:
        return page, u.fragment
    base = root if u.path.startswith("/") else page.parent
    f = (base / unquote(u.path).lstrip("/")).resolve()
    if u.path.endswith("/") or f.is_dir():
        f = f / "index.html"
    return f, u.fragment


FEED_LINK = '<link rel="alternate" type="application/atom+xml" title="EMSuite releases" href="/releases.atom">'


def check_feed_links(root=None):
    """Every page links the release feed in its head, and the feed's newest entry of each app is the release its
    update feed offers."""
    root = root or ROOT
    errors = [f"{p.relative_to(root)}: no link to the release feed in its head ({FEED_LINK})"
              for p in sorted(p for p in root.rglob("*.html") if not SKIP & set(p.relative_to(root).parts))
              if FEED_LINK not in p.read_text().split("</head>")[0]]
    atom = root / "releases.atom"
    if not atom.is_file():
        return errors + ["releases.atom: missing: run python3 tools/build_feed.py"]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_feed
    newest = build_feed.newest_app_versions(atom.read_text())
    for path in build_feed.APPS:
        f = root / path
        if not f.is_file():
            continue
        channel = ET.parse(f).getroot().find("channel")
        ver = channel.findtext(f"item/{SPARKLE}shortVersionString")
        app = channel.findtext("title")
        if newest.get(app) != ver:
            errors.append(f"releases.atom: the newest {app} entry is {newest.get(app)}, {path} offers {ver}: "
                          "run python3 tools/build_feed.py")
    return errors


def check_moved(root=None):
    """Each moved page forwards to its new address, and no page, the sitemap or the update feeds link the old one."""
    root = root or ROOT
    errors = []
    for old, new in MOVED.items():
        f = root / old
        if not f.is_file():
            errors.append(f"{old}: missing; the old address must keep serving a page that forwards to {new}")
            continue
        src = f.read_text()
        if not re.search(rf'<meta http-equiv="refresh" content="0; url={re.escape(new)}">', src):
            errors.append(f"{old}: has no <meta http-equiv=\"refresh\" content=\"0; url={new}\">")
        if f'<link rel="canonical" href="{SITE}{new}">' not in src:
            errors.append(f"{old}: its canonical link must name {SITE}{new}")
        if '<meta name="robots" content="noindex">' not in src:
            errors.append(f"{old}: a forwarding page carries noindex")
        old_url = "/" + old.removesuffix("index.html")
        for page in sorted(p for p in root.rglob("*.html") if not SKIP & set(p.relative_to(root).parts)):
            if page == f:
                continue
            for ref in parse(page).refs:
                t = target(page, ref, root)
                if t and t[0] == f.resolve():
                    errors.append(f"{page.relative_to(root)}: links the old address {ref}; link {new}")
        for listing in ("sitemap.xml", "appcast/mac4dstem.xml", "appcast/macem.xml"):
            p = root / listing
            if p.is_file() and f"{SITE}{old_url}" in p.read_text():
                errors.append(f"{listing}: names the old address {SITE}{old_url}; name {SITE}{new}")
    return errors


def check_links():
    errors, parsed = [], {}
    for page in pages():
        parsed[page] = parse(page)
    for page, p in parsed.items():
        for ref in p.refs:
            t = target(page, ref)
            if t is None:
                continue
            f, frag = t
            name = page.relative_to(ROOT)
            if not f.is_file():
                errors.append(f"{name}: {ref} names no file")
            elif frag and f.suffix == ".html":
                ids = parsed[f].ids if f in parsed else parse(f).ids
                if frag not in ids:
                    errors.append(f"{name}: {ref} names no id on its page")
    return errors, len(parsed)


def latest(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{ORG}/{repo}/releases/latest",
                                 headers={"Accept": "application/vnd.github+json"})
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    return json.load(urllib.request.urlopen(req, timeout=30))


def check_releases():
    errors = []
    for app, rel in APPS.items():
        r = latest(REPOS[app])
        ver = r["tag_name"].lstrip("v")
        base = dmg_base(app, ver)
        dmg = next((a for a in r["assets"] if a["name"] == f"{base}.dmg"), None)
        if dmg is None:
            errors.append(f"{rel}: the latest {app} release {r['tag_name']} has no {base}.dmg, so the page's "
                          f"releases/latest/download/{base}.dmg link is a 404: build it with tools/release.sh "
                          "on that tag and attach it")
            continue
        size = f"{dmg['size'] / 1e6:.1f} MB"
        text = (ROOT / rel).read_text()
        for stated in sorted(set(re.findall(r"Version (\d+\.\d+\.\d+)", text))):
            if stated != ver:
                errors.append(f"{rel}: says Version {stated}, the latest {app} release is {ver}")
        meta = re.search(r'<p class="get-meta">(.*?)</p>', text, re.S)
        if not meta or f"Version {ver}" not in meta.group(1) or size not in meta.group(1):
            errors.append(f"{rel}: the download line must read Version {ver} and {size}")
        ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', text, re.S).group(1))
        if ld.get("softwareVersion") != ver:
            errors.append(f"{rel}: JSON-LD softwareVersion {ld.get('softwareVersion')}, latest is {ver}")
        if ld.get("fileSize") != size:
            errors.append(f"{rel}: JSON-LD fileSize {ld.get('fileSize')}, the {base}.dmg of {ver} is {size}")
        if not ld.get("downloadUrl", "").endswith(f"/{base}.dmg"):
            errors.append(f"{rel}: JSON-LD downloadUrl must point at {base}.dmg")
        errors += check_feed(app, ver, r["assets"])
        errors += check_stamps(DOCS_APPS[app], ver)
    releases = (ROOT / "suite/releases.html").read_text()
    for pkg in PACKAGES:
        ver = latest(pkg)["tag_name"]
        m = re.search(rf"<tr><td>{pkg}</td><td>([^<]*)</td>", releases)
        if not m or m.group(1) != ver:
            errors.append(f"suite/releases.html: {pkg} {m.group(1) if m else 'missing'}, latest tag is {ver}: "
                          "run tools/build_suite_pages.py --fetch")
    return errors


def check_feed(app, ver, assets):
    """The update feed names the latest release: its version, and its versioned DMG with the release's length."""
    if app not in FEEDS:
        return []
    path, first = FEEDS[app]
    if tuple(int(n) for n in ver.split(".")) < first:
        return []
    feed = ROOT / path
    if not feed.is_file():
        return [f"{path}: missing; the {app} {ver} download reads it to update itself. Commit the feed "
                f"tools/release.sh wrote for v{ver}"]
    try:
        item = ET.parse(feed).getroot().find("channel/item")
    except ET.ParseError as e:
        return [f"{path}: not readable XML ({e})"]
    if item is None:
        return [f"{path}: has no item"]
    errors = []
    for key in ("version", "shortVersionString"):
        stated = item.findtext(f"{SPARKLE}{key}")
        if stated != ver:
            errors.append(f"{path}: sparkle:{key} {stated}, the latest {app} release is {ver}")
    enclosure = item.find("enclosure")
    name = f"{dmg_base(app, ver)}-{ver}.dmg"
    url = enclosure.get("url", "") if enclosure is not None else ""
    if url != f"https://github.com/{ORG}/{REPOS[app]}/releases/download/v{ver}/{name}":
        errors.append(f"{path}: the enclosure must point at {name} on the v{ver} release, not {url or 'nothing'}")
    elif not (enclosure.get(f"{SPARKLE}edSignature") or "").strip():
        errors.append(f"{path}: the enclosure has no sparkle:edSignature")
    else:
        asset = next((a for a in assets if a["name"] == name), None)
        if asset is None:
            errors.append(f"{path}: the v{ver} release has no {name} for the feed to point at")
        elif str(asset["size"]) != enclosure.get("length"):
            errors.append(f"{path}: length {enclosure.get('length')}, the release's {name} is {asset['size']} bytes")
    return errors


def check_stamps(app, ver, src=None):
    """Every docs page of `app` that carries applies_to names the major.minor of `ver`, the app's latest release."""
    src = src or ROOT / "docs-src"
    if not (src / "nav.json").exists():
        return []
    current = ".".join(ver.split(".")[:2])
    errors = []
    for section in json.loads((src / "nav.json").read_text())["sections"]:
        if section.get("app") != app:
            continue
        for path in (p for group in section["groups"] for p in group["pages"]):
            front = (src / f"{path}.md").read_text().split("---", 2)[1]
            m = re.search(r"^applies_to:\s*(\S+)\s*$", front, re.M)
            if m and m.group(1) != current:
                errors.append(f"docs-src/{path}.md: applies_to {m.group(1)}, the latest {app} release is {ver}: read the "
                              f"page against {current}, correct it, and set applies_to: {current}")
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="check links and old app names only")
    a = ap.parse_args()
    errors, n = check_links()
    print(f"links: {n} pages checked")
    errors += check_feed_links()
    print("feed: every page links it, and it names each app's latest release")
    errors += check_moved()
    print(f"moved: {len(MOVED)} old addresses checked")
    errors += check_names()
    print(f"names: {n} pages checked for old app names")
    if not a.offline:
        errors += check_releases()
        print(f"releases: {len(APPS)} apps and {len(PACKAGES)} packages checked")
    for e in errors:
        print("error:", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

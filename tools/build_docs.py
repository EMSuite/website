#!/usr/bin/env python3
"""Build the documentation pages in docs/ from the Markdown sources in docs-src/.

    python3 tools/build_docs.py           # write docs/
    python3 tools/build_docs.py --check   # exit 1 if docs/ is not what the sources give (CI)

docs-src/nav.json is the table of contents: the sections (one per app, plus the shared ones), their groups and the
order of the pages. Each page is docs-src/<path>.md: a front-matter block, then Markdown. It is written to
docs/<path>.html in the site's header and footer with the section's sidebar, and its Markdown is copied to
docs/<path>.md so that an agent can read the same page a person does.

Front matter (plain `key: value` lines between two `---` lines):
    title        the page's heading and its name in the sidebar            required
    description  one sentence for search engines and for llms.txt          required
    nav          a shorter name for the sidebar                            optional
    applies_to   the app version the page was read against, as "5.4"       optional; shown as "Applies to ... and later"
    recipe       tutorials: the name of the reference recipe it follows    optional; needs dataset
    dataset      tutorials: the dataset's key in docs-src/datasets.json    optional

A dataset must be in docs-src/datasets.json with its licence and DOI, and a recipe must be one listed there for the
page's dataset (a copy of the public recipes' names, since the suite repository that holds them is private).

Each section of nav.json goes live on its own with "live": true. A live section's pages are indexed and listed in
sitemap.xml and llms.txt; the pages of a section without it ask search engines not to index them and stay out of both. Needs Python-Markdown (tools/requirements.txt).
"""
import argparse, html, json, re, sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs-src"
OUT = ROOT / "docs"
SITE = "https://mac4dstem.com"
KEYS = {"title", "description", "nav", "applies_to", "recipe", "dataset"}
EXTENSIONS = ["extra", "admonition", "sane_lists", "toc"]
TITLE_MAX = 70   # tools/check_site.py holds every page to it
# The link-preview picture of each app's pages; shared pages use the site's.
OG_IMAGES = {"4DSTEM Studio": "/assets/og.jpg", "Electron Microscopy Studio": "/assets/mactem-og.jpg"}
MARK = ("<!-- docs:start (tools/build_docs.py) -->", "<!-- docs:end -->")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{head_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{site}{url}">
<link rel="alternate" type="text/markdown" href="{markdown_url}">
<meta name="color-scheme" content="light dark">
<meta name="robots" content="{robots}">

<meta property="og:type" content="article">
<meta property="og:site_name" content="{site_name}">
<meta property="og:url" content="{site}{url}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{site}{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="icon" href="/assets/icon-512.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">

<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/docs.css">
</head>

<body>
<a class="skip" href="#main">Skip to content</a>

<header class="masthead">
  <div class="wrap">
    <a class="masthead-mark" href="/"><img src="/assets/icon-512.png" alt="" width="512" height="512"><span><em>4D</em>STEM Studio</span></a>
    <nav aria-label="Sections">
      <a href="/electron-microscopy-studio/">Electron Microscopy Studio</a>
      <a href="/docs/" aria-current="page">Docs</a>
      <a href="/suite/">Kits</a>
    </nav>
  </div>
</header>

<div class="wrap docs">
  <nav class="docs-nav" aria-label="Documentation">
{sidebar}
  </nav>

  <main id="main">
    <article class="doc">
{kicker}      <h1>{title}</h1>
{stamp}"""

FOOT = """{pager}    </article>
  </main>
</div>

<footer class="site-footer">
  <div class="wrap">
    <span>Siegen, Germany</span>
    <nav aria-label="Legal and support">
      <a href="/support.html">Support</a>
      <a href="/privacy.html">Privacy</a>
      <a href="/impressum.html">Impressum</a>
    </nav>
  </div>
</footer>
</body>
</html>
"""


class DocsError(Exception):
    pass


def split_front_matter(text, where="page"):
    """The front-matter fields and the Markdown body of a page source."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise DocsError(f"{where}: the first line must be --- (front matter)")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise DocsError(f"{where}: the front matter is not closed by ---") from None
    meta = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if not sep or key not in KEYS:
            raise DocsError(f"{where}: unknown front-matter line {line!r} (keys: {', '.join(sorted(KEYS))})")
        if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[key] = value
    for key in ("title", "description"):
        if not meta.get(key):
            raise DocsError(f"{where}: front matter needs {key}")
    if "applies_to" in meta and not re.fullmatch(r"\d+\.\d+", meta["applies_to"]):
        raise DocsError(f"{where}: applies_to is major.minor, as 5.4, not {meta['applies_to']!r}")
    return meta, "\n".join(lines[end + 1:]).strip() + "\n"


DOI = re.compile(r"^10\.\d{4,9}/\S+$")


def load_datasets(src=SRC):
    """docs-src/datasets.json: the public datasets by key. Each needs a title, a DOI and a licence."""
    f = src / "datasets.json"
    if not f.is_file():
        return {}
    datasets = json.loads(f.read_text())["datasets"]
    for key, d in datasets.items():
        for field in ("title", "doi", "licence"):
            if not str(d.get(field, "")).strip():
                raise DocsError(f"datasets.json: {key} has no {field}")
        if not DOI.match(d["doi"]):
            raise DocsError(f"datasets.json: {key}: {d['doi']!r} is not a DOI (10.xxxx/...)")
    return datasets


def check_sources(where, meta, datasets):
    """A page's dataset is a listed public dataset, and its recipe one of that dataset's."""
    if "recipe" in meta and "dataset" not in meta:
        raise DocsError(f"{where}: recipe {meta['recipe']!r} needs the dataset it runs on (dataset: <key>)")
    if "dataset" not in meta:
        return
    d = datasets.get(meta["dataset"])
    if d is None:
        raise DocsError(f"{where}: dataset {meta['dataset']!r} is not in docs-src/datasets.json, which lists each "
                        "public dataset with its licence and DOI")
    if "recipe" in meta and meta["recipe"] not in d.get("recipes", []):
        raise DocsError(f"{where}: recipe {meta['recipe']!r} is not a recipe of {meta['dataset']} in "
                        "docs-src/datasets.json; add the recipe to the suite's plan file first, then here")


TASKS = "tasks/"
TASK_LIMITS = {"words": 200, "title": 60, "description": 160}
STOP = {"a", "an", "and", "the", "on", "of", "from", "in", "to"}


def words(markdown_text):
    """The words a reader reads in a page body: link targets, tags, entities and Markdown marks left out."""
    text = re.sub(r"\]\([^)]*\)", "]", markdown_text)
    text = re.sub(r"<[^>]+>|&\w+;|[`*_#|>\[\]]", " ", text)
    return [w for w in text.split() if re.search(r"\w", w)]


def check_task(path, meta, body):
    """A task page is short and named by its task: body, title and description within their limits, and every word
    of its address in its title, so the address, the title and the search all say the same task."""
    where = f"docs-src/{path}.md"
    errors = []
    n = len(words(body))
    if n > TASK_LIMITS["words"]:
        errors.append(f"{where}: {n} words, a task page has at most {TASK_LIMITS['words']}")
    if len(meta["title"]) > TASK_LIMITS["title"]:
        errors.append(f"{where}: the title has {len(meta['title'])} characters, at most {TASK_LIMITS['title']}")
    if len(meta["description"]) > TASK_LIMITS["description"]:
        errors.append(f"{where}: the description has {len(meta['description'])} characters, at most {TASK_LIMITS['description']}")
    title = set(re.findall(r"[a-z0-9]+", meta["title"].lower()))
    missing = [w for w in path[len(TASKS):].split("-") if w not in STOP and w not in title]
    if missing:
        errors.append(f"{where}: the title lacks the address's words {', '.join(missing)}")
    return errors


def url_of(path):
    """The address of a page: its folder for an index page, else its .html file."""
    if path == "index":
        return "/docs/"
    if path.endswith("/index"):
        return f"/docs/{path[:-len('index')]}"
    return f"/docs/{path}.html"


def load(src=SRC):
    """nav.json with every page's front matter and body read in: (nav, pages by path)."""
    nav = json.loads((src / "nav.json").read_text())
    if "live" in nav:
        raise DocsError('nav.json: "live" is set per section, not for the whole documentation')
    for section in nav["sections"]:
        if not isinstance(section.get("live", False), bool):
            raise DocsError(f'nav.json: section {section["title"]}: "live" is true or false')
    datasets = load_datasets(src)
    pages, listed = {}, []
    for section in nav["sections"]:
        section["paths"] = [p for group in section["groups"] for p in group["pages"]]
        for path in section["paths"]:
            file = src / f"{path}.md"
            if not file.is_file():
                raise DocsError(f"nav.json lists {path}, but docs-src/{path}.md does not exist")
            if path in pages:
                raise DocsError(f"nav.json lists {path} twice")
            meta, body = split_front_matter(file.read_text(), f"docs-src/{path}.md")
            check_sources(f"docs-src/{path}.md", meta, datasets)
            if "applies_to" in meta and not section.get("app"):
                raise DocsError(f"docs-src/{path}.md: applies_to needs a section with an app name in nav.json")
            if path.startswith(TASKS) and path != TASKS + "index":
                problems = check_task(path, meta, body)
                if problems:
                    raise DocsError("; ".join(problems))
            pages[path] = {"path": path, "meta": meta, "body": body, "section": section, "url": url_of(path)}
            listed.append(path)
    unlisted = sorted(str(f.relative_to(src))[:-3] for f in src.rglob("*.md") if str(f.relative_to(src))[:-3] not in pages)
    if unlisted:
        raise DocsError("not in nav.json: " + ", ".join(f"docs-src/{p}.md" for p in unlisted))
    return nav, pages


def sidebar(nav, pages, page):
    """The sections, then the pages of the current section in their groups."""
    esc = html.escape
    out = ['    <p class="docs-group">Documentation</p>', '    <ul class="docs-sections">']
    for section in nav["sections"]:
        first = pages[section["paths"][0]]
        here = section is page["section"]
        many = len(section["paths"]) > 1   # then the page itself is marked in the list below
        mark = "" if not here else (' aria-current="page"' if first is page and not many else ' aria-current="true"')
        out.append(f'      <li><a href="{first["url"]}"{mark}>{esc(section["title"])}</a></li>')
    out.append("    </ul>")
    section = page["section"]
    if len(section["paths"]) > 1:
        for group in section["groups"]:
            if group.get("title"):
                out.append(f'    <p class="docs-group">{esc(group["title"])}</p>')
            out.append("    <ul>")
            for path in group["pages"]:
                p = pages[path]
                mark = ' aria-current="page"' if p is page else ""
                name = "Overview" if path == section["paths"][0] else p["meta"].get("nav") or p["meta"]["title"]
                out.append(f'      <li><a href="{p["url"]}"{mark}>{esc(name)}</a></li>')
            out.append("    </ul>")
    return "\n".join(out)


def pager(pages, page):
    """Previous and next page inside the section, in sidebar order."""
    paths = page["section"]["paths"]
    i = paths.index(page["path"])
    parts = []
    for j, cls, word in ((i - 1, "prev", "Previous"), (i + 1, "next", "Next")):
        if 0 <= j < len(paths):
            p = pages[paths[j]]
            parts.append(f'<a class="{cls}" href="{p["url"]}"><span>{word}</span>{html.escape(p["meta"]["title"])}</a>')
    if not parts:
        return ""
    return '      <nav class="docs-pager" aria-label="Previous and next page">' + "".join(parts) + "</nav>\n"


def body_html(text):
    out = markdown.Markdown(extensions=EXTENSIONS, output_format="html").convert(text)
    # A table scrolls sideways inside its own panel on a phone, never the page.
    out = re.sub(r"<table\b[^>]*>", lambda m: '<div class="tablewrap">' + m.group(0), out).replace("</table>", "</table></div>")
    return out


def render(nav, pages, page):
    meta, section = page["meta"], page["section"]
    esc = html.escape
    group = next((g.get("title") for g in section["groups"] if page["path"] in g["pages"]), "")
    first = page["path"] == section["paths"][0]
    kicker = "" if first else " · ".join(esc(x) for x in (section["title"], group) if x)
    stamp = ""
    if meta.get("applies_to"):
        stamp = f'      <p class="docs-applies">Applies to {esc(section["app"])} {esc(meta["applies_to"])} and later</p>\n'
    top = page["path"] == "index"
    head_title = meta["title"] if top else f'{meta["title"]} — {section["title"]} documentation'
    if len(head_title) > TITLE_MAX:
        head_title = f'{meta["title"]} — Documentation'
    head = HEAD.format(
        head_title=esc(head_title), og_title=esc(meta["title"], quote=True),
        site_name=esc(section.get("app") or "4DSTEM Studio and Electron Microscopy Studio", quote=True),
        og_image=OG_IMAGES.get(section.get("app"), "/assets/og.jpg"),
        description=esc(meta["description"], quote=True), site=SITE, url=page["url"],
        markdown_url=f'/docs/{page["path"]}.md', robots="index, follow" if section.get("live") else "noindex",
        sidebar=sidebar(nav, pages, page), title=esc(meta["title"]), stamp=stamp,
        kicker=f'      <p class="kicker">{kicker}</p>\n' if kicker else "")
    return head + body_html(page["body"]).rstrip() + "\n" + FOOT.format(pager=pager(pages, page))


def markdown_copy(page):
    """The page as Markdown for agents: its title, its description, the body as written."""
    meta = page["meta"]
    lines = [f'# {meta["title"]}', "", meta["description"], ""]
    if meta.get("applies_to"):
        lines += [f'Applies to {page["section"]["app"]} {meta["applies_to"]} and later.', ""]
    return "\n".join(lines) + page["body"]


def llms_txt(nav, pages):
    out = ["# mac4dstem.com documentation", "",
           "> " + nav["summary"], ""]
    for section in (s for s in nav["sections"] if s.get("live")):
        out += [f'## {section["title"]}', ""]
        for path in section["paths"]:
            p = pages[path]
            out.append(f'- [{p["meta"]["title"]}]({SITE}/docs/{path}.md): {p["meta"]["description"]}')
        out.append("")
    return "\n".join(out)


def sitemap(nav, pages, current):
    """sitemap.xml with the live sections' addresses between the two marker comments."""
    lines = ["  " + MARK[0]]
    live = any(s.get("live") for s in nav["sections"])
    if live:
        for p in (p for p in pages.values() if p["section"].get("live")):
            lines += ["  <url>", f'    <loc>{SITE}{p["url"]}</loc>', "    <priority>0.6</priority>", "  </url>"]
    block = "\n".join(lines + ["  " + MARK[1]])
    if MARK[0] in current:
        return re.sub(re.escape(MARK[0]) + r".*?" + re.escape(MARK[1]), lambda _: block.lstrip(), current, flags=re.S)
    if not live:
        return current
    return current.replace("</urlset>", block + "\n</urlset>")


def outputs(src=SRC, root=ROOT):
    """Every file the sources give, by path under the repository root."""
    nav, pages = load(src)
    files = {}
    for page in pages.values():
        name = page["path"]
        files[f"docs/{name}.html"] = render(nav, pages, page)
        files[f"docs/{name}.md"] = markdown_copy(page)
    if any(s.get("live") for s in nav["sections"]):
        files["llms.txt"] = llms_txt(nav, pages)
    current = (root / "sitemap.xml").read_text() if (root / "sitemap.xml").is_file() else ""
    if current:
        files["sitemap.xml"] = sitemap(nav, pages, current)
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if docs/ differs from what the sources give")
    a = ap.parse_args()
    try:
        files = outputs()
    except DocsError as e:
        print(f"error: {e}")
        sys.exit(1)
    wanted = {ROOT / name for name in files}
    extra = sorted(p for p in OUT.rglob("*") if p.is_file() and p not in wanted) if OUT.is_dir() else []
    if a.check:
        stale = [name for name, text in files.items()
                 if not (ROOT / name).is_file() or (ROOT / name).read_text() != text]
        for name in stale:
            print(f"error: {name} is not what docs-src gives: run python3 tools/build_docs.py")
        for p in extra:
            print(f"error: {p.relative_to(ROOT)} has no source in docs-src: run python3 tools/build_docs.py")
        print(f"docs: {len(files)} files checked")
        sys.exit(1 if stale or extra else 0)
    for name, text in files.items():
        (ROOT / name).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / name).write_text(text)
    for p in extra:
        p.unlink()
    print(f"docs: {len(files)} files written" + (f", {len(extra)} removed" if extra else ""))


if __name__ == "__main__":
    main()

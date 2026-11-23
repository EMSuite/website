#!/usr/bin/env python3
"""Tests for tools/build_docs.py:  python3 -m unittest discover -s tools -p 'test_*.py'"""
import json, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_docs as b

PAGE = "---\ntitle: {title}\ndescription: A page.\n{extra}---\n\n## Heading\n\n| a | b |\n|---|---|\n| 1 | 2 |\n"


class Site:
    """A small docs-src and sitemap.xml in a temporary folder."""

    def __init__(self, live=False, extra=""):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.src = self.root / "docs-src"
        (self.src / "app").mkdir(parents=True)
        nav = {"live": live, "summary": "Docs.", "sections": [
            {"title": "Overview", "groups": [{"pages": ["index"]}]},
            {"title": "App", "app": "App Studio", "groups": [
                {"pages": ["app/index"]}, {"title": "Get started", "pages": ["app/install"]}]}]}
        (self.src / "nav.json").write_text(json.dumps(nav))
        (self.src / "index.md").write_text(PAGE.format(title="Documentation", extra=""))
        (self.src / "app" / "index.md").write_text(PAGE.format(title="App", extra=""))
        (self.src / "app" / "install.md").write_text(PAGE.format(title="Install", extra=extra))
        (self.root / "sitemap.xml").write_text("<urlset>\n  <url>\n    <loc>https://mac4dstem.com/</loc>\n  </url>\n</urlset>\n")

    def outputs(self):
        return b.outputs(self.src, self.root)


class FrontMatter(unittest.TestCase):
    def test_fields_and_body(self):
        meta, body = b.split_front_matter('---\ntitle: "Open: your data"\ndescription: One.\napplies_to: 5.4\n---\n\nText.\n')
        self.assertEqual(meta, {"title": "Open: your data", "description": "One.", "applies_to": "5.4"})
        self.assertEqual(body, "Text.\n")

    def test_refusals(self):
        for text in ("Text.\n", "---\ntitle: A\n", "---\ntitle: A\n---\n", "---\ntitle: A\ndescription: B\ncolour: red\n---\n",
                     "---\ntitle: A\ndescription: B\napplies_to: 5.4.1\n---\n"):
            with self.assertRaises(b.DocsError, msg=text):
                b.split_front_matter(text)


class Build(unittest.TestCase):
    def test_pages_markdown_copies_and_addresses(self):
        files = Site(extra="applies_to: 5.4\n").outputs()
        self.assertEqual(sorted(f for f in files if f.startswith("docs/")), [
            "docs/app/index.html", "docs/app/index.md", "docs/app/install.html", "docs/app/install.md",
            "docs/index.html", "docs/index.md"])
        page = files["docs/app/install.html"]
        self.assertIn("<h1>Install</h1>", page)
        self.assertIn("Applies to App Studio 5.4 and later", page)
        self.assertIn('<a href="/docs/app/install.html" aria-current="page">Install</a>', page)
        self.assertIn('<a href="/docs/app/" aria-current="true">App</a>', page)
        self.assertIn('<a class="prev" href="/docs/app/">', page)
        self.assertIn('<div class="tablewrap"><table>', page)
        self.assertIn('<h2 id="heading">', page)
        self.assertIn('<link rel="canonical" href="https://mac4dstem.com/docs/app/install.html">', page)
        self.assertTrue(files["docs/app/install.md"].startswith("# Install\n\nA page.\n\nApplies to App Studio 5.4 and later.\n"))

    def test_not_live_is_hidden_from_search(self):
        site = Site()
        files = site.outputs()
        self.assertIn('<meta name="robots" content="noindex">', files["docs/index.html"])
        self.assertNotIn("llms.txt", files)
        self.assertEqual(files["sitemap.xml"], (site.root / "sitemap.xml").read_text())

    def test_live_is_listed_once(self):
        site = Site(live=True)
        files = site.outputs()
        self.assertIn('<meta name="robots" content="index, follow">', files["docs/index.html"])
        self.assertIn("- [Install](https://mac4dstem.com/docs/app/install.md): A page.", files["llms.txt"])
        self.assertEqual(files["sitemap.xml"].count("<loc>https://mac4dstem.com/docs/app/install.html</loc>"), 1)
        (site.root / "sitemap.xml").write_text(files["sitemap.xml"])
        self.assertEqual(site.outputs()["sitemap.xml"], files["sitemap.xml"])

    def test_the_tutorial_template_builds(self):
        site = Site()
        nav = json.loads((site.src / "nav.json").read_text())
        nav["sections"][1]["groups"].append({"title": "Tutorials", "pages": ["app/tutorial"]})
        (site.src / "nav.json").write_text(json.dumps(nav))
        template = Path(__file__).resolve().parent / "tutorial-template.md"
        (site.src / "app" / "tutorial.md").write_text(template.read_text())
        page = site.outputs()["docs/app/tutorial.html"]
        for part in ("What you will measure", "Steps", "Reading the result", "Export", "The same analysis by an agent"):
            self.assertIn(f">{part}</h2>", page)
        self.assertIn('<source srcset="/assets/docs/APP/TUTORIAL/01-open.webp" type="image/webp">', page)
        self.assertIn("Applies to App Studio 2.1 and later", page)

    def test_nav_and_sources_must_agree(self):
        site = Site()
        (site.src / "app" / "stray.md").write_text(PAGE.format(title="Stray", extra=""))
        with self.assertRaisesRegex(b.DocsError, "not in nav.json: docs-src/app/stray.md"):
            site.outputs()
        (site.src / "app" / "stray.md").unlink()
        (site.src / "app" / "install.md").unlink()
        with self.assertRaisesRegex(b.DocsError, "docs-src/app/install.md does not exist"):
            site.outputs()

    def test_applies_to_needs_an_app(self):
        site = Site()
        (site.src / "index.md").write_text(PAGE.format(title="Documentation", extra="applies_to: 5.4\n"))
        with self.assertRaisesRegex(b.DocsError, "applies_to needs a section with an app name"):
            site.outputs()


if __name__ == "__main__":
    unittest.main()

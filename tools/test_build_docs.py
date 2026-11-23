#!/usr/bin/env python3
"""Tests for tools/build_docs.py:  python3 -m unittest discover -s tools -p 'test_*.py'"""
import json, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_docs as b

PAGE = "---\ntitle: {title}\ndescription: A page.\n{extra}---\n\n## Heading\n\n| a | b |\n|---|---|\n| 1 | 2 |\n"


class Site:
    """A small docs-src and sitemap.xml in a temporary folder."""

    def __init__(self, live=(), extra=""):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.src = self.root / "docs-src"
        (self.src / "app").mkdir(parents=True)
        nav = {"summary": "Docs.", "sections": [
            {"title": "Overview", "groups": [{"pages": ["index"]}]},
            {"title": "App", "app": "App Studio", "groups": [
                {"pages": ["app/index"]}, {"title": "Get started", "pages": ["app/install"]}]}]}
        for section in nav["sections"]:
            if section["title"] in live:
                section["live"] = True
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
        self.assertEqual(page.count('<div class="tablewrap">'), page.count("</table></div>"))
        html_table = b.body_html('<table class="methods">\n<tr><td>a</td></tr>\n</table>\n')
        self.assertEqual(html_table.count('<div class="tablewrap"><table class="methods">'), 1)
        self.assertEqual(html_table.count("</table></div>"), 1)
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
        site = Site(live=("Overview", "App"))
        files = site.outputs()
        self.assertIn('<meta name="robots" content="index, follow">', files["docs/index.html"])
        self.assertIn("- [Install](https://mac4dstem.com/docs/app/install.md): A page.", files["llms.txt"])
        self.assertEqual(files["sitemap.xml"].count("<loc>https://mac4dstem.com/docs/app/install.html</loc>"), 1)
        (site.root / "sitemap.xml").write_text(files["sitemap.xml"])
        self.assertEqual(site.outputs()["sitemap.xml"], files["sitemap.xml"])

    def test_a_mixed_nav_lists_only_its_live_sections(self):
        site = Site(live=("App",))
        files = site.outputs()
        self.assertIn('<meta name="robots" content="index, follow">', files["docs/app/install.html"])
        self.assertIn('<meta name="robots" content="noindex">', files["docs/index.html"])
        self.assertIn("<loc>https://mac4dstem.com/docs/app/install.html</loc>", files["sitemap.xml"])
        self.assertIn("<loc>https://mac4dstem.com/docs/app/</loc>", files["sitemap.xml"])
        self.assertNotIn("<loc>https://mac4dstem.com/docs/</loc>", files["sitemap.xml"])
        self.assertIn("## App", files["llms.txt"])
        self.assertNotIn("## Overview", files["llms.txt"])
        self.assertNotIn("(https://mac4dstem.com/docs/index.md)", files["llms.txt"])

    def test_a_whole_docs_live_switch_is_refused(self):
        site = Site()
        nav = json.loads((site.src / "nav.json").read_text())
        nav["live"] = True
        (site.src / "nav.json").write_text(json.dumps(nav))
        with self.assertRaisesRegex(b.DocsError, "set per section"):
            site.outputs()

    def datasets(self, site):
        (site.src / "datasets.json").write_text(json.dumps({"datasets": {
            "gold": {"title": "Gold rings", "doi": "10.5281/zenodo.14113591", "licence": "CC BY 4.0",
                     "recipes": ["diffraction-au-grating"]}}}))

    def test_a_tutorial_on_a_listed_dataset_and_recipe_builds(self):
        site = Site(extra="dataset: gold\nrecipe: diffraction-au-grating\n")
        self.datasets(site)
        self.assertIn("docs/app/install.html", site.outputs())

    def test_a_recipe_that_does_not_exist_is_refused(self):
        site = Site(extra="dataset: gold\nrecipe: gold-by-hand\n")
        self.datasets(site)
        with self.assertRaisesRegex(b.DocsError, "recipe 'gold-by-hand' is not a recipe of gold"):
            site.outputs()

    def test_a_recipe_needs_its_dataset(self):
        site = Site(extra="recipe: diffraction-au-grating\n")
        self.datasets(site)
        with self.assertRaisesRegex(b.DocsError, "needs the dataset"):
            site.outputs()

    def test_an_unlisted_dataset_is_refused(self):
        site = Site(extra="dataset: my-own-scan\n")
        self.datasets(site)
        with self.assertRaisesRegex(b.DocsError, "dataset 'my-own-scan' is not in docs-src/datasets.json"):
            site.outputs()

    def test_a_dataset_without_licence_or_doi_is_refused(self):
        for field, value in (("licence", ""), ("doi", ""), ("doi", "zenodo 14113591")):
            site = Site()
            self.datasets(site)
            d = json.loads((site.src / "datasets.json").read_text())
            d["datasets"]["gold"][field] = value
            (site.src / "datasets.json").write_text(json.dumps(d))
            with self.assertRaisesRegex(b.DocsError, f"gold", msg=f"{field}={value!r}"):
                site.outputs()

    def test_the_committed_datasets_have_licence_and_doi(self):
        self.assertGreater(len(b.load_datasets()), 0)

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

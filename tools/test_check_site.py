#!/usr/bin/env python3
"""Tests for tools/check_site.py:  python3 -m unittest discover -s tools -p 'test_*.py'"""
import json, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_site as c


class Stamps(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.src = Path(self.tmp.name)
        (self.src / "app").mkdir()
        (self.src / "other").mkdir()
        nav = {"sections": [
            {"title": "Overview", "groups": [{"pages": ["index"]}]},
            {"title": "App", "app": "App Studio", "groups": [{"pages": ["app/index"]}, {"title": "Start", "pages": ["app/install"]}]},
            {"title": "Other", "app": "Other Studio", "groups": [{"pages": ["other/index"]}]}]}
        (self.src / "nav.json").write_text(json.dumps(nav))
        self.page("index")
        self.page("app/index")
        self.page("app/install", "applies_to: 5.4\n")
        self.page("other/index", "applies_to: 2.1\n")

    def page(self, path, extra=""):
        (self.src / f"{path}.md").write_text(f"---\ntitle: Page\ndescription: A page.\n{extra}---\n\napplies_to: 9.9 in the text is not a stamp.\n")

    def test_current_stamp_passes_on_any_patch(self):
        self.assertEqual(c.check_stamps("App Studio", "5.4.0", self.src), [])
        self.assertEqual(c.check_stamps("App Studio", "5.4.7", self.src), [])

    def test_stale_stamp_fails_and_names_the_page(self):
        errors = c.check_stamps("App Studio", "5.5.0", self.src)
        self.assertEqual(len(errors), 1)
        self.assertIn("docs-src/app/install.md", errors[0])
        self.assertIn("applies_to: 5.5", errors[0])

    def test_each_app_is_checked_against_its_own_release(self):
        self.assertEqual(c.check_stamps("Other Studio", "2.1.3", self.src), [])
        self.assertEqual(len(c.check_stamps("Other Studio", "3.0.0", self.src)), 1)

    def test_no_docs_folder_is_no_error(self):
        self.assertEqual(c.check_stamps("App Studio", "5.5.0", self.src / "missing"), [])


class DMGNames(unittest.TestCase):
    def test_the_renaming_release_and_later_carry_the_new_name(self):
        self.assertEqual(c.dmg_base("mac4DSTEM", "5.4.2"), "mac4DSTEM")
        self.assertEqual(c.dmg_base("mac4DSTEM", "5.4.3"), "4DSTEM-Studio")
        self.assertEqual(c.dmg_base("mac4DSTEM", "5.10.0"), "4DSTEM-Studio")
        self.assertEqual(c.dmg_base("macEM", "2.1.0"), "macEM")
        self.assertEqual(c.dmg_base("macEM", "2.1.1"), "Electron-Microscopy-Studio")


class OldNames(unittest.TestCase):
    def test_split_wordmark_is_caught(self):
        self.assertEqual(len(c.old_names('<h1 class="wordmark">mac<em>4D</em>STEM</h1>')), 1)
        self.assertEqual(len(c.old_names('<h1>mac<em>EM</em></h1>')), 1)

    def test_alt_and_meta_are_read(self):
        self.assertEqual(len(c.old_names('<img src="a.png" alt="The macTEM window">')), 1)
        self.assertEqual(len(c.old_names('<meta property="og:title" content="mac4DSTEM">')), 1)

    def test_file_and_domain_names_pass(self):
        ok = ('<p>Download mac4DSTEM.dmg or mac4DSTEM-5.4.1.dmg from mac4dstem.com; the session is scan.mac4dstem.h5 '
              'or scan.dm4.mactem.h5.</p><a href="/mactem/">Electron Microscopy Studio</a>'
              '<script>var x = "macEM";</script><img src="/assets/mactem-og.jpg" alt="">')
        self.assertEqual(c.old_names(ok), [])

    def test_store_names_pass(self):
        self.assertEqual(c.old_names('<h1><em>4D</em>STEM Studio</h1><h1>Electron Microscopy <em>Studio</em></h1>'), [])

    def test_block_tags_do_not_join_words(self):
        self.assertEqual(c.old_names('<p>mac</p><p>EM</p>'), [])


class Moved(unittest.TestCase):
    FORWARD = ('<!DOCTYPE html><html><head><meta name="robots" content="noindex">'
               '<link rel="canonical" href="https://mac4dstem.com/electron-microscopy-studio/">'
               '<meta http-equiv="refresh" content="0; url=/electron-microscopy-studio/"></head>'
               '<body><a href="/electron-microscopy-studio/">moved</a></body></html>')

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for d in ("mactem", "electron-microscopy-studio", "docs"):
            (self.root / d).mkdir()
        (self.root / "mactem/index.html").write_text(self.FORWARD)
        (self.root / "electron-microscopy-studio/index.html").write_text("<p>The app</p>")
        (self.root / "index.html").write_text('<a href="/electron-microscopy-studio/">EM Studio</a>')
        (self.root / "sitemap.xml").write_text("<loc>https://mac4dstem.com/electron-microscopy-studio/</loc>")

    def test_a_forwarding_page_and_new_links_pass(self):
        self.assertEqual(c.check_moved(self.root), [])

    def test_a_link_to_the_old_address_fails(self):
        (self.root / "docs/page.html").write_text('<a href="/mactem/">old</a><a href="../mactem/index.html">old</a>')
        errors = c.check_moved(self.root)
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("docs/page.html" in e for e in errors))

    def test_the_sitemap_naming_the_old_address_fails(self):
        (self.root / "sitemap.xml").write_text("<loc>https://mac4dstem.com/mactem/</loc>")
        self.assertEqual(len(c.check_moved(self.root)), 1)

    def test_an_old_address_that_does_not_forward_fails(self):
        (self.root / "mactem/index.html").write_text("<p>The old page, still here</p>")
        self.assertEqual(len(c.check_moved(self.root)), 3)

    def test_a_missing_old_address_fails(self):
        (self.root / "mactem/index.html").unlink()
        self.assertEqual(len(c.check_moved(self.root)), 1)


class Heads(unittest.TestCase):
    GOOD = ('<html><head><title>Install — Docs</title>'
            '<meta name="description" content="Install the app on an Apple silicon Mac: requirements and download.">'
            '<link rel="canonical" href="https://mac4dstem.com/{rel}">'
            '<meta property="og:title" content="Install">'
            '<meta property="og:image" content="https://mac4dstem.com/assets/og.jpg"></head>'
            '<body><h1>Install</h1></body></html>')

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "assets").mkdir()
        (self.root / "assets" / "og.jpg").write_bytes(b"jpg")
        (self.root / "docs").mkdir()

    def write(self, rel, text=None):
        (self.root / rel).write_text(text or self.GOOD.format(rel=rel.removesuffix("index.html")))

    def test_a_complete_head_passes(self):
        self.write("docs/install.html")
        self.write("docs/index.html")
        self.assertEqual(c.check_heads(self.root), [])

    def test_each_part_fails_on_its_own(self):
        good = self.GOOD.format(rel="page.html")
        cases = {
            "title has 71": good.replace("Install — Docs", "x" * 71),
            "description has 10": good.replace("Install the app on an Apple silicon Mac: requirements and download.", "Too short."),
            "2 <h1>": good.replace("<h1>Install</h1>", "<h1>A</h1><h1>B</h1>"),
            "canonical link": good.replace("https://mac4dstem.com/page.html", "https://mac4dstem.com/other.html"),
            "no og:title": good.replace('<meta property="og:title" content="Install">', ""),
            "names no file": good.replace("og.jpg", "missing.jpg"),
            "picture of this site": good.replace("https://mac4dstem.com/assets/og.jpg", "https://example.org/a.jpg"),
        }
        for want, text in cases.items():
            self.write("page.html", text)
            errors = c.check_heads(self.root)
            self.assertEqual(len(errors), 1, f"{want}: {errors}")
            self.assertIn(want, errors[0])

    def test_404_and_forwarding_pages_need_only_a_title(self):
        self.write("404.html", "<html><head><title>Not found</title></head><body><h1>Not found</h1></body></html>")
        self.write("old.html", '<html><head><title>Moved</title><meta http-equiv="refresh" content="0; url=/new/"></head></html>')
        self.assertEqual(c.check_heads(self.root), [])


if __name__ == "__main__":
    unittest.main()

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


if __name__ == "__main__":
    unittest.main()

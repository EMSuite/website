#!/usr/bin/env python3
"""Tests for tools/build_feed.py and the feed checks of tools/check_site.py:
python3 -m unittest discover -s tools -p 'test_*.py'"""
import shutil, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_feed as f
import check_site as c

APPCAST = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle">
  <channel>
    <title>{app}</title>
    <item>
      <title>{app} {ver}</title>
      <pubDate>{date}</pubDate>
      <sparkle:version>{ver}</sparkle:version>
      <sparkle:shortVersionString>{ver}</sparkle:shortVersionString>
      <sparkle:fullReleaseNotesLink>https://github.com/EMSuite/{repo}/releases/tag/v{ver}</sparkle:fullReleaseNotesLink>
      <description sparkle:format="plain-text">{app} {ver} notes &amp; fixes.</description>
    </item>
  </channel>
</rss>
"""
RELEASES = ("<tr><td>ImagoKit</td><td>0.11.0</td><td>2026-11-16</td><td>tag</td></tr>\n"
            "<tr><td>EMSuiteUI</td><td>0.13.0</td><td>2026-11-18</td><td>tag</td></tr>\n")


class Feed(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "appcast").mkdir()
        (self.root / "suite").mkdir()
        self.appcast("mac4dstem", "4DSTEM Studio", "4DSTEM-Studio", "5.4.3", "Wed, 18 Nov 2026 21:02:06 GMT")
        self.appcast("macem", "Electron Microscopy Studio", "Electron-Microscopy-Studio", "2.1.1", "Thu, 19 Nov 2026 06:54:15 GMT")
        (self.root / "suite" / "releases.html").write_text(f"<html><head>{f.LINK}</head><body><table>{RELEASES}</table></body></html>")
        (self.root / "index.html").write_text(f"<html><head>{f.LINK}</head><body></body></html>")

    def appcast(self, name, app, repo, ver, date):
        (self.root / "appcast" / f"{name}.xml").write_text(APPCAST.format(app=app, repo=repo, ver=ver, date=date))

    def build(self):
        text = f.render(f.entries(self.root))
        (self.root / "releases.atom").write_text(text)
        return text

    def test_newest_first_with_apps_and_kits(self):
        text = self.build()
        titles = [l.strip()[7:-8] for l in text.splitlines() if l.strip().startswith("<title>")][1:]
        self.assertEqual(titles, ["Electron Microscopy Studio 2.1.1", "4DSTEM Studio 5.4.3", "EMSuiteUI 0.13.0", "ImagoKit 0.11.0"])
        self.assertIn("notes &amp; fixes.", text)
        self.assertEqual(f.newest_app_versions(text), {"Electron Microscopy Studio": "2.1.1", "4DSTEM Studio": "5.4.3"})

    def test_a_new_release_is_added_and_the_old_one_kept(self):
        self.build()
        self.appcast("macem", "Electron Microscopy Studio", "Electron-Microscopy-Studio", "2.2.0", "Mon, 30 Nov 2026 10:00:00 GMT")
        text = self.build()
        self.assertIn("Electron Microscopy Studio 2.1.1", text)
        self.assertEqual(f.newest_app_versions(text)["Electron Microscopy Studio"], "2.2.0")
        self.assertEqual(text, self.build(), "building twice changes nothing")

    def test_check_site_passes_a_current_feed(self):
        self.build()
        self.assertEqual(c.check_feed_links(self.root), [])

    def test_check_site_fails_a_feed_behind_the_update_feed(self):
        self.build()
        self.appcast("macem", "Electron Microscopy Studio", "Electron-Microscopy-Studio", "2.2.0", "Mon, 30 Nov 2026 10:00:00 GMT")
        errors = c.check_feed_links(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("newest Electron Microscopy Studio entry is 2.1.1", errors[0])

    def test_check_site_fails_a_page_without_the_link(self):
        self.build()
        (self.root / "other.html").write_text("<html><head></head><body><a href='/releases.atom'>feed</a></body></html>")
        errors = c.check_feed_links(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("other.html", errors[0])


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Tests for tools/build_methods.py:  python3 -m unittest discover -s tools -p 'test_*.py'"""
import sys, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_methods as m

PARITY = """# Parity

Intro with `tools/run-tests.sh`, nightly.

## Readers (exact)

| Function | Reference | Test | Tolerance | Notes |
|---|---|---|---|---|
| `ANGReader.read` | `orix.io.plugins.ang.file_reader` | `ANGReaderTests` | exact | LF and CR (#518) |
| `KikuchiReflectors.dSpacing` | `diffsims` | same | rtol 1e-7 | \\|F\\| only |

### Known limits and decisions

- prose that stays in the file

## Grains, KAM and GOS (figures F11, F12)

| Function | Reference | Test | Tolerance | Notes |
|---|---|---|---|---|
| `KAM.compute` (#514) | orix `kernel_average_misorientation`, [paper](docs/x.md); Rowenhorst et al. 2015 (D-SEM-19) | `KAMTests` | 1e-12; which macEM reads | n |

## Not a parity table

| A | B |
|---|---|
| 1 | 2 |
"""


class Methods(unittest.TestCase):
    def test_three_columns_per_section_and_nothing_else(self):
        parts = m.sections(PARITY)
        self.assertEqual([h for h, _ in parts], ["Readers (exact)", "Grains, KAM and GOS"])
        self.assertEqual(parts[0][1][0], ["`ANGReader.read`", "`orix.io.plugins.ang.file_reader`", "exact"])
        self.assertEqual(parts[0][1][1][2], "rtol 1e-7", "an escaped pipe in Notes does not shift the columns")

    def test_internal_ids_links_and_old_names_are_left_out(self):
        row = m.sections(PARITY)[1][1][0]
        self.assertEqual(row[0], "`KAM.compute`")
        self.assertEqual(row[1], "orix `kernel_average_misorientation`, paper; Rowenhorst et al. 2015")
        self.assertEqual(row[2], "1e-12; which Electron Microscopy Studio reads")

    def test_the_page_names_its_tag_and_counts(self):
        text = m.page(PARITY, "v2.1.1")
        self.assertIn("applies_to: 2.1\n", text)
        self.assertIn("3 functions in 2 groups", text)
        self.assertIn("https://github.com/EMSuite/Electron-Microscopy-Studio/blob/v2.1.1/docs/parity.md", text)
        self.assertNotIn("nightly", text)
        self.assertIn("<thead><tr><th>Function</th><th>Reference</th><th>Tolerance</th></tr></thead>", text)
        self.assertIn("<td><code>ANGReader.read</code></td>", text)
        self.assertNotIn("<th>Test</th>", text)


if __name__ == "__main__":
    unittest.main()

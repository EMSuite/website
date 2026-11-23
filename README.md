# mac4dstem.com

Source for [mac4dstem.com](https://mac4dstem.com), the website of the macEM suite: two free,
native macOS applications for electron microscopy, [mac4DSTEM](https://github.com/EMSuite/4DSTEM-Studio)
(4D-STEM) and [macEM](https://github.com/EMSuite/Electron-Microscopy-Studio) (TEM images, spectra and diffraction),
and the six Swift kits they are built on.

The site is static: **plain HTML, CSS, and vanilla JavaScript, with no build step,
no dependencies, and no framework.** Pushing to `main` publishes through GitHub
Pages within about a minute.

## Running it locally

Any static file server will do. From the repository root:

```bash
python3 -m http.server 4173
```

Then open <http://localhost:4173>. Pages reference assets by absolute path, so
opening `index.html` directly from the filesystem will not load the stylesheet.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | The mac4DSTEM page and landing page. Page-specific styling lives in its `<style>` block. |
| `electron-microscopy-studio/index.html` | The Electron Microscopy Studio page, in the landing page's style (its own `<style>` block, the demo left out). |
| `mactem/index.html` | Forwards the page's old address to `/electron-microscopy-studio/` (noindex, canonical link). `tools/check_site.py` fails when it stops forwarding or when anything in the site links it. |
| `privacy.html` | Privacy policy for both applications and the site. |
| `support.html` | Support, requirements, and known limitations of both applications. |
| `impressum.html` | Provider identification (§ 5 DDG). |
| `404.html` | The page GitHub Pages serves for an unknown address. |
| `assets/site.css` | Styling shared across all pages. |
| `assets/demo.js` | The interactive virtual-imaging demo. |
| `suite/` | Kits overview, benchmarks and releases pages for the macEM suite. Generated, do not edit. |
| `tools/build_suite_pages.py` | Generates `suite/` from the kits' and MacEMUI's CHANGELOG, `docs/parity.md` and `docs/benchmarks.md`. Run `python3 tools/build_suite_pages.py --fetch` after a kit or MacEMUI release. |
| `docs-src/` | The documentation's sources: `nav.json` (sections, groups, page order) and one Markdown file per page. |
| `docs-src/datasets.json` | The public datasets tutorials may use: DOI, licence, and the names of the suite's reference recipes on each (a copy, since the suite repository is private). |
| `docs/` | The documentation pages and their Markdown copies. Generated, do not edit. |
| `assets/docs.css` | Styling of the documentation pages, on top of `site.css`. |
| `tools/build_docs.py` | Generates `docs/` from `docs-src/`. Needs Python-Markdown: `pip install -r tools/requirements.txt`. |
| `tools/check_site.py` | The CI check: internal links, no old app names (mac4DSTEM, macEM, macTEM) in the page text, and versions and download sizes against the GitHub releases. |
| `tools/tutorial-template.md` | The skeleton every tutorial starts from (see Writing a tutorial). A test builds it. |
| `tools/docs_pictures.py` | Puts a reviewed picture into the documentation as WebP and PNG. Development only. |
| `tools/build_methods.py` | Generates the Electron Microscopy Studio Methods page (`docs-src/electron-microscopy-studio/methods.md`) from the app's `docs/parity.md` at a release tag: function, reference, tolerance. Run `python3 tools/build_methods.py --fetch` after each app release, then `tools/build_docs.py`. |
| `tools/export_atlas.py` | Regenerates the demo dataset. Development only. |

## Writing a documentation page

1. Add `docs-src/<section>/<page>.md`. It starts with a front-matter block, then Markdown:

   ```markdown
   ---
   title: Install
   description: One sentence for search engines.
   applies_to: 5.4
   ---

   ## What you need
   ```

   `applies_to` is the app version the page was read against; the page shows "Applies to … 5.4 and later".
   A tutorial also names its `recipe` and `dataset`: the dataset is a key of `docs-src/datasets.json`, which lists each
   public dataset with its DOI and licence and the suite's recipes that run on it, and the build refuses a tutorial
   whose dataset or recipe is not there.
   When the app has a new minor release, `tools/check_site.py` fails for every page whose `applies_to` is behind it:
   read the page against the new version, correct it, and move the stamp. A feature that arrived with that version
   gets a note in the text, `!!! note "New in 5.5"`. There are no copies of the documentation per version.
2. List the page in `docs-src/nav.json`, in the group and at the place where the sidebar should show it.
3. Run `python3 tools/build_docs.py` and commit `docs-src/` and `docs/` together. CI fails when they disagree.

Links between pages are absolute (`/docs/4dstem-studio/install.html`). Tables, fenced code, notes
(`!!! note "Title"`, `!!! warning`) and raw HTML work; a control's name is written
`<span class="ui">Detect All Disks</span>` and a key `<kbd>⌘R</kbd>`. Pictures go to `assets/docs/<section>/<page>/`.

Each section in `nav.json` goes live on its own: `"live": true` on the section indexes its pages and lists them in
`sitemap.xml` and `llms.txt`. A section without it stays hidden (noindex, in neither list) until it is reviewed. Live
today: the overview and Electron Microscopy Studio. The `.nojekyll` file makes GitHub Pages serve the repository as it is, Markdown included.

## Writing a tutorial

A tutorial takes the reader through one analysis of one public dataset, from the open file to the exported result.

1. **Start from the recipe.** Every tutorial follows a reference recipe of the suite (`tools/door/plan.json` for
   4DSTEM Studio, `plan-macEM.json` for Electron Microscopy Studio): its settings, the flags it expects and its numbers
   with their tolerances. Never work the settings out again on the page. A dataset without a recipe gets one first, in
   a suite pull request.
2. **Copy the template.** `cp tools/tutorial-template.md docs-src/<app>/tutorials/<name>.md` and list the page in
   `nav.json` in a "Tutorials" group. Front matter: `recipe` is the recipe's name, `dataset` the dataset's key; the
   dataset must be public and on the [Example data](docs-src/data/index.md) page with its licence and DOI.
3. **Fill the five parts:** what you will measure and what you need; the steps, each with what to click, every
   setting and why it has this value, and the app's signal to check before going on (fit RMS, "not quantitative",
   flags, counts) with what to do when it is flagged; reading the result; the export; the same analysis by an agent.
4. **Pictures.** Result figures come through the agent door (`get_result_image`, `get_pattern_image`: the figures
   File › Export writes), window pictures from the release walk on the Mac, in the dark appearance, from public data
   only. Look at every picture before it is committed, then run
   `python3 tools/docs_pictures.py SHOT.png <app> <name> 01-open` (needs Pillow): it writes a WebP and a PNG fallback
   1600 px wide to `assets/docs/<app>/<name>/` and prints the `<figure>` to paste. Store screenshots are not reused.
5. **Build and check:** `python3 tools/build_docs.py`, then `python3 tools/check_site.py --offline`. Mark the pull
   request "no science review yet" until the page has had one.

## Checks and releases

CI (`.github/workflows/ci.yml`) runs on every push to `main`, on pull requests, and once a day. It scans for
references to private material and runs `tools/check_site.py`: every internal link and `#fragment` must resolve, every page that can be a search result has one `<h1>`, a title of at most 70 characters, a description of 50 to 160, a canonical link to itself and a link preview (`og:title` and an `og:image` that is a file of the site), no page text (alt text and link previews included) may use an old app name, each
app page must state the latest release's version and `.dmg` size (in the text and in the JSON-LD), and
`suite/releases.html` must name each kit's and EMSuiteUI's latest tag. Run it locally with
`python3 tools/check_site.py` (or `--offline` for links and names only).

After an app release, update the version and size on its page and regenerate the Methods page (`tools/build_methods.py --fetch`). After a kit or MacEMUI release, regenerate `suite/`.

Everything else in `assets/` is a generated artefact — images, icons, the social
card, and the demo data. None of it is edited by hand.

## The interactive demo

The landing page includes a working 4D-STEM virtual-imaging demo running entirely
in the browser, on a real experimental scan of a NiCu alloy.

A 4D-STEM dataset records a full diffraction pattern at every probe position, so
real space and diffraction space each produce the other. Placing a mask on the
detector integrates it into a virtual image; selecting a region of the scan
integrates it into a diffraction pattern. Both directions recompute in a few
milliseconds, so the masks respond as you drag them.

### How the data is shipped

The full datacube is far too large to serve, so `tools/export_atlas.py` reduces it
to a single sprite atlas:

- The scan is binned 2×2 to 100×100 positions, keeping the atlas at 3200×3200 —
  below Safari's canvas area limit.
- Each 32×32 diffraction pattern becomes one tile, at pixel `(rx*32, ry*32)`.
- Intensities are **log-companded** to 8 bits. Eight bits cannot hold the linear
  range between the direct beam and the dark-field signal, so the page rebuilds a
  256-entry lookup table from `demo-manifest.json` and decompands before summing.
  Integrals therefore stay linear in the units the microscope recorded.

The atlas is stored losslessly. Lossy compression was measured introducing up to 9%
error in dark-field sums even at high quality, because adjacent tiles are unrelated
patterns and the codec bleeds signal across tile boundaries.

The atlas is only fetched when the demo is approached, and never on metered or slow
connections, where a load button appears instead.

### Regenerating it

Place the source `.h5` datacube in `datacube/` (gitignored — it is far above
GitHub's file size limit) and run:

```bash
pip install h5py numpy pillow
```

```bash
python3 tools/export_atlas.py [--src FILE.h5] [--previews DIR]
```

This rewrites `assets/demo-atlas.png` and `assets/demo-manifest.json`; `--previews` also writes mean-pattern,
bright-field and dark-field check images to `DIR`.

## Privacy

The site sets no cookies, runs no analytics, and makes no third-party requests. It
uses the system font stack rather than a hosted webfont. See
[privacy.html](privacy.html).

## Licence

The site is released under the GNU General Public License v3.0 ([`LICENSE`](LICENSE)), as are
both applications and the kits. mac4DSTEM's analysis algorithms are ported from and validated
against [py4DSTEM](https://github.com/py4dstem/py4DSTEM); work published using mac4DSTEM should
cite py4DSTEM for the underlying methods.

## Contact

**mail@mac4dstem.com**

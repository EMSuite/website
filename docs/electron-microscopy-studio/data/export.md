# Export

What Electron Microscopy Studio exports from each part, as PNG pictures, CSV tables, method JSON, orientation maps in .ang and .ctf, and a session report.

Applies to Electron Microscopy Studio 2.1 and later.
<p class="lede">Pictures leave the app as PNG, numbers as CSV, and the method as JSON, so a result can be repeated.</p>

The export commands are in the <span class="ui">File</span> menu and as buttons in the inspector of each part. A command is available when its part has the result.

## By part

| Part | Exports |
|---|---|
| Image | <span class="ui">Export Image…</span> (<kbd>⇧⌘E</kbd>), <span class="ui">Export Profile…</span> |
| FFT | <span class="ui">Export Transform…</span> (<kbd>⌥⌘E</kbd>), <span class="ui">Export Radial Profile…</span>, <span class="ui">Export Spots…</span> |
| Patterns | Map PNG, Pattern PNG, Pattern with Overlay, Overlay CSV, Metadata JSON, Method JSON |
| Indexing | Map PNG, Results CSV, EDAX ANG, Oxford CTF, Method JSON |
| Maps | Map PNG, Grains CSV, Histogram CSV, Texture PNG |
| EDS | Spectrum CSV, Maps, Results CSV, Method JSON, Regions CSV |
| EELS | Results CSV, Spectrum CSV, Spectrum MSA, Regions CSV, Maps, Per-pixel CSV, Method JSON |
| Results | <span class="ui">Export Results…</span> (<kbd>⌥⇧⌘E</kbd>), <span class="ui">Export Session Report…</span> |

## What the files are for

- **PNG** is for pictures: images, maps, patterns and transforms.
- **CSV** tables open in any spreadsheet or script.
- **Method JSON** records the settings a result was made with. Keep it with the result.
- **EDAX ANG** and **Oxford CTF** carry an indexed map to other EBSD software, such as MTEX or orix.
- **Spectrum MSA** is the EMSA format that spectroscopy software reads.

## The session report

<span class="ui">Export Results…</span> writes every finished measurement of the file as one CSV.

<span class="ui">Export Session Report…</span> writes the SEM work of the session (patterns, indexing, maps and SEM spectra) as one report with its figures, as Markdown or PDF. It states the date, the app version and the packages the app is built with.

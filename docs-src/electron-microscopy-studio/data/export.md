---
title: Export
description: What Electron Microscopy Studio exports from each part, as PNG pictures, CSV tables, method JSON, orientation maps in .ang and .ctf, and a session report.
applies_to: 2.6
---

<p class="lede">Pictures leave the app as PNG, or as PDF or SVG figures for a paper; numbers as CSV; and the method as JSON, so a result can be repeated.</p>

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
| Diffraction | <span class="ui">Export Figure…</span> (<kbd>⇧⌘E</kbd>), <span class="ui">Copy Figure</span> (<kbd>⇧⌘C</kbd>), <span class="ui">Save Phase as CIF…</span>, <span class="ui">Export Spots…</span> (the Spots CSV) |
| Results | <span class="ui">Export Results…</span> (<kbd>⌥⇧⌘E</kbd>), <span class="ui">Export Session Report…</span> |

## What the files are for

- **PNG** is for pictures: images, maps, patterns and transforms.
- **PDF and SVG** figures are for a paper: the FFT, the EDS and EELS spectra and maps, the orientation maps and the diffraction pattern leave with their rings, boundaries and scale bar as vectors and every label as live text. <span class="ui">Copy Figure</span> pastes the figure into Keynote.
- **CSV** tables open in any spreadsheet or script.
- **Method JSON** records the settings a result was made with. Keep it with the result.
- **The methods record**: every export carries a record of how its numbers were made (the source by fingerprint, each step and setting, the app and kit versions). <span class="ui">File › Export Methods Record…</span> saves the room's record as JSON, and <span class="ui">Edit › Copy Methods Paragraph</span> (<kbd>⌥⌘C</kbd>) copies it as a paragraph for a methods section.
- **HyperSpy files**: <span class="ui">File › Export HyperSpy File…</span> writes the Image room's image, the Diffraction room's pattern or the EELS room's spectrum image as a `.hspy` that `hs.load` opens, with the methods record in its metadata.
- **EDAX ANG** and **Oxford CTF** carry an indexed map to other EBSD software, such as MTEX or orix.
- **Spectrum MSA** is the EMSA format that spectroscopy software reads.

## The session report

<span class="ui">Export Results…</span> writes every finished measurement of the file as one CSV.

<span class="ui">Export Session Report…</span> writes the SEM work of the session (patterns, indexing, maps and SEM spectra) as one report with its figures, as Markdown or PDF. It states the date, the app version and the packages the app is built with.

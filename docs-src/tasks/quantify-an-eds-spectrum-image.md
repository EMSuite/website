---
title: Quantify an EDS spectrum image
nav: Quantify EDS
description: Quantify a TEM EDS spectrum image on a Mac: element maps, regions, and the composition in at% and wt% with uncertainties. An SEM one gives line intensities.
applies_to: 2.6
---

<p class="lede">Element maps and a composition from Velox and GMS TEM spectrum images; an SEM spectrum gives line intensities.</p>

1. Open the spectrum image with <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>). It opens in Spectroscopy › EDS with its maps and spectrum.
2. Pick the elements in the periodic table of the inspector. <span class="ui">Auto ID</span> proposes some; remove what cannot be in the sample. Draw a region on any map.
3. Click <span class="ui">Quantify</span>. For a TEM spectrum image the table gives at% and wt% with uncertainties (Cliff-Lorimer), and the maps can show wt% and at%. For an SEM file the table gives the net counts and says why it gives no composition.

!!! warning "A first estimate"
    An SEM spectrum or map (Bruker, EDAX or JEOL) gives the line intensities with their uncertainty and no wt% or at%, as exSpy does for SEM spectra: the thin-film k-factors do not hold for a bulk sample. The fit is checked against exSpy, but the compositions are not yet validated against standards. Check them against a standard measured under the same conditions before you report them.

[EDS](/docs/electron-microscopy-studio/reference/eds.html) lists every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

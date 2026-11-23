---
title: Quantify an EDS spectrum image
nav: Quantify EDS
description: Quantify a TEM or SEM EDS spectrum image on a Mac: element maps, regions, and the composition in at% and wt% with uncertainties.
applies_to: 2.1
---

<p class="lede">Element maps and a composition from Velox, GMS, Bruker, EDAX and JEOL EDS files.</p>

1. Open the spectrum image with <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>). It opens in Spectroscopy › EDS with its maps and spectrum.
2. Pick the elements in the periodic table of the inspector. <span class="ui">Auto ID</span> proposes some; remove what cannot be in the sample. Draw a region on any map.
3. Click <span class="ui">Quantify</span>. The table gives at% and wt% with uncertainties (Cliff-Lorimer), and the maps can show wt% and at%.

!!! warning "A first estimate"
    The fit is checked against exSpy, but the compositions are not yet validated against standards. Check them against a standard measured under the same conditions before you report them.

[EDS](/docs/electron-microscopy-studio/reference/eds.html) lists every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

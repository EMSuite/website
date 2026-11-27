---
title: Index EBSD patterns on a Mac
nav: Index EBSD patterns
description: Index EBSD and TKD patterns on a Mac by Hough or dictionary indexing, as kikuchipy does, and export the map as .ang or .ctf.
applies_to: 2.6
---

<p class="lede">From a pattern file to an orientation map, with the methods and settings of kikuchipy and pyEBSDindex.</p>

1. Open an h5ebsd pattern file with <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>). In EBSD › Patterns, set the processing and the detector geometry.
2. In EBSD › Indexing, add a phase from the presets or from a CIF, and choose <span class="ui">Hough</span>, or <span class="ui">Dictionary</span> with an EMsoft master pattern.
3. Click <span class="ui">Index</span>. Read the quality maps first, then the IPF map. Export the orientations as an EDAX `.ang` or an Oxford `.ctf` file.

A dictionary run can refine the orientations and the projection centre after indexing. [EBSD Indexing](/docs/electron-microscopy-studio/reference/ebsd-indexing.html) lists every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

---
title: Measure d-spacings from an HRTEM image
nav: Measure d-spacings
description: Measure lattice spacings from the FFT of an HRTEM image on a Mac: draw a region, find the spots, read each d-spacing.
applies_to: 2.6
---

<p class="lede">The Fourier transform of a lattice image has a pair of spots for each set of fringes. Electron Microscopy Studio measures each spot and gives its spacing.</p>

1. Open the image with <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>) and choose <span class="ui">FFT</span> under Imaging in the sidebar.
2. Drag a square region over the crystal. A window tapers its edges, so the edge of the region does not streak the transform.
3. Click <span class="ui">Find Spots</span>, or click a spot yourself. Each spot is listed with its d-spacing and its |q|; ⚠ marks a spot with another peak close by.

The spacing is in nm when the image is calibrated, and in pixels when it is not. A masked inverse shows where in the image the frequencies of chosen spots come from. [FFT](/docs/electron-microscopy-studio/reference/fft.html) lists every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

# Index a measured spot pattern against a CIF

Find the zone axis and orientation of a single-crystal electron diffraction pattern against a CIF or a Materials Project phase on a Mac.

Applies to Electron Microscopy Studio 2.6 and later.
<p class="lede">From a spot pattern to the crystal's zone axis and orientation, with the spots that explain it.</p>

1. Open the pattern with <span class="ui">Open…</span> (<kbd>⌘O</kbd>) and choose <span class="ui">Diffraction › Calibrate</span>. Check that <span class="ui">Calibration</span> shows a scale and the beam energy; calibrate on a ring of a standard if the file has no scale.
2. Choose <span class="ui">Index</span>. In <span class="ui">Phases</span>, click <span class="ui">Add Phase…</span>: search the Materials Project by elements or formula, or open your own CIF. Index waits until a phase is shown.
3. Click <span class="ui">Index</span> in the toolbar (<kbd>⌘R</kbd>). It finds the spots and the orientation. The header gives the zone axis, the tilt from it, how many spots it explains and the misfit. A tie or a half turn about the beam is stated, never hidden: step through them with <span class="ui">Solution</span> and <span class="ui">Flip 180°</span>.

Delete a false spot or click a missed one, then index again. [Diffraction](/docs/electron-microscopy-studio/reference/diffraction.html) lists every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

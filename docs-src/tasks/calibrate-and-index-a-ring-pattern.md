---
title: Calibrate and index a ring pattern
nav: Calibrate and index rings
description: Calibrate an electron diffraction pattern on a gold, aluminium or silicon ring, then index its rings and spots against your own phase.
applies_to: 2.6
---

<p class="lede">Take the scale from a ring of a standard, then read which reflections your rings and spots are.</p>

1. Open the pattern with <span class="ui">Open…</span> (<kbd>⌘O</kbd>) and choose <span class="ui">Diffraction › Calibrate</span>.
2. With the <span class="ui">Ring</span> tool, drag from the inner to the outer edge of a ring. Pick the <span class="ui">Standard</span> (Au, Al or Si) and the ring's family, then click <span class="ui">Calibrate on Ring</span>. The inspector gives the camera length and how far the fitted scale is from the file's.
3. Show the phase of your sample: in <span class="ui">Phases</span>, <span class="ui">Add Phase…</span> finds it on the Materials Project or opens your CIF. The standard sets the scale only; the rings and spots are indexed against the phases you show. Fit the rings and click the spots of your sample. Each is matched to a reflection within the <span class="ui">Tolerance</span>.

<span class="ui">Readout CSV…</span> writes the rings and spots. [Diffraction](/docs/electron-microscopy-studio/reference/diffraction.html) lists every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

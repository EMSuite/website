---
title: Simulate a diffraction pattern from a CIF
nav: Simulate a diffraction pattern
description: Simulate the electron diffraction spots of any crystal from a CIF or a Materials Project phase on a Mac, down any zone axis, with double diffraction.
applies_to: 2.6
---

<p class="lede">See which spots a crystal gives down a zone axis before you tilt to it, or over your own pattern.</p>

1. Choose <span class="ui">File › New Simulation</span>. In <span class="ui">Phases</span>, click <span class="ui">Add Phase…</span> and pick a Materials Project phase or open a CIF. Set the <span class="ui">Voltage</span> and the <span class="ui">Camera length</span> in <span class="ui">Microscope</span>.
2. Type a <span class="ui">Zone axis</span>, such as `110`, and an <span class="ui">In-plane rotation</span>, or drag the crystal or the pattern to tilt it.
3. In <span class="ui">Simulation</span>, switch on <span class="ui">hkl labels</span>, and <span class="ui">Double diffraction</span> for the spots a crystal forbids but two beams add. The <span class="ui">Excitation error</span> starts at 0.02 Å⁻¹, as py4DSTEM. <span class="ui">Intensities</span> picks kinematic or dynamical spots.

<span class="ui">Spots CSV…</span> writes the table and <span class="ui">Figure…</span> the picture. [Diffraction](/docs/electron-microscopy-studio/reference/diffraction.html) lists every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

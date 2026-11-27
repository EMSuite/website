---
title: Open DM3, DM4 and EMD files on a Mac
nav: Open DM3, DM4 and EMD files
description: Open DigitalMicrograph .dm3 and .dm4, Velox .emd and TIA .ser files natively on a Mac, with the pixel size read from the file.
applies_to: 2.6
---

<p class="lede">Electron Microscopy Studio opens the files TEM software writes, natively on Apple silicon, with the calibration the microscope stored.</p>

1. Choose <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>) and pick a DigitalMicrograph `.dm3` or `.dm4` file, a Velox `.emd` file, a TIA `.ser` file (with its `.emi`), a TIFF or an MRC file.
2. The image opens in the Imaging workspace. The <span class="ui">Calibration</span> section of the inspector shows the pixel size and the field of the file it came from. An image without one is marked "Not calibrated".
3. Measure with the <span class="ui">Distance</span>, <span class="ui">Angle</span> and <span class="ui">Profile</span> tools, or save the picture with <span class="ui">File › Export Image…</span> (<kbd>⇧⌘E</kbd>).

In the Finder, a `.dm3`, `.dm4`, `.mrc`, `.emd` or `.ser` file shows its image as its icon, and the space bar shows the image with its scale bar and the header of the file (Quick Look), without opening the app. The same command opens EDS and EELS spectrum images, SEM images and EBSD scans; each opens in its own workspace. [File formats](/docs/electron-microscopy-studio/data/formats.html) lists every format, and [Image](/docs/electron-microscopy-studio/reference/image.html) every control.

<p><a class="get-btn" href="https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg">Download Electron Microscopy Studio</a></p>
<p class="get-meta">Free. For Apple silicon Macs with macOS 26 or later. <a href="/docs/electron-microscopy-studio/install.html">How to install</a></p>

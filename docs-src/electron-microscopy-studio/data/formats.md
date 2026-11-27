---
title: File formats
description: The TEM and SEM file formats Electron Microscopy Studio opens: images, EDS and EELS spectrum images, EBSD patterns, orientation maps and paired files.
applies_to: 2.6
---

<p class="lede">Open the file the microscope wrote. What the file holds decides where it opens.</p>

Open a file with <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>) or from <span class="ui">File › Open Recent</span>. The same command opens every kind of file, not only images.

## What opens

| Kind of data | Formats | Opens in |
|---|---|---|
| TEM images | DigitalMicrograph `.dm3` and `.dm4`, Velox `.emd`, TIA `.ser` (with its `.emi`), TIFF, MRC | Imaging |
| Pictures | A pattern or image saved as PNG or JPEG (from a paper or a camera export); its scale is typed or fitted to a ring of a known phase | Imaging, or Diffraction for a pattern |
| SEM images | TIFF from Thermo Fisher (FEI), Zeiss and Tescan, read with the microscope's settings; JEOL `.img` and `.map` | Imaging |
| TEM spectrum images | EDS from Velox and GMS, EELS from GMS, TIA spectra and spectrum images, single `.msa` spectra | Spectroscopy |
| HyperSpy files | The images, EELS and EDS spectrum images and spectra of a `.hspy` file, each in its room | Imaging or Spectroscopy |
| SEM-EDS | Bruker `.bcf` and `.spx`; EDAX `.spd`, `.lsd` and `.spc`; JEOL `.pts`, `.eds` and `.asw`; an SEM spectrum in a HyperSpy `.hspy` file | Spectroscopy |
| EBSD and TKD patterns | h5ebsd from kikuchipy, Bruker, EDAX and Oxford Instruments (`.h5oina`); EDAX `.up1` and `.up2`; Oxford `.ebsp`; NORDIF `Pattern.dat` | EBSD › Patterns |
| Orientation maps | `.ang`, `.ctf`, Oxford `.h5oina` saved without patterns, `.h5` maps from orix, Bruker Esprit and EDAX OIM saved without patterns, EMsoft's dictionary indexing | EBSD › Maps |

A diffraction pattern is an image file; open it and go to the Diffraction workspace. A simulation document (`.emsim`) opens in Diffraction too, and a phase opens from a CIF file with <span class="ui">Add Phase…</span>.

In the Finder, a `.dm3`, `.dm4`, `.mrc`, `.emd` or `.ser` file shows its image as its icon, and the space bar shows the image with its scale bar and the header of the file (Quick Look). A `.ser` file shows its image without its `.emi`, but with no calibration then.

TKD patterns are read and indexed as EBSD patterns are. No TKD dataset has been checked in the app yet.

## Files that are read together

Some files are read together with a file of the same name beside them. Keep them in one folder:

| You open | The app also reads |
|---|---|
| EDAX `.spd` or `.lsd` | the `.spc` of the same name |
| EDAX `.up1` or `.up2` | the `.ang` of the same name |
| Oxford `.ebsp` | the `.ctf` of the same name |
| NORDIF `Pattern.dat` | `Setting.txt` and the background pattern in its folder |

For a NORDIF scan the app asks for the folder the first time, because macOS gives it only the file you picked. Choose the folder and click <span class="ui">Allow</span>; the app remembers it.

!!! warning "JEOL .asw projects"
    A JEOL `.asw` project names other files. The app is not given access to those yet, so a project may not open. Open the `.pts` or `.eds` file itself.

## Calibration from the file

The app reads the pixel size, and for SEM images the microscope's settings, from the file. The <span class="ui">Calibration</span> section of the Image inspector shows the pixel size and the field it came from. When the file carries none, the image is marked "Not calibrated" and lengths are given in pixels.

For an SEM image with a databar, <span class="ui">Settings › Images › Hide the SEM databar</span> crops the bar from the picture.

## When a file is not read

The app does not guess. A file it cannot read is listed with "Can't read" and the reason, or an alert says why it cannot be opened. [Troubleshooting](/docs/electron-microscopy-studio/troubleshooting.html#a-file-does-not-open) lists the usual cases.

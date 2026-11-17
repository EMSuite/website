---
title: Export
description: Exporting from 4DSTEM Studio: figures as PNG or PDF, results as data files that py4DSTEM reads, and EDS spectra, maps and tables.
applies_to: 5.4
---

<p class="lede">Figures for a paper, and the numbers behind them for further work.</p>

## Figures

| Command | Key | What you get |
|---|---|---|
| File › Export Result PNG… | <kbd>⇧⌘E</kbd> | The result on screen: the image or map with its colour scale and scale bar |
| File › Export Diffraction PNG… | <kbd>⌥⌘E</kbd> | The diffraction pattern on screen |

In the <span class="ui">Results</span> workspace, the <span class="ui">Figure</span> section of the inspector sets how a figure is written:

| Setting | Choices |
|---|---|
| Format | PNG, or PDF (vector) |
| Image size | A multiple of the data's own pixels |
| Detector outline | Draw the virtual detector on the pattern, or leave it off |
| Regions | Draw the scan regions, or leave them off |

The defaults for format and image size are in <span class="ui">Settings › General</span> under <span class="ui">Exported images</span>. <span class="ui">Show scale bar</span> is in <span class="ui">Settings › Appearance</span>.

## Data

In the <span class="ui">Results</span> workspace, the <span class="ui">Export</span> menu writes the numbers.

| Command | What you get |
|---|---|
| Export Data… | The result on screen as its own `.h5` file: the values exactly as computed, not the colours of the picture, with pixel size, units and how the result was made |
| Export Bundle… | Several results of the dataset together in one `.h5` file |

Both are EMD files that py4DSTEM reads, so an analysis can continue in Python.

A result that exists only as a colour image, such as a colour-coded orientation map, has no single number per pixel and is exported as a figure.

## EDS

With a spectrum image open, the File menu also has:

| Command | What you get |
|---|---|
| Export Spectrum CSV… | The spectrum on screen as a table |
| Export Maps… | The element maps as pictures |
| Export Results CSV… | The quantification table |
| Export Method JSON… | The settings the quantification used |
| Export Regions CSV… | The regions you pinned and their results |

## What every export carries

Each exported file names the method its result came from. Keep the dataset's [session file](/docs/4dstem-studio/data/sessions.html) with your exports: it holds the settings, so the figure in a paper can be made again.

---
title: EBSD Patterns
description: Reference for the Patterns part of the EBSD workspace in Electron Microscopy Studio: virtual images, the processing stages with kikuchipy's names, and the exports.
applies_to: 2.1
---

<p class="lede">Patterns browses the patterns of an EBSD or TKD scan, forms virtual images from them, and processes them before indexing. This page lists every control of the part, which is in the EBSD workspace.</p>

The part needs an h5ebsd pattern file. The processing follows kikuchipy; the names in brackets below are kikuchipy's, so a run can be redone in Python.

## Calibration

The detector values of the file: they are shown, not edited. The projection centre is in the Bruker convention, as kikuchipy stores it.

## Virtual images

| Control | What it does |
|---|---|
| Grid | <span class="ui">1</span> is the whole detector, the virtual BSE image. A larger number cuts the detector into that many tiles each way. |
| Map | The image the scan map draws: the mean, a tile, or the colour mix |
| Red, Green, Blue | The tile summed into each channel of the colour mix |
| Tiles | Shows the image of every tile in a pane under the map. A click makes it the map. |

In the colour mix each channel is normalised to its median and spread, then the three are rescaled together, as in kikuchipy.

## Processing

Each stage is a section with a switch. The pattern on screen shows the stages as they are set now; <span class="ui">Process</span> runs them over the whole scan. The stages that need the neighbouring patterns show only once Process has run.

| Stage | Controls | What it does |
|---|---|---|
| Static background | <span class="ui">Remove</span>, <span class="ui">Source</span>, <span class="ui">Operation</span>, <span class="ui">Scale</span> | Removes the shading of the detector, which is the same in every pattern (remove_static_background). When the file carries no static background, the mean pattern of the scan stands in. |
| Dynamic background | <span class="ui">Remove</span>, <span class="ui">Filter</span>, <span class="ui">Operation</span>, <span class="ui">Std</span>, <span class="ui">Truncate</span> | Removes the low-frequency intensity of each pattern, a Gaussian blur of it (remove_dynamic_background). An empty Std is kikuchipy's default, the pattern width divided by 8. |
| Average neighbours | <span class="ui">Average</span>, <span class="ui">Window</span> | Averages each pattern with its neighbours in the scan, weighted by the window (average_neighbour_patterns) |
| NLPAR | <span class="ui">Average</span>, <span class="ui">Radius</span>, λ | Averages each pattern with its similar neighbours (pyebsdindex NLPAR). The radius r searches (2 r + 1) × (2 r + 1) patterns. λ is chosen from the noise of the scan. |
| FFT filter | <span class="ui">Filter</span>, <span class="ui">Pass</span>, cutoffs and widths in pixels | Multiplies the spectrum of each pattern by a transfer function (fft_filter). Low-pass smooths the noise. |
| Intensity | <span class="ui">Intensity</span>, <span class="ui">Percentiles</span>, <span class="ui">Std</span>, <span class="ui">÷ √n</span>, <span class="ui">Equalise</span>, <span class="ui">Kernel</span>, <span class="ui">Clip limit</span> | Rescales each pattern to the full grey range (rescale_intensity), optionally between two percentiles, or normalises it. Equalise is the contrast-limited adaptive histogram equalisation (adaptive_histogram_equalization). |
| Size | <span class="ui">Bin</span> | Sums k × k pixels (downsample). The note below says the size of the processed patterns and the binning of the detector that follows. |

<span class="ui">Pattern</span>, in the Static background section, switches the pattern on screen between the file's own and the processed one.

!!! note "Indexing uses what you set here"
    The processing, the background and the geometry belong to Patterns. A change here makes the result in Indexing stale.

## Export

| Export | What it writes |
|---|---|
| The scan map | The map on screen as a PNG, one pixel per scan point |
| The pattern | The pattern on screen as a PNG, one pixel per detector pixel, with its colormap and contrast |
| The pattern with overlay | The pattern with the Kikuchi overlay as drawn: bands, edges, zone axes and labels |
| The overlay as CSV | The band lines (hkl, ends in detector pixels, θ) and the zone axes (uvw, position), for a figure made elsewhere |
| The header as JSON | The scan, pattern and detector header as the reader holds it |
| The processing | Every stage with its parameters in kikuchipy's names, to redo the run in Python |

## Method

Pattern processing as in kikuchipy 0.13.1; NLPAR as in pyEBSDindex (Brewick et al., Ultramicroscopy 200 (2019) 50). The functions and their tolerances are listed in the [parity notes](https://github.com/EMSuite/Electron-Microscopy-Studio/blob/main/docs/parity.md).

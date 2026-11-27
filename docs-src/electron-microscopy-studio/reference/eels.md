---
title: EELS
description: Reference for EELS in Electron Microscopy Studio: alignment, thickness, deconvolution, edges, fitting, references and the exports.
applies_to: 2.6
---

<p class="lede">EELS maps the thickness from the low loss and quantifies core-loss edges of an EELS spectrum image. This page lists every control of the part, which is in the Spectroscopy workspace.</p>

!!! warning "Not yet validated against reference data"
    The thickness and the edge fits are checked against exSpy, but they have not yet been validated against samples of known thickness or composition. Check them against a reference measured under the same conditions before you report them.

Open a file with <span class="ui">Open EELS Spectrum Image…</span>. <span class="ui">Run</span> does the stages in order: the thickness, the deconvolution if one is chosen, and the fit of the picked edges. What a file allows depends on what it holds: the thickness needs the low loss with its zero-loss peak, the edges need a core-loss spectrum image.

## Maps

| Control | Choices | What it does |
|---|---|---|
| Maps | <span class="ui">ZLP</span>, <span class="ui">t/λ</span>, <span class="ui">t</span>, <span class="ui">at%</span>, <span class="ui">wt%</span> | What the tiles show. A choice the file cannot give is off and says why. |
| Filter | | Smooths the t/λ, t, at% and wt% maps for display. It is on by default, and a filtered tile says so. Edge intensities and the ZLP shift are never filtered. |

The filter changes the picture only. The readout, the histogram, the results and every export use the raw values.

## Tools

The region tools are those of [EDS](/docs/electron-microscopy-studio/reference/eds.html#tools): Select, Rectangle, Ellipse, Polygon and Line.

## Edges

Click an element in the periodic table to quantify its edge. Right-click for the edge, or to switch it off. Each edge has a background window and a signal window on the spectrum; drag them there. <span class="ui">Reset Windows</span> puts every window back to its default, and a double-click on one window resets that edge alone.

## Processing

| Control | Choices | What it does |
|---|---|---|
| Align method | Maximum, then cross-correlation | How the zero-loss peak of each pixel is found |
| Signal from, Signal to | eV | Where <span class="ui">Align</span> searches for the zero-loss maximum, and the window of its cross-correlation (exSpy signal_range) |
| Crop | off, on | On: drops the channels a shift left undefined. Off: keeps every channel, extrapolated linearly at the ends. |
| Align | | Aligns the zero-loss peak across the map |
| Threshold | <span class="ui">Estimated</span>, <span class="ui">Fixed</span> with an energy | Where the zero-loss peak ends and the inelastic signal begins. Estimated uses one rule for the whole map. Noisy data want a fixed threshold. |
| Deconvolution | <span class="ui">Off</span>, <span class="ui">Fourier-log</span>, <span class="ui">Fourier-ratio</span>, <span class="ui">Richardson-Lucy</span> | See below |
| Iterations | | With Richardson-Lucy: the number of iterations, 15 by default. More iterations amplify the noise. |
| FWHM, Estimate | eV | With Fourier-ratio: the width of the zero-loss peak. Empty means estimated from the low loss of the first pixel. Type it when the estimate is refused. |
| Mean free path λ | <span class="ui">No λ</span>, <span class="ui">Typed λ</span>, <span class="ui">Estimate λ</span> | No λ gives t/λ only. A typed λ in nm gives t = λ · t/λ. The estimate is Iakoubovskii's λ from the beam energy, the convergence and collection angles and a density. |
| Density, Convergence, Collection | | The values the estimate of λ needs |

| Deconvolution | What it does |
|---|---|
| Off | The edge model fits the core loss as stored |
| Fourier-log | The low loss by its zero-loss peak: the single-scattering distribution. It is drawn dashed; the thickness and the fit do not use it. |
| Fourier-ratio | The core loss by the low loss. The edge model then fits the single-scattering core loss, not convolved with the low loss. |
| Richardson-Lucy | The low loss by its zero-loss peak as the point-spread function. It is drawn dashed; the thickness and the fit do not use it. |

A pixel where a step cannot be done is left without a value, and the inspector counts those pixels with the reason.

## Fitting

| Control | Choices | What it does |
|---|---|---|
| Model | <span class="ui">Exact NNLS</span>, <span class="ui">MLLS</span> | Exact NNLS fits each edge on its own windows: a power law on the background window, the intensity of the edge non-negative on the signal window. MLLS is one linear least-squares fit per pixel from the first background window to the end of the axis, with every edge at once. |
| Fit to | eV | With MLLS: the upper end of the fit. Empty means the end of the axis. |
| Background | <span class="ui">Power law</span>, <span class="ui">LCPL</span>, <span class="ui">Polynomial</span>, <span class="ui">Linear</span> | The background under the edges. A choice the model cannot take is off and says why. |
| Convolve low loss | off, on | Convolves the edge model with the low loss, to account for plural scattering. Off without a low loss, and with Fourier-ratio. |
| Beam energy, Convergence α, Collection β | keV, mrad | From the file, or typed. The line below says which is which. |
| Fit quality | | The residual sum of squares over the fitted channels, and Pearson's χ² |

## References

Reference spectra for the fit, listed with their source.

| Control | What it does |
|---|---|
| Edge | The edge whose signal window the reference covers |
| From Region | Takes the spectrum of the region over that window, less the background, as the reference |
| Import… | Reads a reference spectrum from an MSA file |
| Remove | Removes the selected reference |

## Export

| Button | What it writes |
|---|---|
| Results CSV… | The results table: the intensity of each edge with its 1σ, the areal density, at% and wt%, with the thickness line and the references of the methods |
| Method JSON… | What made the map and the fit, each method with its reference, and the SHA-256 of the record |
| Spectrum CSV…, Spectrum MSA… | The spectrum on screen: the low loss and the core loss, and the model where it is fitted |
| Regions CSV… | The pixels, the total intensity, t/λ and the intensities and at% of the edges for each kept region |
| Maps… | The colour mix and the maps as one PNG. <span class="ui">Scale bar</span> and <span class="ui">Regions</span> add the scale bar and the selected region. |
| Spectrum PDF…, Spectrum SVG…, Maps PDF…, Maps SVG… | The spectrum and the maps as vector figures for a paper: the spectrum as one path and every label as live text |
| Per-pixel CSV… | Every pixel: t/λ, its counting σ, the intensities, the zero-loss centre, the threshold, t, and the reason where there is no value |

The exports need the thickness map; the results need the edges fitted. The counts are as the file stores them: no gain or dark reference is applied.

## Method

Thickness by the log-ratio method: Malis, Cheng and Egerton, Journal of Electron Microscopy Technique 8 (1988) 193. Deconvolution after Egerton, Electron Energy-Loss Spectroscopy in the Electron Microscope, 3rd edition (2011), chapter 4. The edge model follows exSpy with its DFT GOS tables. The estimate of λ after Iakoubovskii et al., Microscopy Research and Technique 71 (2008) 626. The numbers are checked against exSpy; the app names the reference of each method in the inspector and in the Method JSON, and the functions and their tolerances are listed in SpectroKit's [parity notes](https://github.com/EMSuite/SpectroKit/blob/main/docs/parity.md).

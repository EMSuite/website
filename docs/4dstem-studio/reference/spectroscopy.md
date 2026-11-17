# Spectroscopy

Reference for the Spectroscopy workspace of 4DSTEM Studio: EDS maps, elements, regions, quantification, fitting and the exports.

Applies to 4DSTEM Studio 5.4 and later.
<p class="lede">Spectroscopy works on an EDS spectrum image, alone or beside the 4D scan of the same area. This page lists every control of its EDS tool.</p>

The workspace needs a spectrum image. Open one with <span class="ui">Open Spectrum Image…</span>. The window then shows the element maps, the spectrum of the selected region below them, and the results beside the spectrum. <span class="ui">Quantify</span> in the header fits the spectrum of the region.

## Maps

| Control | Choices | What it does |
|---|---|---|
| Maps | <span class="ui">Net</span>, <span class="ui">wt%</span>, <span class="ui">at%</span>, <span class="ui">Thickness</span> | What the tiles show: the net counts of each line window, the composition from the k-factors, or the mass thickness in kg/m² |
| Filter | <span class="ui">Off</span>, <span class="ui">3 × 3 average</span>, <span class="ui">Gaussian σ 1 px</span> | Smooths the wt%, at% and Thickness maps for display. It is on by default, and a filtered tile says so. Net maps are never filtered. |

The filter changes the picture only. The readout, the exports and the results use the raw values.

## Elements

Pick the elements in the periodic table of the inspector. <span class="ui">Auto ID</span> proposes elements from the spectrum of the region. Treat the proposal as a start: remove what cannot be in the sample, and add what you know is there.

## Tools

| Tool | What it does |
|---|---|
| Select | Click a region to select it, drag to move the view. <kbd>⌫</kbd> deletes the selected region, the arrow keys move it. |
| Rectangle | Drag a rectangle on any map to sum its pixels |
| Ellipse | Drag to draw the ellipse inside a rectangle |
| Polygon | Click the corners on any map; click the first corner to close the polygon |
| Line | Drag a line on any map: each map is plotted along it, in a small chart over the spectrum |

With a shape tool, <kbd>Return</kbd> draws the shape in the middle of the map.

With a 4D scan of the same area open, <span class="ui">Source</span> pools the spectrum over a phase or a diffraction group of the scan instead of <span class="ui">Drawn regions</span>.

## Quantification

| Control | Choices | What it does |
|---|---|---|
| Continuum | <span class="ui">Empirical</span>, <span class="ui">Polynomial</span> | The background under the peaks. Empirical fits a continuum over the whole spectrum with the step of the Al K edge. Polynomial is the whole-range polynomial of sixth order, as in exSpy. |
| k-factors | <span class="ui">Computed</span>, <span class="ui">Typed</span> | Computed uses k-factors from Bote-Salvat cross sections, the Krause yield and the EPQ detector efficiency. Typed uses the Cliff-Lorimer k-factors you give, with their source. <span class="ui">Edit k-factors…</span> opens them. |
| Maps method | <span class="ui">Cliff-Lorimer</span>, <span class="ui">Zeta factor</span>, <span class="ui">Cross section</span> | How the wt% and at% maps are quantified. The zeta factor and the cross section method need the dose and their factors: <span class="ui">Edit factors…</span>. The results table is always Cliff-Lorimer. |
| Beam energy | keV | Read from the file. Type it when the file does not state it. |
| Absorption | off, on | Corrects for absorption in the sample, weighted over the four detectors. It needs the thickness and the detector geometry of the file. |
| Thickness, Thickness ± | nm | The sample thickness for the absorption correction, and its uncertainty |
| Fit quality | | How well the last fit describes the spectrum |

When the absorption correction cannot be applied, the inspector says "Absorption not applied:" and the reason. The composition is then uncorrected.

## Fitting

| Control | Choices | What it does |
|---|---|---|
| Estimator | <span class="ui">Least squares</span>, <span class="ui">Poisson ML</span> | How the model is fitted to the counts |
| σ_k | % | The relative uncertainty of a computed k-factor. It is carried into the uncertainties of the composition. |
| Poly order | 0 to 8 | With the polynomial continuum: its order |
| Lock energy axis | off, on | On: the energy offset, gain and peak width are not refined on the pooled spectrum |
| Fit to | keV | The upper end of the fitted range. Empty means the default: the end of the axis or the beam energy, but at most 20 keV. |

## Results

The table beside the spectrum shows the net counts of the picked elements before <span class="ui">Quantify</span>, and the composition in at% and wt% after it, each with its uncertainty. The reference element is marked "ref.": its computed k-factor is 1 by definition, and the others are relative to it. A value marked "not a measurement" has a note that says why. The line under the table counts the notes of the fit and of Auto ID; read them before you use a number.

## Export

| Button | What it writes |
|---|---|
| Results CSV… | The results table: element, line, net counts, at% and wt%, with the record of the fit |
| Method JSON… | The quantification method, with its SHA-256 |
| Spectrum CSV…, Spectrum MSA… | The spectrum on screen as energy and counts, or as an EMSA/MAS file |
| Regions CSV… | The pixels, counts, net counts and composition of each kept region |
| Maps… | The maps as one PNG. <span class="ui">Scale bar</span> and <span class="ui">Regions</span> add the scale bar and the selected region. |
| Composition by Class… | With a 4D scan: every phase of the scan fitted with this method, one row per class, as CSV |

The results and the method need <span class="ui">Quantify</span> first. [Export](/docs/4dstem-studio/data/export.html) says what every export carries.

## Method

Cliff and Lorimer, Journal of Microscopy 103 (1975) 203, for the composition from intensity ratios. The fit follows exSpy, the reference the numbers are checked against; the functions and their tolerances are listed in SpectroKit's [parity notes](https://github.com/EMSuite/SpectroKit/blob/main/docs/parity.md).

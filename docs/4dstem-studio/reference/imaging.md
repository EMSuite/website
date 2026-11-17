# Imaging

Reference for the Imaging workspace of 4DSTEM Studio: virtual imaging with its detector shapes and presets, diffraction from a scan region, and diffraction groups.

Applies to 4DSTEM Studio 5.4 and later.
<p class="lede">Imaging turns the scan into pictures: a virtual image from a detector you draw, and the diffraction of a region you choose. This page lists every control of its two tasks.</p>

## Virtual imaging

| Control | What it does |
|---|---|
| Direction | What dragging on the panes controls. <span class="ui">Detector</span>: the virtual detector on the diffraction pane, which produces the image of the scan. <span class="ui">Region</span>: the scan region, which produces the diffraction pattern. |

### Detector → real space

| Control | What it does |
|---|---|
| Shape | The detector drawn on the diffraction pane: <span class="ui">Circle</span>, <span class="ui">Annulus</span>, <span class="ui">Rectangle</span> or <span class="ui">Point</span> (a single pixel) |
| Preset | <span class="ui">BF</span> (bright field), <span class="ui">ADF</span> and <span class="ui">HAADF</span> (annular dark field) set the detector in one click. <span class="ui">Custom</span> is shown once you change it. |
| Centre and radii | The detector's position and size in detector pixels. Type them, or drag the detector on the diffraction pane. |

The image of the scan updates while you drag. Each pixel of it is the signal that fell on the detector at that scan position.

The presets are fractions of the detector. Measure the beam in Prepare (<span class="ui">Calibrate Origin</span>) and they fit the beam instead.

### Region to diffraction

| Control | What it does |
|---|---|
| Shape | The scan region summed into the diffraction pattern: one position, a rectangle or a circle |
| Half-width or Radius | The size of the region in scan pixels |

With a single position, dragging on the image steps through the patterns. With a rectangle or a circle, the diffraction pane shows the summed pattern of the region and updates while you drag.

## Diffraction groups

This task sorts the scan positions into groups with similar diffraction patterns. It needs no calibration and no model of the sample, so it is a quick first look at what a scan contains.

| Control | Choices | What it does |
|---|---|---|
| Binned size | 8 × 8, 16 × 16, 32 × 32 | Each pattern is log-scaled, normalised and binned to this many pixels per side before grouping |
| Components | a number | The principal components kept from the binned patterns |
| Groups | a number | The number of groups (k-means on the principal components) |
| Group Patterns | | Runs the grouping over every scan position |
| Find similar to current position | | Shows how similar every pattern is to the one at the selected scan position, using the last grouping |

After a run the section reports:

- how much of the variance the first three components explain,
- the size of each group,
- the settings the result was computed with, including the seed, so the run can be repeated exactly.

"From an earlier run — the settings above have changed" means the map on screen no longer matches the settings. Run <span class="ui">Group Patterns</span> again.

!!! note "What the groups are"
    The groups are regions with similar patterns, not phases. Two orientations of one phase fall into different groups, and thickness changes can split one. Use the groups to choose where to look, then identify what is there in Bragg Disks and Crystal Maps.

## Method

Virtual imaging and the grouping follow py4DSTEM: Savitzky et al. (2021), Microsc. Microanal. 27, 712. The grouping is principal component analysis followed by k-means. The numbers are in the app's [parity notes](https://github.com/EMSuite/4DSTEM-Studio/blob/main/docs/parity.md).

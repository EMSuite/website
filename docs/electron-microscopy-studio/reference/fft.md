# FFT

Reference for the FFT part of the Imaging workspace in Electron Microscopy Studio: the region, the window, spots and d-spacings, the radial profile, the masked inverse and the HRTEM filters.

Applies to Electron Microscopy Studio 2.1 and later.
<p class="lede">FFT shows the Fourier transform of an image or of a region of it, measures its spots, and filters the image through a mask. This page lists every control of the part, which is in the Imaging workspace.</p>

## Region

| Control | What it does |
|---|---|
| Transformed | What is transformed: the whole image, or the region with its position and size |
| Use Centred Square | Sets the largest centred square as the region |
| Clear Region | Transforms the whole image again |
| Δq, or Δq (x) and Δq (y) | The frequency step between neighbouring bins of the transform |

Draw a region on the image to transform only that part.

## Before the transform

| Control | Choices | What it does |
|---|---|---|
| Window | | Tapers the edges of the region before the transform. A hard edge streaks the spectrum along both axes. |
| Smoothing | <span class="ui">None</span>, <span class="ui">Gaussian</span> with σ | Smooths the region first |
| Band-pass | <span class="ui">None</span>, <span class="ui">Difference of Gaussians</span>, <span class="ui">Butterworth high-pass</span>, <span class="ui">Butterworth low-pass</span> | Keeps a band of frequencies. <span class="ui">Low σ</span> or <span class="ui">Cutoff</span> sets it. |

The inspector sums the steps up in one line that starts "Before the transform:". The picture is drawn as log₁₀ of the power. The window changes the picture, never a number.

## Spots

Click a spot on the transform to measure it. The spot is listed in the inspector with its values.

| Control | What it does |
|---|---|
| Find Spots | Puts the strongest reflections on the transform, each measured as a click would be |
| Threshold, Distance, Most spots | The finder's settings: the level as a fraction of the range, the least distance between spots in bins, and the most spots it places |
| Measure at… | Measures at a position you type, <span class="ui">kx</span> and <span class="ui">ky</span> in bins |
| In Mask | Passes this spot in the masked inverse. Only a measured spot can be in the mask. |
| Remove, Remove All | Deletes one spot, or all |

A yellow ring is a measured spot, a blue one the selected spot, and a dashed one a spot that could not be measured. ⚠ marks a spot with another peak close by: its position is less certain.

## Radial Profile

The mean power against |q|. Point at the chart to read a bin.

## Masked Inverse

Appears once a spot is measured. The inverse transform through a mask around the spots marked <span class="ui">In Mask</span> shows where in the image those frequencies come from.

| Control | Unit | What it does |
|---|---|---|
| Radius | bins | The mask passes everything within this distance of the centre of a spot |
| Edge | bins | The mask falls to nothing over this distance beyond the radius |

## HRTEM Filters

A re-implementation of D. R. G. Mitchell's HRTEM filter script for Digital Micrograph (ABSF and Wiener). <span class="ui">Parameters</span> holds the settings, <span class="ui">Filter</span> runs it, and <span class="ui">Last run</span> says what the run did.

!!! warning "Filtered images are for looking, not for measuring"
    The app states the limits itself. A lattice that falls between two Fourier bins loses amplitude: on synthetic lattices it keeps 5 to 57 % in a 128 px region and 77 to 97 % at 256 px. Intensities are not preserved: the mean of the output is below that of the input.

## Display

<span class="ui">View</span> chooses what the image pane shows, for example the image itself or the masked inverse.

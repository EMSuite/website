---
title: Prepare
description: Reference for the Prepare workspace of 4DSTEM Studio: every calibration step and control, what it unlocks, the signals the app shows and how to read them.
applies_to: 5.4
---

<p class="lede">Prepare is where the dataset is calibrated. This page lists every control of its inspector under the name the app shows.</p>

## Calibration

The <span class="ui">Calibration</span> section lists five steps and the voltage. Each row shows its state (<span class="ui">Not set</span>, <span class="ui">From file</span>, <span class="ui">Measured</span>, <span class="ui">Manual</span>, <span class="ui">From session</span> or <span class="ui">Not quantitative</span>) and has the action that sets it.

| Step | What it unlocks | How it is set |
|---|---|---|
| Origin & probe | Descan-corrected DPC, Bragg vectors, strain and reconstruction | <span class="ui">Calibrate Origin</span>, or <span class="ui">Use Detector Centre as Origin</span> for a centre by hand |
| Ellipse distortion | Corrects detector distortion in Bragg, strain and orientation coordinates | <span class="ui">Fit Detector Ellipse</span> |
| R–Q rotation | Scan-frame DPC and iDPC, calibrated reconstruction geometry | <span class="ui">Measure R–Q Rotation</span> |
| Q pixel scale | Reciprocal units, physical orientation matching, quantitative phase | From the file, typed, or <span class="ui">Calibrate from Selected Material</span> |
| R pixel scale | Real-space axes, scale bars, quantitative reconstruction sampling | From the file or typed. It cannot be measured from the data: enter it from the acquisition parameters. |

<span class="ui">Voltage</span> is the accelerating voltage in kV. It is read from the file when the file carries it. Without it, mrad and Å⁻¹ cannot be converted.

Typing a value into a row replaces the one that was there; the row's state becomes <span class="ui">Manual</span>.

Under the rows the verdict reads "Quantitative — all 5 steps set", or "Quantitative in 3 of 5 steps" with what is still needed. Point at a row to read its detail and what it unlocks.

<span class="ui">Clear Calibration</span> returns every step to <span class="ui">Not set</span> without reloading the file. The voltage stays. Results computed against the old values are discarded or should be rerun; the confirmation says which.

## Fit diagnostics & advanced correction

This section is closed at first. It holds the choices behind the origin and what the fits reported.

| Control | What it does |
|---|---|
| Origin source | Where the origin comes from: a fit, the file, the session, or a centre set by hand |
| Origin fit | The surface fitted through the per-position origins: <span class="ui">Constant</span>, <span class="ui">Plane</span> (the default, as in py4DSTEM) or <span class="ui">Parabola</span> |
| Origin method | <span class="ui">Centre of mass</span> is the fast default. <span class="ui">Friedel</span> finds the beam through a beam stop by the pattern's own symmetry; it is slower and meant for data whose direct beam is hidden. |
| Calibrate Origin | Finds the beam centre at every scan position, fits the surface, and measures the probe radius |
| Origin from Bragg Peaks | Follows the direct beam among the detected Bragg disks instead of the centre of mass. For crystals whose strong disks pull the centre of mass off the beam. Needs <span class="ui">Detect All Disks</span> first. |
| Measure R–Q Rotation | Measures the rotation between the scan and the detector |
| Fit Distortion from Spots | Measures the detector's stretch on the matrix crystal's own spots, for a scan of one crystal that has no ring. Nothing changes until you click <span class="ui">Apply Distortion</span>. |
| Flip 180° | The rotation measurement cannot tell θ from θ + 180°. If iDPC contrast is inverted, flip it here. |
| Typed θ, Transposed, Apply Rotation | Enter the R–Q rotation by hand in py4DSTEM's convention (`QR_rotation` in degrees, `QR_flip`) |

What the fits report:

| Row | How to read it |
|---|---|
| Probe radius | The measured radius of the direct beam in detector pixels. Disk detection builds its kernel at this radius. |
| Fit residual | The RMS distance, in pixels, between the measured origins and the fitted surface. Small is good; a value over 1 px on a spot pattern brings the hint to use <span class="ui">Origin from Bragg Peaks</span>. |
| Positions used | The fit is robust: positions whose origin lies far from the surface are excluded and the surface is fitted again. "Nothing excluded" means there was no outlier tail, not that every position measured well. |
| Q shell check | The Q scale from a crystal assumes the innermost detected peak is the innermost allowed reflection. With two shells visible the app checks this; with one it cannot, and says so. |
| R–Q rotation | The measured or typed rotation, with ⊤ when the detector axes are transposed |
| Spot distortion | The stretch of the long over the short axis, its direction, and how far the detected spots are from the fitted ones |

## Ellipse correction

| Control | What it does |
|---|---|
| Fit annulus inner, Fit annulus outer | The radii, in detector pixels from the origin, between which the ring is fitted. Choose an annulus around a ring that is present in every pattern. |
| Fit Ellipse | Fits the ring in the annulus. The annulus must contain a ring with broad angular coverage. |
| Fit Anyway | Offered when the app refuses a fit because only a few of 36 sectors carry ring signal. Spots from a few grains fit an ellipse as well as a distorted detector does, so use it only if the annulus holds exactly one ring. The result is marked "Fit anyway". |
| Semi-axis a, Semi-axis b, θ, Apply Ellipse | Enter an ellipse by hand in py4DSTEM's convention: a is the longer semi-axis, θ the tilt of the a axis from qx in degrees. Only b/a and θ change the correction. |

The <span class="ui">Correction</span> row shows the ellipse in use. It is applied to calibrated Bragg maps, strain and orientation. <span class="ui">Residual</span> shows the fit's residual and how many of 36 sectors carried signal.

## A centre by hand

<span class="ui">Use Detector Centre as Origin</span> sets the origin to the centre of the virtual detector: put the detector on the direct beam first. <span class="ui">Origin x</span> and <span class="ui">Origin y</span> take the beam centre's column and row in pixels. <span class="ui">Restore Fitted Origin</span> brings back the fitted origin that the manual centre set aside.

## Method

The calibration follows py4DSTEM: Savitzky et al. (2021), *py4DSTEM: A Software Package for Four-Dimensional Scanning Transmission Electron Microscopy Data Analysis*, Microsc. Microanal. 27, 712. The app's results are checked against it; the numbers are in the app's [parity notes](https://github.com/EMSuite/4DSTEM-Studio/blob/main/docs/parity.md).

If a step is flagged, see [Troubleshooting](/docs/4dstem-studio/troubleshooting.html#the-calibration-says-not-quantitative).

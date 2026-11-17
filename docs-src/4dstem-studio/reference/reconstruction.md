---
title: Reconstruction
description: Reference for the Reconstruction workspace of 4DSTEM Studio: DPC and iDPC, parallax, and single-slice ptychography, with what each task needs.
applies_to: 5.4
---

<p class="lede">Reconstruction recovers phase from the 4D scan: DPC and iDPC, parallax, and single-slice ptychography. This page says what each task is and what it needs.</p>

!!! warning "Not yet checked on real data"
    The tasks of this workspace follow py4DSTEM. They have not yet been checked on real datasets the way the other workspaces have, and there are no tutorials for them. Treat a reconstruction as a first look, and compare it with py4DSTEM before you report it.

## The tasks

| Task | What it does |
|---|---|
| DPC & iDPC | Maps the deflection of the beam at each scan position and integrates it to the projected phase |
| Parallax | Aligns the bright-field images, fits the aberrations, corrects the phase and sections the depth |
| Single-slice ptychography | Reconstructs the object and the probe iteratively from the whole scan |

## What a task needs

The <span class="ui">Requirements</span> section at the top of the inspector lists what a task still needs. Missing values are rejected, not guessed.

| Task | Needs |
|---|---|
| DPC & iDPC | The origin calibrated in Prepare. The deflection in mrad needs the accelerating voltage and the Q pixel size. A meaningful iDPC and vector direction need the rotation between scan and detector. |
| Parallax | The calibration the Requirements section names. The task runs in stages, each unlocked by the one before: prepare the preview, align the bright-field stack, fit and correct the phase, then inspect or reconstruct the products. |
| Single-slice ptychography | The calibration the Requirements section names, and a defocus to start from |

## DPC & iDPC

<span class="ui">Display</span> chooses the picture. When the requirements for a quantitative result are not met, the inspector reads "Qualitative iDPC" with the reason, and the values are in relative units. <span class="ui">Open Prepare to Calibrate</span> takes you to the missing step.

## Parallax

| Stage | Button |
|---|---|
| 1 Prepare preview | <span class="ui">Prepare Parallax Preview</span> |
| 2 Align bright-field stack | <span class="ui">Align Next Level</span> runs the next step of the coarse-to-fine alignment. <span class="ui">Reset Alignment</span> discards the completed levels. |
| 3 Fit and correct phase | <span class="ui">Fit Aberrations</span>. The fit is a diagnosis: the calibration and the aligned data stay unchanged. |
| 4 Inspect or reconstruct products | The corrected images, and <span class="ui">Compute Depth Stack</span> for the depth sections |

<span class="ui">Run details</span> records what each stage did.

## Method

DPC and iDPC after Lazić, Bosch and Lazar, Ultramicroscopy 160 (2016) 265. Parallax and ptychography as implemented in py4DSTEM: Varnavides et al., arXiv:2309.05250.

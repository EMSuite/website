---
title: Strain
description: Reference for the Strain task in the Crystal Maps workspace of 4DSTEM Studio: the reference, the basis, the strain components and how to read the fit diagnostics.
applies_to: 5.4
---

<p class="lede">Strain measures how the lattice at each scan position differs from a reference lattice. This page lists every control of the task, which is in the Crystal Maps workspace.</p>

Strain works on the detected disks of the whole scan. Run <span class="ui">Detect All Disks</span> in Bragg Disks first, with the origin calibrated in Prepare.

## Settings

| Control | Choices | What it does |
|---|---|---|
| Reference | <span class="ui">Whole-scan mean</span>, <span class="ui">Current real-space ROI</span> | Defines zero strain. With the whole scan, strain is measured relative to the mean lattice. With the ROI, the region around the selected scan point is treated as unstrained. |
| Basis | <span class="ui">Automatic</span>, <span class="ui">Manual g₁ / g₂</span> | The pair of reciprocal lattice vectors every position is indexed against |
| g₁ x, g₁ y, g₂ x, g₂ y | pixels | With a manual basis: the two vectors as offsets from the origin, in calibrated detector pixels |
| Compute Strain Map | | Fits the lattice at every scan position and computes the strain against the reference |
| Component | ε_xx, ε_yy, ε_xy, θ (rotation), Fit residual, Indexed | The map shown |

Choose the reference with care. A region of the matrix far from any feature is the usual choice. The whole-scan mean suits a scan that is mostly unstrained matrix.

## The components

| Component | What it shows |
|---|---|
| ε_xx, ε_yy | The normal strain along the two axes of the frame (see below): positive where the lattice is stretched against the reference |
| ε_xy | The shear strain |
| θ (rotation) | The rotation of the lattice against the reference |
| Fit residual | How far the detected disks lie from the fitted lattice at each position. A map of where the fit can be trusted. |
| Indexed | The positions where a lattice could be fitted at all |

## Reading the diagnostics

| Row | How to read it |
|---|---|
| Basis consensus or Basis support | How well the reference's disks agree on the basis: consensus for an automatic basis, support for a manual one |
| Basis fit | The RMS distance in pixels between the reference's disks and the fitted basis, and the condition number κ of the basis. A large κ means g₁ and g₂ are nearly parallel: choose another pair. |
| Local fits | The share of positions that were indexed, and the median RMS of their fits in pixels |
| Reference inliers | How many of the reference's disks fit the basis |

## Warnings

| The app says | What to do |
|---|---|
| Too few peaks | Indexing needs the direct beam and two more reflections in a pattern. Lower the detection thresholds in Bragg Disks, not the reference. <span class="ui">Go to Bragg Disks</span> takes you there. |
| No single lattice fits the whole reference | The reference mixes regions with different lattices. Choose an unstrained region with <span class="ui">Use the current ROI as the reference</span>, move the region onto an unstrained area, or set g₁ and g₂ by hand. |
| Detection settings changed — rerun Detect All Disks before strain | The disks were made with other settings than those shown. Detect again. |

## The frame of the components

Under <span class="ui">Component</span> the app says which axes the components are along:

- "Scan frame (R–Q … applied)": the R–Q rotation is calibrated, so ε_xx and ε_yy are along the horizontal and vertical of the map.
- "Components along detector x/y — R–Q rotation not calibrated", in orange: the components are along the detector's axes, which need not be the map's. Measure the R–Q rotation in Prepare before you read directions from the map.

Strain uses the origin from Prepare. Calibrate it first, so that the disk positions are corrected for the beam's movement over the scan.

## Method

Strain mapping from Bragg disk positions as in py4DSTEM: Savitzky et al. (2021), Microsc. Microanal. 27, 712. The numbers are in the app's [parity notes](https://github.com/EMSuite/4DSTEM-Studio/blob/main/docs/parity.md).

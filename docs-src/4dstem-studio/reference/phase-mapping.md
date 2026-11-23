---
title: Phase mapping
description: Reference for phase mapping in 4DSTEM Studio's Crystal Maps: the phases, the matrix, the matching settings, and how to read the phase map and its evidence.
applies_to: 5.4
---

<p class="lede">Phase mapping decides, for each scan position, which of the phases you named explains its detected disks. This page lists every control of the task, which is in the Crystal Maps workspace.</p>

The task is made for a matrix with precipitates. One phase is the matrix. Its reflections are removed from every pattern, and the other phases are looked for in what is left. Where too little is left, the position is the matrix.

Phase mapping works on the detected disks of the whole scan and compares distances in Å⁻¹, so it needs the Q pixel size. Run <span class="ui">Detect All Disks</span> in Bragg Disks first. Weak precipitate reflections are easy to lose, so tune the detection on a pattern with a precipitate in it.

!!! warning "Not yet validated against reference data"
    Phase mapping has been compared only with published results on public aluminium-alloy datasets. It has not been validated against samples of known phase fractions or on other alloys. Treat the map and its fractions as a guide, and check them against patterns you can index by hand before you report them.

## Phases

| Control | What it does |
|---|---|
| Add Phase | Adds a phase from <span class="ui">Materials Project…</span> or <span class="ui">From CIF file…</span> |
| The row of a phase | Its name and colour, with a button to remove it |
| Matrix | Which of the phases is the matrix. The matrix is stated, not found. |
| Excitation slab | Per phase: how far from the Bragg condition its reflections still count as excited, in Å⁻¹. A thin plate or a needle needs more than a bulk crystal. Empty means the default. |
| Parallel to matrix | Per phase: the plane (hkl) or direction [uvw] of the phase that lies parallel to one of the matrix, as an orientation relationship is written. List each variant, for example (002) ∥ (200), (002) ∥ (020). Empty means any in-plane rotation. |

The phases are yours to name. The app does not guess them from the dataset.

## Matching

| Control | Unit | What it does |
|---|---|---|
| Max \|q\| | Å⁻¹ | The structures are searched out to this radius, or to the edge of the detector when that is nearer |
| Pair radius | Å⁻¹ | How close a detected disk must lie to a predicted reflection to count as that reflection |
| Matrix removal | Å⁻¹ | How close a detected disk must lie to a matrix reflection to be removed as matrix |
| Not indexed above | Å⁻¹ | A position whose best mean distance is above this is not indexed, rather than given a forced label. It is smaller than the pair radius. |
| Ignore peaks beyond | Å⁻¹ | Disks further out are left out of the match. 0 means the edge of the detector. Use it for a masked or cropped pattern, whose edge is a ring of maxima no phase explains. |
| On this detector | | The distances above in detector pixels, so you can see whether the detector resolves them |
| Scale to This Detector | | Appears with a warning when the distances are too fine or too coarse for the detector, and scales them |
| Map Phases | | Runs the match over the whole scan |

!!! note "Settings belong to a dataset"
    The distances depend on the camera length, the binning and the precipitates. Settings that separate the phases on one dataset are not defaults for the next. Check the map against patterns you can read by hand.

## Typed zone axes

By default the orientations of every phase are found from its structure. <span class="ui">Advanced › Typed zone axes</span> switches to the older way, where each phase is matched at a zone axis you type, against a reference library. These controls appear with it.

| Control | What it does |
|---|---|
| Zone axis | Per phase: the axis the phase is viewed along |
| Find Matrix Zone Axis | Measures which axis the matrix is viewed along and lists the candidates, best first |
| Orientations | The size of the reference library. It turns orange when the library is larger than the app allows. |
| Max \|q\|, In-plane step | The radius the library reaches, in Å⁻¹, and the step of the in-plane rotation, in degrees |
| Advanced › Vectors per orientation | The most reflections kept per orientation. A library that holds every allowed reflection matches anything; the cap keeps a match informative. |
| Advanced › Min. intensity | Reflections weaker than this fraction of the strongest of an orientation are dropped |
| Advanced › Excitation slab | The default excitation slab of the library, in Å⁻¹ |
| Classifier | <span class="ui">Search</span> or <span class="ui">Known variants</span>. Known variants scores every remaining disk, and the residual cutoff alone decides. |
| Residual cutoff | A position whose best orientation leaves a larger mean distance between its disks and the predicted spots is not indexed |
| Direct matrix, max | A position with at most this many disks left after the matrix removal is the matrix |
| Specific reflections, min | A winner that matches fewer reflections the matrix does not also have falls back to the matrix. The default is 1; 0 turns the rule off. |

Each row of the zone axis list shows the axis, the share of the disks it explains and the mean distance in Å⁻¹. Symmetry-equivalent axes should tie exactly. A row marked "at chance" explains no more than random vectors would, and one marked "no better than a wrong axis" explains no more than a wrong axis does on this data. When no axis beats chance, or none stands out, the app says so: check the Q pixel size and the disk detection before you go on.

## Result

| Button | What it shows |
|---|---|
| Show Phase Map | Each position in the colour of its phase |
| Show Objects | The precipitates as separate objects |
| Show Match Distance | The mean distance between the disks and the predicted spots of the winning phase |
| Show Reliability | How far the phase of each position is ahead of the best other phase, from 0 to 100 |
| Show Orientation | The positions of one phase coloured by their orientation (IPF-Z); the other phases grey. <span class="ui">Orientation of</span> chooses the phase. |

| Row | What it says |
|---|---|
| Phase fractions | The share of the scan each phase takes |
| Matrix evidence | How much of the detected signal at the matrix positions the matrix itself accounts for, as a median. Near 100 % the matrix explains the pattern. Well below it, a position is matrix because nothing else fitted. There is no threshold: the number falls as the detection admits more noise. |
| Evidence | A diagnosis in words when the match is weakly supported |
| Reliable above | A position is drawn as its best phase when that phase is at least this far ahead of the next one; below it the position is not indexed. Moving it redraws the map and matches nothing again. |
| Chance match at max \|q\| | The share of random vectors the densest phase would match by chance. A match carries information only well above it. |
| Orientations, Matrix in-plane | The size of the library used and the fitted in-plane rotation of the matrix |

## Warnings

| The app says | What to do |
|---|---|
| "Detection settings changed — rerun Detect All Disks" | Run <span class="ui">Detect All Disks</span> again, then <span class="ui">Map Phases</span> |
| The map is from an earlier run and the settings have changed since | Run <span class="ui">Map Phases</span> again |
| "The Å⁻¹ scale is exploratory, not calibrated" | Every distance is only as good as the scale. Calibrate the Q pixel size in [Prepare](/docs/4dstem-studio/reference/prepare.html). |
| "The session keeps its picture, not the map behind it" | A reopened session shows the saved picture. Run <span class="ui">Map Phases</span> to work with the map. |

## Method

Vector matching of detected Bragg disks after removal of the matrix reflections, after Thronsen et al., Ultramicroscopy 255 (2024) 113861. The phase reliability follows Rauch and Dupuy, Archives of Metallurgy and Materials 50 (2005) 87. How the app compares with the paper on its public dataset is written down in the [parity notes](https://github.com/EMSuite/4DSTEM-Studio/blob/main/docs/parity.md).

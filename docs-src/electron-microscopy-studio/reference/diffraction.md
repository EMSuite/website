---
title: Diffraction
description: Reference for Diffraction in Electron Microscopy Studio: calibrate, index against your phases, simulate, tilt plan, powder and thickness.
applies_to: 2.6
---

<p class="lede">Diffraction measures one electron diffraction pattern and simulates what a crystal gives. Its parts sit under Diffraction in the workspace list: Calibrate, Index, Simulate, Tilt Plan, Powder and Thickness. This page lists every control, part by part.</p>

The pattern fills the centre. Index and Simulate show the crystal beside it, Tilt Plan the zone axes near the beam, Powder the powder pattern. The tables (the readout, the spots) are tabs of the bottom area. The verb of the part is in the toolbar: <span class="ui">Calibrate on Ring</span>, <span class="ui">Index</span>, <span class="ui">Simulate</span> or <span class="ui">Measure Thickness</span>.

Diffraction takes a pattern: a recorded file, or a Simulation document and its CBED pattern. A simulated HRTEM or STEM image is a real-space image: Diffraction says so and offers Image and FFT.

## Calibrate

### Tools

| Tool | What it does |
|---|---|
| Ring | Drag from the inner to the outer edge of a ring. The ring is fitted inside that annulus. Double-click to fit again. |
| Spot | Click a spot to measure it. With the keyboard: <kbd>⌥</kbd> and an arrow move the cursor, <kbd>Return</kbd> adds the spot. |

### Centre

| Control | What it does |
|---|---|
| Row, Column | The centre of the pattern in pixels |
| Use Ring's Centre | Takes the fitted centre of the selected ring as the centre of the pattern |

### Calibration

The scale of the pattern in Å⁻¹ per pixel comes from the file, from a ring of a standard, or from a value you type. The standard is for the scale only: it is never used as the phase of your pattern.

| Control | What it does |
|---|---|
| Scale | The scale in use and its source |
| Standard | The calibration standard the pattern is of: Au, Al or Si |
| Ring | The family of reflections the fitted ring belongs to, with its spacing in Å |
| Calibrate on Ring | Fits the ring in the annulus and takes Δq from its radius and the listed spacing of the family |
| Clear | Removes the ring calibration |
| L | The camera length that follows, in pixels, and in mm when the pixel pitch of the camera is known |
| Δq typed | A scale you type, in Å⁻¹ per pixel |
| Beam | The beam energy from the file. Type it when the file does not state it. |
| Camera, Pixel pitch | The camera, or its pixel pitch in mm, for the camera length in mm |

When both exist, the inspector says how far the fitted Δq is from the axis of the file, in percent. Check a large difference before you rely on either.

### Rings and Spots

| Control | What it does |
|---|---|
| Inner, Outer | The annulus a ring is fitted in, in pixels |
| Fit Ring | Fits a ring in the annulus |
| Remove, Remove All | Deletes the selected ring or spot, or all |

## Phases

The phases are the crystals your pattern is indexed against and simulated from. Nothing is assumed: until you show a phase, Index and the ring labels wait for one, as py4DSTEM, pyxem and CrysTBox ask you to name the crystal.

| Control | What it does |
|---|---|
| Add Phase… | Finds a phase on the Materials Project by elements or formula, or opens a CIF. The phase goes into My Phases, your library on this Mac. |
| Find Phases… | Ranks My Phases (your library, the standards, the crystals of the open patterns) and, if you search, Materials Project phases by how many of the measured rings or spots each explains. It says "explains", never "is". <span class="ui">Use Phase</span> shows the chosen one. |
| The switch of a phase | Shows the phase: Index, the labels and the simulation use the phases shown |
| Update from Library | Takes the library's copy of the phase. Index and the readout start again. |
| Save as CIF… | Saves the phase as a CIF, with its symmetry and where it came from |
| q max | How far out reflections are listed for indexing, in Å⁻¹ (no 2π) |
| Tolerance | How far a measured q may be from a listed one to count as that reflection, in percent of q |

The Materials Project search sends only what you typed, when you press Search. Without a network, open your own CIF files.

## Index

<span class="ui">Index</span> finds the spots of a spot pattern and the orientation of the shown phase that explains them: the zone axis, the in-plane rotation and, with <span class="ui">Fit scale</span>, the scale. The pattern's header gives the zone axis, the tilt from it, how many spots it explains and the misfit. A tie or a half turn about the beam is stated, never hidden.

| Control | What it does |
|---|---|
| Solution | Steps through the orientations Index cannot tell apart, at most five, the best first |
| Flip 180° | Turns the simulated spots 180° about the beam, the look-alike a centrosymmetric pattern cannot tell apart |
| Remove Spots | Removes every spot, found or clicked, and keeps the rings and their scale. Index then finds the spots again. |
| Fit scale | On: Index fits the scale within ±3 % of the room's. Off: it holds the room's scale. |
| Zone axis | The beam direction [u v w]. Type one, or drag the simulated pattern or the crystal to tilt and turn it. |
| In-plane rotation | The pattern's turn about the beam |

### Simulation over the pattern

| Control | What it does |
|---|---|
| Simulated spots | Draws the kinematical spot pattern of the shown phase at the orientation over the pattern |
| hkl labels | Labels the spots with their indices |
| Double diffraction | Also draws, as dashed rings, the spots a twice-diffracted beam adds where the crystal forbids a reflection, such as 002 in silicon down [1 1 0] |
| Excitation error | σ of the excitation envelope, 0.02 Å⁻¹ by default as py4DSTEM |
| Unit cell | Draws the edges of the unit cell in the crystal pane |

### Precipitate

Places a precipitate in the shown crystal and draws the spots of its variants over the pattern.

| Control | What it does |
|---|---|
| Precipitate | None, a phase of your library, a standard, or the crystal of another open pattern |
| First pair, Second pair | The orientation relationship, typed as a paper states it: a plane `(h k l)` or direction `[u v w]` of the precipitate parallel to one of the matrix, twice (as orix builds a relationship). The first pair is kept exact; the second fixes the turn about it. |
| Example | Fills in a relationship from the literature with its reference, such as β″ (Mg₅Si₆) in Al (Andersen et al. 1998). It warns when your matrix is not the paper's. |
| Variants | Draws the shown variants' spots as pink diamonds. Variants of one group give the same spots in this view. |
| Double diffraction | Also draws the spots a beam diffracted by the matrix and again by a variant adds |

## Simulate

<span class="ui">File › New Simulation</span> opens a Simulation document: a simulated pattern with the crystal beside it and no measured pattern under it. Choose its phase with <span class="ui">Add Phase…</span>.

| Section | Controls |
|---|---|
| Microscope | Voltage, the camera length, Cₛ, the focal and angular spread |
| Orientation | The zone axis and the in-plane rotation, as in Index. Drag the pattern or the crystal to tilt and turn it. |
| Simulation | Simulated spots, hkl labels, double diffraction, the excitation error, and <span class="ui">Intensities</span>: Kinematic (the |F|² of each reflection with the excitation envelope) or Dynamical (the multislice's beams at a thickness) |
| Specimen | The source of the atoms (the phase, or a model you open), the beam direction, the box and the thickness. <span class="ui">Show HRTEM Image</span> and <span class="ui">Show STEM Image</span> open each as its own tab, in Image. |
| HRTEM | Defocus (with <span class="ui">Scherzer</span>), thickness, field of view, objective aperture and the potential. <span class="ui">Defocus and Thickness Table…</span> shows a through-focus, through-thickness series; <span class="ui">Export abTEM Script…</span> writes the same run as an abTEM script. |
| Thermal Vibrations | Frozen phonons and their configurations, with the σ of each element |
| Beside Measured | Places a measured image beside the simulated one, or inset, at the measured scale |
| STEM | Probe semiangle, defocus, scan step and the detector (BF, ABF, ADF, HAADF or custom angles) |
| CBED | Beam semiangle (<span class="ui">Fit Discs</span> sets it so the discs just touch), the angular step, the thickness and the pattern edge. <span class="ui">Show CBED Pattern</span> opens the pattern in Diffraction, where <span class="ui">Simulate</span> runs it. |

The HRTEM, CBED and STEM images are multislice simulations, checked against abTEM. The image shows simulated data only and says so.

## Tilt Plan

The holder's tilts to the zone axes near the indexed orientation.

| Control | What it does |
|---|---|
| α now, β now | The stage tilts when the pattern was recorded |
| α limit, β limit | How far the holder tilts either way, 30° by default |
| Tilt axis, β sense | The α axis in the pattern and the sense of β. Find them with <span class="ui">Calibrate</span> from a second indexed pattern of the crystal at other tilts, 10° or more apart. |
| Zone axis | A zone axis near the beam, nearest first, with its angle and, once the axis is calibrated, the tilts that bring it on |

<span class="ui">Tilt List CSV…</span> writes the list.

## Powder

The powder pattern of the shown phases: electron rings against q at this pattern's beam energy, or an X-ray pattern against 2θ.

| Control | What it does |
|---|---|
| Pattern | Electron or X-ray |
| Radiation | The X-ray line, Cu Kα by default (pymatgen's list) |
| 2θ from, 2θ to, q max | The range drawn |
| Compare with | A second phase drawn beside: a phase of your library, a standard or another open crystal |
| Mark overlaps | Marks the peaks the phases share, and each phase's strongest peak that no other has |

## Thickness

<span class="ui">Measure Thickness</span> fits the two-beam intensity across a diffracted disc of a CBED pattern (Kelly et al. 1975). Tilt so one reflection is strong. <span class="ui">Use in Simulation</span> sets the Simulation document's specimen thickness to the result.

## Export

| Button | What it writes |
|---|---|
| Readout CSV… | The fitted rings and measured spots, with their q and d |
| Spots CSV… | The simulated spots |
| Tilt List CSV… | The zone axes near the beam, with the tilts to each |
| Powder CSV…, Powder XY… | The peak table, and the pattern as x, y |
| Figure… | The pattern with its marks, labels and scale bar, as PDF, SVG or PNG |

The display controls are those of [Image](/docs/electron-microscopy-studio/reference/image.html#display).

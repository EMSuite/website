# Diffraction

Reference for the Diffraction workspace of Electron Microscopy Studio: the centre, the calibration on a standard, rings and spots, the crystal and indexing.

Applies to Electron Microscopy Studio 2.1 and later.
<p class="lede">Diffraction measures a single diffraction pattern: its centre, its scale, the d-spacings of rings and spots, and which reflections of a crystal they are. This page lists every control of the workspace.</p>

## Tools

| Tool | What it does |
|---|---|
| Ring | Drag from the inner to the outer edge of a ring. The ring is fitted inside that annulus. |
| Spot | Click a spot |

## Centre

| Control | What it does |
|---|---|
| Row, Column | The centre of the pattern in pixels |
| Use Ring's Centre | Takes the fitted centre of the selected ring as the centre of the pattern |

## Calibration

The scale of the pattern in Å⁻¹ per pixel comes from the file, from a ring of a standard, or from a value you type.

| Control | What it does |
|---|---|
| Scale | The scale in use and its source |
| Standard | The standard the pattern is of: Au, Al or Si |
| Ring | The family of reflections the fitted ring belongs to, with its spacing in Å |
| Calibrate on Ring | Fits the ring in the annulus and takes Δq from its radius and the listed spacing of the family |
| Clear | Removes the ring calibration |
| L | The camera length that follows, in pixels, and in mm when the pixel pitch of the camera is known |
| Δq typed | A scale you type, in Å⁻¹ per pixel |
| Beam | The beam energy from the file. Type it when the file does not state it. |
| Camera, Pixel pitch | The camera, or its pixel pitch in mm, for the camera length in mm |

When both exist, the inspector says how far the fitted Δq is from the axis of the file, in percent. Check a large difference before you rely on either.

## Rings and Spots

| Control | What it does |
|---|---|
| Inner, Outer | The annulus a ring is fitted in, in pixels |
| Fit Ring | Fits a ring in the annulus |
| Remove, Remove All | Deletes the selected ring or spot, or all |

## Crystal

| Control | What it does |
|---|---|
| Crystal | The crystal the rings and spots are indexed against: a built-in one or a CIF |
| Open CIF… | Reads a crystal from a CIF file |
| k_max | How far out reflections are listed, in Å⁻¹ |
| Tolerance | How far a measured q may be from a listed one to count as that reflection, in percent of q |

## Display and export

The display controls are those of [Image](/docs/electron-microscopy-studio/reference/image.html#display). <span class="ui">Export Readout CSV…</span> writes the readout of the rings and spots as CSV.

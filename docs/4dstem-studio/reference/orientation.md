# Orientation

Reference for orientation mapping in 4DSTEM Studio's Crystal Maps: the area, the phase model, quality levels, the engine, the Q scale and the display modes.

Applies to 4DSTEM Studio 5.4 and later.
<p class="lede">Orientation matches the detected disks at each scan position against templates of one crystal and maps the orientation that fits best. This page lists every control of the task, which is in the Crystal Maps workspace.</p>

Orientation works on the detected disks of the whole scan. Run <span class="ui">Detect All Disks</span> in Bragg Disks first, and choose a phase model. When the detection settings change afterwards, the task asks you to run <span class="ui">Detect All Disks</span> again.

## Area

Start small. A preview takes seconds and shows whether the phase model and the Q scale fit before you map the whole scan.

| Control | What it does |
|---|---|
| Area | <span class="ui">Preview</span>, <span class="ui">Region</span> or <span class="ui">Full scan</span> |
| Center X, Center Y, Half-size | With a region: the square that is matched, in scan positions. The orange square on the image shows it. |
| Work, Expected | How many positions will be matched, and the time the app expects |
| Use Full Scan | Switches the area to the full scan |

| Area | What is matched | The button reads |
|---|---|---|
| Preview | At most 32 × 32 positions across the scan, shown as coarse blocks. A quick check of the whole field. | <span class="ui">Preview Orientation</span> |
| Region | The orange square, at full spatial resolution | <span class="ui">Map Selected Region</span> |
| Full scan | Every scan position | <span class="ui">Run Full Orientation Map</span> |

## Phase model

The phase model is the crystal the patterns are matched against. You choose it; the app never infers it from the name of the dataset.

| Control | What it does |
|---|---|
| Phase model | The crystal to match: one from the built-in library, one you imported, or a custom cell |
| Materials Project… | Imports a structure by its Materials Project id |
| Import CIF… | Imports a structure from a CIF file |
| Symmetry | The symmetry of the chosen model, for example cubic m-3m or hexagonal 6/mmm |
| Source | Where the model comes from: <span class="ui">Imported CIF</span>, <span class="ui">Materials Project</span> with its id, <span class="ui">Built-in library</span> or <span class="ui">Custom cell</span> |
| Element, Structure, a | With a custom cell: the element, the cubic structure and the lattice parameter in Å |

A custom cell is a cubic cell of one element. Every other phase needs a CIF file or a Materials Project structure.

## Quality

| Quality | Templates |
|---|---|
| Fast | 96 |
| Balanced | 200 |
| Best | 400 |

More templates sample the orientations more finely and take longer. A monoclinic phase uses four times the number, because its orientation zone is larger. More templates are not always more accurate: see the warning below.

!!! warning "How accurate the orientations are"
    The accuracy was measured on simulated aluminium patterns at 200 templates. On most zone axes the result is exact to the spacing of the templates. It is up to 1.9° off on ⟨011⟩ and 13.6° off on ⟨122⟩. It was not measured for other phases, and more templates measured worse. Check an orientation you want to report against a pattern you can index by hand.

## Engine and Q scale

| Control | Choices | What it does |
|---|---|---|
| Engine | <span class="ui">Automatic</span>, <span class="ui">Accelerate CPU</span>, <span class="ui">Metal GPU</span> | Where the matching runs. Automatic uses the CPU engine, which is the one checked on real data. |
| Will use | | The engine the next run takes |
| Refine in-plane angle | off by default | Places the in-plane angle between the steps of the 128-step grid, at the top of a parabola through the best match. It runs on the CPU engine only. |
| Interpretation | <span class="ui">Physical</span>, <span class="ui">Exploratory</span> | Whether the result rests on a calibrated Q scale |
| Q scale, Provenance | | The scale in Å⁻¹ per pixel and where it comes from |
| Review Q Calibration in Prepare | | Opens Prepare at the Q pixel size |
| Exploratory scale | Å⁻¹ per pixel | A scale you type to try a match when the dataset has no calibrated one |

Template matching compares distances in reciprocal space, so it needs the Q pixel size. With a calibrated scale the result is <span class="ui">Physical</span>. With a typed scale it is <span class="ui">Exploratory</span>, and stays so: a typed scale can help you look at the match, but it is not a calibration. Calibrate the Q pixel size in [Prepare](/docs/4dstem-studio/reference/prepare.html) before you report orientations.

## Result

| Display | What it shows |
|---|---|
| IPF · Z | The crystal direction along the beam, coloured by the inverse pole figure key of the symmetry |
| Reliability | How clearly the best template wins over the others |
| Score | The match score of the best template |
| Symmetry FZ angle | The rotation angle of the orientation after it is reduced into the fundamental zone of the symmetry |
| In-plane angle | The rotation about the beam direction, relative to the matched template |
| Euler φ₁, Euler Φ, Euler φ₂ | The three Euler angles |
| Mirrored match | Where the pattern matched the mirror image of the template |

The in-plane angle of a mirrored match is measured from the mirror image, as in py4DSTEM. Angles on the two sides of a mirror boundary do not compare.

Read <span class="ui">Reliability</span> and <span class="ui">Score</span> before the colours. A position with a low score has few disks or disks the model does not explain. A position with low reliability has two templates that fit about equally well.

## Method

Automated crystal orientation mapping by template matching of Bragg disk positions, after Ophus et al., Microscopy and Microanalysis 28 (2022) 390, as implemented in py4DSTEM. The matching runs in DiffractoKit and is checked against py4DSTEM; the functions and their tolerances are listed in the kit's [parity notes](https://github.com/EMSuite/DiffractoKit/blob/main/docs/parity.md).

# EBSD Indexing

Reference for EBSD indexing in Electron Microscopy Studio: phases, Hough and dictionary indexing, refinement, comparing two results and the exports.

Applies to Electron Microscopy Studio 2.1 and later.
<p class="lede">Indexing finds the crystal orientation of every pattern of an EBSD or TKD scan, by Hough indexing or by dictionary indexing. This page lists every control of the part, which is in the EBSD workspace.</p>

The part needs an h5ebsd pattern file and at least one phase. The names in brackets are those of pyEBSDindex and kikuchipy.

## Calibration

The patterns the run uses, the projection centre and the pattern size. <span class="ui">Edit in Patterns</span> takes you to Patterns, where the processing and the geometry are set.

## Phases

| Control | What it does |
|---|---|
| The switch of a phase | Index against this phase |
| Edit | The phase whose reflector list and removal the controls below apply to |
| Reflectors | The reflector list of pyEBSDindex used for the phase |
| Preset, Add Preset | Adds a built-in phase |
| Add from CIF… | Adds the structure of a CIF. It needs the space group number. |
| Remove | Takes the phase out of the list. The file is unchanged. |

A phase of the file that states no space group or lattice is left out, and the inspector names it.

## Method

<span class="ui">Hough</span> detects the bands of each pattern and votes for an orientation. <span class="ui">Dictionary</span> compares every pattern with simulated patterns of a master pattern. Dictionary needs a master pattern. The section is marked "stale" when the settings no longer match the result.

## Hough

| Control | Name | What it does |
|---|---|---|
| Bands | nBands | The number of bands detected in each pattern |
| ρ mask | rhoMaskFrac | The fraction of the ρ range of the Radon transform at each edge where no band is taken |
| ρ bins, θ bins | nRho, nTheta | The bins of the Radon transform across the distance from the centre, and over 180° of band angle |
| ρ width, θ width | rSigma, tSigma | The width of the band-shaped kernel, in Radon bins |
| Tolerance | angTol | How far an interband angle may be from that of a reflector pair to vote for it, in degrees |
| Early exit | nband_earlyexit | A pattern stops voting once this many bands agree on one orientation |
| Reset Hough | | Back to the values of kikuchipy's tutorial |

Hough indexing runs on the CPU in double precision.

## Dictionary

| Control | What it does |
|---|---|
| Open Master Pattern… | Opens an EMsoft EBSD or TKD master pattern (`.h5`), as kikuchipy loads it |
| The master of a phase | The master pattern the dictionary of the phase is simulated from. Its space group must be that of the phase. |
| Resolution | The mean angle between neighbouring orientations of the dictionary, from 1° to 15° |
| Dictionary | The number of orientations sampled, one simulated pattern each |
| Metric | How a pattern and a simulated pattern are compared |
| Keep | The best matches kept per pattern (keep_n). The map shows the best. |
| Signal mask | None compares every pixel. The circular mask compares only the pixels inside the inscribed circle of the pattern. |
| Chunk | How many dictionary patterns are simulated and compared at once, as the memory allows |
| Reset Dictionary | Back to 4°, NCC, keep 5, no mask |

With more than one phase on, each phase has its own dictionary, and each point takes the phase whose best match scores highest.

## Refine

| Control | What it does |
|---|---|
| After indexing | Refines every indexed pattern against the master pattern after the dictionary run |
| Refine | What is refined: the orientation, the projection centre, or both |
| Angle trust, PC trust | How far the refinement may move the orientation, in degrees, and the projection centre |
| Solver | Nelder–Mead, as SciPy's, at kikuchipy's default tolerances |
| Mean score | The mean score over the refined points, as indexed and as refined |
| PC mean, PC std | The mean and the standard deviation of the refined projection centres |
| Reset Refine | Back to the trust region of kikuchipy's tutorial: orientation, ±2° and ±0.05 |

## The map

| Control | What it does |
|---|---|
| Map | What the map draws: IPF-Z, IPF-X, IPF-Y, Euler, Phase, Confidence index, Fit, Matched bands, Pattern quality, Score or OSM, as the method provides them |
| Detected bands | Draws the bands the Hough transform found on the pattern: matched ones solid green with their family, unmatched ones dashed orange |
| Compare | Shows two results side by side on one zoom, with the histogram of the disorientation between them |
| A, B | The two results: the last Hough or Dictionary run of the part, or the indexing the file holds |

Read the quality maps before the colours. A point with few matched bands or a low score has an orientation you should not rely on.

## Export

The map on screen as PNG; the result as a table with one row per point; the orientations as an EDAX `.ang` or an Oxford `.ctf` file; and every input of the run in the names of kikuchipy and orix, to redo it in Python. <span class="ui">Open in Maps</span> shows the run in [Maps](/docs/electron-microscopy-studio/reference/ebsd-maps.html) without a file.

## Method

Hough indexing: Krieger Lassen 1994 (Radon transform), Wright and Adams 1992 (triplet voting), Shuster and Oh 1981 (QUEST), Rowenhorst et al. 2024 (pyEBSDindex), as kikuchipy drives it. Dictionary indexing: Chen et al. 2015 and Jackson et al. 2019, with the master patterns of EMsoft (Callahan and De Graef 2013). Orientations and colours as in orix. The app shows the full references in the Info tab; the functions and their tolerances are listed in the [parity notes](https://github.com/EMSuite/Electron-Microscopy-Studio/blob/main/docs/parity.md).

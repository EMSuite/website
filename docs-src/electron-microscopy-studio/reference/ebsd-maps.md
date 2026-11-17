---
title: EBSD Maps
description: Reference for the Maps part of the EBSD workspace in Electron Microscopy Studio: the source, the map layers, phases, grains, texture and the exports.
applies_to: 2.1
---

<p class="lede">Maps shows an orientation map and what follows from it: phases, grains, misorientation and texture. This page lists every control of the part, which is in the EBSD workspace.</p>

Maps opens an `.ang` or `.ctf` map, an `.h5oina` file saved without patterns, an `.h5` file of orix, or an EBSD pattern file that carries a map. It also shows a run of [Indexing](/docs/electron-microscopy-studio/reference/ebsd-indexing.html).

## Maps

| Control | What it does |
|---|---|
| Source | Which result the map shows: a map file, the indexing the pattern file holds, or the run of the Indexing part |
| Map | What the map draws: the IPF colours along a sample axis, the phases, a property of the file, or a derived map |

| Derived map | Unit |
|---|---|
| KAM, the kernel average misorientation | ° |
| GOS, the grain orientation spread | ° |
| GND, the density of geometrically necessary dislocations | log₁₀ m⁻² |
| Grains | |
| Schmid factor | |

## Phases

The phases of the map with their colours. A phase without a known point group has no IPF colours: its points are black.

## Export

| Button | What it writes |
|---|---|
| Map PNG… | The map on screen as a figure: whole pixels per point, a scale bar, and the colour key or the phase legend beside it |
| Grains CSV… | The grain table: size, equivalent diameter, mean orientation, GOS, neighbours and the largest Schmid factor of each grain |
| Histogram CSV… | The distribution of the Histogram tab (KAM, GOS or grain size): the edges and the count of each bin |
| Texture PNG… | The pole figures, the IPF-Z density and the ODF sections of the texture phase as one figure, each with its colour bar |

## Method

Orientations, symmetry and IPF colours as in orix 0.15.0. The functions and their tolerances are listed in the [parity notes](https://github.com/EMSuite/Electron-Microscopy-Studio/blob/main/docs/parity.md).

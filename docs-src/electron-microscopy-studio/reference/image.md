---
title: Image
description: Reference for the Image part of the Imaging workspace in Electron Microscopy Studio: calibration, display, the measuring tools, particles and stacks.
applies_to: 2.6
---

<p class="lede">Image shows a TEM or SEM image with its calibration, and measures on it: distances, angles, line profiles and particles. This page lists every control of the part, which is in the Imaging workspace.</p>

## Calibration

| Row | What it says |
|---|---|
| Horizontal (x), Vertical (y) | The size of a pixel along each axis, with its unit |
| Source | Where the calibration comes from |

| The inspector says | What it means |
|---|---|
| "Not calibrated: the scale bar counts pixels." | The file carries no pixel size. Distances are in pixels. |
| "Pixels are not square: the scale bar uses x, and the image is drawn one pixel per pixel." | The two axes differ. Read distances along y with care. |

## Display

| Control | What it does |
|---|---|
| Colormap | The colours the values are drawn in |
| The histogram | The values of the image, with the contrast window that sets black and white |
| Gamma | Bends the grey scale between black and white, from 0.2 to 5 |
| Log | Draws log₁₀(1 + I). For a picture that spans decades, such as a diffraction pattern. |
| Show Scale Bar | Draws the scale bar on the image |

The display changes the picture only. Every measurement uses the values of the file.

## Measure

| Tool | What it does |
|---|---|
| Pan | Moves the view |
| Distance | Drag between two points: the length |
| Angle | Three points: the angle between the two legs |
| Profile | Drag a line: the values along it. <span class="ui">Width</span> sets how many pixels wide the line is; <span class="ui">Export Profile…</span> saves the profile as CSV. |

The marks are listed in the inspector. <span class="ui">Remove</span> deletes one, <span class="ui">Remove All</span> all of them. Every mark is also a row in [Results](/docs/electron-microscopy-studio/reference/results.html).

## Particles

Particles finds objects by a threshold and measures each one.

| Control | Choices | What it does |
|---|---|---|
| Objects | <span class="ui">Bright</span>, <span class="ui">Dark</span> | Whether the objects are brighter or darker than the background |
| Threshold | <span class="ui">Manual</span>, <span class="ui">Otsu</span> | A level you set, or Otsu's method |
| Level | | With a manual threshold: the level |
| Smoothing σ | pixels | Smooths the image with a Gaussian before the threshold |
| Connectivity | | Which neighbours of a pixel belong to the same object |
| Minimum area | | Objects smaller than this are left out |
| Tint mask | off, on | Tints the pixels on the object side of the threshold while you edit the settings |
| Region | <span class="ui">Draw Region</span>, <span class="ui">Whole Image</span> | Drag a rectangle: only its pixels are analysed, and an object cut by its border is an edge object |
| Show Objects, Hide | | Finds the objects and draws them, or hides them |
| Counted only | off, on | The table lists only the objects that are counted |

When the image is not calibrated, or its pixels are not square, the sizes are in pixels. After you change a setting the inspector reads "The settings changed since these objects were found: Show Objects again."

## Stack

For a file with several frames.

| Control | What it does |
|---|---|
| Frame | The frame on screen and how many there are |
| Previous, Next | Step through the frames |
| Same contrast for every frame | Pins the contrast window at the range of this frame, so a change of brightness between frames shows |

## Info

The Info tab lists the file, the object in it, the size in pixels, the voltage, both axes and the range of the values. <span class="ui">Acquisition</span> holds the microscope settings the file records, and <span class="ui">Lineage</span> the record of the steps saved with the image.

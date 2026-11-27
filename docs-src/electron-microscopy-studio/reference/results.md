---
title: Results
description: Reference for the Results workspace of Electron Microscopy Studio: the table of every measurement of a file, what each row records, and the export.
applies_to: 2.6
---

<p class="lede">Results lists every finished measurement of the open file in one table, whichever part made it. This page lists every control of the workspace.</p>

## Show

One switch per kind of result, each with its count.

| Kind | Made in |
|---|---|
| Marks | Image: distances, angles and profiles |
| FFT Spots | FFT |
| Calibration | Diffraction |
| Rings and spots | Diffraction |
| EDS composition | EDS |
| EELS thickness, EELS edges | EELS |

## A result

Select a row; the Info tab shows it.

| Row | What it says |
|---|---|
| Result | The name of the measurement |
| Value | The number with its unit |
| Source | Where on the image it was measured |
| Record | What was recorded with it |
| Method | How it was measured |

A result is removed in the part that made it; the Info tab names that part. Below the result, <span class="ui">Source Image</span> lists the file, the object, the size, both axes and any notes of the reader.

## Session and export

<span class="ui">Session</span> shows the session file the measurements are kept in, with <span class="ui">Show in Finder</span> and <span class="ui">Choose Session File…</span>; see [Sessions](/docs/electron-microscopy-studio/data/sessions.html). <span class="ui">All results as CSV…</span> exports every finished measurement of the file. It is dimmed while nothing is measured yet, or while a read is running.

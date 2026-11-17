---
title: Results
description: Reference for the Results workspace of 4DSTEM Studio: reviewing a result, saving it to the session, comparing two saved results and exporting.
applies_to: 5.4
---

<p class="lede">Results is where you review what the other workspaces made, keep it with the dataset, compare two results and export them. This page lists every control of the workspace.</p>

Until you have made an image, a map or a reconstruction, the workspace reads "No Results Yet".

## The result on screen

| Control | What it does |
|---|---|
| Save to Results | Keeps the result on screen with the dataset. It is there again when you reopen the dataset. |
| Export › Export Result PNG… | The picture as you see it |
| Export › Export Data… | The values as computed, as an `.h5` file |
| Export › Export Bundle… | Several results of the dataset in one `.h5` file |
| Quantifications | The numbers that belong to the result |

[Export](/docs/4dstem-studio/data/export.html) describes the files, and [Sessions](/docs/4dstem-studio/data/sessions.html) what is kept with the dataset.

## Saved products

The inspector lists the saved results of the dataset, each with its size, its unit and its sampling. Click one to show it.

| Control | What it does |
|---|---|
| Set as A, Set as B | Loads the result into the comparison |
| Remove | Removes the saved result from the session, after you confirm |

A session can also hold the settings a result was made with. To use them on a dataset, choose <span class="ui">Dataset › Apply Saved Controls</span>.

## Compare saved products

With A and B set, the workspace shows both side by side.

| Control | What it does |
|---|---|
| Same scale | Colours A and B with one range, from the lowest to the highest value in either. Without it each uses its own range, so the same colour can mean different values. |
| Zoom In, Zoom Out, Reset | Zoom all panels together. Drag to pan; double-click, or <span class="ui">Reset</span>, shows the whole image again. |
| Clear | Removes A and B from the comparison. The saved products stay in the session. |

When A and B match in kind, size, units, sampling and quantitative state, a third panel shows the difference A − B. When they do not, the workspace reads "Difference unavailable:" and the reason.

## Figure

| Control | What it does |
|---|---|
| Format | The file format of an exported figure |
| Image size | The scale of an exported image. A PDF is vector and has no pixels to scale. |
| Detector outline | Draws the virtual detector on an exported pattern |
| Regions | Draws the regions on an exported image |

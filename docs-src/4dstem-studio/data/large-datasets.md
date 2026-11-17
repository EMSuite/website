---
title: Large datasets
description: Opening large 4D-STEM datasets in 4DSTEM Studio: crop and binning before loading, memory, and where to keep the files.
applies_to: 5.4
---

<p class="lede">A 4D-STEM scan can be tens of gigabytes. Choose how much of it to load before it is loaded.</p>

## Open with Options

<span class="ui">Open with Options…</span>, on the welcome screen and in the File menu, shows the dataset before loading it: a preview, its sizes, and what your choice will cost in memory.

Under <span class="ui">Size</span> you see:

| Row | What it tells you |
|---|---|
| File on disk | The size of the file |
| Scan (Rx × Ry) | The number of scan positions |
| Detector (Qx × Qy) | The size of each diffraction pattern |
| Whole cube | The memory the whole dataset would take |
| This selection | The memory your crop and binning will take |

Then choose:

- **A crop.** Load only part of the scan. The source file is never changed.
- **Diffraction binning**, with <span class="ui">Bin factor</span>. Binning by 2 adds each 2 × 2 block of detector pixels into one.

Click <span class="ui">Load</span> when the selection fits.

!!! note "Crop or bin?"
    A crop of the detector limits the angular range. Binning keeps the range but makes disk positions coarser. With a bin factor of 2 the counts become 4 times larger and each reciprocal pixel 2 times coarser, so check any absolute threshold you set before.

To see these options every time, set <span class="ui">Settings › General › "Open Dataset…" does</span> to <span class="ui">Show options</span>.

## Memory

The app keeps the data at the bit depth it was stored in. A 16-bit scan takes half the memory of the same scan held as 32-bit numbers.

With <span class="ui">Keep in memory</span> on, the dataset is read into memory once and every analysis runs from there. With it off, analyses read the file in pieces as they go, which needs little memory and more time.

The app warns when a selection would take more than half of the Mac's memory. Other apps may slow down then; crop or bin instead.

## Where to keep the files

Work from a local disk. A dataset on a network share is read far more slowly every time an analysis goes through the whole scan.

For long runs, <span class="ui">Settings › General › Keep the Mac awake during long runs</span> stops the Mac from sleeping in the middle.

## Make a smaller copy

<span class="ui">File › Preprocess Raw Data…</span> writes a new `.h5` file from a raw dataset, with a crop of the scan, binning and a hot-pixel filter of your choice. The original stays as it is. Use it when you will come back to the same reduced dataset often.

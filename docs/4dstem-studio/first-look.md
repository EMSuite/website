# First look

See a first virtual image in 4DSTEM Studio within minutes, using the demo dataset that comes with the app.

Applies to 4DSTEM Studio 5.4 and later.
<p class="lede">From the welcome screen to a virtual image in a few minutes, with the demo dataset that comes with the app. No download needed.</p>

## Open the demo

1. Open 4DSTEM Studio. The welcome screen offers <span class="ui">Open Dataset…</span>, <span class="ui">Open with Options…</span> and <span class="ui">Try Demo Data</span>.
2. Click <span class="ui">Try Demo Data</span>.

The demo is a small synthetic 4D-STEM dataset. Every workspace works on it, and nothing on your disk is touched. When it is open, the status line reads "Demo ready — start in Prepare".

!!! note "What a 4D-STEM dataset is"
    At every position of the scan the detector records a whole diffraction pattern. So the data has four dimensions: two of the scan and two of the detector. The app always shows both sides: a diffraction pattern, and an image of the scan.

## Make a virtual image

A virtual image shows, for every scan position, how much signal fell on a chosen part of the detector.

1. Go to the <span class="ui">Imaging</span> workspace in the sidebar, or press <kbd>⌘2</kbd>. Its first task, <span class="ui">Virtual imaging</span>, is selected.
2. In the inspector on the right, set <span class="ui">Direction</span> to <span class="ui">Detector</span>. Dragging now moves the virtual detector.
3. Choose a <span class="ui">Preset</span>: <span class="ui">BF</span> (bright field), <span class="ui">ADF</span> (annular dark field) or <span class="ui">HAADF</span> (high-angle annular dark field).
4. Drag the detector on the diffraction pane, or type its centre and radii. The image of the scan updates while you drag.

Try the bright-field preset first, then an annular one, and watch how the contrast of the image changes: bright field collects the direct beam, the annular detectors collect what the sample scattered away from it.

## Look at the diffraction of a region

The other direction works too: choose a region of the scan and see its diffraction pattern.

1. Set <span class="ui">Direction</span> to <span class="ui">Region</span>.
2. Drag on the image of the scan. The diffraction pane shows the pattern there, or the summed pattern of the region you drag.

This is the quickest way to find out what is in a scan: look at the pattern in the matrix, on a feature, and in vacuum if there is any.

## Save the picture

Choose <span class="ui">File › Export Result PNG…</span> (<kbd>⇧⌘E</kbd>) for the image, or <span class="ui">Export Diffraction PNG…</span> (<kbd>⌥⌘E</kbd>) for the pattern.

## Next

- Open your own data with <span class="ui">Open Dataset…</span> (<kbd>⌘O</kbd>). For a large file, <span class="ui">Open with Options…</span> shows a preview first and lets you choose a crop or binning before loading.
- Work from a local disk. A dataset on a network share is read far more slowly every time an analysis goes through the whole scan.
- [The window](/docs/4dstem-studio/window.html) explains where everything is.

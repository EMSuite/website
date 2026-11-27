# First look

See a first measurement in Electron Microscopy Studio within minutes, using the demo data that comes with the app.

Applies to Electron Microscopy Studio 2.6 and later.
<p class="lede">From the welcome screen to a measured distance and a Fourier transform in a few minutes, with the demo data that comes with the app. No download needed.</p>

## Open a demo

1. Open Electron Microscopy Studio. The welcome window offers <span class="ui">Open Image…</span> and <span class="ui">Try Demo Data</span>, and lists your recent files and the tutorials.
2. Click <span class="ui">Try Demo Data</span> and choose <span class="ui">Lattice Image</span>.

The image opens in the Imaging workspace. The <span class="ui">Calibration</span> section of the inspector on the right shows the pixel size and where it came from.

## Measure a distance

1. Choose the <span class="ui">Distance</span> tool in the <span class="ui">Measure</span> section of the inspector, or press <kbd>⌃⌘2</kbd>.
2. Drag across the feature you want to measure, for example over ten lattice fringes.

The fringes of the demo image are 0.235 nm apart, so ten of them measure 2.35 nm. The measurement appears in the Measure section, in the unit of the image and in pixels. The <span class="ui">Angle</span> tool (<kbd>⌃⌘3</kbd>) and the <span class="ui">Profile</span> tool (<kbd>⌃⌘4</kbd>) work the same way; <span class="ui">Pan</span> (<kbd>⌃⌘1</kbd>) moves the picture again.

## Look at the Fourier transform

1. Under Imaging in the sidebar, choose <span class="ui">FFT</span>.
2. The window shows the image and its Fourier transform side by side. Drag on the image to draw a square region and transform only that part.
3. In the <span class="ui">Spots</span> section of the inspector, click <span class="ui">Find Spots</span>. The spots are ringed and listed.

A lattice image gives sharp spots in its transform, one pair for each set of fringes. The further out a spot lies, the finer the spacing it stands for.

## Save the picture

Choose <span class="ui">File › Export Image…</span> (<kbd>⇧⌘E</kbd>).

## Try the other demos

<span class="ui">Try Demo Data</span>, also under <span class="ui">Help › Open Demo Data</span>, has one document for every part of the app. Each opens where it belongs:

| Demo | Opens in |
|---|---|
| Lattice Image | Imaging › Image |
| SEM Image (generated) | Imaging › Image |
| Au Diffraction Pattern | Diffraction |
| Nanowire Spot Pattern (pyxem) | Diffraction |
| Silicon Simulation (CIF) | Diffraction |
| Ni EBSD Patterns (kikuchipy) | EBSD › Patterns |
| Duplex Steel Orientation Map (orix) | EBSD › Maps |
| EDX Spectrum Image | Spectroscopy › EDS |
| SEM-EDS Spectrum (BAM TM002) | Spectroscopy › EDS |
| EELS Spectrum Image | Spectroscopy › EELS |

The lattice image, the gold diffraction pattern, the SEM image and the two spectrum images are generated. The nickel patterns, the orientation map, the nanowire spot pattern and the SEM-EDS spectrum are public data; [Example data](/docs/data/) names their sources.

## Next

- Open your own file with <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>). The file decides where it opens: an image in Imaging, a spectrum image in Spectroscopy, an EBSD scan in EBSD.
- [The window](/docs/electron-microscopy-studio/window.html) explains where everything is.

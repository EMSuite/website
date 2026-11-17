# Bragg Disks

Reference for the Bragg Disks workspace of 4DSTEM Studio: the probe kernel, the detector, every disk detection setting with its default, and the counts the app reports.

Applies to 4DSTEM Studio 5.4 and later.
<p class="lede">Bragg Disks finds the diffraction disks in every pattern. This page lists every control of its inspector under the name the app shows.</p>

The detector correlates each pattern with a probe kernel and keeps the correlation peaks that pass the settings. The settings and their defaults are py4DSTEM's.

## Probe kernel

| Control | What it does |
|---|---|
| Source | Where the kernel comes from: <span class="ui">Synthetic</span> (a disk of the probe radius), <span class="ui">Current CBED / ROI</span> (the pattern on screen), <span class="ui">File's probe</span> (a probe stored in the file) or <span class="ui">Vacuum scan…</span> (a separate scan without a sample) |
| Probe radius | The radius the synthetic kernel is built at, in detector pixels. Empty until <span class="ui">Calibrate Origin</span> measures it. A typed value replaces the measured one. |
| Measured kernel mode | <span class="ui">Flat</span> uses the probe as it is: py4DSTEM's recommendation for bullseye and other structured probes, and it needs no radius. <span class="ui">Sigmoid trench</span> subtracts a disk whose edge falls smoothly to zero between the probe radius and twice it, so the kernel sums to zero, has a negative trench around the probe, and the correlation responds to the disk edge (py4DSTEM's `sigmoid` kernel). It is only as good as the probe radius. |
| Build Kernel | Builds the kernel from the chosen source |
| Kernel | The kernel in use: its source, its mode and its radius |

For a ring-shaped probe the app notes where the probe's outer edge is and offers a button to use that radius.

## Detector

| Control | What it does |
|---|---|
| Detector | <span class="ui">Classical</span> or <span class="ui">Neural net</span>. The neural net proposes candidate positions on the whole pattern; the classical refinement still measures every one. |
| Threshold | The pick threshold on the neural net's heatmap, 0.3 to 0.99. Lower accepts more candidates. |
| Model | The neural-net model in use: <span class="ui">Bundled</span>, or one you fine-tuned on your own labels. Each result records which model made it. |
| Compare Detectors | Shows a map of the peaks the two detectors do not share at each position. Available once <span class="ui">Detect All Disks</span> has run with each detector. |

The neural net is offered when <span class="ui">Settings › Analysis › Offer the learned (neural net) detector</span> is on.

## Disk detection

With a kernel built, the pattern on screen shows the detected disks as rings, and this section counts them:

| Row | How to read it |
|---|---|
| Current CBED | The number of disks found in the pattern on screen |
| Acceptance funnel | How many candidates there were and how many were accepted, then how many passed the absolute threshold, the relative threshold and the spacing rule. It shows which setting removes the disks you miss. |
| Peaks found | After <span class="ui">Detect All Disks</span>: the number of disks in the whole scan |
| Per pattern | The median and the range of disks per pattern over the scan |

<span class="ui">Detect All Disks</span>, the toolbar's action, runs the detection over the whole scan (<kbd>⌘R</kbd>).

## Advanced detection

Changes update the rings on the current pattern at once. Run <span class="ui">Detect All Disks</span> again to apply them to strain and orientation.

| Setting | Default | What it does |
|---|---|---|
| Maximum peaks | 70 | The most disks kept for each pattern |
| Pattern smoothing σ | 0 px | Gaussian smoothing of each pattern before the correlation. Too much merges nearby features. |
| Correlation smoothing σ | 2 px | Gaussian smoothing of the correlation map before its maxima are picked. Zero turns it off. |
| Minimum absolute | 0 | The weakest correlation peak kept, on the absolute correlation scale. It depends on the data and the kernel. Zero turns it off. |
| Minimum relative | 0.5 % | The weakest peak kept, as a fraction of the reference peak. Zero turns it off. |
| Reference peak | #1 | The peak the relative threshold is measured against, by brightness rank. #1 is the brightest. |
| Reference outside | 0 px | Measures the relative threshold against the brightest candidate at least this far from the brightest one, so that a saturated direct beam does not set the scale. For a flat plateau, set at least its diameter. 0 keeps py4DSTEM's rule. |
| Minimum spacing | 60 px | The smallest distance between two disks. When two candidates are closer, the brighter one is kept. Building a kernel sets it to fit the probe unless you chose a value. |
| Edge exclusion | 20 px | Drops maxima closer than this to the edge of the detector |
| Correlation power | 1 | 1 is cross-correlation (robust on noisy data), 0 is phase correlation (sharp, for patterned probes), values between mix both |
| Subpixel localization | Fourier multicorr | Pixel is fastest, parabolic is quick, Fourier multicorr refines for strain-grade positions |
| Fourier upsampling | 16× | The upsampling used by Fourier multicorr. Higher is finer and slower. |

<span class="ui">Reset Recommended Settings</span> puts every setting back to its default.

The defaults are scaled to the detector when a dataset opens, so a small detector starts with a smaller spacing and edge exclusion than the table shows.

## Training labels

This section is for fine-tuning the neural net on your own data.

| Control | What it does |
|---|---|
| Label centres on click | While on, a click on the diffraction pane adds a disk centre at the current scan position; a click near one removes it |
| This position, Labelled | How many centres are labelled here and in the whole scan |
| Clear This Position | Removes every centre at the current scan position |
| Save to Session | Writes the labels to the session file beside the dataset |
| Export Labels…, Import Labels… | Writes the labels to a JSON file, or replaces the current labels with those of a file |
| Split | About 30 % of the labelled positions are held out. They judge the fine-tuned model and never train it. |
| Train Model… | Fine-tunes the bundled model on the training positions and judges it against the active model on the held-out ones. It is offered only if it is at least as good on recall and precision and better on one. |

## Warnings

| The app says | What it means |
|---|---|
| Detection failed on this pattern | The detection itself failed here. The empty result is a failure, not a pattern without disks. |
| This pattern was truncated to the configured maximum peak count | More disks passed than <span class="ui">Maximum peaks</span> allows |
| The selected reference-peak rank is absent in this pattern | There are fewer peaks than the rank of <span class="ui">Reference peak</span>, so the relative threshold cannot be applied |
| Detection settings changed — rerun Detect All Disks | The disks of the whole scan were made with other settings than those shown |

## Method

Template matching as in py4DSTEM: Savitzky et al. (2021), Microsc. Microanal. 27, 712. Hybrid correlation: Pekin et al. (2017), Ultramicroscopy 176, 170. The numbers are in the app's [parity notes](https://github.com/EMSuite/4DSTEM-Studio/blob/main/docs/parity.md).

For how to judge a detection, see [Troubleshooting](/docs/4dstem-studio/troubleshooting.html#disk-detection-finds-too-few-or-too-many-disks).

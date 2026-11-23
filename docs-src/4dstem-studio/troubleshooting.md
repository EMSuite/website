---
title: Troubleshooting
description: Answers to common problems in 4DSTEM Studio: files that do not open, folder access, large datasets, calibration, disk detection, updates and the agent door.
applies_to: 5.4
---

<p class="lede">The app says what is wrong in its own words. This page lists those messages and what to do about each.</p>

## A file does not open

**The app refuses the file and names a reason.** The reader never guesses. The message says what it found and what it expected; [File formats](/docs/4dstem-studio/data/formats.html#when-a-file-is-refused) explains the usual ones.

**"Could not open …".** The file is missing, or macOS did not let the app read it. Check that the file is where you picked it, and open it again with <span class="ui">Open Dataset…</span> (<kbd>⌘O</kbd>).

**"Vendor data is truncated".** The file is shorter than its header says, which usually means a copy that did not finish. Copy the file again from the microscope computer.

**"… is no longer reachable: its disk was disconnected".** The dataset is on an external disk or a network share that went away. Reconnect it and reopen the dataset.

**"Dataset rank … is not supported".** The HDF5 dataset you chose is not a 4D-STEM scan. The app expects a dataset with three or four dimensions.

## The app asks for a folder

Merlin and EMPAD data, and session files, sit in more than one file. macOS may give the app only the file you picked. The app then shows an Open panel on the dataset's folder: click <span class="ui">Open</span> there. It asks once and remembers the folder.

If the dataset's folder cannot be written to, for example on a read-only share, use <span class="ui">Change Session File…</span> to keep the session somewhere else. See [Sessions](/docs/4dstem-studio/data/sessions.html).

## The dataset is large or the app is slow

**"More than half of this Mac's memory; other apps may slow down."** The selection you are about to load is large for this Mac. In <span class="ui">Open with Options…</span>, crop the scan or raise the <span class="ui">Bin factor</span> until <span class="ui">This selection</span> fits, or turn <span class="ui">Keep in memory</span> off.

**Keep in memory is dimmed.** The dataset would not fit; the caption under the switch says by how much. Crop or bin, or work from the file.

**Everything works but is slow.** With <span class="ui">Keep in memory</span> off, each analysis reads the file in pieces. A dataset on a network share or a slow external disk is read at that disk's speed: copy it to the internal disk. [Large datasets](/docs/4dstem-studio/data/large-datasets.html) has the details.

## The calibration says "Not quantitative"

The <span class="ui">Prepare</span> workspace lists each part of the calibration with its state: <span class="ui">Not set</span>, <span class="ui">From file</span>, <span class="ui">Measured</span>, <span class="ui">Manual</span>, <span class="ui">From session</span> or <span class="ui">Not quantitative</span>. The verdict underneath reads <span class="ui">Quantitative</span>, or "Not quantitative — still needed:" followed by the parts that are in the way.

| The verdict or the row says | What to do |
|---|---|
| A part is <span class="ui">Not set</span> | Measure it in Prepare, or type the value if you know it. The voltage and the pixel sizes come from the file when it carries them. |
| Origin: "Spot pattern" or "Centre of mass scattered" | The strong disks of a crystal pull the centre of mass off the beam. Run <span class="ui">Detect All Disks</span> in Bragg Disks, then <span class="ui">Origin from Bragg Peaks</span> in Prepare. Check afterwards that the Bragg vector map shows sharp spots. |
| Origin: "Beam stop over the direct beam" | Set the origin method to Friedel when the row suggests it; otherwise set the origin by hand. |
| Origin: "exceeds probe radius; recalibrate before quantitative use" | The fit moved further than the probe is wide. Run <span class="ui">Calibrate Origin</span> again after checking the probe radius. |
| Origin: "Window pull … (the window is mostly background…)" | The fit window holds little signal. The maps are fine for finding features; do not quote their numbers. |

!!! note "You can still work"
    A dataset that is not quantitative can still be imaged and mapped. The results are marked, and their numbers are in pixels. Use them to find features, and calibrate before you report values.

## Disk detection finds too few or too many disks

Tune on single patterns first: one on a feature and one in the matrix. Change one setting at a time and look at the circles on the pattern after each change.

| What you see | What to change |
|---|---|
| Circles on empty background | Raise <span class="ui">Minimum relative</span>. To find the noise floor, lower it until false disks appear on the background, then set it just above. |
| Weak disks are missing | Lower <span class="ui">Minimum relative</span>. If a saturated direct beam sets the scale, use <span class="ui">Reference outside</span> to measure against the brightest disk outside that radius. |
| Circles larger or smaller than the disks | The probe radius is wrong. Correct <span class="ui">Probe radius</span> and click <span class="ui">Build Kernel</span> again. |
| Neighbouring disks are lost in pairs | <span class="ui">Minimum spacing</span> is larger than the distance between the closest real disks. Lower it. |
| Disks at the detector edge are missing | <span class="ui">Edge exclusion</span> drops disks cut by the edge. That is expected. |
| "This pattern was truncated to the configured maximum peak count." | Raise <span class="ui">Maximum peaks</span>, or raise the threshold if the extra disks are noise. |
| Noisy data, unstable positions | Raise <span class="ui">Pattern smoothing σ</span> or <span class="ui">Correlation smoothing σ</span>, and keep <span class="ui">Correlation power</span> at 1. |

There is no single right value. The defaults are scaled to the detector, and the right threshold depends on the dynamic range of your data.

**"Detection settings changed — rerun Detect All Disks".** Strain, orientation and phase maps are built from the disks of the whole scan. After you change a detection setting, run <span class="ui">Detect All Disks</span> again before the next map.

## A step cannot run

When a step cannot run, the app names what is missing. The usual ones:

- **"Needs Detect All Disks first."** The step works on the detected disks. Run <span class="ui">Detect All Disks</span> in Bragg Disks.
- **"mrad needs accelerating voltage and Q pixel calibration."** Set both in Prepare.
- **"From an earlier run — the settings above have changed."** The result on screen no longer matches the settings. Run the step again.

## Updates

The app checks once a day whether a newer version exists. To check now, choose <span class="ui">Check for Updates…</span> in the app menu. To turn the daily check off, clear <span class="ui">Settings › General › Check for updates automatically</span>.

If an update does not install, download the current disk image from the [4DSTEM Studio page](/) and replace the app in Applications. Your settings, recent datasets and sessions stay.

## An agent cannot connect

1. Open <span class="ui">Settings › Agents</span> and turn on <span class="ui">Let agents on this Mac look at open windows</span>.
2. Read <span class="ui">Status</span>. "On (port 47811), no agent has asked yet" means the app is listening and the agent has not reached it. "Could not open:" is followed by the reason. The port in the status is the one the app uses; it takes another when 47811 is in use.
3. Click <span class="ui">Copy Connection Command</span> and paste it into Terminal once. The command holds the token; an agent set up with an older token is refused after <span class="ui">New Token</span>.

**The agent can look but not act.** Tools that change something need <span class="ui">Let agents run analyses</span>, which is off by default.

**The agent is on another computer.** The app answers only on the Mac it runs on. Run the agent on the same Mac.

## Something else

Write to [mail@mac4dstem.com](mailto:mail@mac4dstem.com) or open an issue on [GitHub](https://github.com/EMSuite/4DSTEM-Studio/issues). Say which version you use (<span class="ui">About 4DSTEM Studio</span> in the app menu), the file format, and the message the app showed. [Support](/support.html) has the contact details.

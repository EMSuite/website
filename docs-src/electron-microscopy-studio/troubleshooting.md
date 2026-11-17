---
title: Troubleshooting
description: Answers to the usual problems in Electron Microscopy Studio: files that cannot be read, folder access, a workspace or part that is dimmed, images without a scale, updates and the agent door.
applies_to: 2.1
---

<p class="lede">The app says what is wrong in its own words. This page lists those messages and what to do about each.</p>

## A file does not open

**"Can't read …" in the window.** The file is listed but its content could not be read. The sentence underneath gives the reason. If the file was on a disk or share that was away, reconnect it and click <span class="ui">Try Again</span>.

**An alert says the app can't open this file.** The file is not one of the formats the app reads, or it is damaged. The alert names what the reader found. A file that was cut short while copying has to be copied again from the microscope computer.

## The app asks for a folder

A NORDIF EBSD scan is read together with the `Setting.txt` and the background pattern beside it. macOS gives the app only the file you picked, so the app shows a panel on the scan's folder: choose that folder, or one around it, and click <span class="ui">Allow</span>. The app remembers the folder and does not ask again for scans inside it.

## A workspace or a part is dimmed

Each part of a workspace needs its own kind of data. A dimmed one says why when you point at it:

| The reason | What it means |
|---|---|
| No file open holds an image | Image, FFT and Diffraction work on an image. Open one. |
| No file open holds an EDS spectrum image | EDS needs a spectrum image with X-ray counts. |
| No file open holds an EELS spectrum image | EELS needs an energy-loss spectrum image. |
| No file open holds EBSD patterns | Patterns and Indexing need an EBSD pattern dataset. |
| No file open holds an orientation map | Maps needs an indexed map. |
| The open images belong to a spectrum image, not a diffraction pattern | The image is the survey image of a spectrum image. Diffraction needs a diffraction pattern. |

## The image has no scale

**"Not calibrated: the scale bar counts pixels."** The file carries no pixel size. Distances, profiles and particle sizes are then given in pixels. The <span class="ui">Calibration</span> section of the Image inspector shows what the file carries and where it came from.

**"Pixels are not square".** The file's two axes have different pixel sizes. The scale bar uses the horizontal axis.

**A diffraction pattern without a scale.** For the Diffraction workspace, record a standard under the same conditions, choose it under <span class="ui">Standard</span>, drag an annulus over one of its rings and click <span class="ui">Calibrate on Ring</span>.

## Updates

The app checks once a day whether a newer version exists. To check now, choose <span class="ui">Check for Updates…</span> in the app menu. To turn the daily check off, clear <span class="ui">Settings › Software Update › Check for updates automatically</span>.

If an update does not install, download the current disk image from the [Electron Microscopy Studio page](/mactem/) and replace the app in Applications. Your settings stay.

## An agent cannot connect

1. Open <span class="ui">Settings › Agents</span> and turn on <span class="ui">Let agents on this Mac look at open windows</span>.
2. Read <span class="ui">Status</span>. "On (port 47812), no agent has asked yet" means the app is listening and the agent has not reached it. "Could not open:" is followed by the reason.
3. Click <span class="ui">Copy Connection Command</span> and paste it into Terminal once. The command holds the token; an agent set up with an older token is refused after <span class="ui">New Token</span>.

**The agent can look but not act.** Tools that change something need <span class="ui">Let agents run analyses</span>, which is off by default.

**The agent is on another computer.** The app answers only on the Mac it runs on. Run the agent on the same Mac.

## Something else

Write to [mail@mac4dstem.com](mailto:mail@mac4dstem.com) or open an issue on [GitHub](https://github.com/EMSuite/Electron-Microscopy-Studio/issues). Say which version you use, the file format, and the message the app showed. [Support](/support.html) has the contact details.

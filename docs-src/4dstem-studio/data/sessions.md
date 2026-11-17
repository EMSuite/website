---
title: Sessions
description: How 4DSTEM Studio saves your work on a dataset in a session file beside it, what the Dataset menu does, and how results stay reproducible.
applies_to: 5.4
---

<p class="lede">Your work on a dataset is kept in a session file beside it. The dataset itself is never changed.</p>

## The session file

The session file sits in the same folder as the dataset and has its name with the ending `.mac4dstem.h5`. For `scan.dm4` it is `scan.mac4dstem.h5`.

When you open the dataset again, the app finds the session file and brings back what was saved in it. Move or copy the two files together.

## What you save

In the <span class="ui">Dataset</span> menu:

| Command | What it does |
|---|---|
| Save Current Result to Session | Keeps the result on screen with the dataset |
| Save Calibration to Session | Keeps the calibration, so the next open starts calibrated |
| Apply Saved Controls | Sets the controls back to the settings a saved result was made with. Shown when a saved result is selected. |
| Change Session File… | Uses a session file in another place, for example when the dataset's folder is read-only |
| Allow Access to Session File… | Gives the app permission for a session file macOS has not let it read |
| Ignore Session… | Opens the dataset again without its saved session, for this one time |

Saved results are listed in the <span class="ui">Results</span> workspace under <span class="ui">Saved products</span>. From there you can compare two of them side by side or remove one.

<span class="ui">Ignore Session…</span> asks before it acts: reopening replaces what is in the window, so results you computed and did not save are gone. The session file itself stays untouched.

## The record of how a result was made

Every step is written down as it runs.

- **Output**, in the bottom pane, is the log: each step with its settings, its numbers and any warning.
- **Lineage**, beside it, shows each result and the steps it came from. Turn on <span class="ui">Active path only</span> to see just the steps behind the result on screen.

Because the settings are saved with the result, a result can be made again: on the same dataset with <span class="ui">Apply Saved Controls</span>, and by anyone you send the dataset and its session file to.

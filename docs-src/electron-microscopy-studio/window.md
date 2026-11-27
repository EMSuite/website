---
title: The window
description: The parts of the Electron Microscopy Studio window: sidebar and workspaces, the picture, the inspector, the Output pane, the menus and their keyboard shortcuts.
applies_to: 2.6
---

<p class="lede">One window per file. The sidebar lists five workspaces, one for each kind of data.</p>

## Workspaces

The sidebar on the left lists the workspaces, top to bottom. Each has a shortcut. A workspace with more than one part lists its parts below it.

| Workspace | Key | Parts | What you do there |
|---|---|---|---|
| Imaging | <kbd>⌘1</kbd> | Image, FFT | TEM and SEM images and their Fourier transform |
| Diffraction | <kbd>⌘2</kbd> | | Calibration, d-spacings, indexing, phases, and simulation of spots, HRTEM, CBED and STEM images |
| EBSD | <kbd>⌘3</kbd> | Patterns, Indexing, Maps | EBSD and TKD: patterns, indexing and orientation maps |
| Spectroscopy | <kbd>⌘4</kbd> | EDS, EELS | EDS and EELS spectra and spectrum images |
| Results | <kbd>⌘5</kbd> | | Review and export the numbers |

The file decides what is available. A workspace or a part with no data for the open file is dimmed, and says why when you point at it; see [Troubleshooting](/docs/electron-microscopy-studio/troubleshooting.html#a-workspace-or-a-part-is-dimmed). Going back to a workspace returns to the part you left it in.

## The picture and the inspector

The middle of the window shows the data: the image, the pattern, the map or the spectrum. The inspector on the right holds the settings and the results of the part you are in. Show or hide it with <kbd>⌥⌘I</kbd>.

## Output

<span class="ui">Output</span>, below the picture, is the log: every step the app ran, with its numbers and any warning. Show or hide it with <kbd>⌃⌘L</kbd>. Read it after each step.

## Running a step

Most results update while you work. A step that goes through a whole scan, such as indexing, runs when you ask for it.

| Command | Key |
|---|---|
| Workspace › run the current step (the menu names it) | <kbd>⌘R</kbd> |
| Workspace › Stop | <kbd>⌘.</kbd> |

## More shortcuts

| Command | Key |
|---|---|
| File › New Window | <kbd>⌘N</kbd> |
| File › Open Image… | <kbd>⌘O</kbd> |
| File › Reopen Last Session | <kbd>⇧⌘O</kbd> |
| File › Close (the image, dataset, map or spectrum image shown) | <kbd>⌘W</kbd> |
| File › Close Window | <kbd>⇧⌘W</kbd> |
| File › New Simulation… | <kbd>⇧⌘N</kbd> |
| File › Save Simulation | <kbd>⌘S</kbd> |
| File › Export Image… (Export Figure… in Diffraction) | <kbd>⇧⌘E</kbd> |
| File › Export Transform… | <kbd>⌥⌘E</kbd> |
| File › Export Results… | <kbd>⌥⇧⌘E</kbd> |
| Image › Pan, Distance, Angle, Profile | <kbd>⌃⌘1</kbd> to <kbd>⌃⌘4</kbd> |
| Edit › Copy Figure (Diffraction) | <kbd>⇧⌘C</kbd> |
| Edit › Copy Methods Paragraph | <kbd>⌥⌘C</kbd> |
| Help › the documentation | <kbd>⌘?</kbd> |
| Show or hide the sidebar | <kbd>⌃⌘S</kbd> |

In the EDS part, <kbd>⌃⌘0</kbd> to <kbd>⌃⌘4</kbd> choose the region tools instead: select, rectangle, ellipse, polygon and line.

## Settings

<span class="ui">Settings…</span> in the app menu (<kbd>⌘,</kbd>) has four parts: Images, Agents, Materials Project and Software Update.

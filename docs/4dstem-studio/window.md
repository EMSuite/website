# The window

The parts of the 4DSTEM Studio window: sidebar and workspaces, the two image panes, the inspector, the bottom pane, the menus and their keyboard shortcuts.

Applies to 4DSTEM Studio 5.4 and later.
<p class="lede">One window per dataset. The sidebar lists the workspaces in the order an analysis usually takes.</p>

## Workspaces

The sidebar on the left lists the workspaces, top to bottom. Each has a shortcut.

| Workspace | Key | What you do there |
|---|---|---|
| Prepare | <kbd>⌘1</kbd> | Inspect and calibrate the dataset |
| Imaging | <kbd>⌘2</kbd> | Virtual images and diffraction groups |
| Bragg Disks | <kbd>⌘3</kbd> | Detect Bragg disks and label them |
| Crystal Maps | <kbd>⌘4</kbd> | Strain, orientation and phases from Bragg disks |
| Reconstruction | <kbd>⌘5</kbd> | DPC, parallax and ptychography |
| Spectroscopy | <kbd>⌘6</kbd> | EDS spectrum images, alone or with the 4D scan |
| Results | <kbd>⌘7</kbd> | Review, save and export |

A workspace with more than one task lists its tasks below it, for example <span class="ui">Strain</span>, <span class="ui">Orientation</span> and <span class="ui">Phase mapping</span> in Crystal Maps. <kbd>⌥⌘↓</kbd> and <kbd>⌥⌘↑</kbd> step through the tasks.

Spectroscopy needs a spectrum image; with a 4D scan alone it is not available.

## The panes

The middle of the window shows the data: a diffraction pattern, and the scan as an image or a map. What you drag on one changes what the other shows.

## The inspector

The inspector on the right holds the settings of the task you are in. Show or hide it with <kbd>⌥⌘I</kbd>.

## The bottom pane

Below the panes are <span class="ui">Output</span> and <span class="ui">Lineage</span>. Output is the log: every step the app ran, with its numbers and any warning. Lineage shows how each result was made, step by step. Show or hide the bottom pane with <kbd>⌃⌘L</kbd>.

Read Output after each step. When a step is flagged there, for example a calibration that is not good enough for quantitative results, deal with it before you build the next step on it.

## Running a task

Some results update while you drag, such as a virtual image. Others are computed over the whole scan when you ask for it.

| Command | Key |
|---|---|
| Analysis › Run Current Task | <kbd>⌘R</kbd> |
| Analysis › Cancel Analysis | <kbd>⌘.</kbd> |

## More shortcuts

| Command | Key |
|---|---|
| File › New Dataset Window | <kbd>⌘N</kbd> |
| File › Open Dataset… | <kbd>⌘O</kbd> |
| File › Reopen the last dataset | <kbd>⇧⌘O</kbd> |
| File › Export Result PNG… | <kbd>⇧⌘E</kbd> |
| File › Export Diffraction PNG… | <kbd>⌥⌘E</kbd> |
| Show or hide the sidebar | <kbd>⌃⌘S</kbd> |

## Settings

<span class="ui">Settings…</span> in the app menu (<kbd>⌘,</kbd>) has six parts: General, Appearance, Analysis, Materials Project, Agents and Advanced. The defaults follow py4DSTEM, so an analysis started here and one started in Python begin from the same values.

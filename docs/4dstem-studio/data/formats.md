# File formats

The 4D-STEM file formats 4DSTEM Studio opens, the companion files some of them need, and what the app says when it refuses a file.

Applies to 4DSTEM Studio 5.4 and later.
<p class="lede">What opens, what a format needs beside its main file, and what the app tells you when it refuses one.</p>

## What opens

| Format | Files | Notes |
|---|---|---|
| HDF5 | `.h5`, `.hdf5`, `.emd`, `.hspy` | py4DSTEM and EMD files, HyperSpy files, Velox `.emd` |
| Digital Micrograph | `.dm4`, `.dm3` | |
| Merlin | `.mib` with its `.hdr` | One file or a set of numbered files |
| EMPAD | `.xml` with its `.raw` | |

The app decides by the content of a file, not by its name alone: the extension picks the candidates and the first bytes confirm them.

Open a file with <span class="ui">Open Dataset…</span> (<kbd>⌘O</kbd>), by dropping it on the window, or from the recent datasets on the welcome screen.

## Formats with companion files

Two formats keep one dataset in more than one file:

- **Merlin**: the `.mib` data and a `.hdr` header with the scan size. You can pick either; picking the header opens its `.mib` files.
- **EMPAD**: the `.xml` description and the `.raw` data.

Keep the files of one dataset together in one folder.

macOS may give an app access only to the file you pick. When the app then needs a companion file with another name, it asks you for the folder, with an Open panel that already shows it. It asks once and remembers the folder.

## When a file is refused

The app never guesses. If it cannot open a file as a 4D dataset, it says why:

| The app says | What it means |
|---|---|
| "… is a TIFF image, not a 4D dataset." | TIFF and MRC images and stacks are not 4D-STEM data. Open them in Electron Microscopy Studio. |
| "… is a single spectrum: it opens in the Spectroscopy room, not as a 4D dataset." | A spectrum file (`.msa`) belongs to the Spectroscopy workspace. |
| "… is not a format the app opens (or its extension and its first bytes disagree)." | The format is unknown, or the file was renamed to an extension that does not match its content. |
| "… can't be read: … Open it with File › Open, which gives the app access to it." | macOS has not given the app permission for this file. Opening it through the Open panel grants it. |

A file that is damaged, or that an HDF5 library cannot read safely, is refused with a sentence as well, and the app stays open.

If a file from your microscope should open and does not, write to <a href="mailto:mail@mac4dstem.com">mail@mac4dstem.com</a> with the format, the instrument and the message the app showed.

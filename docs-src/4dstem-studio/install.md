---
title: Install 4DSTEM Studio
nav: Install
description: Install 4DSTEM Studio on an Apple silicon Mac: requirements, download, updating and removing the app.
applies_to: 5.4
---

<p class="lede">The app is free. It needs no Python, no other runtime and no account.</p>

## What you need

| | |
|---|---|
| Mac | Apple silicon |
| macOS | 26 or later |
| Download | About 20 MB. Your datasets are far larger: keep them on a local disk. |

On macOS 14 to 25, [version 3.0.0](https://github.com/EMSuite/4DSTEM-Studio/releases/tag/v3.0.0) still runs. These pages describe the current version.

## Install

1. [Download the disk image](https://github.com/EMSuite/4DSTEM-Studio/releases/latest/download/4DSTEM-Studio.dmg).
2. Open it and drag the app to your Applications folder.
3. Open the app from Applications. It is signed and notarized, so macOS opens it without a security warning.

The app starts with a welcome screen. [First look](/docs/4dstem-studio/first-look.html) takes it from there.

## Update

The app looks for a new version once a day and offers it when there is one. To look now, choose <span class="ui">Check for Updates…</span> in the app menu.

Looking for an update asks mac4dstem.com which version is current. Nothing else is sent; see [Privacy](/privacy.html).

## Remove

Drag the app from Applications to the Trash.

Your datasets are not touched. The app saves your work on a dataset in a session file beside it, named after the dataset and ending in `.mac4dstem.h5`. Keep these files if you want to pick the work up again later, or delete them with the app.

## If something goes wrong

See [Support](/support.html), or write to <a href="mailto:mail@mac4dstem.com">mail@mac4dstem.com</a>.

---
title: Electron Microscopy Studio for facilities and IT
nav: Facilities and IT
description: What Electron Microscopy Studio installs, touches and connects to, its licence and where to report a problem. For facility managers and IT staff.
applies_to: 2.1
---

<p class="lede">A free, signed and notarized Mac app. No account, no Python, no server. It reads the files you choose and sends nothing about them anywhere.</p>

## Install

| Path | How | Updates |
|---|---|---|
| Disk image | [Download the .dmg](https://github.com/EMSuite/Electron-Microscopy-Studio/releases/latest/download/Electron-Microscopy-Studio.dmg), drag the app to Applications | The app checks once a day; the check can be turned off in Settings |
| Mac App Store | Install from the store page | The App Store updates it |

Needs an Apple silicon Mac with macOS 26 or later, and about 36 MB. To remove it, drag the app to the Trash.

## What the app touches

- It runs in the macOS App Sandbox. It opens only the files and folders a person picks in an Open or Save panel.
- Next to an image it writes one session file, `<name>.mactem.h5`. Your data file is never changed.
- Settings and recent files are in the app's own container.
- It sends no analytics, no crash reports and no usage data.

## What it connects to

- **Update check** (disk image only): once a day it reads a small feed from mac4dstem.com, with no system profile. An update you accept is downloaded from GitHub.
- **Agent access**: off by default. When a person turns it on in Settings, the app listens on this Mac's loopback address only, and answers only requests that carry its token.
- **Release 2.3 adds one connection**: the phase search, which asks the Materials Project for crystal structures. It starts only when a person searches, and sends the search terms. Nothing else leaves the Mac.

## Licence and reports

GPL-3.0-only; the source is on [GitHub](https://github.com/EMSuite/Electron-Microscopy-Studio). Questions and bugs go to the [issue tracker](https://github.com/EMSuite/Electron-Microscopy-Studio/issues). Security problems go through the repository's private reporting (Security tab, then Report a vulnerability). Other questions: <a href="mailto:mail@mac4dstem.com">mail@mac4dstem.com</a>. See also [Privacy](/privacy.html).

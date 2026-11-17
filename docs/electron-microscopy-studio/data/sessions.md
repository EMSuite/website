# Sessions

How Electron Microscopy Studio keeps the measurements you draw on an image in a session file beside it, and how they come back.

Applies to Electron Microscopy Studio 2.1 and later.
<p class="lede">The distances, angles and profiles you draw on an image are kept in a session file beside the image. Your data file is never changed.</p>

## The session file

The session file sits in the same folder as the image and has its whole name with `.mactem.h5` added. For `scan.dm4` it is `scan.dm4.mactem.h5`.

## Save

In the Image part of Imaging, choose <span class="ui">File › Save to Session</span> (<kbd>⌘S</kbd>).

The first time, a save panel shows the session file's name in the image's folder. Click <span class="ui">Save</span> without changing the name or the folder: the app finds the file again by them. macOS needs this one click to let the app write beside your image. Later saves need no panel.

When you close an image with marks that are not saved, the app asks first.

## Open again

Open the image as usual. The marks from its session file come back with it.

If macOS did not give the app the session file, the image's row says "session file needs access". In the <span class="ui">Measure</span> section of the inspector, click <span class="ui">Choose Session File…</span> and pick it. <span class="ui">Show in Finder</span> there shows where the session file is.

## The last session

<span class="ui">File › Reopen Last Session</span> (<kbd>⇧⌘O</kbd>) opens the files you had open when you last quit, in the place you left. It is offered, never done at launch, so a large file is not loaded before you ask.

## Moving data

Move or copy the image and its `.mactem.h5` file together and keep their names. A session file belongs to the image it was saved for.

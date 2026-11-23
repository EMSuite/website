---
title: Measure WHAT on WHICH SAMPLE
nav: Short name for the sidebar
description: One sentence of 50 to 160 characters: what the reader measures, on which public dataset, in which app.
applies_to: 2.1
recipe: RECIPE-NAME
dataset: DATASET-KEY
---

<p class="lede">One sentence: the result the reader holds at the end, and why it matters.</p>

## What you will measure

Two or three sentences on the physical question and the number or map that answers it.

| You need | |
|---|---|
| The app | APP NAME APPLIES_TO or later ([install](/docs/APP/install.html)) |
| The data | [DATASET TITLE](https://doi.org/DOI), FORMAT, SIZE ([licence and citation](/docs/data/)) |
| Time | About N minutes |

## Steps

Every setting below is the recipe's. Where the dataset needs a value other than the app's default, the step says so and why: that is what you would have to learn on your own data.

### 1. Open the data

1. What to click: <span class="ui">Open Image…</span> (<kbd>⌘O</kbd>), which file.
2. What the app shows.

**Check before you go on:** the signal the app gives at this step (a calibration source, a count, a flag) and the value the recipe expects, with its tolerance. If it is flagged: what to do.

<figure>
  <picture>
    <source srcset="/assets/docs/APP/TUTORIAL/01-open.webp" type="image/webp">
    <img src="/assets/docs/APP/TUTORIAL/01-open.png" alt="What the picture shows, in one sentence" width="1600" height="1000" loading="lazy">
  </picture>
  <figcaption>What to look at in the picture.</figcaption>
</figure>

### 2. NEXT STEP

| Setting | Value | Why this value |
|---|---|---|
| <span class="ui">Control</span> | the recipe's value | one line |

**Check before you go on:** the app's signal (fit RMS, "not quantitative", counts) and what to do when it is flagged.

## Reading the result

What the result means physically, how good it is (the recipe's expected numbers with their tolerances), and the usual mistakes.

## Export

The figure and the data: which command, which file, and what is in it ([Export](/docs/APP/data/export.html)).

## The same analysis by an agent

The prompt to give an agent connected to the app, in a code block, and a link to the [agent guides](/docs/agents/).

```text
Open DATASET in APP and REPEAT THE TUTORIAL'S STEPS. Report the app's flags at each step.
```

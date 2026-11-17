# Example data

The public example datasets for 4DSTEM Studio and Electron Microscopy Studio, each with what it shows, its source, its licence and how to cite it.
<p class="lede">Data to learn the apps on. Every dataset here is public and is listed with its source, its licence and how to cite it.</p>

No data file is kept on this site. Each dataset is linked at the place where its authors published it, so you always get their current version and their own description.

## In the apps

Both apps carry demo data, so a first look needs no download.

| App | How to open it | What it is |
|---|---|---|
| 4DSTEM Studio | <span class="ui">Try Demo Data</span> on the welcome screen | A small synthetic 4D-STEM dataset on which every workspace works. See [First look](/docs/4dstem-studio/first-look.html). |
| Electron Microscopy Studio | <span class="ui">Try Demo Data</span> on the welcome screen | Generated examples, and four public files: the nickel EBSD patterns and their master pattern, a two-phase orientation map and an SEM-EDS spectrum (credits below). |

## For 4DSTEM Studio

| Dataset | What it shows | Format | Licence |
|---|---|---|---|
| [SrTiO3 along [100], high magnification](https://doi.org/10.5281/zenodo.5113449) | An atomic-resolution scan, 128 × 128 positions with 256 × 256 patterns, recorded at 300 kV on a probe-corrected FEI Titan 80-300 with a Merlin detector | Merlin (`.mib` and `.hdr`) | CC BY 4.0 |
| [BiFeO3–BaTiO3 films](https://doi.org/10.5281/zenodo.23890861) | Atomic-resolution scans of oxide films recorded on an EMPAD detector, published with ADF and iDPC images | EMPAD (`.raw` and `.xml`) | CC BY 4.0 |
| [Sheared β″ precipitates in Al-Mg-Si](https://doi.org/10.5281/zenodo.2652906) | Scanning precession electron diffraction of a peak-aged AA6060 alloy after compression: a matrix with small precipitates | HDF5 | CC BY 4.0 |
| [Precipitate phase mapping in aluminium alloys](https://doi.org/10.5281/zenodo.6645396) | Scanning precession electron diffraction of an Al-Cu-Li alloy with T1 and θ′ precipitates, 512 × 512 positions, with the authors' phase maps | See the record | CC BY 4.0 |

Cite them as:

- Strauch, A., Clausen, A., Weber, D. & Müller-Caspary, K. (2021). *High-resolution 4D STEM dataset of SrTiO3 along the [1 0 0] axis at high magnification*. Zenodo. doi:10.5281/zenodo.5113449
- Xu, M., Zhu, M., Kim, T., Wu, L., Spanier, J., Martin, L. & LeBeau, J. (2026). *Data for: Measuring the structure of defect clusters in (1-x)BiFeO3 - (x)BaTiO3 alloys with advanced electron microscopy and ptychography*. Zenodo. doi:10.5281/zenodo.23890861
- Christiansen, E., Marioara, C. D., Holmedal, B., Hopperstad, O. S. & Holmestad, R. (2019). *Data for "Nano-scale characterisation of sheared β″ precipitates in a deformed Al-Mg-Si alloy"*. Zenodo. doi:10.5281/zenodo.2652906. The paper: Sci. Rep. 9, doi:10.1038/s41598-019-53772-4
- Thronsen, E., Bergh, T., Thorsen, T. I., Christensen, E. F. & Frafjord, J. (2022). *Dataset for "Scanning precession electron diffraction data analysis approaches for phase mapping of precipitates in aluminium alloys"*. Zenodo. doi:10.5281/zenodo.6645396. The paper: Ultramicroscopy 255 (2024) 113861

## For Electron Microscopy Studio

| Dataset | What it shows | Format | Licence |
|---|---|---|---|
| [Nickel EBSD patterns with varying camera gain](https://doi.org/10.5281/zenodo.7497682) | EBSD patterns of recrystallised nickel, recorded at 20 kV with a NORDIF detector. A part of it is the app's nickel demo scan. | NORDIF (`Pattern.dat` and `Setting.txt`) | CC BY 4.0 |
| [EBSD map of shot-peened RR1000](https://doi.org/10.5281/zenodo.4730184) | An orientation map of a nickel superalloy, 0.45 µm step, recorded at 20 kV | Oxford `.ctf` | CC BY 4.0 |
| [Large SEM-BSE images of hydrated alite](https://doi.org/10.5281/zenodo.8210797) | Very large backscattered-electron images of cement pastes, recorded at 10 to 15 kV on a Helios G4 UX | See the record | CC BY 4.0 |
| [pyxem demo data](https://doi.org/10.5281/zenodo.14113591) | Among others a ring pattern of a polycrystalline gold cross-grating (`au_xgrating_20cm.tif`), a standard for calibrating diffraction patterns | TIFF and others | CC BY 4.0 |

Cite them as:

- Ånes, H. W., Hjelen, J., van Helvoort, A. T. J. & Marthinsen, K. (2019). *Electron backscatter patterns from Nickel acquired with varying camera gain*. Zenodo. doi:10.5281/zenodo.7497682
- Orozco-Caballero, A. & Quinta da Fonseca, J. (2021). *EBSD dataset for the HRDIC strain localization study in shot peened Ni superalloy*. Zenodo. doi:10.5281/zenodo.4730184
- Kleiner, F. (2023). *Large SEM-BSE images of hydrated alite of ages from 1 day up to 1 year*. Zenodo. doi:10.5281/zenodo.8210797
- Francis, C. (2024). *Pyxem 4D STEM Demo Data*. Zenodo. doi:10.5281/zenodo.14113591

The demo files in the app come from the nickel dataset above (Ånes et al., CC BY 4.0), the nickel master pattern of [kikuchipy](https://kikuchipy.org) (doi:10.5281/zenodo.7498645, CC BY 4.0), the data of [orix](https://orix.readthedocs.io) (the ferrite and austenite map, CC BY 4.0) and [exSpy](https://github.com/hyperspy/exspy) (the EDS spectrum of the BAM EDS-TM002 standard, GPL-3.0).

## Using a dataset

!!! note "Licence"
    CC BY 4.0 lets you use, share and adapt the data when you name its authors. Cite the dataset as above in anything you publish with it. The licence shown here was read from each record; the record itself is what counts.

Some of these files are large. Before you open a large 4D-STEM scan, read [Large datasets](/docs/4dstem-studio/data/large-datasets.html): crop or bin it with <span class="ui">Open with Options…</span> so that it fits your Mac.

More datasets are added as the tutorials are written. Each tutorial names the dataset it uses.

# Constrained optimized water suppression for 1H MRS of Metabolites and Macromolecules in 3 brain regions at 3T using sLASER

Contact: Kay Igwe, M.S. ([kci2104 [at] columbia [dot] edu](mailto:kci2104@columbia.edu))

## Overview

These data were collected as part of a study to test the efficacy of COWS, a new water suppression software package, for acquisition of both metabolite and macromolecule spectra. [COWS](https://doi.org/10.1002/mrm.30550) [sLASER](https://doi.org/10.1002/mrm.21302) localization.

Data types included are defaced *T*<sub>1</sub>-weighted 3D structural MRI images and single-voxel sLASER MRS data in the prefrontal cortex, posterior frontal lobe, and occipital lobe.

## Methods

### Participants

Ten healthy adults (5 women, 5 men, mean age = 31 ± 9 years).


Data from all 10 participants are available in this repository.

### Scanning

One 1-hr scan sessions for each participant with 2 T1 scans, one pre-MRS T1 scans used for voxel localization and a post-MRS T1 scan for measuring degreee of participant movement.

### MR protocol

MR data were acquired at Zuckerman Mind Brain Behavior Institute at Columbia University on a MAGNETOM Prisma 3 T (Siemens Healthineers, Erlangen, Germany) using a <sup>1</sup>H 32-reeive channel RF phased-array head and neck coil.

#### MRI

3D *T*<sub>1</sub>-weighted MPRAGE structural MRI acquisition parameters:

- MPRAGE
- TE/TR/TI = 2.26/2300/900 ms
- Flip angle = 8°
- Voxel resolution = 1 × 1 × 1 mm<sup>3</sup>
- FOV = 256 × 192 x 256 mm<sup>3</sup>
- Matrix size = 256 × 192 x 256
- Slices = 192


#### MRS

General acquisition parameters:

- Volumes of interest = prefrontal cortex, posterior frontal lobe, and occipital lobe
- Voxel resolution = 25 × 25 × 25 mm<sup>3</sup>
- Spectral width = 4000 Hz
- Number of points = 2048
- TE/TR = 26/2000 ms
- Number of transients (for Metabolite Scans) = 32
- Number of transients (for Macromolecule Scans) = 64
- Manual first-order B0 shimming using the Siemens Prisma VE11C native active shimming tool

MRS:

- Metabolite acquisition: Ace, Ala, Asc, Asp, Ch, Cr, GABA, Glc, Glu, Gln, Gly, GPC, GSH, Lac, mI, NAA, NAAG, PCr, PCh, PE, sI, and Tau
- Macromolecule ONLY acquisition
- Water reference acquisition
- Acquisition: sLASER
- COWS(7;236) water suppression: Water suppression scheme with 7 pulses that takes 236 ms to complete
- COWS(12;626) water suppression: Water suppression scheme with 12 pulses that takes 626 ms to complete
- VAPOR(12;626) water suppresion: Water suppression scheme with 7 pulses that takes 626 ms to complete


SPECTRA and MRI Per Participant

DAT FILE SPECTRA (RAW)
Each *.dat file contains both the spectrum and associated water reference

1. sub-\*_acq\*-01_svs_slaser_vapor7_metab_PFC.dat
2. sub-\*_acq\*-02_svs_slaser_vapor7_mm_PFC.dat
3. sub-\*_acq\*-03_svs_slaser_cows7_metab_PFC.dat
4. sub-\*_acq\*-04_svs_slaser_cows7_mm_PFC.dat
5. sub-\*_acq\*-05_svs_slaser_cows12_metab_PFC.dat
6. sub-\*_acq\*-06_svs_slaser_vapor7_metab_Occipital.dat
7. sub-\*_acq\*-07_svs_slaser_vapor7_mm_Occipital.dat
8. sub-\*_acq\*-08_svs_slaser_cows7_metab_Occipital.dat
9. sub-\*_acq\*-09_svs_slaser_cows7_mm_Occipital.dat
10. sub-\*_acq\*-10_svs_slaser_cows12_metab_Occipital.dat
11. sub-\*_acq\*-11_svs_slaser_vapor7_metab_Parietal.dat
12. sub-\*_acq\*-12_svs_slaser_vapor7_mm_Parietal.dat
13. sub-\*_acq\*-13_svs_slaser_cows7_metab_Parietal.dat
14. sub-\*_acq\*-14_svs_slaser_cows7_mm_Parietal.dat
15. sub-\*_acq\*-15_svs_slaser_cows12_metab_Parietal.dat


MAT FILE SPECTRA

Prefrontal Cortex
1. Metabolite Spectrum - using COWS(7;236) Water Suppression
2. Metabolite Water Scan - after COWS(7;236)
3. Macromolecule Spectrum - using COWS(7;236) Water Suppression
4. Macromolecule Water Scan - after COWS(7;236)
5. Metabolite Spectrum - using COWS(12;626) Water Suppression
6. Metabolite Water Scan - after COWS(12;626) Metabolite Scan
7. Metabolite Spectrum - using VAPOR(7;626) Water Suppression
8. Metabolite Water Scan - after VAPOR(7;626) Metabolite Scan
9. Macromolecule Spectrum - using VAPOR(7;626) Water Suppression
10. Macromolecule Water Scan - after VAPOR(7;626) Metabolite Scan

Posterior Frontal Lobe
1. Metabolite Spectrum - using COWS(7;236) water suppression
2. Metabolite Water Scan - after COWS(7;236)
3. Macromolecule Spectrum - using COWS(7;236) water suppression
4. Macromolecule Water Scan - after COWS(7;236)
5. Metabolite Spectrum - using COWS(12;626) water suppression
6. Metabolite Water Scan - after COWS(12;626) metabolite scan
7. Metabolite Spectrum - using VAPOR(7;626) water suppression
8. Metabolite Water Scan - after VAPOR(7;626) metabolite scan
9. Macromolecule Spectrum - using VAPOR(7;626) water suppression
10. Macromolecule Water Scan - after VAPOR(7;626) metabolite scan

Occipital Lobe
1. Metabolite Spectrum - using COWS(7;236) water suppression
2. Metabolite Water Scan - after COWS(7;236)
3. Macromolecule Spectrum - using COWS(7;236) water suppression
4. Macromolecule Water Scan - after COWS(7;236)
5. Metabolite Spectrum - using COWS(12;626) water suppression
6. Metabolite Water Scan - after COWS(12;626) metabolite scan
7. Metabolite Spectrum - using VAPOR(7;626) water suppression
8. Metabolite Water Scan - after VAPOR(7;626) metabolite scan
9. Macromolecule Spectrum - using VAPOR(7;626) water suppression
10. Macromolecule Water Scan - after VAPOR(7;626) metabolite scan


MRI FILES
Each T1w MPRAGE brain scan was brain extracted using HDBET (https://github.com/MIC-DKFZ/HD-BET).

Before MRS: This is the T1w MPRAGE scan for voxel placement
1. sub-\*/anat/sub-\*_T1w.nii.gz

After MRS: Second T1w MPRAGE scan performed within the same session for subject movement calculations after the MRS scans.
1. derivatives/mrs_mat/sub-\*_mat/sub-\*_T1w.nii.gz


SOFTWARE and FILE TYPES Included
1. COWS (Constrained optimized water suppression)
	- SOFTWARE: https://inventions.techventures.columbia.edu/technologies/cows-water--CU21111
	- Manuscript: Constrained optimized water suppression for <sub>1</sub>H MR spectroscopy https://doi.org/10.1002/mrm.30550
2. INSPECTOR Compatible -> .MAT
	- SOFTWARE: https://inventions.techventures.columbia.edu/technologies/inspector-magnetic--CU17130
	- Manuscript: INSPECTOR: free software for magnetic resonance spectroscopy data inspection, processing, simulation and analysis https://doi.org/10.1038/s41598-021-81193-9
3. TWIX File format -> .DAT


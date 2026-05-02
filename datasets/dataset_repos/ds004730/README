# Effects of propofol anesthesia on rates of cerebral protein synthesis (rCPS)

## Introduction

In this dataset all subjects (n=10) are males between the ages of 20 and 24 years (M=22.1, SD=1.6). See the `participants.tsv` file at the root of the dataset for full participant information. See [the reference below](#reference) for more information about this dataset.

Included in this dataset are L-[1-<sup>11</sup>C]Leucine 4D Positron Emission Tomography (PET) images, co-registered defaced 3D anatomical Magnetic Resonanace Imaging (MRI) T1-weighted images, blood sampling data, FreeSurfer derivative files, and FreeSurfer "fsaverage" group-averaged rCPS left and right hemisphere surface statistical maps. All data were collected on the NIH campus in Bethesda, Maryland, USA. For descriptions of data acquisition and processing methods, please see the methods sections of the published papers listed in the `dataset_description.json` file.

## Data Overview

This dataset contains both BIDS rawdata and BIDS derivatives. The rawdata is composed of:

1. `sub-*/ses-MRI/anat/*_T1w.{nii.gz,json}`: Defaced/anonymized anatomical MRI T1-weighted images
    - These T1-weighted images were converted to BIDS NIfTI using MATLAB's `niftiwrite` function, then co-registered to the rCPS derivative images, and then defaced with [FreeSurfer's MiDeFace](https://surfer.nmr.mgh.harvard.edu/fswiki/MiDeFace) to anonymize faces. All defaced images passed a visual inspection using [Dr. Pradeep Raamana's VisualQC](https://github.com/raamana/visualqc) to ensure that no identifiable facial features were present.
2. `sub-*/ses-{SESSION}/pet/*_pet.{nii.gz,json}`: PET data
    - The PET data are shared as-acquired after BIDS conversion. `{SESSION}` above is either `Awake` or `Propofol`.
3. `sub-*/ses-{SESSION}/pet/*_blood.{tsv,json}`: Blood sampling data
    - Blood samples were measured throughout the PET sessions. The timing and measurements are recorded in these files.

The derivatives dataset is composed of:

1. `derivatives/freesurfer/`: FreeSurfer recon-all derivative files
    - The FreeSurfer recon-all derivative files are commonly provided derivatives from FreeSurfer including (but not limited to) the white matter boundary and pial boundary surfaces, cortical thickness, and cortical parcellation.
2. `derivatives/rCPS/`: Originally computed rCPS statistical maps
    - Provided by the authors, these are the original statistical maps from the paper.
3. `derivatives/rcps-modified-petprep/sub-*/`: Modified "PETprep-matlab" (scripts made just for these data) derivative files. The code used to make these is [located here on Zenodo](https://doi.org/10.5281/zenodo.7768340).
    - The intermediary files used produced by [`rcps-modified-petprep`](https://doi.org/10.5281/zenodo.7768340) to calculate the group-averaged rCPS surface maps.
4. `derivatives/rcps-modified-petprep/group/`: Modified "PETprep-matlab" (scripts made just for these data) group-averaged statistical maps.
    - FreeSurfer "fsaverage" group-averaged rCPS left and right hemisphere surface maps, each with 163,842 vertices.

## Notes

1. The following datasets were prepared to the Brain Imaging Data Structure (BIDS) standard at the same time with the same filename and folder organizations due to their similarity:

    - [rCPS in subjects with fragile X syndrome](https://openneuro.org/datasets/ds004654)
    - [Effects of propofol anesthesia on rCPS](https://openneuro.org/datasets/ds004730)
    - [rCPS and memory formation during sleep](https://openneuro.org/datasets/ds004731)
    - [rCPS in stages of sleep](https://openneuro.org/datasets/ds004733)

2. There is currently no BIDS standard for rCPS statistical maps. As such, their naming was inspired by [a currently unnumbered BIDS Extension Proposal, linked here](https://docs.google.com/document/d/1KHzp-yk8KXvkUIhtN71WU0m4P4kKT9C1yvI-i9_kNeY/edit?usp=sharing).

## Reference

*Bishu, S., Schmidt, K. C., Burlin, T. V., Charming, M. A., Horowitz, L., Huang, T., Liu, Z., Qin, M., Vuong, B.-K., Unterman, A. J., Xia, Z., Zametkin, A., Herscovitch, P., Quezado, Z., & Smith, C. B. (2009). Propofol Anesthesia Does Not Alter Regional Rates of Cerebral Protein Synthesis Measured with L-[1-<sup>11</sup>C]Leucine and PET in Healthy Male Subjects. Journal of Cerebral Blood Flow & Metabolism, 29(5), 1035–1047. [https://doi.org/10.1038/jcbfm.2009.7](https://doi.org/10.1038/jcbfm.2009.7)*

## Questions or feedback

For dataset questions or feedback, please email the NIMH Data Science & Sharing Team at [nimhdsst@mail.nih.gov](mailto:nimhdsst@mail.nih.gov).

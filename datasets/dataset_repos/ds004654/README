# Rates of cerebral protein synthesis (rCPS) in subjects with fragile X syndrome

## Introduction

In this dataset all subjects (n=28) are males between the ages of 18 and 24 years (M=21.3, SD=1.9) and free of psychotropic medication. There are 16 healthy control subjects and 12 subjects with fragile X syndrome. See the `participants.tsv` file at the root of the dataset for full participant information. See [the references below](#references) for more information about this dataset.

Included in this dataset are L-[1-<sup>11</sup>C]Leucine 4D Positron Emission Tomography (PET) images, co-registered defaced 3D anatomical Magnetic Resonanace Imaging (MRI) T1-weighted images, blood sampling data, FreeSurfer derivative files, and FreeSurfer "fsaverage" group-averaged rCPS left and right hemisphere surface statistical maps. All data were collected on the NIH campus in Bethesda, Maryland, USA. For descriptions of data acquisition and processing methods, please see the methods sections of the published papers listed in the `dataset_description.json` file.

## Data Overview

This dataset contains both BIDS rawdata and BIDS derivatives. The rawdata is composed of:

1. `sub-*/ses-MRI/anat/*_T1w.{nii.gz,json}`: Defaced/anonymized anatomical MRI T1-weighted images
    - These T1-weighted images were converted to BIDS NIfTI using MATLAB's `niftiwrite` function, then co-registered to the rCPS derivative images, and then defaced with [FreeSurfer's MiDeFace](https://surfer.nmr.mgh.harvard.edu/fswiki/MiDeFace) to anonymize faces. All defaced images passed a visual inspection using [Dr. Pradeep Raamana's VisualQC](https://github.com/raamana/visualqc) to ensure that no identifiable facial features were present.
2. `sub-*/ses-{SESSION}/pet/*_pet.{nii.gz,json}`: PET data
    - The PET data are shared as-acquired after BIDS conversion. `{SESSION}` above is either `Awake` or `Dex`.
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

3. `sub-HM20` was removed from this dataset because they were missing both PET and MRI data.

## References

1. *Schmidt, K. C., Loutaev, I., Quezado, Z., Sheeler, C., & Smith, C. B. (2020). Regional rates of brain protein synthesis are unaltered in dexmedetomidine sedated young men with fragile X syndrome: A L-[1-<sup>11</sup>C]Leucine PET study. Neurobiology of Disease, 143, 104978. [https://doi.org/10.1016/j.nbd.2020.104978](https://doi.org/10.1016/j.nbd.2020.104978)*

2. *Schmidt, K. C., Loutaev, I., Burlin, T. V., Thurm, A., Sheeler, C., & Smith, C. B. (2022). Decreased rates of cerebral protein synthesis in conscious young adults with fragile X syndrome demonstrated by L-[1-<sup>11</sup>C]Leucine PET. Journal of Cerebral Blood Flow & Metabolism, 42(9), 1666–1675. [https://doi.org/10.1177/0271678X221090997](https://doi.org/10.1177/0271678X221090997)*

## Questions or feedback

For dataset questions or feedback, please email the NIMH Data Science & Sharing Team at [nimhdsst@mail.nih.gov](mailto:nimhdsst@mail.nih.gov).

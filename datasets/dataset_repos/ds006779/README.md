## Description of Dataset

Penn LEAD (Penn Longitudinal Executive functioning in Adolescent Development) is a data resource designed to investigate transdiagnostic executive function during development.

* Note that we are running into some technical issues uploading the full XCP-D data to OpenNeuro. Data for all subjects will be uploaded as soon as possible as available.

This repository contains data derivatives from running XCP-D.
We provide derivatives including post-processed clean BOLD time series that are denoised, filtered, and censored,  ALFF and ReHo maps, parcellated time series and functional connectivity matrices calculated from Pearson correlations, as well as quality control metrics and figures.

The link to the accompanying raw dataset is here: https://openneuro.org/datasets/ds006688 [accession number ds006688].

The Docker Hub link for XCP-D is [here.](https://hub.docker.com/layers/pennlinc/xcp_d/0.10.7/images/sha256-fa10fe96b9ed1cb63322cfebc7dff8a21b7dcca84487b977c06be3d2c863f33a)

The quality control recommendations for fMRI can be found on [Github](https://github.com/PennLINC/transdiagnostic_executive_function/tree/main/QC/qc_csvs/final_QC_csvs). Both QC recommendations for fMRI and T1 structural data should be taken into account for fMRI data.

*Note that we manually deleted extra n-back task runs from the data upon consulting the scanner notes after running XCP-D. Hence, the html files for the following subjects that originally had an extra n-back run will incorrectly specify that there were two runs:
- sub-20149, ses-1
- sub-20212, ses-1
- sub-20238, ses-2
- sub-20352, ses-2
- sub-20934, ses-1
- sub-20964, ses-1
- sub-20968, ses-2
- sub-21035, ses-1
- sub-21197, ses-1
- sub-21516, ses-2
- sub-21553, ses-1
- sub-21738, ses-1
- sub-23676, ses-1
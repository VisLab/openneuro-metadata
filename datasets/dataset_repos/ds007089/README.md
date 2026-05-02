## Description of Dataset
PennLEAD (Penn Longitudinal Executive functioning in Adolescent Development) is a data resource designed to investigate transdiagnostic executive function.

This repository contains data derivatives from running sMRIPrep (fMRIPrep with the anatomical-only parameter).
We provide both surface-level data from Freesurfer such as cortical thickness, curvature, and sulcal depth, and volumetric derivatives such as skull-stripped T1-weighted images, tissue segmentations, brain masks, and the volume of subcortical regions.

The link to the accompanying raw dataset is here: https://openneuro.org/datasets/ds006688 [accession number ds006688].

The Docker Hub link to fMRIPrep is [here](https://hub.docker.com/layers/nipreps/fmriprep/25.0.0/images/sha256-04555ac849ec9e08fa8c70ebf0e0eb6fc99fd54b589c4108b5309de7dca0194b).

The quality control recommendations for sMRI can be found on [GitHub](https://github.com/PennLINC/transdiagnostic_executive_function/tree/main/QC/qc_csvs/final_QC_csvs).

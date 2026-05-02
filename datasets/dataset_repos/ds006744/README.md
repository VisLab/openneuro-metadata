## Description of Dataset

Penn LEAD (Penn Longitudinal Executive functioning in Adolescent Development) is a data resource designed to investigate transdiagnostic executive function during development.

This repository contains data derivatives from running ASLPrep for perfusion data.
We provide derivatives including standard ceberal blood flow maps, SCORE-processed CBF, SCRUB CBF, BASIL CBF, and BASIL CBF with partial volume correction, as well as quality control metrics.

The link to the accompanying raw dataset is here: https://openneuro.org/datasets/ds006688 [accession number ds006688].

The Docker Hub link for ASLPrep is [here.](https://hub.docker.com/layers/pennlinc/aslprep/0.7.5/images/sha256-1cc832ac1bfdc2f6bec126c84bc9bdb8b8cb6dc2995f58d5d3aaaca04f4a99ba)

The quality control recommendations for ASL can be found on [Github](https://github.com/PennLINC/transdiagnostic_executive_function/tree/main/QC/qc_csvs/final_QC_csvs). Both QC recommendations for ASL and T1 structural data should be taken into account for ASL data.
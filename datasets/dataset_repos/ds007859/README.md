# A Sex-Balanced Longitudinal Developmental Task-Free fMRI Rat Dataset

## 1. MRI Data Overview
This dataset contains longitudinal task-free functional and anatomical data from 36 Wistar rats (18 male and 18 female). Each subject was scanned across 5 developmental timepoints (sessions) at approximately postnatal day 28, 35, 49, 70 and 91
Data was acquired on a 7T Bruker scanner using an 8 channel rat head surface array coil. The scan parameters and sedation followed the standardrat protocol (Grandjean et al., 2023; https://doi.org/10.1038/s41593-023-01286-8)

## 2. Other Data Overview
This dataset also includes a range of other data for these subjects such as puberty onset, oestrous smears, daily bodyweights.
It also contains a range of derivative generated during preprocessing including, an unbiased population template, preprocessed timeseries, seed files and seed timeseries.

## 3. Directory Guide
The dataset is in BIDS format

* **'participants.tsv'** Contains the participant_id, wave_number, litter_id, puberty_onset_age_days, date_of_birth and date_of_puberty.
* **'sub-<ID>/sub-<ID>_sessions.tsv** Contains the session_id, target_age_group, age_days, weight_g (weight on day of scan), respiration_bpm (average respiration during scan) and scan_date.
* **'sub-<ID>/ses-<ID>/** Contains contains the func and anat folders with the respective scans.

Beyond the raw BIDS data, this dataset includes source data and several derivatives generated during preprocessing. (Please see the individual `README.md` files within each derivative folder for exact methodology and parameters).

* **'sourcedata/oestrous_smears'**: Contains raw `.jpg` microscopy images of oestrous smears.
* **'sourcedata/growth_metrics'**: Daily body weights and weekly body/tail length measurements.
* **'sourcedata/subject_summary'**: Contains the date of each scan session to allow identification of the oestrous smear from the same day.
* **'derivatives/population_template/'**: Contains the unbiased, study-specific optimized_antsMultivariateTemplateConstruction population templates (0.2mm and 0.3mm resolutions) and transformed ROIs used in technical validation (`tpl-normative`).
* **'derivatives/RABIES/'**: Contains the fully preprocessed, confound-corrected timeseries registered to the normative template (`space-normative`). This folder also contains the 'fd', 'motion' parameters and 'tsnr' files from RABIES
* **'derivatives/AFNI_masks/'**: Contains strict, intensity-thresholded binary brain masks used to replace the default RABIES masks during confound correction as default masks were found to include region without any signal.
* **'derivatives/AFNI_seed_connectivity'**: Contains the seed timeseries and correlation maps (and z maps) for all the seeds used for validation.
* **'derivatives/BEN_weight'**: Contains the brain extraction net (BEN) weight used to create masks for template construction. 

## 4. Notes and Missing Data
* sub-2023080406 does not have ses-1 (P28) scan due to technical issues with the scanner
* A small number of physiological recordings (e.g., respiration rates for specific sessions) were lost or unrecorded due to hardware issues. These are  denoted as `n/a` in the `sessions.tsv` files.


## 5. Citation and Contact
If you use this dataset or its derivatives in your research, please cite the accompanying manuscript:
* [Insert Paper Title Here]
* [Insert DOI or Journal Link Here]

For questions regarding the dataset, pipelines, or templates, please contact:
* Daniel P. McLoone - mclooned@tcd.ie - Trinity College Institute of Neuroscience, Trinity College Dublin

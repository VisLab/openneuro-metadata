Longitudinal EEG Test-Retest Reliability in Healthy Individuals
================================================================

Dataset Description
-------------------
This dataset contains longitudinal resting-state EEG recordings from 43 healthy adults, 
collected over four sessions spanning approximately two years, with an average interval 
of 7.2 months between sessions. The dataset includes raw EEG data and relevant metadata 
following the BIDS standard.

Purpose
-------
The dataset was acquired to assess the test-retest reliability of EEG signals using 
an automated preprocessing pipeline, including independent component analysis and 
wavelet-enhanced artifact removal. It allows for analysis of neural components, 
relative power in regions of interest (ROIs), and longitudinal stability of EEG measures.

Data Structure
--------------
- `dataset_description.json` : Dataset metadata and authorship information.
- `participants.tsv` : Participant demographics and IDs.
- `sub-XX/eeg/` : Folder for each participant containing EEG data files.

EEG Data
--------
Each participant folder contains EEG recordings in BIDS-compliant format. Data 
include:
- Raw EEG signals (`.eeg`, `.vhdr`, `.vmrk`)
- Associated metadata files (`.json`) describing recording parameters and task information.

Usage Notes
-----------
- All participants provided written informed consent. 
- Data are de-identified and do not contain personally identifiable information.
- Users should cite the following paper when using this dataset:
  Henao Isaza V, et al. Longitudinal test-retest reliability of quantitative EEG in 
  healthy individuals using an automated preprocessing approach. DOI: 10.1016/j.bspc.2026.109484

License
-------
This dataset is publicly available under a Creative Commons CC0 license.

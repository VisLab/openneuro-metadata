# High Density Resting State EEG of Phantom Limb Pain and Controls

This dataset comprises resting state high density EEG data (64 or 128 channels) collected from three categories of subjects: amputees with phantom limb pain, amputees without phantom limb pain, and intact, pain free controls. The data has been organised according to the BIDS standard for more accessible reuse. Recordings are approximately 7 minutes long with eyes opened or closed, as indicated by task.

## Usage

For loading and using the data in Matlab we recommend using pop_importbids by EEGLab, example usage here: https://eeglab.org/tutorials/11_Scripting/Analyzing_EEG_BIDS_data_in_EEGLAB.html

For a complete pipeline for resting state EEG preprocessing and feature extraction in Matlab we recommend DISCOVER-EEG:
Cristina Gil. (2024). crisglav/discover-eeg: 2.0.0 (2.0.0). Zenodo. https://doi.org/10.5281/zenodo.10797803

## Phenotype data note

Session-level questionnaire data are stored in `phenotype/pain-questionnaire_sessions.tsv` with descriptions of the corresponding questionnaire items in `phenotype/pain-questionnaire_sessions.json`. The phenotype files are currently ignored by the BIDS Validator due to incomplete support for phenotype indexing across multiple sessions.

## License
CC0
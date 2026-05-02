# Grant DataSet

## Overview
This dataset contains MRI scans acquired from a single participant for the purpose of studying [brief description of the study's purpose, e.g., "brain structure and function in a healthy 13-year-old male."].

## Dataset Structure
- `sub-01/`: Contains all data related to the participant identified as `sub-01`.
  - `anat/`: Contains anatomical MRI data.
    - `sub-01_T1w_acq-sagittal.nii.gz`: Sagittal T1-weighted scan.
    - `sub-01_T2w_acq-axial-fse.nii.gz`: Axial T2-weighted scan using Fast Spin Echo.
    - [Include any other relevant scans with brief descriptions]
  - `dwi/`: Contains diffusion-weighted imaging data.
    - `sub-01_dwi.nii.gz`: Primary diffusion-weighted scan.
    - `sub-01_dwi.bval`, `sub-01_dwi.bvec`: Gradient directions and b-values for DWI.
  - `func/`: Contains functional MRI (fMRI) data if applicable.
    - `sub-01_task-rest_bold.nii.gz`: Resting-state BOLD fMRI scan.

## Methods
- **Scanner**: [Details of the MRI scanner used, e.g., "GE Signa HDxt 1.5T"]
- **Software**: [Details of software used for data acquisition and processing, if applicable]

## Notes
- The dataset follows BIDS version 1.9.0 standards.
- [Any other notes relevant to users of the dataset, e.g., "No preprocessing has been applied to the data."]

## Acknowledgments
Thanks to XYZ for supporting this research.

## Funding
This research was supported by [None or specify any funding sources].

## References
None at this time.

## How to Acknowledge
Please cite this dataset if you use it.

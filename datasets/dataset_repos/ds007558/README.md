# Dataset Description

## Overview
This dataset contains EEG recordings from a study investigating neural activity changes before and after an intervention. The data are organized following the Brain Imaging Data Structure (BIDS) specification.

The dataset includes multiple participant groups and timepoints:
- Group 1, Group 2, Group 3
- Pre-intervention (pre) and Post-intervention (post)

## Participants
Participants are labeled using anonymized IDs (e.g., sub-001, sub-002, etc.). Demographic and session-related information are provided in the corresponding TSV files where applicable.

## Data Structure
The dataset follows the BIDS format:

- `sub-XXX/`
  - `ses-pre/` or `ses-post/`
    - `eeg/`
      - EEG recordings (.edf)
      - Metadata files (.json)
      - Events files (.tsv)

Each subject contains EEG recordings organized by session (pre/post).

## Experimental Design
The study compares neural activity before and after an intervention. Participants are divided into different groups to evaluate potential differences in outcomes.

## Data Acquisition
EEG data were recorded using standard acquisition systems. Detailed acquisition parameters are stored in the accompanying JSON sidecar files.

## Data Processing
The dataset has been reorganized into BIDS format. File naming, metadata, and structure have been standardized to ensure compatibility with BIDS-compliant tools.

## Known Issues
- Some warnings may appear during BIDS validation but do not affect data usability.
- All critical validation errors have been resolved.

## Usage Notes
This dataset can be used for:
- EEG signal analysis
- Functional connectivity studies
- Pre/post intervention comparisons

## License
Please refer to the dataset repository for licensing information.

## Acknowledgements
We thank all participants and researchers involved in data collection and processing.
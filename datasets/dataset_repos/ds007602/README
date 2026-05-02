# EEG-Speech Brain Decoding Dataset

## Overview
This dataset contains EEG recordings and audio data.

## Sessions
Sessions are labeled by recording date in YYYYMMDD format.
- Example: `ses-20240401` = recorded on April 1, 2024

Multiple recordings on the same day are distinguished by run numbers:
- `run-N`: Nth recording of the day

## Tasks
- **speechopen**: Overt speech production task
  - Participants vocalize visually presented text

## File Format Notes

### EEG Data
Raw EEG data is stored:
- **Path**: `sub-*/ses-*/eeg/*_eeg.edf`
- **Note**: EDF format is not officially part of BIDS-EEG specification
- Files are excluded in `.bidsignore` but documented here for reference
- Future releases may include EDF conversions for full BIDS compliance

### Behavioral Data (Audio)
Vocal recordings are stored in `beh/` directories:
- **Path**: `sub-*/ses-*/beh/*_recording-vocal_beh.wav`
- **Note**: Not officially part of BIDS-EEG spec, but included for analysis convenience
- Excluded in `.bidsignore`

## Directory Structure
```
dataset_root/
├── README                          (this file)
├── CHANGES                         (version history)
├── dataset_description.json        (dataset metadata)
├── participants.tsv                (participant information)
├── participants.json               (participant column descriptions)
├── task-speechopen_eeg.json        (task-level EEG metadata)
├── task-speechopen_events.json     (events column descriptions)
├── .bidsignore                     (files to ignore in validation)
│
├── code/                           (analysis and preprocessing code)
│   ├── preprocessing/              (EEG and audio preprocessing)
│   ├── training/                   (model training scripts)
│   ├── evaluation/                 (evaluation metrics)
│   └── bids/                       (BIDS conversion scripts)
│
├── sub-01/                         (participant data)
│   └── ses-YYYYMMDD/              (session by date)
│       ├── eeg/                    (EEG recordings)
│       └── beh/                    (behavioral/audio data)
│
└── derivatives/                    (processed data)
    └── pipeline-standard/          (standard preprocessing)
```
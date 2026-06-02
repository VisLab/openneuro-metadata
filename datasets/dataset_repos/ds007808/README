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
- **listening**: Auditory listening task
  - Participants listen to prerecorded speech stimuli
- **listeningcovert**: Auditory listening followed by covert speech imagery

## EEG Acquisition Devices
Recordings are split by acquisition label:
- **acq-pangolin**: g.tec g.Pangolin. Stored channels include 128 EEG channels plus audio monitor, EOG, EMG, trigger, and in 140-channel recordings one auxiliary mastoid/reference channel that is not used for analysis.
- **acq-scarabeo**: g.tec g.SCARABEO. Stored channels include 64 EEG-related channels, with channels 62 and 63 corresponding to mastoid electrodes, plus audio monitor, EOG, EMG, and trigger channels.
- **acq-eego**: ANT Neuro eego sports. Stored channels include EEG channels 0..30 and 32..63, channel 31 as miscellaneous, audio monitor, EOG, upper- and lower-lip EMG, miscellaneous auxiliary channels, and trigger.

Run-level `*_channels.tsv` files provide the authoritative channel typing for each recording.
For g.Pangolin sessions, `*_electrodes.tsv` and `*_coordsystem.json` files provide 3D coordinates for EEG001..EEG128 from g.tec electrode digitization (`electrodes_uhd.xml`). Electrode coordinate files are not provided for g.SCARABEO or eego sports sessions because verified channel-to-position coordinate mappings are not available in this release.

## File Format Notes

### EEG Data
Raw EEG data is stored:
- **Path**: `sub-*/ses-*/eeg/*_eeg.edf`
- **Note**: EDF files are included as the raw EEG recordings for this BIDS-EEG dataset.

### Behavioral Data (Audio)
Task audio files are stored in `beh/` directories:
- **Speech production**: `sub-*/ses-*/beh/*_recording-vocal_beh.wav`
- **Listening**: `sub-*/ses-*/beh/*_recording-audio_beh.wav`
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
├── task-speechopen_acq-pangolin_eeg.json               (speech production EEG metadata)
├── task-speechopen_acq-scarabeo_eeg.json               (speech production EEG metadata)
├── task-speechopen_acq-eego_eeg.json                   (speech production EEG metadata)
├── task-listening_acq-pangolin_eeg.json                (listening EEG metadata)
├── task-speechopen_acq-pangolin_events.json            (speech production events column descriptions)
├── task-speechopen_acq-pangolin_recording-vocal_beh.json
├── task-listening_acq-pangolin_recording-audio_beh.json
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

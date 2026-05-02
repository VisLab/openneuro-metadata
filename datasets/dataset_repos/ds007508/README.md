# Numerosity and Risk Dataset

## Overview

This dataset contains functional MRI data from a behavioral economics experiment investigating how risky choices are made and how risk preferences change rapidly during decision-making. The data are organized according to the Brain Imaging Data Structure (BIDS) standard.

## Publication

**Rapid Changes in Risk Preferences Originate from Bayesian Inference on Parietal Magnitude Representations**

Authors: Gilles de Hollander, Marcus Grueschow, Franciszek Hennel, Christian C. Ruff

Preprint: https://www.biorxiv.org/content/10.1101/2024.08.23.609296v2.full

## Experiment Description

Participants completed a gambling task while undergoing fMRI scanning. The experiment examined the neural mechanisms underlying risk preference and how participants integrate information about potential outcomes and probabilities during decision-making. The study focuses on parietal cortex representations of magnitude and their role in Bayesian inference during risky choices.

## Dataset Contents

- **Bold fMRI data**: Functional brain imaging during the gambling task
- **Anatomical data**: High-resolution structural MRI for each participant
- **Behavioral data**: Choice, reaction times, and monetary outcomes logged in BIDS events files

## Data Organization

Data are organized according to BIDS standard with the following structure:
```
ds-risk_bids2/
├── sub-XX/
│   ├── ses-01/
│   │   ├── anat/
│   │   │   └── anatomical images
│   │   ├── func/
│   │   │   ├── BOLD images
│   │   │   └── task events
│   │   └── physio/
│   │       └── physiological recordings
│   └── ...other sessions...
└── dataset_description.json
```

## Usage

For complete analysis code and scripts, see: https://github.com/Gilles86/risk_experiment

## License

This dataset is made available under the Public Domain Dedication and License v1.0. Full text: http://www.opendatacommons.org/licenses/pddl/1.0/

We request that researchers using this dataset acknowledge the authors and cite the associated publication.

## Contact

For questions regarding this dataset, please contact the corresponding authors or visit the project repository.

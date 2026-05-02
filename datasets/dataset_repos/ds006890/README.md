Longitudinal Multitask Wireless ECoG Data from Two Fully Implanted Macaca fuscata — README

## Overview
This repository contains a wireless subdural ECoG (iEEG) dataset from *Macaca fuscata* monkeys,
organized in compliance with the iEEG-BIDS specification.
Recordings were acquired several times each week using a wireless, inductively powered implant. The data were curated and organized in BIDS format to facilitate reproducible research in neuroscience.

Keywords: wireless subdural ECoG, iEEG, Macaca fuscata, BIDS-compliant dataset,
longitudinal recordings, task-based neurophysiology

## BIDS Organization
- dataset_description.json
- participants.tsv, participants.json
- README.md, CHANGES.md
- sub-<id>/ses-<index>/ieeg/ (with *_ieeg.edf, *_ieeg.json, *_channels.tsv, *_events.tsv, *_scans.tsv, *_electrodes.tsv, *_electrodes.json, *_coordsystem.json)

## Tasks
Tasks include rest, pressing, reaching, listening, sep.
Only curated and validated tasks are exported.

## Signals and Channels
- Uniform sampling rate per file.
- channels.tsv lists physiological (ECoG), trigger (TRIGGER) and auxiliary channels (MISC).

## Usage
This dataset can be loaded with BIDS-compatible toolboxes such as MNE-Python, FieldTrip, or EEGLAB.
Inspect *_events.tsv for task timing and *_channels.tsv for channel information.

## Participants
Each subject corresponds to an individual monkey (e.g., sub-monkeyb, sub-monkeyc).

## Ethics
All animal procedures complied with Japanese laws and institutional regulations, including the Science Council of Japan Guidelines for Proper Conduct of Animal Experiments and national standards on pain relief and euthanasia, and were approved by the Animal Experiment Committee — The University of Osaka (approval FBS-25-002). 

## License and Citation
License: CC BY 4.0
Citation: [Authors], “[Dataset Title],” [Repository/DOI], [Year].

## Contact
Maintainer: Huixiang Yang, The University of Osaka, yanghuixiang@bci.med.osaka-u.ac.jp
For issues, please use the repository issue tracker.
# COAT fMRI Dataset

This dataset contains fMRI data collected during the Category Learning (CAT) task 
and a resting-state scan (REST). The study investigates category learning and memory in 
healthy young (18-30) and older (60+) adult participants.

## Dataset Contents
- Anatomical (T1w, T2w) images
- Functional MRI during:
  - CAT task (4 runs per participant)
  - Resting-state task (1 run per participant)
- Behavioral logs and trial-level data in `events.tsv` files
- Participant demographics in `participants.tsv`

## Participants
- 64 participants
- Ages: 18–30, 60+
- All participants right-handed

## Experimental Tasks
### Category Learning (CAT)
Participants viewed binary dimension cartoon animals and categorized them into one of two categories 
without feedback. 


### Rest
Participants fixated (eyes open) on a central cross for 6 minutes.

## Data Acquisition
- Scanner: Siemens Skyra 3T
- Multiband EPI sequence, TR = 2s, TE = 25 ms, MB = 3
- High-resolution T1w and T2w anatomical images also collected

## Data Notes
- Data have been anonymized and defaced
- Raw DICOMs are not included in this dataset
- Trial-level behavioral variables are documented in `task-cat_events.json`

## How to cite
If you use this dataset, please cite:
Bowman, C. R., & Zeithamova, D. (2026). Ventromedial prefrontal cortex supports prototype representations in healthy older adults. Neurobiology of Aging. https://doi.org/10.1016/j.neurobiolaging.2026.02.006
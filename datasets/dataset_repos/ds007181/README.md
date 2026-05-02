# Structural MRI, Resting-state fMRI, and PSG/EEG Dataset of Zoster-associated Neuralgia
**Summary**  
This dataset includes anatomical T1-weighted MRI and raw multi-echo resting-state fMRI, as well as PSG data from a study investigating the difference between healthy controls (HC) and zoster-associated neuralgia (ZAN) patients.  
MRI and PSG data were partially overlapping across participants. Participants with available data in at least one modality were included in the dataset, following the BIDS specification.

- For project code and full analysis pipelines (including between-subject comparisons, functional connectivity analyses, and correlation-based statistical modeling), see:  
  [project-zan-neuro](https://github.com/ellebai/zan-neuro)

**Participants** 
- 29 healthy adults (HC) and 27 zoster-associated neuralgia adults (ZAN) for MRI data. 
- 32 healthy adults and 27 zoster-associated neuralgia adults for PSG data.
- See `participants.tsv` for sex, age, group (HC vs. ZAN) 

**Tasks**  
- Functional scans are resting-state.

**What’s included**  
- `sub-*/anat/`  
  - Defaced T1w MRI: `sub-XX_T1w.nii.gz` (+ JSON sidecar if available).  
- `sub-*/func/`  
  - Raw multi-echo BOLD: `sub-XX_task-rest_bold.nii.gz`.
- `sub-*/eeg/`  
  - Defaced T1w MRI: `sub-XX_task-sleep_acq-PSG_eeg.edf`, `sub-XX_task-sleep_acq-PSG_channels.tsv`, `sub-XX_task-sleep_acq-PSG_events.tsv`.
- Top-level: `participants.tsv`, `task-rest_bold.json`, `README.md`.

**Notes on data quality & privacy**  
- T1w images were defaced prior to sharing.  
- Functional files are raw (converted with dcm2niix); files with SPM-style prefixes (r/w/y/s*) were excluded.
- Sleep stages were manually scored based on polysomnography (PSG) data according to the criteria of the American Academy of Sleep Medicine (AASM). Sleep staging followed the standard AASM classification system, including Wake (W), Non-REM stages N1, N2, N3, and Rapid Eye Movement (REM) sleep. Stage N3 corresponds to slow-wave sleep as defined in the AASM manual; no separate N4 stage was used.
- EEG signals were recorded with reference to linked mastoids (M1/M2), and channel names reflect the referenced configuration (e.g., Fp1–M2).

**Folder conventions (BIDS)**  
```
zan/
  sub-01/
    anat/sub-01_T1w.nii.gz    
    func/sub-01_task-rest_bold.nii.gz
  sub-02/
    anat/sub-02_T1w.nii.gz    
    func/sub-02_task-rest_bold.nii.gz  
    eeg/ sub-02_task-sleep_acq-PSG_eeg.edf  
  sub-03/ ...
```

**How to cite**  
These data are associated with a manuscript currently under revision. Please cite the dataset DOI when using these data.

**Contacts**  
- Haolei Bai — ellebai83@gmail.com  
(You may also contact the corresponding author from the manuscript.)

**License**  
This dataset is shared under **CC0**.

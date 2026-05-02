# Emotion Processing and Regulation Task (Static Stimuli) — EEG Dataset

This dataset contains EEG recordings and behavioral data from the **Emotion Processing and Regulation** task with static emotional stimuli. 

* **Preregistration:** [https://osf.io/g8qey](https://osf.io/g8qey)
* **Preprint:** [https://osf.io/preprints/psyarxiv/v9dt3_v2](https://osf.io/preprints/psyarxiv/v9dt3_v2)

---

## Participants

* **N = 148** right-handed, neurologically healthy adults with normal or corrected-to-normal vision.

---

## Experimental Design

The single session comprised 240 trials, split evenly across six conditions defined by stimulus content type Participants completed 240 trials in a single session, evenly allocated to a 2 (content: social, non-social) × 3 (regulation requirement: watch-neutral, watch-negative, reappraise-negative) factorial design. On each trial, they viewed a static image for 5 s and either passively watched it or reappraised it as instructed. They then rated arousal and subsequently valence of the image on separate 9-point scales.

---

## EEG Data Acquisition

* **EEG Cap:** 64-channel QuickCap
* **Amplifier:** Neuroscan SynampsRT
* **Sampling rate:** 1000 Hz
* **Impedance:** below 5 kΩ

### Recorded Channels

FP1, FPZ, FP2, AF3, AF4, F7, F5, F3, F1, FZ, F2, F4, F6, F8,
FT7, FC5, FC3, FC1, FCZ, FC2, FC4, FC6, FT8, T7, C5, C3, C1, CZ, C2, C4, C6, T8,
M1, TP7, CP5, CP3, CP1, CPZ, CP2, CP4, CP6, TP8, M2, P7, P5, P3, P1, PZ, P2, P4, P6, P8,
PO7, PO5, PO3, POZ, PO4, PO6, PO8, CB1, O1, OZ, O2, CB2

### Additional Sensors

* HEO (Horizontal EOG)
* VEO (Vertical EOG)
* EKG
* GSR/EDA

---

## EEG Preprocessing

All preprocessing was conducted in **MATLAB R2020b** using **EEGLAB 2023.0** and **ERPLAB 9.10**. The preprocessing pipeline and fully commented scripts are available in `code/Preprocessing_EEG.m`.

### Summary of preprocessing steps

1. **Band-pass filtering:** 0.1–30 Hz (zero-phase Hamming-windowed FIR)
2. **Downsampling:** 250 Hz
3. **Re-referencing:** average mastoids (M1, M2)
4. **Automatic bad-channel rejection:** *clean_rawdata* (autocorrelation = 0.8)
5. **ICA:** *runica* algorithm
6. **Automatic component rejection:** **ADJUST** and **SASICA**
7. **Spherical interpolation** of removed channels
8. **Epoching:** −200 to 5000 ms relative to stimulus onset
9. **Baseline correction:** −200 ms pre-stimulus
10. **Artifact rejection:** ±100 µV within 200 ms moving window (100 ms step)
11. **Condition averaging:** using ERPLAB

---

## Derivatives & Supplemental Data

### `derivatives/processed_erps/`

Contains averaged ERP files (`.erp`) for each participant after preprocessing.

### `code/`

Includes MATLAB preprocessing scripts and documentation (`Preprocessing_EEG.m`).


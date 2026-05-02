## Participants

This dataset includes 25 native Mandarin Chinese speakers (14 females, mean age = 24.04 ± 2.28 years) who participated in both EEG and fMRI experiments. The participants were all right-handed, with no reported history of neurological disorders. They were enrolled in undergraduate or graduate programs in Shanghai. All participants gave informed consent, and the experiments were approved by the Ethics Committee of the Ninth People's Hospital, affiliated with Shanghai Jiao Tong University School of Medicine (SH9H-2019-T33-2 and SH9H-2022-T379-2).

In the case of French participants, due to legal constraints, additional session considerations were taken into account, such as shorter session durations.

## Experiment Procedure

MRI Scanning Sessions

Participants underwent both EEG and fMRI experiments while listening to the Chinese version of *Le Petit Prince*. During the MRI session, participants were instructed to maintain fixation on a crosshair on the screen and minimize eye movements and head motions. The task involved attending to different talkers in the multitalker condition (single male, single female, mixed male, and mixed female talkers).

Session Breakdown

- The entire session lasted approximately 70 minutes for fMRI participants, including a series of 4 conditions (single-talker, mixed-attended, and mixed-unattended conditions).
- Quiz questions were administered after each run to assess participants' comprehension of the narrative.

In the French cohort, due to legal time constraints, the experiment durations were adjusted.

## Stimuli

The stimuli were selected excerpts from the Chinese version of *Le Petit Prince* (available at [xiaowangzi.org](http://www.xiaowangzi.org/)). These audio clips were previously used in both EEG (Li et al., 2024) and fMRI (Li et al., 2022) studies.

The English and Chinese versions were enhanced with visual stimuli (e.g., images of scenes from the book) to align with the storyline. However, visual stimuli were not presented in the French version to comply with legal restrictions. 

## Acquisition

MRI Hardware & Scanning Parameters

- EEG: Data were collected using a 64-channel actiCAP system, sampled at 500 Hz, and filtered between 0.016 and 80 Hz.
- fMRI: Scanning was performed on a 7.0 T Terra Siemens MRI scanner at the Zhangjiang International Brain Imaging Centre. The scanning parameters differed slightly between the English/Chinese and French studies due to equipment availability.

  - Functional MRI: 85 interleaved axial slices (1.6×1.6×1.6 mm voxel size, TR = 1000 ms, TE = 22.2 ms)
  - Anatomical MRI: MP-RAGE sequence, T1-weighted images (voxel size = 0.7×0.7×0.7 mm).

## Preprocessing

MRI Data Processing

1. DICOM to NIfTI Conversion: All raw MRI data were converted to NIfTI format using `dcm2niix` (version 1.0.20220505) and processed using the `fMRIPrep` pipeline (version 20.2.0).
2. Anatomical Preprocessing:
   - Skull stripping
   - Segmentation into gray matter (GM), white matter (WM), and cerebrospinal fluid (CSF)
   - Registration to the Montreal Neurological Institute (MNI) space using MNI152NLin2009cAsym:res-2 template.
3. Functional Preprocessing:
   - Motion correction
   - Slice-timing correction
   - Multi-echo ICA for denoising
   - Voxel resampling to native and MNI spaces.

Note: Visual stimuli processing for the English and Chinese conditions was handled separately to avoid potential biases in the analysis.


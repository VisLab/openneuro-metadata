# Simultaneous cortico-spinal fMRI (CoSpine) Motor-dataset

**Version:** v1.0.0  
**Date:** 2025-06-30  
**BIDS-compliant**

---

## 1. Dataset Overview

This is the first open-access, BIDS-compliant cortico-spinal task-based fMRI dataset using **voluntary motor tasks**. It enables exploration of cortico-spinal dynamics during repetitive hand movements by providing simultaneous brain-and-spinal fMRI, physiological recordings, and task structure.

- **Task:** Voluntary hand grasping (left and right)
- **Modalities:** fMRI (task-motor BOLD), structural MRI (T1w), EPI-based field maps (reverse phase encoding), physiological signals (pulse & respiration), events/behavioural logs
- **Subjects:** 22 healthy participants  


---

## 2. Experimental Design

- **Task:** Participants performed hand grasping using a **6.5 cm diameter dynamometer**.
- **Cueing:** Auditory cues presented via MRI-compatible headphones.
- **Design:** 12 blocks in total (6 for each hand). Each block consisted of **8 grasps at 1 Hz**.
- **ITI:** Randomized between **16–20 seconds**.
- **Software:** Stimuli were presented and synchronized using **E-Prime 2.0** on Windows.

Event timings (onset, duration) and trial types (motorL, motorR) are documented in each `*_events.tsv`.

---

## 3. Data Acquisition

- **Scanner:** 3T Siemens Prisma (Erlangen, Germany)
- **Head coil:** Standard 64-channel head-neck coil
- **fMRI protocol:** Simultaneous acquisition of brain and spinal cord
- **Physiology:** Pulse and respiration recorded during all task runs

---

## 4. Dataset Structure

## 4. Dataset Structure

```text
dataset/
├── dataset_description.json
├── README
├── task-motor_events.json
├── participants.tsv + .json
├── sub-01/
│   ├── anat/
│   │   ├── sub-01_T1w.nii.gz
│   │   └── sub-01_T1w.json
│   ├── fmap/
│   │   ├── sub-01_dir-AP_epi.nii.gz
│   │   ├── sub-01_dir-AP_epi.json
│   │   ├── sub-01_dir-PA_epi.nii.gz
│   │   └── sub-01_dir-PA_epi.json
│   └── func/
│       ├── sub-01_task-motorL_bold.nii.gz
│       ├── sub-01_task-motorL_bold.json
│       ├── sub-01_task-motorL_events.tsv
│       ├── sub-01_task-motorL_recording-pulse_physio.tsv.gz
│       ├── sub-01_task-motorL_recording-pulse_physio.json
│       ├── sub-01_task-motorL_recording-respiratory_physio.tsv.gz
│       ├── sub-01_task-motorL_recording-respiratory_physio.json
│       ├── sub-01_task-motorR_bold.nii.gz
│       ├── sub-01_task-motorR_bold.json
│       ├── sub-01_task-motorR_events.tsv
│       ├── sub-01_task-motorR_recording-pulse_physio.tsv.gz
│       ├── sub-01_task-motorR_recording-pulse_physio.json
│       ├── sub-01_task-motorR_recording-respiratory_physio.tsv.gz
│       └── sub-01_task-motorR_recording-respiratory_physio.json
```



## 5 Quality control / preprocessing

- Structural T1-weighted images have been defaced for privacy.
- Preprocessed data is placed in `derivatives/preprocessed/`.

---


## Contact

Zhaoxing Wei (zhaoxing.wei@dartmouth.edu)  
Yazhuo Kong (kongyz@psych.ac.cn)
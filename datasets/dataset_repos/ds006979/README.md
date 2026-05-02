# BIDS-EEG Dataset: Examining Perceptual Grouping on Stages of Processing in Visual Working Memory: An ERP Study

**Authors: Hanane Ramzaoui, Melissa Beck**

## 1. Description: Project Overview

We present an electrophysiological dataset recorded from fifty-three subjects performing a bilateral change-detection task to investigate how perceptual grouping, based on color repetition, influences Visual Working Memory (VWM) processing efficiency.

The study is designed to temporally isolate and measure the neural correlates of several critical VWM stages: **individuation encoding**, **maintenance**, **initial comparison**, **percept-memory comparison**, and **decision making/late comparison**. This is achieved using specific **Event-Related Potential (ERP) markers** (N2pc, CDA, N2, FN400).

---

## 2. Experimental Task and Conditions

Subjects were cued to encode the colors of 2 or 3 squares in one visual hemifield. After a maintenance period, a single-item probe was presented to determine if its color had changed.

### Key Manipulations

The memory array contained four primary conditions:

* **Unrepeated (UR):** Arrays with 2 or 3 unique colors (**2-UR, 3-UR**).
* **Repeated (R):** Arrays with 3 items, where two colors were repeated. This condition was further subdivided based on spatial arrangement:
    * Two repeated colors with strong spatial proximity **(3-RSP)**.
    * Two repeated colors with weak spatial proximity **(3-RWP)**.

The Probe in Repeated Conditions

In the repeated conditions (3-RSP and 3-RWP), the single-item probe could test two different item types for change detection:

* **Repeated Item:** The probe tests one of the two squares that share the same color.
* **Unrepeated Item (Singleton):** The probe tests the single square with the unique color.

---

## 3. Primary Neurophysiological Measurements

The study leverages the following ERP components to index different VWM processing stages: 

| VWM Stage | ERP Marker | Event Locking |
| :--- | :--- | :--- |
| **Individuation Encoding** | **N2pc** | Stimulus-Locked |
| **Maintenance/Load** | **CDA** (Contralateral Delay Activity) | Stimulus-Locked |
| **Initial Comparison** | **N2pc** | Probe-Locked |
| **Percept-Memory Comparison** | **N2** | Probe-Locked |
| **Decision Making/Late Comparison** | **FN400** | Probe-Locked |

---

## 4. Acquisition Details and Structure

### Acquisition Parameters

| Parameter | Detail |
| :--- | :--- |
| **Subjects (N)** | 53 (N=39 used for stimulus-locked ERPs, see `participants.tsv` for details) |
| **Electrode System** | BioSemi ActiveTwo System |
| **Number of Channels** | 71 (64 scalp, 3 EOG, 2 Mastoid, 1 CMS/DRL) |
| **Sampling Rate (Acquisition)** | 512 Hz |
| **Total Trials** | 1248 trials |

### BIDS Compliance

The data is structured following the Brain Imaging Data Structure (BIDS) standard for EEG.

* **Acquisition Parameters:** Detailed recording specifications (e.g., 512 Hz sampling rate, Sinc filter details) are provided in the task-level BIDS JSON files (task-myexperiment_eeg.json).
* **Methodology:** Comprehensive details on offline preprocessing (e.g., re-referencing to average mastoids, ICA artifact removal, 0.1 Hz high-pass filtering) and the precise analysis plan (e.g., ERP measurement windows, HEOG artifact thresholds, channel clusters) are provided in the stage 1 protocol on OSF (https://doi.org/10.17605/OSF.IO/8ZS96).

---

## 5. Event Codes/Triggers

The following table maps the trigger codes recorded in the EEG data to the specific experimental events.

* **Acronym Key:** UR = Unrepeated; RWP = Repeated Weak Proximity; RSP = Repeated Strong Proximity.

| Trigger Code | Event Description |
| :---: | :--- |
| "11" | Stimulus: 2-UR \| Left Cue \| Change \| Unrepeated Probe |
| "12" | Stimulus: 3-UR \| Left Cue \| Change \| Unrepeated Probe |
| "13" | Stimulus: 3-RWP \| Left Cue \| Change \| Unrepeated Probe |
| "14" | Stimulus: 3-RSP \| Left Cue \| Change \| Unrepeated Probe |
| "17" | Stimulus: 3-RWP \| Left Cue \| Change \| Repeated Probe |
| "18" | Stimulus: 3-RSP \| Left Cue \| Change \| Repeated Probe |
| "19" | Stimulus: 2-UR \| Left Cue \| No-Change \| Unrepeated Probe |
| "20" | Stimulus: 3-UR \| Left Cue \| No-Change \| Unrepeated Probe |
| "21" | Stimulus: 3-RWP \| Left Cue \| No-Change \| Unrepeated Probe |
| "22" | Stimulus: 3-RSP \| Left Cue \| No-Change \| Unrepeated Probe |
| "25" | Stimulus: 3-RWP \| Left Cue \| No-Change \| Repeated Probe |
| "26" | Stimulus: 3-RSP \| Left Cue \| No-Change \| Repeated Probe |
| "27" | Stimulus: 2-UR \| Right Cue \| Change \| Unrepeated Probe |
| "28" | Stimulus: 3-UR \| Right Cue \| Change \| Unrepeated Probe |
| "29" | Stimulus: 3-RWP \| Right Cue \| Change \| Unrepeated Probe |
| "30" | Stimulus: 3-RSP \| Right Cue \| Change \| Unrepeated Probe |
| "33" | Stimulus: 3-RWP \| Right Cue \| Change \| Repeated Probe |
| "34" | Stimulus: 3-RSP \| Right Cue \| Change \| Repeated Probe |
| "35" | Stimulus: 2-UR \| Right Cue \| No-Change \| Unrepeated Probe |
| "36" | Stimulus: 3-UR \| Right Cue \| No-Change \| Unrepeated Probe |
| "37" | Stimulus: 3-RWP \| Right Cue \| No-Change \| Unrepeated Probe |
| "38" | Stimulus: 3-RSP \| Right Cue \| No-Change \| Unrepeated Probe |
| "41" | Stimulus: 3-RWP \| Right Cue \| No-Change \| Repeated Probe |
| "42" | Stimulus: 3-RSP \| Right Cue \| No-Change \| Repeated Probe |
| "51" | Probe Onset event: 2-UR \| Left Cue |
| "52" | Probe Onset event: 3-UR \| Left Cue |
| "53" | Probe Onset event: 3-RWP \| Left Cue |
| "54" | Probe Onset event: 3-RSP \| Left Cue |
| "55" | Probe Onset event: 2-UR \| Right Cue |
| "56" | Probe Onset event: 3-UR \| Right Cue |
| "57" | Probe Onset event: 3-RWP \| Right Cue |
| "58" | Probe Onset event: 3-RSP \| Right Cue |
| "120" | Manual Response: Correct. |
| "121" | Manual Response: Incorrect. |

---

## 6. Protocol Registration and Reference

For this dataset project, the approved Stage 1 protocol (registered report) can be found at this OSF link (2024, October 15): https://doi.org/10.17605/OSF.IO/8ZS96

---

## 7. Contact and Ethics

* **Affiliation:** Louisiana State University
* **Ethical Approval:** Institutional Review Board of Louisiana State University (IRBAM-23-0273 from March 1, 2023)
* **Contact:** hramzaoui@lsu.edu

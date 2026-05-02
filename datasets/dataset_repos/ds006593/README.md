# Multimodal Sensor Fusion for EEG-Based BCI Typing Systems

## Dataset Overview

This dataset contains recordings of EEG and EyeTracking for a BCI spelling task. The data were collected in 2023 at Northeastern University.

- N=21
- Calibration task were proctored using BciPy [1]
- The dataset is organized in accordance with the Brain Imaging Data Structure (BIDS) specification (version 1.7.0).

## Methodology

Calibration data were collected from control participants (n=21, mean age 23.6 ± 3.1 years) in a quiet lab room at Northeastern University. EEG data were collected using the DSI-24, dry electrode cap (Wearable Sensing, San Diego CA) at a sampling rate of 300 Hz. The device employs a hardware filter permitting a collection bandwidth of 0.003–150 Hz. Data were recorded from Fp1/2, Fz, F3/4, F7/8, Cz, C3/4, T7/T8, T3/T4, Pz, P3/P4, P7/P8, T5/T6, O1/2 with linked-ear reference (A1 and A2) and ground at A1. All data were collected using a Lenovo Legion 5 Pro Laptop with Windows 11, an Intel Core i7-11800H @ 2.30 GHz, 16 GB DDR4 RAM, and a NVIDIA GeForce RTX 3050. Trigger fidelity on the experiment laptop was verified using the Matrix Time Test Task in BciPy and a photodiode. The results of this timing test were used to determine static offsets between hardware and prevent experimentation with any timing violations greater than +/− 10 ms. The Eyetracker data were collected using a portable eye tracker (Tobii Pro Nano) at a sampling rate of 60 Hz. The matrix paradigm and the data acquisition modules are developed in BciPy [1], which is a standalone application for experimental data collection. This work focuses on a specific BCI paradigm called single-character-presentation (SCP) based visual presentation, which consists of symbols presented in matrix form and individually highlighted in randomized order. Calibration task presented letter characters at a rate of 4 Hz, with 100 inquiries consisting of 10 letters each (1 target, 9 non-target). In 10% of the inquiries, only non-target characters were shown. The stimuli included all 26 letters of the English alphabet, as well as the characters “_” for space and “<“ for backspace. The order of target stimuli was randomly distributed among the inquiries. Between inquiries, there was a two-second blank screen. Each inquiry consisted of a one-second prompt showing the target letter, followed by a 0.5s fixation, and then the presentation of 10 letters. The letters were displayed in the center of the screen, in white on a black background. Target prompts and stimuli were presented in white, while fixation crosses were rendered in red.


The experimental protocol was approved by the Northeastern University Institutional Review Board (IRB). All participants provided written informed consent prior to participation.

## Directory Structure
The datasets follows the BIDS convention with the following structure: /sub-[subject]/ses-[session]/[eeg or et]. To load the BIDS formatted data into BciPy Simulator, please see the following directory: /sourcedata/bcipy_metadata. This directory contains the raw BciPy parameter files. It also contains the output of the matrix display (matrix.png) for eyetracking visualization.

## Contact Information

For questions or issues regarding this dataset, please contact the corresponding author [Basak Celik](celik.b@northeastern.edu) via email.

[1] Memmott T, Koçanaoğulları A, Lawhead M, Klee D, Dudy S, Fried-Oken M, Oken B. BciPy: brain-computer interface software in Python. Brain-Computer Interfaces, 8(4), 137-53, 2021.
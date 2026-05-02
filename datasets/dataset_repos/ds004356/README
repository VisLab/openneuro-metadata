# README

## Details related to access to the data

Please contact the following authors for further information:
- Tong Shan (email: tshan@ur.rochester.edu)
- Ross K. Maddox (email: rmaddox@ur.rochester.edu)

## Overview

The goal of this study is to derive Auditory Brainstem Response (ABR) from continuous music and speech stimuli using deconvolution method. Data collected from Jun to Aug, 2021.

The details of the experiment can be found at Shan et al. (2024). There were two phases in this experiment. For the first phase, ten trials of one-minute clicks were presented to the subjects. For the second phase, the 12 types (six genres of music and six types of speech) of 12 s stimuli clips were presented. There were 40 trials 
for each type with shuffled order. Between trials, there was a 0.5 s pause. 

The code for stimulus preprocessing and EEG analysis is available on Github: 

https://github.com/maddoxlab/Music_vs_Speech_abr


## Format

This dataset is formatted according to the EEG Brain Imaging Data Structure. It includes EEG recording from subject 001 to subject 024 (excluding subject 014 and subject 021) in raw brainvision format (including `.eeg`, `.vhdr`, and `.vmrk` triplet) and stimuli files in format of `.wav`. 

For some subjects (sub-03 & sub-19), there are 2 "runs" of data that the first run (`run-01`) only contains the click phase (phase 1), and the second run includes the data for the ABR analysis. 

Triggers with values of "1" were recorded to the onset of the stimulus, and shortly after triggers with values of "4" or "8" were stamped to indicate the stimulus types and the trial number out of 40. This was done by converting the decimal trial number to bits, denoted b, then calculating 2 ** (b + 2). Triggers of "999" denote the start of a new segment of EEG. We've specified these trial numbers and more metadata of the events in each of the `*_eeg_events.tsv` file, which is sufficient to know which trial corresponded to which type of stimulus and which file.


## Subjects

24 subjects participated in this study.

**Subject inclusion criteria**
1. Age between 18-40.
2. Normal hearing: audiometric thresholds of 20 dB HL or better from 500 to 8000 Hz.
3. Speak English as their primary language.
4. Self-reported normal or correctable to normal vision.

**Subject exclusion criteria**
1. Subject 014 self-withdrew partway through the experiment.
2. Subject 021 was excluded because of technical problems during data collection that led to unusable data.

Therefore, after excluding the two subjects, there were 22 subjects (11 male and 11 female) with an age of 22.7 ± 5.1 (mean ± SD) years that we included in the analysis. Please see `subjects.tsv` for more demography.

## Apparatus

Subjects were seated in a sound-isolating booth on a chair in front of a 24-inch BenQ monitor with a viewing distance of approximately 60 cm. Stimuli were presented at an average level of 65 dB SPL and a sampling rate of 48000 Hz through ER-2 insert earphones plugged into an RME Babyface Pro digital sound card. The stimulus presentation for the experiment was controlled by a python script using a custom package, `expyfun`. 



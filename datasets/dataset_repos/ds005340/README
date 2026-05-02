
README
------
Details related to access to the data
-------------------------------------
Please contact the following authors for further information:
    Melissa Polonenko(email: mpolonen@umn.edu)
    Ross Maddox (email: rkmaddox@med.umich.edu)

Overview
--------
This is the "peaky_pitchshift"" dataset for the paper
Polonenko MJ & Maddox RK (2024), with citation listed below.

Peer-reviewed manuscript:

Melissa J. Polonenko, Ross K. Maddox; Fundamental frequency predominantly drives talker differences in auditory brainstem responses to continuous speech. JASA Express Lett. 1 November 2024; 4 (11): 114401. https://doi.org/10.1121/10.0034329

BioRxiv pre-print:

Melissa Jane Polonenko, Ross K Maddox (2024). Fundamental frequency predominantly drives talker differences in auditory brainstem responses to continuous speech. bioRxiv 2024.07.12.603125; doi: https://doi.org/10.1101/2024.07.12.603125



Auditory brainstem responses (ABRs) were derived to continuous peaky speech
from two talkers with different fundamental frequencies (f0s) and from clicks
that have mean stimulus rates set to the mean f0s. Data was collected from
May to June 2021.

Aims:
    1) replicate the male/female talker effect with each at their natural f0
    2) systematically determine if f0 is the main driver of this talker difference
    3) evaluate if the f0 effect resembles the click rate effect

The details of the experiment can be found at Polonenko & Maddox (2024). 

Stimuli:
    1) randomized click trains at 3 stimulus rates (123, 150, 183 Hz), 
    30 x 10 s trials each for a total of 90 trials (15 min, 5 min each rate)
    2) peaky speech for a male and female narrator at 3 f0s (123, 150, 183 Hz),
    120 x 10 s trials each of the 6 narrator-f0 combo for a total of 720 trials
    (2 hours, 20 min each)
    
    NOTE: f0s used: original f0s (low & high respectively) and f0s
    shifted to the other narrator's f0 and an f0 at the midpoint between the f0s.
    click rates used: set to the mean f0s used for the speech

The code for stimulus preprocessing and EEG analysis is available on Github:
    https://github.com/polonenkolab/peaky_pitchshift

Format
------
The dataset is formatted according to the EEG Brain Imaging Data Structure. It 
includes EEG recording from participant 01 to 15 in raw brainvision format
(3 files: .eeg, .vhdr, .vmrk) and stimuli files in format of .hdf5. The stimuli
files contain the audio ('x'), and regressors for the deconvolution 
('pinds' are the pulse indices, 'anm' is an auditory nerve model regressor,
 which was used during analyses but was not included as part of the article). 

Generally, you can find detailed event data in the .tsv files and descriptions
in the accompanying .json files. Raw eeg files are provided in the Brain
Products format.

Participants
------------
15 participants, mean ± SD age of 24.1 ± 6.1 years (19-35 years)

Inclusion criteria:
    1) Age between 18-40 years
    2) Normal hearing: audiometric thresholds 20 dB HL or better from 500 to 8000 Hz
    3) Speak English as their primary language

Please see participants.tsv for more information.

Apparatus
---------
Participants sat in a darkened sound-isolating booth and rested or watched
silent videos with closed captioning. Stimuli were presented at an average level
of 65 dB SPL and a sampling rate of 48 kHz through ER-2 insert earphones
plugged into an RME Babyface Pro digital sound card. Custom python scripts
using expyfun were used to control the experiment and stimulus presentation.

Details about the experiment
----------------------------
For a detailed description of the task, see Polonenko & Maddox (2024) and the
supplied `task-peaky_pitch_eeg.json` file. The 6 peaky speech conditions
(2 narrators x 3 f0s) were randomly interleaved for each block of trials
(i.e., for trial 1, the 6 conditions were randomized) and the story token
was randomized. This means that the participant would not be able to follow
the story. For clicks the trials were not randomized (already random clicks).

Trigger onset times in the tsv files have already been corrected for the tubing
delay of the insert earphones (but not in the events of the raw files).
Triggers with values of "1" were recorded to the onset of the 10 s audio, and
shortly after triggers with values of "4" or "8" were stamped to indicate the
overall trial number out of 120 for each speech conditon and out of 30 for each
click condition. This was done by converting the decimal trial number to bits,
denoted b, then calculating 2 ** (b + 2). We've specified these trial numbers
and more metadata of the events in each of the '*_eeg_events.tsv" file, which
is sufficient to know which trial corresponded to which type of stimulus
(clicks, male narrator, female narrator), which f0 (low, mid, high), and which
file - e.g., male_low_000_regress.hdf5 for the male narrator with the low f0.




README
------
Details related to access to the data
-------------------------------------
Please contact the following authors for further information:
    Melissa Polonenko (email: mpolonen@umn.edu) [corresponding author]
    Ross Maddox (email: rkmaddox@med.umich.edu)

Overview
--------
This is the "peaky_snr" dataset for the paper by
Polonenko MJ & Maddox RK, with citation listed below.

eNeuro: Polonenko, M. J., & Maddox, R. K. (2025). The effect of speech masking on the human subcortical response to continuous speech. eNeuro 24 March 2025, 12 (4) ENEURO.0561-24.2025; https://doi.org/10.1523/ENEURO.0561-24.2025

BioRxiv: https://www.biorxiv.org/content/10.1101/2024.12.10.627771v1

Auditory brainstem responses (ABRs) were derived to continuous peaky speech
from between one up to five simultaneously presented talkers and from clicks.
Data was collected from June to July 2021.


Goal: To better understand masking’s effects on the subcortical neural encoding
of naturally uttered speech in human listeners.

To do this we leveraged our recently developed method for determining the
auditory brainstem response (ABR) to speech (Polonenko and Maddox, 2021).
Whereas our previous work was aimed at encoding of single talkers, here we
determined the ABR to speech in quiet as well as in the presence of varying
numbers of other talkers. 

The details of the experiment can be found at Polonenko & Maddox (2024). 

Stimuli:
    1) randomized click trains at an average rate of 40 Hz, 
    60 x 10 s trials for a total of 10 minutes;
    2) peaky speech for up to 5 male narrators. 30 minutes of each SNR
    (clean, 0 dB, -3 dB, -6 dB), corresponding to 1, 2, 3, and 5 talkers
    presented simultaneously, each set to 65 dB. 
    
    NOTE: files for each story were completely randomized. Random combinations
    were created so that each story was equally represented in the data.

The code for stimulus preprocessing and EEG analysis is available on Github:
    https://github.com/polonenkolab/peaky_snr

Format
------
The dataset is formatted according to the EEG Brain Imaging Data Structure. It 
includes EEG recording from participant 01 to 25 in raw brainvision format
(3 files: .eeg, .vhdr, .vmrk) and stimuli files in format of .hdf5. The stimuli
files contain the audio ('audio'), and regressors for the deconvolution 
('pinds' are the pulse indices, 'anm' is an auditory nerve model regressor,
 which was used during analyses but was not included as part of the article). 

Generally, you can find detailed event data in the .tsv files and descriptions
in the accompanying .json files. Raw eeg files are provided in the Brain
Products format.

Participants
------------
25 participants, mean ± SD age of 23.4 ± 5.5 years (19-37 years)

Inclusion criteria:
    1) Age between 18-40 years
    2) Normal hearing: audiometric thresholds 20 dB HL or better from 500 to 8000 Hz
    3) Speak English as their primary language

Please see participants.tsv for more information.

Apparatus
---------
Participants sat in a darkened sound-isolating booth and rested or watched
silent videos with closed captioning. Stimuli were presented at an average level
of 65 dB SPL (per story; total for 5 talkers = 71 dB) and a sampling rate of 
48 kHz through ER-2 insert earphones plugged into an RME Babyface Pro digital
sound card. Custom python scripts using expyfun were used to control the 
experiment and stimulus presentation.

Details about the experiment
----------------------------
For a detailed description of the task, see Polonenko & Maddox (2024) and the
supplied `task-peaky_snr_eeg.json` file. The 4 SNR speech conditions and the
story tokens were randomized. This means that the participant would not be able
to follow the stories. For clicks the trials were not randomized
(already random clicks).

Trigger onset times in the tsv files have already been corrected for the tubing
delay of the insert earphones (but not in the events of the raw files).
Triggers with values of "1" were recorded to the onset of the 10 s audio, and
shortly after triggers with values of "4" or "8" were stamped to indicate info
about the trial. This was done by converting the decimal trial number to bits,
denoted b, then calculating 2 ** (b + 2). We've specified these trial triggers
and more metadata of the events in each of the '*_eeg_events.tsv" file, which
is sufficient to know which trial corresponded to which type of stimulus
(clicks or speech), snr, and which files of which stories were presented.
e.g., alice_000_peaky_diotic_regress.hdf5 for the first file of the story
called 'alice' (Alice in Wonderland).



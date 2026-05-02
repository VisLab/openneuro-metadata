# Intraoperative EEG dataset during medianus-tibialis stimulation with 8 different rates
This dataset was obtained from the publication [1] wherein we varyied the stimulus repetition rate and recorded medianus and tibial nerve SEP. 
We randomly sampled a number of sweeps corresponding to recording durations up to 20 s and calculated the signal-to-noise ratio (SNR).

There are 14 adults subjects and 4 children subjects with continuous EEG data split in sessions (tibial left/right, medianus left/right) and runs (1 run for each stimulation rate).
We also provide processed data (derivatives) for all the sessions. 
In total there are 34 medianus SEP and 32 tibial SEP sessions.
 
## Repository structure

### Main directory (SEP rate/)
Contains metadata files in the BIDS standard about the participants and the study. Folders are explained below.

### Subfolders
* SEP rate/sub-**/
Contains folders for each subject, named sub-<subject number> and session information.
* SEP rate/sub-**/ses-01/eeg
Contains the raw eeg data in .edf format for each subject. 
Each *eeg.edf file contains EEG data from one stimulation rate (see scans.tsv column stimRate).
Details about the channels are given in the corresponding .tsv file. 
* SEP rate/derivatives
Contains folders for each subject,named sub-<subject number> and session information that include processed data
* SEP rate/derivatives/sub-**/ses-01/eeg/
Contains processed data for each subject.


# Note from the paper
"The offline data processing used the continuous EEG that was recorded in parallel to the SEP recordings. 
Data analysis was performed with custom scripts in Matlab (www.mathworks.com). To detect the SEP stimulation artefact, 
we first filtered the EEG (high pass cutoff = 200 Hz) and performed local peak detection (minimum peak prominence between peaks = 30 ms,
minimum peak width = 4 ms, samples = 0.2 ms). We used the times of the detected stimulus artifact as triggers to define sweeps with 
post-stimulus recording sweep length 50 ms for medianus SEP and 100 ms for tibial SEP. We resampled the data to sampling rate 1200 Hz before
further processing. We classified sweeps with amplitude > 10 ÂµV as artefact-ridden and excluded them from further analysis."

BIDS Conversion
---------------
bids-starter-kid and custom Matlab scripts were used to convert the dataset into BIDS format. 


References
----------
[1] Dimakopoulos V, Selmin G, Regli L, Sarnthein J, Optimization of signal-to-noise ratio in short-duration SEP recordings by variation of stimulation rate, Clinical Neurophysiology, 2023, ISSN 1388-2457, https://doi.org/10.1016/j.clinph.2023.03.008.



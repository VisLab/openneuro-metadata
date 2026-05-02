## Summary

This dataset contains magnetoencephalography (MEG) recordings collected while participants read the French text of *Le Petit Prince* presented using a rapid serial visual presentation (RSVP) paradigm.

A separate dataset containing MEG recordings from the auditory listening paradigm is available on OpenNeuro (accession number: ds007523).

This data is analyzed in:

d’Ascoli, S., Bel, C., Rapin, J. et al. Towards decoding individual words from non-invasive brain recordings. Nature Communications 16, 10521 (2025). https://doi.org/10.1038/s41467-025-65499-0

------------------------------------------------------------------------

## Participants

Fifty healthy adults participated in the reading experiment (10 females; mean age = 28.4 years, SD = 5.7 years).

All participants were native French speakers, right-handed, and reported no history of neurological disorders. Written informed consent was obtained prior to participation. The study was approved by the relevant local ethics committee.

------------------------------------------------------------------------

## Stimuli

The stimulus consisted of the French text of *Le Petit Prince*.

The text was presented using a rapid serial visual presentation (RSVP) paradigm:

- Words were displayed individually in white font on a black background  
- Word duration: 225 ms  
- Inter-word interval: 50 ms (black screen)  
- Sentence-final pause: 500 ms  

Timing parameters were selected based on pilot testing to maintain attention and reading fluency.

The text was segmented into 9 parts corresponding to the 9 experimental runs.

- Mean run duration: 8min10s  
- SD: 40s  
- Range: 7min10s to 9min  

------------------------------------------------------------------------

## Experimental Procedure

After informed consent and familiarization with the MEG environment, participants were seated in the MEG chair inside a magnetically shielded room facing a projection screen.

Viewing distance was fixed at 100 cm. Words appeared sequentially at the center of the screen. Participants were instructed to maintain fixation and read attentively while minimizing movement.

The experiment consisted of 9 runs. Short breaks were provided between runs. After each run, participants completed 4 multiple-choice comprehension questions to assess engagement (behavioral responses are not included in this release).

------------------------------------------------------------------------

## Acquisition

### MEG

MEG data for all three tasks were recorded inside the same magnetically shielded room using a whole-head Elekta Neuromag TRIUX MEG system (Elekta Oy, Helsinki, Finland), equipped with 102 magnetometers and 204 planar gradiometers. Data were recorded continuously with a sampling rate of 1000 Hz and an online low-pass filter at 330 Hz and high-pass filter at 0.1 Hz.
Vertical and horizontal electrooculograms (EOG) and an electrocardiogram (ECG) were recorded simultaneously using bipolar electrodes to monitor eye movements and heartbeats.

### Anatomical MRI

For each participant, a high-resolution T1-weighted anatomical MRI scan was acquired using a 3T Siemens Magnetom Prisma MRI scanner (Siemens Healthcare, Erlangen, Germany).
A standard MPRAGE sequence was used. MRI scans were typically acquired right after the MEG recording. Scans were used for coregistration and cortical surface reconstruction for source analysis. 

------------------------------------------------------------------------

## Data Organization

### Raw Data

The root directory includes:

- `dataset_description.json`  
- `participants.tsv` and `participants.json`  
- `task-read_events.json`  
- `sub-01` to `sub-50`  
- `sourcedata/`  
- `derivatives/`  

Each subject directory (`sub-XX`) contains one session (`ses-01`) with:

- `anat/`: T1-weighted MRI (`sub-XX_ses-01_T1w.nii.gz`) and corresponding JSON sidecar  
- `meg/`: 9 MEG runs (`task-read_run-01` to `run-09`), each including:
  - continuous MEG data (`*_meg.fif`)  
  - sidecar JSON files  
  - `events.tsv` and `channels.tsv` files  
  - coordinate system file (`*_coordsystem.json`)  
  - calibration and crosstalk files  
- `sub-XX_ses-01_scans.tsv`: scan-level metadata  

Each run corresponds to one text segment.

Acquisition parameters are provided in the corresponding sidecar JSON files.

### Derivatives

The `derivatives/` directory contains:

- `freesurfer/`: subject-specific FreeSurfer reconstructions and morph maps  
- `preprocessed_data/`: preprocessed MEG data (including SSS-processed files), forward and inverse solutions, noise covariance matrices, source spaces, transformation files, evoked data, and source time courses.

------------------------------------------------------------------------

## Reference

Niso, G., Gorgolewski, K. J., Bock, E., Brooks, T. L., Flandin, G., Gramfort, A., Henson, R. N., Jas, M., Litvak, V., Moreau, J., Oostenveld, R., Schoffelen, J., Tadel, F., Wexler, J., & Baillet, S. (2018). MEG-BIDS, the brain imaging data structure extended to magnetoencephalography. *Scientific Data*, 5, 180110. https://doi.org/10.1038/sdata.2018.110

# Data for Reading reshapes stimulus selectivity in the visual word form area

This contains the raw and pre-processed fMRI data and structural images (T1) used in the article, "Reading reshapes stimulus selectivity in the visual word form area. The preprint is available [here](https://www.biorxiv.org/content/10.1101/2023.10.04.560764v2), and the article will be in press at eNeuro.  

Additional processed data and analysis code are available in an [OSF repository](DOI 10.17605/OSF.IO/2T86C).

Details about the study are included here.

## Participants
We recruited 17 participants (Age range 19 to 38, 21.12 ± 4.44, 4 self-identified as male, 1 left-handed) from the Barnard College and Columbia University student body. The study was approved by the Internal Review Board at Barnard College, Columbia University. All participants provided written informed consent, acquired digitally, and were monetarily compensated for their participation. All participants had learned English before the age of five.

To ensure high data quality, we used the following criteria for excluding functional runs and participants. If the participant moved by a distance greater than 2 voxels (4 mm) within a single run, that run was excluded from analysis. Additionally, if the participant responded in less than 50% of the trials in the main experiment, that run was removed. Finally, if half or more of the runs met any of these criteria for a single participant, that participant was dropped from the dataset. Using these constraints, the analysis reported here is based on data from 16 participants. They ranged in age from 19 to 38 years (mean = 21.12 ± 4.58,). 4 participants self-identified as male, and 1 was left-handed. A total of 6 runs were removed from three of the remaining participants due to excessive head motion.

## Equipment
We collected MRI data at the Zuckerman Institute, Columbia University, a 3T Siemens Prisma scanner and a 64-channel head coil. In each MR session, we acquired a T1 weighted structural scan, with voxels measuring 1 mm isometrically. We acquired functional data with a T2* echo planar imaging sequences with multiband echo sequencing (SMS3) for whole brain coverage. The TR was 1.5s, TE was 30 ms and the flip angle was 62°. The voxel size was 2 mm isotropic.

Stimuli were presented on an LCD screen that the participants viewed through a mirror with a viewing distance of 142 cm. The display had a resolution of 1920 by 1080 pixels, and a refresh rate of 60 Hz. We presented the stimuli using custom code written in MATLAB and the Psychophysics Toolbox (Brainard, 1997; Pelli, 1997). Throughout the scan, we recorded monocular gaze position using an SR Research Eyelink 1000 tracker. Participants responded with their right hand via three buttons on an MR-safe response pad.

## Tasks

### Main Task
Participants performed three different tasks during different runs, two of which required attending to the character strings, and one that encouraged participants to ignore them. In the lexical decision task, participants reported whether the character string on each trial was a real word or not. In the stimulus color task, participants reported whether the color of the character string was red or gray. In the fixation color task, participants reported whether or not the fixation dot turned red. 

On each trial, a single character string flashed for 150 ms at one of three locations: centered at fixation, 3 dva left, or 3 dva right). The stimulus was followed by a blank with only the fixation mark present for 3850 ms, during which the participant had the opportunity to respond with a button press. After every five trials, there was a rest period (no task except to fixation on the dot). The duration of the rest period was either 4, 6 or 8 s in duration (randomly and uniformly selected).

### Localizer for visual category-selective ventral temporal regions
Participants viewed sequences of images, each of which contained 3 items of one category: words, pseudowords, false fonts, faces, and limbs. Participants performed a one-back repetition detection task. On 33% of the trials, the exact same images flashed twice in a row. The participant’s task was to push a button with their right index finger whenever they detected such a repetition. Each participant performed 4 runs of the localizer task. Each run consisted of 77 four-second trials, lasting for approximately 6 minutes. Each category was presented 56 times through the course of the experiment.

### Localizer for language processing regions
The stimuli on each trial were a sequence of 12 written words or pronounceable pseudowords, presented one at a time. The words were presented as meaningful sentences, while pseudowords formed “Jabberwocky” phrases that served as a control condition. Participants were instructed to read the stimuli silently to themselves, and also to push a button upon seeing the icon of a hand that appeared between trials. Participants performed three runs of the language localizer. Each run included 16 trials and lasted for 6 minutes. Each trial lasted for 6s, beginning with a blank screen for 100ms, followed by the presentation of 12 words or pseudowords for 450ms each (5400s total), followed by a response prompt for 400ms and a final blank screen for 100ms. Each run also included 5 blank trials (6 seconds each).

### Data organization
This repository contains three main folders, complying with [BIDS specifications](https://bids.neuroimaging.io/). 
- Inputs contain BIDS compliant raw data, with the only change being defacing the anatomicals using [pydeface](https://pypi.org/project/pydeface/). Data was converted to BIDS format using [heudiconv](https://heudiconv.readthedocs.io/en/latest/).    
- Outputs contain preprocessed data obtained using [fMRIPrep](https://fmriprep.org/en/stable/). In addition to subject specific folders, we also provide the freesurfer reconstructions obtained using fMRIPrep, with defaced anatomicals. Subject specific ROIs are also included in the label folder for each subject in the freesurfer directory. 
- Derivatives contain all additional whole brain analyses performed on this dataset. 

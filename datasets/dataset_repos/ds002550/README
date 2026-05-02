OpenNeuro curator note: This dataset was previously accessible at ds001750. The dataset was reuploaded due to privacy considerations. 

# Data folder corresponding to [this manuscript](https://www.biorxiv.org/content/early/2018/03/16/283234)
#### Differential brain mechanisms of selection and maintenance of information during working memory

Note: One participant didn't sign a sharing data agreement so data of 22 participants are available here (vs. 23 in the manuscript). Results and conclusion are not different with only 22 participants.

Participant folder are organized as:
- ##### 'ses-mri/anat':
contains T1 MRI of the participant
- ##### ses-01:
contains MEG data in BIDS format, behavioral data and HPI position in surface RAS MRI coordinates for session 1
- ##### ses-02:
contains MEG data in BIDS format, behavioral data and HPI position in surface RAS MRI coordinates for session 2

##### Description of non-MEG files:
- ##### behavioral task scripts:
Matlab (psychtoolbox 3) script for Working Memory (WorkMem) and one-back control task (LocaCue)
- ##### hpi_mri_surf.txt:
Contains the X, Y Z coordinates of the nasion, left and right HPI (head position indicator) in surface MRI coordinates. Names of the electrode are NEC (nasion), LEC (left) and REC (right). Others coordinates are for co-registration during the session (not useful here). These HPI coordinates have been acquired from the neuronavigation system brainsight (https://www.rogue-research.com/tms/brainsight-tms/)
- ##### WorkMem+subNumber+date.csv:
###### Contains behavioral results:
- NbTrial: trial number
- FixNbTrial: trial number with good eye fixation
- isFixed: whether the participant fixed the central dot during the trial (1:correct fixation, 0:broke fixation)
- GaborLeft: left gabor (25 possible, 5 spatial frequency* 5 orientations)
- GaborRight: right gabor (25 possible, 5 spatial frequency* 5 orientations)
- Cue: cue (4 possible, 1: left dotted, 2: left solid, 3: right dotted, 4: left solid)
- Change: whether the cued stimulus attribute is different from the corresponding probe attribute (1: different, 0: same)
- sfLeft: spatial frequency of the left gabor (5 possible)
- orientLeft: line orientation of the left gabor (5 possible)
- phaseLeft: phase of the left gabor (5 possible)
- sfRight: spatial frequency of the right gabor (5 possible)
- orientRight: line orientation of the right gabor (5 possible)
- phaseRight: phase of the right gabor (5 possible)
- randomSF: probe spatial frequency if change=1
- randomOrient: line orientation if change=1
- phaseResp: phase of the probe
- Response: response of the participant (1: different, 0: similar)
- isCorrect: correctness of the response (1: correct, 0: uncorrect)
- reactionTime: reaction time from probe onset to participant response
- TrialTime: total trial duration
- runningTime: running time
- fixcrossTime: duration of the fixation dot presentation before stimulus onset (should be between 0.350 and 0.450 s)
- gaborTime: duration of stimulus presentation (should be 0.1 s)
- precueTime: duration between stimulus offset and cue onset (should be between 0.75 and 0.85 s)
- cueTime: duration of the cue presentation (should be 0.1 s)
- postcueTime: duration between cue offset and probe onset (should be between 1.45 and 1.55 s)
- feedbackTime: duration of the feedback (green or red dot, should be 0.1 s)
- triggGabor: trigger sent to MEG acquisition at the stimulus onset
- triggCue: trigger sent to MEG acquisition at the cue onset
- triggProbe: trigger sent to MEG acquisition at the probe onset
- ##### locacue+subNumber+date.csv:
- NbTrial: trial number
- FixNbTrial: trial number with good eye fixation
- isFixed: whether the participant fixed the central dot during the trial (1:correct fixation, 0:broke fixation)
- same: whether 2 consecutive lines are similar (1: similar, 0: different)
- Cue: cue (4 possible, 1: left dotted, 2: left solid, 3: right dotted, 4: left solid)
- Side: side of the cue (1: right, 0: left)
- Press: whether the participant press the button (1: press, 0: no press)
- isCorrect: correctness of the response (1: correct, 0: uncorrect)
- ReactionTime: reaction time when a button is pressed
- TrialTime: total trial duration
- runningTime: running time
- fixcrossTime: duration of the fixation dot
- cueTime: duration of the cue presentation (should be 0.1 s)
- postcueTime: duration between the cue offset and the beginning of the next trial (should be 1.2 s)
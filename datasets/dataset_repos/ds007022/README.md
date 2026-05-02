# LEARNING BRAIN - a longitudinal dataset on neural plasticity dynamics in Braille and music training

The LEARNING BRAIN dataset is a collection of behavioural and preprocessed neuroimaging data from a study on the time-course of neuronal plasticity underlying learning in young adults. The data was acquired from 60 healthy individuals, divided into three groups: Braille (tactile) training, Music (piano) training, and a Control group who underwent no targeted training. Participants underwent between six and seven measurement sessions (time-points).

In particular, the dataset includes the following data:
* two behavioural cognitive tasks at three time-points:
  * n-back task
  * Stroop task
* a single anatomical image per participant, averaged across time-points
* a resting-state fMRI measurement at six or seven time-points:
* five fMRI domain-specific and domain-general tasks at four to seven time-points:
  * finger tapping
  * lexical decision task (tactile Braille)
  * six-dot detection task (tactile)
  * play music task (auditory-motor)
  * passive music listening task (auditory)
* behavioural performance of relevant fMRI tasks:
  * lexical decision task (tactile Braille)
  * six-dot detection task (tactile)
  * play music task (auditory-motor)


The data was acquired between September 2020 and July 2022.

Anonymised images are available in the common MNI152NLin2009cAsym space in nifty (`*.nii`) format. A `participants.tsv` file contains demographic information about the participants (sex, age), their handedness, their number of foreign languages known, and the group to which they were assigned to. A sidecar file 'participants.json' provides details about this file. 

A single anatomical image per subject is provided (`*_T1w.nii.gz`), which is the average of the anatomical images acquired during the study. Therefore, anatomical images are nested within the participants sub-directories, not session sub-directories. A sidecar `*_T1w.json` file provides information about preprocessing. Additionally, a brain mask file created during the preprocessing is available (`*_mask.nii.gz`) and a sidecar file (`*_mask.json`) indicating the anatomical region the mask is derived from. Finally, the following anatomical derivatives are provided: `*_dseg.nii.gz`, `*_label-CSF_probseg.nii.gz`, `*_label-GM_probseg.nii.gz`, `*_label-WM_probseg.nii.gz`, which contain the discrete segmentation file, the probabilistic segmentation file for the cerebrospinal fluid, the probabilistic segmentation file for the grey matter, and the probabilistic segmentation file for the white matter, respectively.

Functional data are nested within session directories and contain one time-series data per participant per task or resting-state (`*_task-<taskname>_*_desc-preproc_bold.nii.gz`), accompanied by a sidecar (`*_task-<taskname>_*_desc-preproc_bold.json`) containing the anonymised information from the DICOM header from the raw file, as well as preprocessing details. Additionally, a mask file derived from the functional data is provided (`*_task-<taskname>_*_desc-brain_mask.nii.gz`), and the confounds file (`*_task-<taskname>_*_desc-confounds_timeseries.tsv`) and its accompanying sidecar (`*_task-<taskname>_*_desc-confounds_timeseries.json`) from the fMRIprep output. For all tasks, a `*_task-<taskname>_events.tsv` file holds time-stamped events and behavioural responses. The necessary information to understand these files is available in tasks-specific files `task-<taskname>_events.json` located in the dataset root directory.

Behavioural data includes an `*_events.tsv` file per participant per behavioural task (n-back, Stroop Task). Sidecar files (`task-n_back.json`, `task-Stroop.json`), which describe the contents of these files, are located in the dataset root directory. 

## Time-points
* ses-pre: one week before the onset of training
* ses-0: at the onset of training
* ses-1: after one week of training
* ses-2: after six weeks of training
* ses-3: after 13 weeks, halfway through training 
* ses-4: at the end of training
* ses-5: after a follow-up period (about 2-3 months)

## Task description
### N-back
This visual n-back task was based on the n-back task available in the Presentation software. The task presented participants with single letters at three difficulty levels: 1-back, 2-back, and 3-back. Participants observed sequences of individual letters and were instructed to press a button whenever the currently displayed letter matched the one shown n steps earlier in the sequence. Each block contained 50 trials, comprising 10 target trials and 40 control trials. During each trial, a stimulus appeared on the screen for 500 ms, followed by a 1000 ms inter-trial interval displaying an empty screen. Before the main experiment, participants completed a practice session of 8 trials for each difficulty level.

### Stroop task
The task was based on the Stroop task available in the Presentation software. It consisted of two distinct block types: ink blocks and colour name blocks. In the ink blocks, participants were instructed to identify the ink colour of the presented stimuli. In contrast, during colour name blocks, the participant’s task was to identify the written colour name itself. Stimuli were presented using four target colours (red, green, blue, or yellow). Control stimuli in ink blocks consisted of strings of Xs instead of words, whereas control stimuli in colour name blocks were written in black ink. The experiment comprised six blocks in total—three ink blocks and three colour name blocks—presented alternately. Each block consisted of 72 trials, evenly divided into incongruent and neutral conditions. Individual trials began with a fixation cross displayed for 500 ms, followed by the stimulus presented until a response was given or until a maximum duration of 5000 ms elapsed. Trials were separated by an empty inter-trial interval of 1000 ms. Before the main experimental phase, participants completed a practice run containing 12 trials per block type, during which feedback was provided.

### Finger Tapping
Participants performed a block-design finger-tapping task, alternating between rest and tapping conditions. Each tapping block was preceded by a short cue indicating hand condition (alternating left/right) [2s]. The starting hand was counterbalanced across participants. During tapping blocks, participants were instructed to tap the indicated hand’s fingers against the thumb in a sequential, looped order (finger order: index, middle, ring, little, ring, middle) for 12s. Participants were instructed to tap at a rate of approximately 60 bpm, but were not given a metronome or other pacing cue. During rest blocks (varying duration: 10 s, 12.5 s and 15 s, counterbalanced across participants), participants were instructed to remain still. No behavioral data were collected for this task.

### Lexical Decision Task - Braille (tactile)
Participants performed a tactile lexical decision task. The stimuli were presented using an MRI-compatible Braille display.
In the experimental condition (lexical decision, LDT), participants were asked whether the presented letter sequence constituted a valid Polish word or a pseudoword—a sequence resembling a real word but nonexistent in Polish. In the control condition (six-dot detection, DD6), participants judged whether a sequence of randomly presented consonants contained exactly two nonlinguistic symbols - the full six-dot Braille characters (⠿). Stimuli were balanced such that half contained exactly two nonlinguistic symbols, and half contained none. Participants responded at the end of each trial using their left hand via a response pad, indicating the presence or absence of the nonlinguistic symbols.

During the task, each condition was presented in 8 blocks. Each block contained 5 stimuli presented for 5 seconds. The block was preceded by a fixation cross displayed for a pseudo-random duration of 6 to 8 seconds, followed by a 2-second visual cue indicating the upcoming task. After each stimulus presentation, participants had a 2-second response window, followed by an inter-stimulus interval lasting between 1 and 2 seconds.

### Six-Dot Detection Task (tactile)
The Six-dot detection task investigated brain activity associated with implicit reading in the tactile modality. In the experimental condition, participants sequentially moved their right index finger from left to right across stimuli, pressing a response button with their left hand whenever encountering a six-dot Braille symbol (⠿) embedded within random letter sequences. Each trial could elicit 0, 1, or 2 responses. Participants were unaware that approximately half of the stimuli within each experimental block included brief, three-letter Braille words.

Each experimental block consisted of 8 stimuli, presented for 5 seconds each, followed by an inter-stimulus interval lasting 1 second. Blocks were separated by 12-second rest periods. Before each block, a fixation cross appeared for a pseudo-random duration ranging from 6 to 8 seconds, followed by a visual cue (lasting 1 to 2 seconds) indicating the upcoming task.

### Playing music (auditory, motor)
This fMRI task investigated brain activation in novice pianists playing musical excerpts from their course curriculum. The task employed alternating "Listen" and "Playback" conditions. During the "Listen" condition, participants heard a music stimulus which was an excerpt from one of the stimuli they learned to play in the piano training course. The participants were instructed to attend to the stimulus and recognise it from their curriculum. The "Playback" condition required participants to immediately reproduce the preceding excerpt stimulus on a commercially available MRI-compatible keyboard, either unimanually (right hand) or bimanually, as indicated by a visual cue.  The participants were instructed to complete playing the fragment even if they made a mistake or they exceeded the time window allotted for the playback. Each musical piece was presented in two consecutive excerpt stimuli (listen1-playback1-listen2-playback2) under the same hand condition. At baseline (TP1), the simplest musical piece from the curriculum was played 16 times (8 unimanual, 8 bimanual). Task difficulty increased as training progressed, with more complex musical pieces and fewer repetitions, but always within 32 trials (16 listen and 16 playback). Stimuli were presented and played during the ‘silent’ TRs of an interleaved silent steady-state (ISSS) sequence (5 TRs image acquisition [7.75s], 4 TRs ‘silent’ [6.2s]). The order of musical pieces was pseudo-randomized and counterbalanced across participants. Behavioural data collected during the task encompassed the pressed key numbers of the MRI-compatible keyboard, and the timing of pressing and releasing the keys.

### Passive Music Listening (auditory)
This task investigated brain activation patterns elicited by musical stimuli. To ensure stimulus novelty, short piano pieces were selected from the MUST dataset. The stimuli are available at osf.io/bfxz7. Neuroimaging data were acquired using an ISSS sequence (5 TRs image acquisition [7.75s], 3 TRs ‘silent’ [4.65s]), with auditory stimuli presented exclusively during the silent TRs. The stimuli were grouped into eight blocks of four stimuli each, one from every MUST category (Balance, Contour, Symmetry, and Complexity), followed by a one duration-matched silence condition per block. Participants were instructed to maintain open eyes and attend to visual cues (musical note symbol: listen to music; dash: silence) while listening to the auditory stimuli. To mitigate habituation, half of the stimuli were repeated at all timepoints, while the other half were novel at each time point. Stimulus presentation order was pseudo-randomized and counterbalanced across participants. No behavioral data were collected for this task.

### Resting state
Participants underwent a 10-minute resting state (RS) scan. During the RS scan participants were asked to rest with their eyes open focusing on a fixation cross in the centre of the screen with the instruction to try to relax, not to think of anything in particular, and not to fall asleep. 


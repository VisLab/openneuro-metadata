Overview
——————————————————
This data is from the paper "Capacity for movement is a major organisational principle in object representations". This is the data of Experiment 1 (EEG: aliveness). The preprint is here: https://doi.org/10.31234/osf.io/3x2qh 

Abstract:
The ability to perceive moving objects is crucial for threat identification and survival. Recent neuroimaging evidence has shown that goal-directed movement is an important element of object processing in the brain. However, prior work has primarily used moving stimuli that are also animate, making it difficult to disentangle the effect of movement from aliveness or animacy in representational categorisation. In the current study, we investigated the relationship between how the brain processes movement and aliveness by including stimuli that are alive but still (e.g., plants), and stimuli that are not alive but move (e.g., waves). We examined electroencephalographic (EEG) data recorded while participants viewed static images of moving or non-moving objects that were either natural or artificial. Participants classified the images according to aliveness, or according to capacity for movement. Movement explained significant variance in the neural data over and above that of aliveness, showing that capacity for movement is an important dimension in the representation of visual objects in humans.  


In this experiment, participants completed two tasks - classification and passive viewing. In the classification task, participants classified single images that appeared on the screen as "alive" or "not alive". This task was time-pressured, and trials timed out after 1 second. In the passive viewing task, participants viewed rapid (RSVP) streams of images, and pressed a button to indicate when the fixation cross changed colour.

Contents of the dataset: 
 - Raw EEG data is available in individual subject folders (BrainVision raw formats .eeg, .vmrk, .vhdr). Pre-processed EEG data is available in the derivatives folders in EEGlab (.set, .fdt) and cosmoMVPA dataset (.mat) format. This experiment has 24 subjects.
 - Scripts for data analysis and running the experiment are available in the code folder. Note that all code runs on both EEG experiments together, so you must download both this and the movement experiment data in order to replicate analyses.
 - Stimuli are also available (400 CC0 images)
 - Results of decoding analyses are available in the derivatives folder.

Further notes: 

Note that the code is designed to run analyses for data and its partner data (experiments 2 and 3 of the paper). Copies in both folders are identical. Scripts need to be run in a particular order (detailed at the top of each script)
#### Further explanations of the code:

1. Run pre-processing of EEG (analyse_EEG_preprocessing.m), and behavioural data (analyse_behavioural_EEG.m)
2. Ensure that the MTurk data has been run (analyse_behavioural_MTurk.m), from the Experiment 1 folder.
3. Run RSA (analyse_rsa.m; reliant on behavioural data and pre-processed EEG data), and run decoding (analyse_decoding.m; reliant on pre-processed EEG data)
4. Run GLMs (analyse_glms.m; reliant on RSA, behavioural)

To only look at the results, the results for each of these analyses is saved in the derivatives already, so there is no need to run any of them again.

Each file named plot_X.m will create a graph as in the paper. Each is reliant on saved data from the above analyses, which are saved in the derivatives folder.


Citing this dataset
———————————————————
If using this data, please cite the associated paper: Preprint - https://doi.org/10.31234/osf.io/3x2qh 

Contact 
———————————————————
Contact Sophia Shatek (sophia.shatek@sydney.edu.au) for additional information. ORCID: 0000-0002-7787-1379

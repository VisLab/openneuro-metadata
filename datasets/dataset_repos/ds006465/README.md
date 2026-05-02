Overview

This dataset, named 3M-CPSEED, consists of electroencephalogram (EEG) recordings obtained from 20 participants engaged in imagined speech tasks. 3M-CPSEED holds significant implications for speech neurophysiology research, not only facilitating exploration of neural activity differences across pinyin articulations but also enabling robust transfer learning studies for other alphabetic languages.

Data Collection

Participants: 20 healthy, right-handed individuals (average age: 24.55 years, standard deviation: 2.58 years; 11 females, 9 males) who are native Chinese speakers.

Materials: To strike a balance between comprehensively capturing the articulatory features of the Chinese phonological system and maintaining a concise, controllable set of stimuli, we selected this set of Pinyin sounds: Finals: "a, i, u, ü"; Initials: "m, f, j, l, k, ch".

Procedure: Participants read Pinyin displayed on a screen at 'speak', 'Silently articulated' and 'imagined' phase. Each participant completed 4 blocks of 1600 trials in total.

Data Structure

The dataset is organized according to the BIDS standard:

Main Folder:
dataset_description.json: Description of the dataset.
participants.tsv: Participant information.
participants.json: Details of columns in participants.tsv.
README: General information about the dataset.
data_all.mat: Labeled EEG data of all subjects in MAT format.
Derivative Data:
preproc/: Preprocessed data, including subfolders for each subject (sub-01, etc.), with data in .mat formats .

Acknowledgments
This work was supported by a 1.3.5 project for disciplines of excellence from West China Hospital (#ZYYC22001).
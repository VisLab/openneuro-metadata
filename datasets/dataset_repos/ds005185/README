EESM19: Ear-EEG Sleep Monitoring data set

This data set was collected as part of development and quality assessment of the ear-EEG as a sleep monitoring platform. Data collection took place between 2018 and 2020. First publication was in 2019 (https://doi.org/10.1038/s41598-019-53115-3), hence the '19' in the name.

The data set consists of 2 parts (a & b): 
a: 20 subjects who each spent 4 nights sleeping with a partial PSG (EEG, EOG and chin EMG electrodes), ear-EEG and a wristworn actigraph, in their own homes. 
b: Of these 20 subjects, 10 also slept a further 12 nights wearing only ear-EEG, actigraph and a single EOG electrode.
Each night is saved as a separate ‘session’, meaning that some subjects have 4 sessions while others have 16. The PSG-nights area always sessions 1-4. Each PSG night has an additional 'scoring' event file, where 'scoring' is the 'acquisition' type. 

Questionnaires:
After each night’s recording, the subject answered a short questionnaire regarding the quality of the night’s sleep. This has been archived as behavioral data (task='comfort'). 

Diaries: 
Besides the comfort questionnaire, the subjects also kept a standardized diary regarding the events of the night. This have been imported too, however only the requried fields 'Syncronization','Electrodetest','Went to bed', 'Lights out' and 'Got up' have been translated from Danish to English. We suggest using an online translation tool for any additional entries.
The diaries have a column 'pressedTrigger', which indicates that the subject marked the precise time of the event on their wrist worn actigraph. As there is some interpretation necessary due to both spurious extra trigger presses and also missing trigger presses, and these event markings eventually turned out not to be important for our own research, we have not exported these trigger times in the data set. However, as the full actigraphy file is included in this data set, any interested future user can do the matching themselves.
For consistency, we have chosen to use the starting time written in the scored edf file ('edf1') as the starting time of each PSG recording. For non-PSG recordings, the starting time is what is written in the diary. An alternative would be using the start time as seen in the wrist actigraph, described below.

Actigraphy:
Subjects wore GENEactive actigraphs ('actiwatches' for short). These record 3-axis acceleration as well as temperature, light and user button presses. Given that the temperature and light readings are very impacted by whether the subjects had their hand above or below the covers, we found that only the actigraphy and button presses had much use. However, all data is found in the actigraphy files (in the behavior folders). 
The ensure the possibility of perfect alignment between actiwatch and EEG recorder (TMSI 'mobita'), at the beginning of each recording, the subjects shook the mobita and the actiwatch together in a repeated rythmical pattern. By accessing the mobita actigraphy data from the .set file (EEG.etc.acc.data) it is possible to get perfect alignment. This is advantageous if very high precision of various sleep events is desired, since the clock in in the actiwatch was very reliable. In practice, we have not used this option, and hence the actigraphy alignment is left up to the user.

Electrode test:
As a quality check on the electrode connections subjects viewed a short video containing various instructions: repeated jaw clenching, open/closed eyes, horizontal eye movements. These are marked in the diaries, and can be used as a simple test that the EEG equipment is working as intended. An analysis of these responses can be found in https://doi.org/10.3389/fncom.2021.565244. 

Note regarding artifact rejection:
We advice against using the data directly from the .poly5 files. The primary reason for this is that we had some issues with faulty shielding on some of the electrodes (good shielding is necessary for dry-contact electrodes). This caused signal leakage between electrodes, which is highly unwanted, and which could make the ear-EEG channels contain PSG data, even after rereferencing. We went to great lengths to identify these electrodes, using both algorithms and physical inspection of all electrodes between recordings, and are confident that there are no issues in the .set files (for which these electrodes have been set to 'NaN'). Note that that this identification and discarding is the only preprocessing which has been done to the EEG data. 

For questions regarding this data set, contact: 
Kaare Mikkelsen, Mikkelsen.kaare@ece.au.dk, https://orcid.org/0000-0002-7360-8629

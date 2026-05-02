Understanding how the brain engages with poetic language is key to advancing empirical research on aesthetic and creative cognition. This experiment involved 64-channel EEG recordings and behavioural ratings from 51 participants who read and evaluated 210 short English-language texts — 70 Haiku (nature-themed), 70 Senryu (emotion-themed), and 70 non-poetic Control texts. Each poem/text was rated on five subjective dimensions: Aesthetic Appeal, Vivid Imagery, Being Moved, Originality, and Creativity — using a 7-point scale.

The full study involved 51 participants, and the data were divided into two BIDS-compliant datasets to ensure technical validation and facilitate upload to OpenNeuro. 

Poetry Assessment EEG Dataset 1 (this dataset) contains data from 47 participants whose continuous EEG recordings passed technical validation and were used in the primary analyses. In this dataset, the participants.tsv file maps anonymized BIDS IDs (sub-001 to sub-047) to the original participant codes used during data collection (P101–P151) 

Poetry Assessment EEG Dataset 2 includes the remaining 4 participants (P105, P141, P142, P146), whose EEG recordings were acquired in segments due to session interruptions and later concatenated during preprocessing. These participants were excluded from the PSD analysis to avoid potential artifacts but are included here for completeness and transparency.

Dataset Structure and Navigation: 
Each subject folder contains four core EEG files:

channels.tsv – EEG channel metadata
eeg.json – EEG recording metadata
eeg.set – Raw EEG data (EEGLAB format)
events.tsv – Event markers aligned with poem presentation

The /code/ directory includes:

Preprocessing.m – MATLAB preprocessing script
BioSemi64.loc – 64-channel coordinate file

The /derivatives/ directory contains:

Behavioural_Ratings/ – One .csv file per participant (e.g., P101.csv), including trial-by-trial ratings across five dimensions: Aesthetic Appeal, Vivid Imagery, Emotional Impact (labeled as 'being moved'), Originality, and Creativity.

Psychometric_Responses/ – A single .csv file with demographic and trait-level questionnaire responses per participant, including: PANAS (mood), Openness, Curiosity, VVIQ (visual imagery), AVIQ (auditory imagery), MAAS (mindfulness), and AReA (aesthetic responsiveness).

Also includes questionnaires.pdf with full questionnaire texts and scoring keys

The /stimuli/ directory includes:

All 210 texts used in the experiment: 70 Haiku (nature-themed poetry), 70 Senryu (emotion-themed poetry), 70 Control (non-poetic matched prose).

Block-wise trial assignments for all seven blocks

Resting-state EEG was recorded at the beginning and end of each session. These segments are embedded within the raw EEG files and can be identified using the following trigger codes in events.tsv:

65285, 65286 → Resting state (before experiment); 65287, 65288 → Resting state (after experiment)

Interested users may also consult Poetry Assessment EEG Dataset 2 to access recordings from the remaining 4 participants excluded from the main analyses. All preprocessing steps, event markers, and metadata structures were applied identically across both datasets (Poetry Assessment EEG Dataset 1 and Poetry Assessment EEG Dataset 2), ensuring consistency. This enables users to apply their own quality control pipelines and include these data if desired.

Of note, the anonymized participant IDs (e.g., PXXX) are used consistently across all data modalities, enabling reliable cross-referencing between EEG data, behavioural ratings, and psychometric responses. Data collection took place at the Department of Psychology at Goldsmiths, University of London, UK. The project was approved by the Local Ethics Committee at the Department of Psychology, Goldsmiths University of London. The experiment was conducted in accordance with the Declaration of Helsinki.


All EEG, behavioural, and psychometric data were anonymized. Participant identifiers were coded (P101–P151), and no names, dates of birth, or other direct identifiers are included.





























                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
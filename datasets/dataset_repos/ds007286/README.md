YaleNeuroConnect is a deeply phenotyped human functional Magnetic Resonance Imaging (fMRI) dataset. The dataset includes 410 diagnostically and demographically diverse participants. 

The dataset includes raw fMRI data of six in-scanner task runs (card guessing, reading the mind in the eyes, gradual onset continuous performance - gradCPT, movie watching, nBack, and stop-signal) and two resting runs. T1-weighted, T2-weighted, and FLASH structural MRI images for each participant are provided. The raw neuroimaging data is stored under each participant's folder. 

In addition, we include processed functional connectivity matrices and mean ROI time courses, processed with the Shen268 and Shen368 functional maps. The functional connectivity matrices are stored under derivatives -> MC_Shen268 and derivatives -> MC_Shen368. The mean ROI time courses are stored under derivatives -> roimean_Shen268 and derivatives->roimean_Shen368.

Three subjects are missing one functional run each (sub-pa0950, sub-pb8448, and sub-pb9916) due to incomplete scan sessions.

A wide range of cognitive, psychiatric, and behavioral scores were collected. Scores were collected using the following test banks: ATQ, BNT, BRIEF, BSI, DKEFS, IRI, MINI, PANAS, PSQI, PSS, WAIS, and WRAML. These scores are listed under the phenotype folder, and each test bank contains multiple scores (tsv file), with a corresponding json file that describes the variables in the tsv file. 

The diagnosis of each participant is listed under phenotype-> diagnosis_binary_table.tsv. 

The dataset also includes quality metrics derived using MRIQC for each participant's T1W, T2W, and fMRI images. These metrics are stored under derivatives->mriqc. 

The code used to display the stimuli during the task fMRI runs is included under derivatives -> task_code.zip. The timestamps for the movie time frames are included under derivatives -> movie_frame_timestamps.

Participants: The dataset was collected at Yale School of Medicine, Magnetic Resonance Research Center, New Haven, Connecticut, USA between February 2018 and May 2025.  

Consent: Written informed consent for participation and data sharing in accordance with a protocol approved by the Yale Institutional Review Board (HIC #2000020891) was obtained from all participants. 

Study design: The study consisted of five parts: 1) MRI scans, 2) self-report questionnaires, 3) demographic and background information, 4) brief psychiatric interview, and 5) a battery of cognitive tests. The whole study takes approximately 2-3 hours. 1) The scanning took approximately 90 minutes during which time anatomical scans and two resting fMRI runs and six task fMRI runs were run. 2) Following the scans, the participant was brought to the behavioral testing room where they completed a set of questionnaires regarding mood and sleep assessments. 3) The participant filled out a diagnostic and background information form, which included questions about mental health or neurological diagnoses, current medications, highest level of education, occupation, and annual household income. Study coordinators next conducted a 4) brief psychiatric interview and 5) administered a battery of cognitive tests.

MRI Acquisition Protocol: The imaging data were collected at Yale on a 3T Siemens Prisma scanner with a 64-channel head coil. A high-resolution 3D anatomical scan (T1-weighted magnetization-prepared rapid acquisition with gradient-echo (MPRAGE) sequence [208 slices acquired in the sagittal plane, repetition time (TR)= 2,400 ms, echo time (TE) = 1.22 ms, flip angle = 8°, slice thickness = 1 mm, in-plane resolution = 1 mm × 1 mm]) was obtained for alignment to common space. The functional data were obtained using a multiband gradient-echo-planar imaging (EPI)43 sequence (75 slices acquired in the axial-oblique plane parallel to the AC–PC line, TR = 1,000 ms, TE = 30 ms, flip angle = 55°, slice thickness = 2 mm, multiband factor = 5, in-plane resolution = 2 mm × 2 mm). Each of the six-task runs and two-resting-state runs was acquired over 6 minutes and 49 seconds, for a total of more than 48 minutes of fMRI data per subject. The total MRI session was less than 90 minutes.

More information about the dataset can be found here: https://pmc.ncbi.nlm.nih.gov/articles/PMC12338928/

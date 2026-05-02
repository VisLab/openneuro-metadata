## Reduced Threat-Related Neural Efficiency: A Possible Biomarker for Pediatric Anxiety Disorder

A comprehensive dataset characterizing a sample of youth aged 8 to 18 years using clinical assessments, structural magnetic resonance imaging (sMRI), and functional magnetic resonance imaging (fMRI).

Data was collected at the National Institute of Mental Health (NIMH), Bethesda, Maryland by the Section on Development and Affective Neuroscience (SDAN). The pre-processing and analysis scripts are shared on the study GitHub repository (https://github.com/NIMH-SDAN/Neural.Efficiency.2025). This dataset allows an array of investigations into brain function and anxiety in youth.

This dataset is licensed under the Creative Commons Zero (CC0) v1.0 License.

## Participant Eligibility and Characteristics

### Inclusion Criteria

##Participants in the study met the following inclusion criteria:
Aged 8 to 18 years and spoke English
Met the criteria for an anxiety disorder (i.e., separation anxiety disorder, generalized anxiety disorder, social phobia, panic disorder) as assessed with the KSADS.
Did NOT meet the criteria for any psychiatric disorder (i.e., healthy volunteer, HV) as assessed with the KSADS

### Exclusion Criteria
Participants meeting any of the criteria listed below were excluded from the study:
Neurological disorders
Pervasive developmental disorders (e.g., autism spectrum disorder)
Psychosis
Bipolar disorders
Substance use
Externalizing disorders such as oppositional defiant disorder (ODD)
Any medical condition that increases risk for MRI (e.g., pacemaker, metallic foreign body in eye, dental braces)
MRI contraindications (e.g., claustrophobia, pregnancy)
Full-scale IQ < 70

### Consent
Institutional Review Board approval, parent or guardian consent, and child assent were obtained. To characterize the sample, we collected data on participants' race/ethnicity and family income.

### Clinical Measures
Completed by Participants :
Screen for Child Related Anxiety Disorders (youth-SCARED)
Wechsler Abbreviated Scale of Intelligence (WASI)

### Completed by Participants' parents/caregivers:
Screen for Child Related Anxiety Disorders (parent-ARI)

### Completed by Clinicians:
Kiddie Schedule for Affective Disorders (KSADS)
Children's Global Assessment Scale (CGAS)
Pediatric Anxiety Rating Scale (PARS)

## Imaging Protocol
Before and after treatment, data on brain structure and function were acquired on a 3.0 Tesla General Electric scanner with an 8- (Cohort 1) or 32-channel (Cohort 2) head coil.

### Functional magnetic resonance imaging data during rest
Blood-oxygen-level-dependent (BOLD) changes were measured with a T2*-weighted sequence while participants passively viewed a fixation cross for 12 minutes (i.e., resting-state). In both cohorts, the repetition time (TR) was 2000 msec. In cohort 1, the echo time (TE) was 30 msec. In cohort 2, multiple echoes were recorded (TE1, 2, 3 = 14.8, 28.4, 42.0 msec). In cohort 1, the flip angle was 90° and in cohort 2, 77°. Across both cohorts, the matrix size was 64x64. However, in cohort 1, we acquired 36 axial interleaved slices with a slice thickness of 4 mm, whereas in cohort 2, we acquired 34 slices with a slice thickness of  3.8 mm.

### Functional magnetic resonance imaging data during the dot-probe task
We also acquired functional magnetic resonance imaging data during a 14-minute emotional dot-probe task. In both cohorts, the TR was 2300 msec, the matrix size was 96x96, and the slice thickness was 3 mm. However, there were differences between cohorts in the echo time (cohort 1: 25 msec, cohort 2: 30 msec), the flip angle (cohort 1: 50°, cohort 2: 70°), and the number of the axial interleaved slices (cohort 1: 41, cohort 2: 44). Further, task data was acquired before the resting-state scan in cohort 1, but that order was reversed in cohort 2

### T1-weighted Scans
Acquired for most participants with TR = 7.6 ms, TE = 3.5 ms, no gap, matrix size = 256x256. Depending on the participant's head size, there were different numbers of slices acquired, although this was 176 slices for most participants in the sample. The slice thickness = 1 mm. 

## Description of Data Formats and Preparation

### Clinical Measures Data
Each clinical assessment has a tabular data file (TSV format) and a corresponding data dictionary (JSON format). The n/a values indicate that the question may have been skipped over by the participant or not presented to/asked of the participant.

### Imaging Data
Imaging data in this study is distributed in NifTI format. The images were acquired with a 3.0 Tesla field strength and were oriented in the axial plane. Visual inspection was performed to exclude any images with significant artifacts or distortions.

We have de-identified the anatomical scans by defacing the scans using the DSST Defacing Pipeline.

### Shared dataset  
Of the 206 enrolled participants, 149 participants consented to share their data publicly and are therefore included in the dataset. 
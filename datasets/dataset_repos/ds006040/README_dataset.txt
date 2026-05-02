1. Dataset Description
This dataset comprises neuroimaging data collected at the Center for Neuroscience Imaging Research (CNIR) at Sungkyunkwan University, the Institute for Basic Science. It includes simultaneous recordings of electroencephalography (EEG), functional magnetic resonance imaging (fMRI), and diffusion-weighted imaging (DWI) from 29 participants aged 19 to 42 years. However, participant sub-003 requested to discontinue the experiment due to difficulties during the EEG-fMRI scan session, and therefore, this participant was excluded from the dataset.

The EEG data comprises 64-channel recordings obtained using a customized Brain Products BrainCapMR, featuring 63 cortical channels and one ECG channel (channel 32) positioned on the back. Additionally, behavioral data from attentional tasks performed inside the scanner were recorded. All participants provided informed consent in compliance with the Institutional Review Board (IRB) guidelines of Sungkyunkwan University. Demographic information and self-reported measures, including personality ratings based on the Big Five Inventory (BFI), were also collected. The study's primary objective is to advance the understanding of brain states during attentional fluctuations by examining the relationship between electrical activity and hemodynamic changes using integrated neuroimaging data.

2. Convert dataset into BIDS compliant format

[2.1 Raw fMRI data into BIDS format]
% dcm2bids version: 2.1.7
% functional data
sub-[subject ID:3 digit number]_task-[task]_run-[run number:1 digit number]_bold.nii.gz
% anatomical data
sub-[subject ID:3 digit number]_T1w.nii.gz
% the file name of behavior record
sub-[subject ID:3 digit number]_task-[task]_run-[run number:1 digit number]_beh

% Example
subject ID : 000
task       : checkerboard
run number : 1

Then, the file name should be "sub-000_task-CB_run-1_bold.nii.gz" / "sub-000_T1w.nii.gz"

[2.2 Raw EEG data into BIDS format]
sub-[subject ID:3 digit number]_task-[task][scanner ON/OFF]_run-[run number:1 digit number]

% Example
subject ID : 000
task       : CB
scanner    : OFF
run number : 1

Then, the file name should be "sub-000_task-CBOFF_run-1".

---------------------------------------------------------------------------------------------------------------

<Read Me for EEG>

1. BIDS converted task name patterns

- The filenames for the EEG data follow the pattern below:

a. Task Names
[Resting-state]
xx_task-EOxx_xx           : Eyes Open
xx_task-ECxx_xx           : Eyes Closed

[Visual task]
xx_task-CBxx_xx           : Checkerboard (15Hz)

[Attentional tasks]
xx_task-GRADxx_xx       : GradCPT
xx_task-IMAGxx_xx       : Imagery
xx_task-IMGRADxx_xx   : GradCPT with Imagery

b. Session Identifiers
xx_task-xxON_xx          : ON session (fMRI ON, EEG ON. Inside the scanner)
xx_task-xxOFF_xx         : OFF session (fMRI OFF, EEG ON. Inside the scanner)

c. Preprocessed files
xx_desc-anc0gradrm_xx : ANC 0 (Artifact Noise Correction 0), gradient removed file
xx_desc-anc0qrsrm_xx   : ANC 0, QRS artifact removed file

---
2. Trigger Information for tasks

- The following triggers are used in the data:

[task-CB (Checkerboard Task)]
S254 : Start of Checkerboard
S155 : Stop of Checkerboard

[task-GRAD and task-IMGRAD (GradCPT and GradCPT with Imagery)]
S245 : Start of GradCPT
S155 : Stop of GradCPT

---
3. Known Issues

- Trigger Count Discrepancies:

[task-CBOFF (Typically 4 sets, 1 set = S254, S155)]
sub-001_task-CBOFF_run-1_eeg (5 sets)
sub-001_task-CBOFF_run-1_desc-anc0qrsrm_eeg (5 sets)
sub-007_task-CBOFF_run-1_eeg (5 sets)
sub-007_task-CBOFF_run-1_desc-anc0qrsrm_eeg (5 sets)

[task-CBON (Typically 7 sets, 1 set = S254, S155)]
sub-028_task-CBON_run-1_eeg (6 sets)
sub-028_task-CBON_run-1_desc-anc0gradrm_eeg (6 sets)
sub-028_task-CBON_run-1_desc-anc0qrsrm_eeg (6 sets)

- In cases where TR information was not recorded due to connection issues, the first TR signal was manually identified based on the regularity of the noise and marked accordingly. Additionally, the calculation process was performed based on the EEG task triggers.

[List of files]
sub-025_task-CBON_run-1_eeg
sub-025_task-CBON_run-1_desc-anc0gradrm_eeg
sub-025_task-CBON_run-1_desc-anc0qrsrm_eeg
sub-025_task-GRADON_run-1_eeg
sub-025_task-GRADON_run-1_desc-anc0gradrm_eeg
sub-025_task-GRADON_run-1_desc-anc0qrsrm_eeg

---
4. Data Preprocessing

- Artifact correction is reflected in the following preprocessed files:  
xx_desc-anc0gradrm_xx : Gradient artifacts removed  
xx_desc-anc0qrsrm_xx   : QRS artifacts removed  


---------------------------------------------------------------------------------------------------------------

<Read Me for fMRI>

1. BIDS converted task names
[Resting-state]
Eyes-open            : EO
Eyes-closed          : EC

[Visual task]
Checkerboard         : CB

[Attentional task]
gradCPT              : GRAD
Imagery              : IMAG
gradCPT with Imagery : IMGRAD


2. TR information for tasks

Task names       : GRAD_run-1, GRAD_run-2, GRAD_run-3, IMAG_run-1, IMAG_run-2, EC_run-1, EO_run-1, IMGRAD_run-1, IMGRAD_run-2
Task duration(s) : 360 seconds
Duration per TR  : 2 seconds
Total # of TR    : 190
* for all GRAD runs *
Analysed TR      : 5-175 (10-350s)
Subject excluded from the validation of the paper due to quality of EEG and fMRI data
: sub-003, sub-006, sub-007, sub-008, sub-024, sub-025, sub-026, sub-027

Task name        : CB_run-1
Task duration(s) : 360 seconds (15s+35s)*7
Duration per TR  : 2 seconds
Total # of TR    : 190 (sub-001~sub-022) // 184 (sub-002, sub-023~sub-029)
Analysed TR      : 4-180 (8-360s)
Subject excluded from the validation of the paper due to EEG channel removal and quality of EEG and fMRI data
 : sub-003, sub-004, sub-006, sub-007, sub-008, sub-009, sub-012, sub-015, sub-020, sub-025


3. Exclude nth TRs with responses in imagery tasks

 Tasks : IMAG_run-1, IMAG_run-2,  IMGRAD_run-1  , IMGRAD_run-2
Sub-001:     86    ,     86    ,       65       ,       79
Sub-002:     85    ,     84    ,       61       ,       81 
Sub-003:     85    ,   50-186  , 54-113;153-183 , 104-124;139-149;172-176;182-186
Sub-004:     86    ,     87    ,       --       ,       82 
Sub-005:     --    ,     86    ,       68       ,       72 
Sub-006:     83    ,     85    ,       81       ,       84 
Sub-007:     85    ,     85    ,       76       ,       69 
Sub-008:    105    ,     91    ,       91       ,       91  
Sub-009:     91    ,     91    ,       91       ,       91  
Sub-010:     91    ,     91    ,       91       ,       97
Sub-011:     91    ,     --    ,      100       ,       93
Sub-012:     91    ,     91    ,       91       ,       91
Sub-013:     97    ,     91    ,       95       ,       91
Sub-014:     --    ,   7-8;91  ,       96       ,       --
Sub-015:     91    ,     95    ,       93       ,       90
Sub-016:     --    ,     --    ,       --       ,       --
Sub-017:    105    ,     91    ,      100       ,       93
Sub-018:     91    ,     91    ,       91       ,       94
Sub-019:     91    ,     91    ,       91       ,       91
Sub-020:     91    ,     91    ,       91       ,       94
Sub-021:     91    ,     91    ,       91       ,       91
Sub-022:     92    ,     91    ,       91       ,       91
Sub-023:     91    ,     91    ,       91       ,       91
Sub-024:    100    ,     92    ,       92       ,       90
Sub-025:     90    ,     90    ,       90       ,       90
Sub-026:     91    ,     91    ,       91       ,       91
Sub-027:     --    ,     98    ,       98       ,       90
Sub-028:     91    ,    110    ,       91       ,       91
Sub-029:     91    ,     91    ,       91       ,       91

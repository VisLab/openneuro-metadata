# HaD-PET: FDG-PET dataset of acute DMT plus harmine effects on brain glucose metabolism

## Overview
This dataset contains raw and selected derivative neuroimaging data from a single-blind, placebo-controlled, randomized crossover study investigating the acute effects of an oromucosal formulation of N,N-dimethyltryptamine (DMT) combined with harmine on cerebral glucose metabolism in healthy volunteers.

The dataset is organized according to BIDS and includes:
- T1-weighted structural MRI scans
- Dynamic brain [18F]FDG-PET scans from two study sessions per participant
- Participant-level metadata in `participants.tsv`
- Selected preprocessing and modeling derivatives under `derivatives/`
- Processing scripts and command records under `code/`

## Study design
Fourteen healthy male participants completed both imaging sessions in a within-subject crossover design. Each participant underwent:
- one placebo session
- one active drug session with buccal DMT plus harmine

Drug administration consisted of three equal dose increments given 20 minutes apart, for a total dose of:
- DMT: 90 mg
- harmine: 120 mg

Approximately 100 minutes after the first administration, participants underwent a resting-state [18F]FDG-PET scan during the peak drug-effect window. PET data were acquired for approximately 67 minutes on a Siemens Biograph Vision Quadra long-axial-field-of-view PET/CT scanner. Structural T1-weighted MRI scans were acquired separately and used for anatomical processing and surface-based normalization.

## Primary aim
The primary aim of the study was to test whether acute DMT plus harmine increases the cerebral metabolic rate of glucose consumption (CMRglc) relative to placebo. Secondary analyses examined the spatial distribution of these effects across the cortical surface and canonical resting-state networks.

## Participants
- N = 14 completers
- healthy adult male volunteers
- age range: 25-43 years
- all participants had prior psychedelic experience

## Ethics and registration
- Approved by the Cantonal Ethics Committees of Bern and Zurich (BASEC-ID: 2022-01515)
- Exemption for DMT administration granted by the Swiss Federal Office of Public Health
- Registered at ClinicalTrials.gov: NCT06252506
- All participants provided written informed consent

## Associated publication
Egger K, Bozsak R, Aicher HD, Sari H, Poetzsch SN, Rominger A, Martin-Soelch C, Smallridge JW, Dornbierer D, Quednow BB, Scheidegger M, Cumming P.  
*Global Increases in Brain Glucose Metabolism Following Acute N,N-Dimethyltryptamine and Harmine Administration in Healthy Volunteers: A randomised [18F]FDG-PET Study.*  
Journal of Cerebral Blood Flow & Metabolism (2026). 
https://doi.org/10.1177/0271678X261454172

## Funding
Swiss National Science Foundation, grant 320030-204978.

## Contact
For questions regarding the dataset, please contact:

**Klemens Egger**  
Psychedelic Research & Therapy Development Lab  
University Hospital of Psychiatry Zurich  
✉️ klemens.egger@bli.uzh.ch
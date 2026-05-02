# FOUNDCOG Data Release v1
This release includes the shareable data collected from 2-month and 9-month old infants who completed the FOUNDCOG pictures task at Trinity College Institute of Neuroscience.

- 172 5-min awake fMRI sessions from 84 2-month-olds and 65 runs from 42 9-month-olds.
- Single band reference scans, in opposite phase encoding directions, used for susceptibility distortion correction using FSL Topup are included per session.
- We share only the raw data from infants whose caregivers gave explicit consent and "permission for pseudo-anonymized data, including the brain imaging data, to be shared with the scientific community and the general public via a fully open database on the internet."
- Participants recruited from the NICU have also been excluded from this fully open database, as per the ethical approval for the study.
- Participants also completed a videos awake fMRI task, resting state, and anatomicals. These are being prepared and will be shared with upcoming publications.


### Guide to Participant IDs
sub-(timepoint in months)(identifier)
- Months is either 2 or 9, depending on the scan session.
- Each subject has a unique 3 digit identifier.
- E.g. participant 033 was scanned at approx. 2-months (sub-2033) and 9-months (sub-9033).
- The corrected gestational age at time of scanning for each subject can be found in participants.tsv.

### Experimental code
- The paradigm was run using Psychopy, the protocol can be found at [https://github.com/ClionaOD/foundcog_paradigm](https://github.com/ClionaOD/foundcog_paradigm)
- Preprocessing used a custom in-house pipeline. This is currently being prepared for sharing and will be made available at [https://github.com/ClionaOD/foundcog_analysis](https://github.com/ClionaOD/foundcog_analysis). 
- The GLM used to generate betas is being prepared for sharing and will be made available at [https://github.com/ClionaOD/foundcog_analysis](https://github.com/ClionaOD/foundcog_analysis).   

## O'Doherty et al. (2025), Nature Neuroscience MVPA Analysis
- Betas available in derivatives/foundcog_glm/betas. Beta values and vcov measurements are shared from the whole brain, aligned to age-appropriate template space. Betas with vcov > 10 were masked from downstream RDM analyses, as described in the paper.
- Fully anonymised RDMs, including n=101 2-month-olds and n=44 9-month-olds are available in derivatives/foundcog_rdms/.
- - Some raw data that was included in the publication has not been shared here. This is the case for infants recruited from the NICU and those whose caregivers did not consent to open sharing. 
- The code used for analysis is being prepared and can be found [https://github.com/ClionaOD/foundcog_analysis](https://github.com/ClionaOD/foundcog_analysis).

### The following runs were excluded from the analysis presented in this publication
- reason: why the run was excluded.
    - motion_1.5mm: >50% of frames had FWD >1.5 mm.
    - manual: scan operator deemed the run of poor quality on day of scanning.
    - terminated: the run was ended too early due to fussiness.
- allruns: whether the subject was excluded entirely from analysis as a result.


| sub        | ses | run | reason        | allruns |
|------------|-----|-----|---------------|---------|
| sub-2000   | 1   | 2   | motion_1.5mm  | False   |
| sub-2000   | 1   | 1   | motion_1.5mm  | False   |
| sub-2008   | 1   | 2   | motion_1.5mm  | False   |
| sub-2008   | 1   | 1   | motion_1.5mm  | False   |
| sub-2010   | 1   | 1   | manual        | False   |
| sub-2010   | 1   | 2   | manual        | False   |
| sub-2013   | 2   | 1   | manual        | False   |
| sub-2014   | 1   | 1   | terminated    | True    |
| sub-2015   | 1   | 2   | motion_1.5mm  | False   |
| sub-2021   | 1   | 2   | manual        | True    |
| sub-2021   | 1   | 1   | manual        | True    |
| sub-2022   | 2   | 1   | motion_1.5mm  | False   |
| sub-2028   | 2   | 1   | motion_1.5mm  | False   |
| sub-2029   | 1   | 1   | motion_1.5mm  | False   |
| sub-2033   | 1   | 2   | motion_1.5mm  | False   |
| sub-2035   | 2   | 2   | motion_1.5mm  | True    |
| sub-2035   | 2   | 1   | motion_1.5mm  | True    |
| sub-2039   | 1   | 1   | motion_1.5mm  | True    |
| sub-2042   | 1   | 1   | motion_1.5mm  | False   |
| sub-2043   | 1   | 3   | motion_1.5mm  | False   |
| sub-2043   | 1   | 1   | motion_1.5mm  | False   |
| sub-2044   | 2   | 1   | manual        | False   |
| sub-2053   | 1   | 1   | motion_1.5mm  | True    |
| sub-2055   | 2   | 1   | manual        | False   |
| sub-2056   | 1   | 1   | manual        | False   |
| sub-2057   | 1   | 2   | motion_1.5mm  | False   |
| sub-2058   | 1   | 1   | motion_1.5mm  | False   |
| sub-2058   | 2   | 2   | terminated    | False   |
| sub-2061   | 1   | 1   | motion_1.5mm  | False   |
| sub-2077   | 2   | 1   | motion_1.5mm  | False   |
| sub-2084   | 1   | 2   | motion_1.5mm  | False   |
| sub-2086   | 1   | 2   | manual        | False   |
| sub-2090   | 2   | 1   | manual        | False   |
| sub-2095   | 2   | 3   | manual        | False   |
| sub-2095   | 2   | 2   | motion_1.5mm  | False   |
| sub-2095   | 2   | 1   | manual        | False   |
| sub-2100   | 1   | 2   | terminated    | False   |
| sub-2101   | 2   | 1   | motion_1.5mm  | True    |
| sub-9002   | 1   | 1   | motion_1.5mm  | True    |
| sub-9005   | 1   | 2   | manual        | False   |
| sub-9007   | 1   | 1   | motion_1.5mm  | True    |
| sub-9014   | 1   | 2   | manual        | False   |
| sub-9014   | 2   | 1   | manual        | False   |
| sub-9017   | 1   | 1   | motion_1.5mm  | True    |
| sub-9019   | 1   | 1   | motion_1.5mm  | False   |
| sub-9022   | 1   | 1   | manual        | True    |
| sub-9022   | 1   | 2   | manual        | True    |
| sub-9038   | 1   | 1   | manual        | True    |
| sub-9040   | 1   | 1   | manual        | True    |
| sub-9070   | 1   | 1   | terminated    | False   |
| sub-9074   | 1   | 1   | motion_1.5mm  | True    |
| sub-9078   | 1   | 1   | terminated    | True    |


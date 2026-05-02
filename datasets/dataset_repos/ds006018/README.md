## The Cognitive Electrophysiology in Socioeconomic Context in Adulthood Dataset

# Data Description
This dataset comprises electroencephalogram (EEG) data collected from 127 young adults (18-30 years), along with retrospective objective and subjective indicators of childhood family socioeconomic status (SES), as well as SES indicators in adulthood, such as educational attainment, individual and household income, food security, and home and neighborhood characteristics. The EEG data were recorded with tasks directly acquired from the Event-Related Potentials Compendium of Open Resources and Experiments ERP CORE (Kappenman et al., 2021), or adapted from these tasks (Isbell et al., 2024). These tasks were optimized to capture neural activity manifest in perception, cognition, and action, in neurotypical young adults. Furthermore, the dataset includes a symptoms checklist, consisting of questions that were found to be predictive of symptoms consistent with attention-deficit/hyperactivity disorder (ADHD) in adulthood, which can be used to investigate the links between ADHD symptoms and neural activity in a socioeconomically diverse young adult sample. The detailed description of the dataset is accepted for publication in Scientific Data, with the title: "Cognitive Electrophysiology in Socioeconomic Context in Adulthood."


# EEG Recording

EEG data were recorded using the Brain Products actiCHamp Plus system, in combination with BrainVision Recorder (Version 1.25.0101). We used a 32-channel actiCAP slim active electrode system, with electrodes mounted on elastic snap caps (Brain Products GmbH, Gilching, Germany). The ground electrode was placed at FPz. From the electrode bundle, we repurposed 2 electrodes by placing them on the mastoid bones behind the left and right ears to be used for re-referencing after data collection. We also repurposed 3 additional electrodes to record electrooculogram (EOG). To capture eye artifacts, we placed the horizontal EOG (HEOG) electrodes ateral to the external canthus of each eye. We also placed one vertical EOG (VEOG) electrode below the right eye. The remaining 27 electrodes were used as scalp electrodes, which were mounted per the international 10/20 system. EEG data were recorded at a sampling rate of 500 Hz and referenced to the Cz electrode. StimTrak was used to assess stimulus presentation delays for both the monitor and headphones. The results indicated that both the visual and auditory stimuli had a delay of approximately 20 ms. Therefore, users should shift the event-codes by 20 ms when conducting stimulus-locked analyses.


# Notes
Before the data were publicly shared, all identifiable information was removed, including date of birth, date of session, race/ethnicity, zip code, occupation (self and parent), and names of the languages the participants reported speaking and understanding fluently. Date of birth and date of session were used to compute age in years, which is included in the dataset. Furthermore, several variables were recoded based on re-identification risk assessments. Users who would like to establish secure access to components of the dataset we could not publicly share due to re-identification risks, should contact the corresponding researcher as described below. The dataset consists of participants recruited for studies on adult cognition in context. To provide the largest sample size, we included all participants who completed at least one of the EEG tasks of interest. Each participant completed each EEG task only once. The original participant IDs with which the EEG data were saved were recoded and the raw EEG files were renamed to make the dataset BIDS compatible.

The ERP CORE experimental tasks can be found on OSF, under Experiment Control Files: https://osf.io/thsqg/

Examples of EEGLAB/ERPLAB data processing scripts that can be used with the EEG data shared here can be found on OSF:

osf.io/thsqg
osf.io/43H75


Contact
 * If you have any questions, comments, or requests, please contact:
 * Elif Isbell: eisbell@ucmerced.edu


# Copyright and License
This dataset is licensed under CC0.


# References

Isbell, E., Peters, A. N., Richardson, D. M., & Rodas De León, N. E. (2025). Cognitive electrophysiology in socioeconomic context in adulthood. Scientific Data, 12(1), 1–9. https://doi.org/10.1038/s41597-025-05209-z

Isbell, E., De León, N. E. R., & Richardson, D. M. (2024). Childhood family socioeconomic status is linked to adult brain electrophysiology. PloS One, 19(8), e0307406.

Isbell, E., De León, N. E. R. & Richardson, D. M. Childhood family socioeconomic status is linked to adult brain electrophysiology - accompanying analytic data and code. OSF https://doi.org/10.17605/osf.io/43H75 (2024).

Kappenman, E. S., Farrens, J. L., Zhang, W., Stewart, A. X., & Luck, S. J. (2021). ERP CORE: An open resource for human event-related potential research. NeuroImage, 225, 117465.

Kappenman, E. S., Farrens, J., Zhang, W., Stewart, A. X. & Luck, S. J. ERP CORE. https://osf.io/thsqg (2020).

Kappenman, E., Farrens, J., Zhang, W., Stewart, A. & Luck, S. Experiment control files. https://osf.io/47uf2 (2020).

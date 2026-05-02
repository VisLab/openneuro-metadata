This dataset contains de-identified resting-state EEG recordings from individuals with Parkinson’s disease (PD) and age-matched healthy control subjects. All EEG data were recorded using standard clinical EEG systems at Neurology Clinic.
Dataset Purpose:
This dataset was originally used to evaluate whether resting-state EEG can help distinguish subjects who were later deceased from those who remained living (mortality classification). Only de-identified EEG data and mortality labels are included.

Participant Information:
- Participants are labeled as either "living" or "deceased" in participants.tsv
- No other demographic or clinical information (age, cognition, UPDRS, disease duration, etc.) is included per data-sharing guidelines.
- All participant IDs are anonymized following BIDS convention (e.g., sub-PD1301).

EEG Acquisition Details:
- Recording type: Resting-state EEG (eyes open)
- Device: Clinical BrainVision EEG system
- File formats: .vhdr, .eeg, .vmrk
- Sampling rate: 500 Hz
- Montage: Standard 10–20 international system
- Recording condition: “task-rest” (no task)

Data Organization:
Data are structured following the BIDS (Brain Imaging Data Structure) EEG standard:
    sub-<ID>/
        ses-01/
            eeg/
                sub-<ID>_ses-01_task-rest_eeg.vhdr
                sub-<ID>_ses-01_task-rest_eeg.eeg
                sub-<ID>_ses-01_task-rest_eeg.vmrk

Mortality Label Format:
- Living subjects: survival_status = "living"
- Deceased subjects: survival_status = "deceased"

Ethics & Privacy:
All subjects provided consent for EEG recording at the University of Iowa Hospitals and Clinics. The publicly shared version here is fully de-identified and contains no clinical or personal health information other than mortality classification.

Suggested Use:
This dataset can be used to explore EEG biomarkers of mortality risk, EEG signal characteristics in PD, or to build machine learning models for classification.

Questions or requests:
Please contact nandakumar-narayanan@uiowa.edu.

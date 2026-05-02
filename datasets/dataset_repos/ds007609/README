Resting-State EEG and Trait Anxiety
====================================

This dataset contains resting-state EEG recordings from 51 participants,
collected as part of a study examining the relationship between resting-state
EEG alpha/theta power, oscillatory dynamics, and trait anxiety.

Participants
------------
51 right-handed undergraduate students (25 female) from the University of
Alberta, aged 17-51 years (mean = 20.4, SD = 4.9), participated for course
credit.

Authors
-------
Tamari Shalamberidze (a), Kyle Nash (a,b), Jeremy B. Caplan (a,b)
(a) Neuroscience and Mental Health Institute, University of Alberta, Edmonton, AB, Canada
(b) Department of Psychology, University of Alberta, Edmonton, AB, Canada

Corresponding Author: Tamari Shalamberidze (shalambe@ualberta.ca)

Related Publication
-------------------
Shalamberidze, T., Nash, K., & Caplan, J.B. (2025). Resting-state EEG and
trait anxiety. Imaging Neuroscience. https://doi.org/10.1162/IMAG.a.44

Recording
---------
EEG was recorded using a 256-channel EGI HydroCel Geodesic Sensor Net
with Net Amps amplifier. The original sampling rate was 500 Hz.
Online reference was Cz.

Paradigm
--------
Participants completed a resting-state protocol consisting of alternating
1-minute eyes-open (EO) and 1-minute eyes-closed (EC) blocks, repeated
twice (EO-EC-EO-EC), for a total of 4 minutes. Transitions between blocks
were signaled by an auditory beep.

Preprocessing
-------------
Data were preprocessed in EEGLAB (MATLAB) with the following steps:
- Bandpass filter: 0.1-50 Hz
- Line noise removal: CleanLine at 60 Hz and 120 Hz
- Channel rejection: kurtosis-based (2x threshold), applied twice
- Re-referencing to the average
- ICA decomposition (runica, extended)
- Artifact component removal via ICLabel (>0.8 probability threshold) + visual inspection
- Spherical interpolation of removed channels

Phenotype Data
--------------
The phenotype/ directory contains anxiety and personality questionnaire scores:
- STAI: State-Trait Anxiety Inventory (Spielberger et al., 1983)
- TIPI: Ten-Item Personality Inventory, emotional stability subscale (Gosling et al., 2003)
- BIS/FFFS: Behavioural Inhibition Scale and Fight-Flight-Freeze System
  from the RST-PQ (Corr & Cooper, 2016), with Heym and Jackson factor structures.
  BIS data are unavailable for the first 5 participants.

Ethics
------
This study received ethics approval from the University of Alberta
Research Ethics Board. Project Name: "Physiological Bases of Human Memory",
No. Pro00113334.

Funding
-------
Partly supported by the Social Sciences and Humanities Research Council
in Canada (SSHRC), and the Natural Sciences and Engineering Research
Council of Canada (NSERC).

License
-------
This dataset is made available under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

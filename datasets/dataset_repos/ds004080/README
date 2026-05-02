# Dataset description
This dataset consists of 74 patients age 4-51 years old where Cortico-Cortical Evoked Potentials (CCEPs) were measured with Electro-CorticoGraphy (ECoG) during single pulse electrical stimulation. For a detailed description see:

- Developmental trajectory of transmission speed in the human brain. D. van Blooijs¹, M.A. van den Boom¹, J.F. van der Aar, G.J.M. Huiskamp, G. Castegnaro, M. Demuru, W.J.E.M. Zweiphenning, P. van Eijsden, K. J. Miller, F.S.S. Leijten, D. Hermes, Nature Neuroscience, 2023, https://doi.org/10.1038/s41593-023-01272-0  
  ¹ these authors contributed equally.

This dataset is part of the RESPect (Registry for Epilepsy Surgery Patients) database, a dataset recorded at the University Medical Center of Utrecht, the Netherlands. The study was approved by the Medical Ethical Committee from the UMC Utrecht.

## Contact 
- Dorien van Blooijs: D.vanBlooijs@umcutrecht.nl
- Frans Leijten: F.S.S.leijten@umcutrecht.nl
- Dora Hermes: hermes.dora@mayo.edu

# Data organization
This data is organized according to the Brain Imaging Data Structure specification. A community-driven specification for organizing neurophysiology data along with its metadata. For more information on this data specification, see https://bids-specification.readthedocs.io/en/stable/ 

Each patient has their own folder (e.g., `sub-ccepAgeUMCU01` to `sub-ccepAgeUMCU74`) which contains the iEEG recordings data for that patient, as well as the metadata needed to understand the raw data and event timing.

Data are logically grouped in the same BIDS session and stored across runs that indicating the day and time point of recording during the monitoring period.
If extra electrodes were added/removed during this period, the session was divided into different sessions (e.g. ses-1a and ses-1b). 
We use the optional run key-value pair to specify the day and the start time of the recording (e.g. run-021315, day 2 after implantation, which is day 1 of the monitoring period, at 13:15).
The task key-value pair in long-term iEEG recordings describes the patient's state during the recording of this file. The task label is “SPESclin“ since these files contain data collected during clinical single pulse electrical stimulation (SPES). 

Electrode positions include Destrieux atlas labels that were estimated by running Freesurfer on the individual subject MRI scan and taking the most common surface label within a sphere around the electrode. All shared electrode positions were then converted to MNI152 space using the Freesurfer surface based non-linear transformation. We note that this surface based transformation distorts the dimensions of the grids, but maintains the gyral anatomy.

# License
This dataset is made available under the Public Domain Dedication and License CC v1.0, whose full text can be found at 
https://creativecommons.org/publicdomain/zero/1.0/. 
We hope that all users will follow the ODC Attribution/Share-Alike Community Norms (http://www.opendatacommons.org/norms/odc-by-sa/); 
in particular, while not legally required, we hope that all users of the data will acknowledge by citing the following in any publication:
Developmental trajectory of transmission speed in the human brain, D. van Blooijs, M.A. van den Boom, J.F. van der Aar, G.J.M. Huiskamp, G. Castegnaro, M. Demuru, W.J.E.M. Zweiphenning, P. van Eijsden, K. J. Miller, F.S.S. Leijten, D. Hermes, Nature Neuroscience, 2023, https://doi.org/10.1038/s41593-023-01272-0

# Code
Code to analyses these data is available at: https://github.com/MultimodalNeuroimagingLab/mnl_ccepAge

# Acknowledgements 
We thank the SEIN-UMCU RESPect database group (C.J.J. van Asch, L. van de Berg, S. Blok, M.D. Bourez, K.P.J. Braun, J.W. Dankbaar, C.H. Ferrier, T.A. Gebbink, P.H. Gosselaar, R. van Griethuysen, M.G.G. Hobbelink, F.W.A. Hoefnagels, N.E.C. van Klink, M.A. van ‘t Klooster, G.A.P. deKort, M.H.M. Mantione, A. Muhlebner, J.M. Ophorst, P.C. van Rijen, S.M.A. van der Salm, E.V. Schaft, M.M.J. van Schooneveld, H. Smeding, D. Sun, A. Velders, M.J.E. van Zandvoort, G.J.M. Zijlmans, E. Zuidhoek and J. Zwemmer) for their contributions and help in collecting the data, and G. Ojeda Valencia for proofreading the manuscript. 

# Funding
Research reported in this publication was supported by the National Institute of Mental Health of the National Institutes of Health under Award Number R01MH122258 (DH, FSSL, the content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health), the EpilepsieNL under Award Number NEF17-07 (DvB) and the UMC Utrecht Alexandre Suerman MD/PhD Stipendium 2015 (WZ).

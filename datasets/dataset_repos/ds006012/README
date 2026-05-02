# A geometric shape regularity effect in the human brain: MEG dataset

Authors:

* Mathias Sablé-Meyer*
* Lucas Benjamin
* Cassandra Potier Watkins
* Chenxi He
* Maxence Pajot
* Théo Morfoisse
* Fosca Al Roumi
* Stanislas Dehaene

*Corresponding author: [mathias.sable-meyer@ucl.ac.uk](mailto:mathias.sable-meyer@ucl.ac.uk)

## Abstract

The perception and production of regular geometric shapes is a characteristic trait of human cultures since prehistory, whose neural mechanisms are unknown. Behavioral studies suggest that humans are attuned to discrete regularities such as symmetries and parallelism, and rely on their combinations to encode regular geometric shapes in a compressed form. To identify the relevant brain systems and their dynamics, we collected functional MRI and magnetoencephalography data in both adults and six-year-olds during the perception of simple shapes such as hexagons, triangles and quadrilaterals. The results revealed that geometric shapes, relative to other visual categories, induce a hypoactivation of ventral visual areas and an overactivation of the intraparietal and inferior temporal regions also involved in mathematical processing, whose activation is modulated by geometric regularity. While convolutional neural networks captured the early visual activity evoked by geometric shapes, they failed to account for subsequent dorsal parietal and prefrontal signals, which could only be captured by discrete geometric features or by more advanced transformer models of vision. We propose that the perception of abstract geometric regularities engages an additional symbolic mode of visual perception.

## Notes about this dataset

We separately share the fMRI dataset at [https://openneuro.org/datasets/ds006010](https://openneuro.org/datasets/ds006010). Below are some notes about the
MEG dataset of N=20 participants:

* The code for the analyses associated to
  [https://doi.org/10.1101/2024.03.13.584141](https://doi.org/10.1101/2024.03.13.584141)
  are provided at
  [https://github.com/mathias-sm/AGeometricShapeRegularityEffectHumanBrain](https://github.com/mathias-sm/AGeometricShapeRegularityEffectHumanBrain).  
  However, these analyses have been performed on pre-processed data _without_
  this defacing steps. I am not publishing this raw data, but should there be
  discrepancies or problems coming from the defacing, I have a copy of the following
  information, which I may ask for permission to share in specific cases:
    1. The original data
    2. The seed used for the anonymization procedure
    3. The shuffling information.  
* Anonymization (including defacing of the `anat` folder) has been performed
  using the following command:  
  `python -c 'import mne_bids; mne_bids.anonymize_dataset("<input>", "<output>", random_state=<number>, daysback=<number>)'`  
  This has shuffled the participant order, changed the dates, defaced the
  anatomy, and stripped gender information from the dataset.
* The data was pre-processed with the configuration file provided at
  [https://github.com/mathias-sm/AGeometricShapeRegularityEffectHumanBrain/blob/main/MEG/POGS_MEG_config.py](https://github.com/mathias-sm/AGeometricShapeRegularityEffectHumanBrain/blob/main/MEG/POGS_MEG_config.py)
  for `mne-bids-pipeline` with the development version at the time,
  `bce60a79241731bdd03fccffa6cf315a35b33ab2` on
  [https://github.com/mne-tools/mne-bids-pipeline/](https://github.com/mne-tools/mne-bids-pipeline/)

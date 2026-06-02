# End-to-End Evaluation of White Matter Microstructure of the Visual Pathway in Asymmetric Glaucoma

This dataset follows the [BIDS](https://bids.neuroimaging.io) specification (v1.10.1) and contains raw diffusion-weighted and anatomical MRI data acquired for the study *"End-to-end evaluation of white matter microstructure of the visual pathway in asymmetric glaucoma"* (Coutiño et al., 2025).

## Overview

The dataset includes multi-shell diffusion MRI, fieldmap images for susceptibility correction, and anatomical T1-weighted and FLAIR images.  
Participants include both **asymmetric glaucoma patients** and **healthy controls** scanned at the Institute of Neurobiology, UNAM (Querétaro, Mexico).

## Participants

- Total number of participants: 62
- Groups:  
  - Asymmetric glaucoma patients  
  - Age-matched healthy controls  
- Demographic information is provided in `participants.tsv`.  

## MRI Acquisition

- **Scanner:** GE Discovery MR750 3T (32-channel head coil)  
- **Location:** MRI Unit, Instituto de Neurobiología, UNAM  
- **Sequences:**
  - `dwi/`: Multi-shell diffusion-weighted images acquired with Hyperband (HB) and/or MUSE protocols (`acq-hb` / `acq-muse`)  
  - `fmap/`: EPI-based fieldmaps (`_epi`) for distortion correction (PhaseEncodingDirection and TotalReadoutTime specified in JSONs)  
  - `anat/`: T1-weighted and FLAIR anatomical scans  

Detailed acquisition parameters (TE, TR, voxel size, slice timing, etc.) are provided in the corresponding JSON sidecars.

## Data Organization

- The dataset is structured in standard BIDS hierarchy:  
sub-/anat/
sub-/dwi/
sub-*/fmap/

## Intended Use

This dataset is intended for research in diffusion MRI modeling, glaucoma-related neurodegeneration, and fixel-based analysis (FBA).  
It supports comparison between classical tensor models (DTI, DKI) and multi-tensor or orientation distribution approaches (CSD, MRDS, TODI).

## Ethics Statement

MRI data were collected under ethical approval from:  
- The **Research Ethics Committee** of the Institute of Neurobiology (UNAM)  
- The **Bioethics Committee** of the Instituto Mexicano de Oftalmología (IMO)  

All participants provided written informed consent according to the Declaration of Helsinki.

## Funding and Acknowledgements

This project was supported by:
- UNAM PAPIIT grant IN213423  
- CONAHCYT grant CF-2023-I-218  
- National Laboratory for MRI (CONAHCYT/SECIHTI)  
- CONAHCYT doctoral fellowship (CVU 1288997)

We thank Dr. Erick Pasaye for MRI support, Luis Aguilar for analysis assistance, and the technical staff (Mirelta Regalado, Leopoldo González-Santos, Juan Ortiz-Retana, Moisés Baltazar) for their help during data collection.

## Citation

If you use this dataset, please cite:

> Coutiño D, Guerrero J, Domínguez-Frausto C.A., García-Guillén M., Coronado-Leija R., Ramírez-Manzanares A., Hernández-Gutiérrez E., Descoteaux M., Ayala M., Badillo M., Concha L. (2025). *End-to-end evaluation of white matter microstructure of the visual pathway in asymmetric glaucoma.* bioRxiv. https://doi.org/10.1101/2025.10.20.683506

## Contact

For questions regarding the dataset or analysis scripts, please contact:  
**Luis Concha** or **Daniela Coutiño**— Instituto de Neurobiología, UNAM  
Email: [lconcha@unam.mx, danielacoutino9872@gmail.com]



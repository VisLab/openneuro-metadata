# DESIGNER Preprocessed Diffusion Dataset (Early Reading)

**Author:** Moramay Ramos-Flores  
Instituto de Neurobiología, Universidad Nacional Autónoma de México (UNAM), Querétaro, México.

## Description
This dataset contains diffusion-weighted MRI (DWI) data from Spanish-speaking children at the early stages of reading acquisition. All DWI data were preprocessed using the **DESIGNER** pipeline and include the corresponding `.nii.gz`, `.bval`, and `.bvec` files. The dataset supports the study of white‑matter pathways involved in phonological awareness and early reading development.

## Participants
The dataset includes **61 Mexican Spanish-speaking children** between **6.0 and 8.5 years old**, classified as **early readers**.  
All children were monolingual, without neurological, developmental, or psychiatric diagnoses, and had no contraindications for MRI.

## Imaging Modalities
- **DWI**: Multishell diffusion (b = 800 and b = 2500)

## De-identification
All data were fully de-identified prior to release. Diffusion images do not contain facial features, and sensitive metadata fields were removed.

## Study Design
This is a **cross-sectional observational study**. No tasks were performed during MRI acquisition. Reading and phonological assessments were conducted outside the scanner.

## Funding
Funding Sources: DGAPA-PAPIIT Universidad Nacional Autónoma de México IN206825, Google Gift 2021, Secretaría de Ciencias, Humanidades, Tecnología e Innovación  CVU 1061192 (MRF).


## Notes
- Dataset follows the **BIDS** specification.  
- Compatible with DIPY, FSL, MRtrix, and pyAFQ.  
- All diffusion images were preprocessed using the **DESIGNER** pipeline.
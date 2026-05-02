# Tetralogy of Fallot Neurodevelopment Research: An Open-Source Dataset
## 1. Introduction
This dataset presents MRI and neurodevelopmental data from 31 pediatric participants (18 males; age range: 4–33 months) who underwent surgical intervention for Tetralogy of Fallot (TOF) at the Children's Hospital of Nanjing Medical University between 2022 and 2023. The study aims to explore the relationship between neurodevelopmental disorders (NDDs) and perioperative risk factors in congenital heart disease (CHD) patients.
## 2. Dataset Overview
This open-source dataset provides neuroimaging, clinical, and behavioral data for investigating neurodevelopmental outcomes in TOF patients. The dataset is structured as follows:
- Demographic and Clinical Data
  - Age at admission, gender, BMI, family income, parental education
  - Surgery-related metrics: age at surgery, cardiopulmonary bypass (CPB) time, aortic cross-clamp time, mechanical ventilation duration, ICU stay, etc.
  - Hemodynamic and respiratory parameters: tidal volume, oxygen saturation, heart rate, blood pressure
- Neurodevelopmental Assessment Data
  - Wechsler Intelligence Scale (WPPSI-IV) scores for cognitive evaluation
  - GESELL developmental scale assessment for younger participants (<2.5 years)
  - Perioperative monitoring of cerebral oxygenation, EEG, and pulse oximetry
  - Follow-up assessments at 1, 3, 6 months, 1 year, and 2 years post-discharge
- Neuroimaging Data
  - Structural MRI (T1, T2, FLAIR, DWI, DTI): Total brain volume, white/gray matter, cortical thickness, hippocampal volume
  - Functional MRI (if applicable)
  - Diffusion Tensor Imaging (DTI) metrics: Fractional anisotropy (FA), Mean Diffusivity (MD), Radial Diffusivity (RD), Axial Diffusivity (AD)
## 3. Data Acquisition
Neuroimaging data were collected using Siemens Avento 1.5T and Philips Ingenia 3.0T MR scanners. For children under 3 years old, sedation with 5% chloral hydrate (1ml/kg) was used before scanning.
- MRI Sequence Parameters:
  - T1-weighted (3D MPRAGE/TFE): High-resolution anatomical imaging
  - T2-weighted (FSE): Structural integrity assessment
  - FLAIR (Fluid Attenuated Inversion Recovery): Detection of periventricular abnormalities
  - Diffusion-Weighted Imaging (DWI): Water molecule diffusion properties
  - Diffusion Tensor Imaging (DTI): White matter microstructural analysis
- Post-processing Methods:
    - Structural MRI: Cortical segmentation, volumetric analysis
    - DTI Processing: Head motion correction, fiber tracking, FA/MD calculations
    - DWI Analysis: ADC mapping and feature extraction using Python-based MRIcron processing
## 4. Data Access
This dataset is open-source and can be accessed through our research portal: 🔗 GitHub Repository
To apply for dataset access, please complete the online form with the following details:
- Full Name
- Email Address
- Affiliation (Institution/University/Hospital)
- Research Purpose
- Contact Information
- Data access approval is subject to manual review to ensure ethical compliance.
## 5. Ethical Approval
This research has been approved by the Ethics Committee of Nanjing Medical University's Affiliated Children's Hospital. All data collection procedures were conducted in accordance with institutional guidelines. Informed consent was obtained from all participants' guardians before data collection.
## 6. Limitations & Future Directions
- Single-Center Data: Currently, the dataset is limited to a single hospital, potentially limiting generalizability.
- Loss to Follow-Up: Some participants may not complete long-term neurodevelopmental assessments.
- Multi-Factorial Influences: Genetic, environmental, and socio-economic factors may affect neurodevelopment beyond the scope of this study.
- Future Expansion: We aim to extend this dataset to a multi-center collaboration and integrate AI-driven predictive analytics.
## 7. Citation
If you use this dataset in your research, please cite our work:
[Author names], "Tetralogy of Fallot Neurodevelopment Research: An Open-Source Dataset," Children's Hospital of Nanjing Medical University, 2025.

For any inquiries, please contact: xuyang3141@gmail.com

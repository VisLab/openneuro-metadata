This dataset contains multimodal magnetic resonance imaging (MRI) and clinical data acquired prospectively from patients diagnosed with olfactory groove meningioma (OGM). Data were collected before and after surgical treatment using a standardized imaging and assessment protocol. The dataset is intended to support research in neuroimaging, neuro-oncology, and computational neuroscience, with a particular focus on tumor-related brain alterations, peritumoral edema effects, and postoperative recovery.
The dataset includes high-resolution structural MRI, diffusion MRI, resting-state functional MRI, and associated clinical and neuropsychological assessments. 

Participants
* Diagnosis: OGM
* Study design:  prospective, single-center
* Imaging time points: preoperative (folders labeled sub-**) and postoperative (folders labeled sub-**fu, when available)


Modalities included:

Structural MRI
* T1-weighted (pre- and post-contrast)
* T2-weighted

Diffusion MRI
* Multi-direction diffusion-weighted imaging (64 directions, b = 1500 s/mm²)
* Multiple b = 0 volumes with opposite phase-encoding directions for distortion correction

Functional MRI
* Resting-state BOLD fMRI (eyes closed)

Data organization

The dataset follows the BIDS standard and includes the following main directories:
* sub-*/anat/ – structural MRI data
* sub-*/dwi/ – raw diffusion MRI data
* sub-*/func/ – resting-state fMRI data
* derivatives/ – processed data outputs


Derivatives
The derivatives/ directory contains processed imaging data, including:
* Preprocessed diffusion MRI data corrected for susceptibility distortions and eddy currents (topup + eddy)
* Diffusion tensor–derived metrics: fractional anisotropy (FA), mean diffusivity (MD), radial diffusivity (RD), and longitudinal/axial diffusivity (LD/AD)
* Tractography files derived from constrained spherical deconvolution (CSD)
* MRIQC output folder with both participant and group-level analyses

Preprocessing summary
* Structural MRI data were visually inspected and defaced for anonymization.
* Diffusion MRI data were corrected for susceptibility-induced distortions, eddy-current effects, and subject motion.
* Diffusion tensor fitting and constrained spherical deconvolution were performed using ExploreDTI.
* Quality control was conducted at multiple stages to ensure adequate data quality for reuse.

Potential reuse
This dataset may be reused for studies of tumor-related brain changes, diffusion MRI methodology  tractography analyses in the presence of mass lesions, imaging biomarker development using multimodal MRI data. 


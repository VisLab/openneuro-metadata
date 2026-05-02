# Data for "Modeling 2D Spatio-Tactile Population Receptive Fields of the Fingertip in Human Primary Somatosensory Cortex"

Susanne Stoll, Falk Luesebrink, D. Samuel Schwarzkopf, Hendrik Mattern, Peng Liu, Johanna Noelle, and Esther Kuehn

---

This repository contains

- data as reported in our manuscript, which is available as a [preprint](https://doi.org/10.1101/2025.05.24.655840).
- data not presented in our manuscript but related to it, such as fMRI data that were not smoothed or goodness-of-fit values that were statistically adjusted for model complexity and not via a cross-validation procedure.

Please report any issues by sending an email to stollsus@gmail.com. Thank you!

For further information, please refer to our [OSF](https://doi.org/10.17605/OSF.IO/4DRZ6) repository.

---

## Content

### TODO

- Annotate novel .label and .png files (revision 1)
- Annotate files with [...] flag.

---

### Abbreviations

- pRF       = population receptive field.
- BOLD      = blood-oxygen-level-dependent.
- BBR       = boundary-based registration.
- HRF       = hemodynamic response function.
- MRI       = magnetic resonance imaging.
- fMRI      = functional magnetic resonance imaging.
- cR^2      = cross-validated goodness-of-fit.
- diff-cR^2 = differential cross-validated goodness-of-fit.
- cSNR      = cross-validated signal-to-noise ratio.
- aR^2      = goodness-of-fit statistically adjusted for model complexity.
- diff-aR^2 = differential goodness-of-fit statistically adjusted for model complexity.
- D2a       = digit 2, i.e. index finger, with letter-based numeration a. 
- SI        = primary somatosensory cortex. 
- BA3b      = Brodmann area 3b.

---

### Root directory

---

- **dataset_description.json**: File that contains general information about the dataset, such as name, authors, and acknowledgements.

- **task-pRF_bold.json**: File that contains information about the spatio-tactile pRF mapping task that was performed whilst acquiring functional BOLD data (fMRI).

- **derivatives**: Folder that contains subfolders hosting derived data.

- **sub-01**: Folder that contains subfolders hosting raw data for subject 01.

- **sub-02**: Folder that contains subfolders hosting raw data for subject 02.

- **sub-03**: Folder that contains subfolders hosting raw data for subject 03.

- **sourcedata**: Folder that contains subfolders hosting source data.

---

### Layers beyond the root directory — raw data

---

The raw data directory contains data resulting from preprocessing step 2 (see manuscript).

#### sub-01/ses-01/anat

The list below focuses on 'sub-01' and 'ses-01'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03') and sessions ('ses-02' to 'ses-04) are equivalent.

- **sub-01_ses-01_T1w.nii.gz**: File that contains T1-weighted anatomical data (MRI) for subject 01 in session 01.

- **sub-01_ses-01_T1w.json**: File that contains information about how _sub-01_ses-01_T1w.nii.gz_ was acquired.

---

#### sub-01/ses-01/func

The list below focuses on 'sub-01', 'ses-01', and 'run-01'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to 'ses-04), and runs ('run-02' to 'run-10') are equivalent.

- **sub-01_ses-01_task-pRF_run-01_bold.nii.gz**: File that contains functional BOLD data (fMRI) for subject 01 and run 01 in session 01 that were acquired during the spatio-tactile pRF mapping task.

- **sub-01_ses-01_task-pRF_run-01_bold.json**: File that contains information about how _sub-01_ses-01_task-pRF_run-01_bold.nii.gz_ was acquired.

---

### Layers beyond the root directory — source data

---

#### sourcedata/sub-01/ses-01/beh

The list below focuses on 'sub-01', 'ses-01', and 'run-01'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to 'ses-04'), and runs ('run-02' to 'run-10') are equivalent.

- **sub-01_ses-01_task-pRF_run-01_beh.mat**: File that contains behavioral data for subject 01 and run 01 in session 01 that were acquired during the spatio-tactile pRF mapping task.

---

#### sourcedata/sub-01/ses-01+02/acq

The list below focuses on 'sub-01' and 'ses-01+02'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03') and sessions ('ses-03+04') are equivalent.

- **sub-01_ses-01+02_acq.pdf**: File that contains acquisition parameters of the scanning sequences used for subject 01 in session 01 and 02.

---

### Layers beyond the root directory — derivatives (root)

The derivatives (root) directory contains data resulting from preprocessing steps 3 to 8 and 11 to 16 (see manuscript).

---

#### derivatives/sub-01/ses-01/anat

The list below focuses on 'sub-01' and 'ses-01'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03') and sessions ('ses-02' to 'ses-04') are equivalent.

- **sub-01_ses-01_T1w_downsampled_biasCorrected_masked.nii.gz**: Like _sub-01_ses-01_T1w_downsampled_biasCorrected.nii.gz_, but masked.

- **sub-01_ses-01_T1w_downsampled_biasCorrected.nii.gz**: Like _sub-01_ses-01_T1w_downsampled.nii.gz_, but B1-bias-field-corrected.

- **sub-01_ses-01_T1w_downsampled_biasCorrected_Warped.nii.gz**: Like _sub-01_ses-01_T1w_downsampled_biasCorrected.nii.gz_, but warped to _sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_.

- **sub-01_ses-01_T1w_downsampled.nii.gz**: Like _sub-01_ses-01_T1w.nii.gz_, but downsampled.

- **sub-01_ses-01_T1w_downsampled_seg8.mat**: File that contains segmentation parameters including information on B1-bias-field correction associated with _sub-01_ses-01_T1w_downsampled.nii.gz_.

---

#### derivatives/sub-01/ses-all/anat

The list below focuses on 'sub-01', ses-01, and 'job0'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to 'ses-04'), and jobs ('job1' to 'job3') are equivalent.

- **job0_r.sh**: File that contains a series of commands involving _sub-01_ses-01_T1w_downsampled_biasCorrected_masked.nii.gz_ necessary for generating _sub-01_ses-all_T1w_downsampled_biasCorrected_masked_template0.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_masked_sub-01_ses-01_T1w_downsampled_biasCorrected_masked00GenericAffine.mat**: File that contains the transformation matrix aligning
  _sub-01_ses-01_T1w_downsampled_biasCorrected_masked.nii.gz_ to _sub-01_ses-all_T1w_downsampled_biasCorrected_masked_template0.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_masked_template0GenericAffine.mat**: [...]

- **sub-01_ses-all_T1w_downsampled_biasCorrected_masked_template0.nii.gz**: File that contains the initial masked T1-weighted anatomical template across all sessions for subject 01. This template is based on _sub-01_ses-[01-04]\_T1w_downsampled_biasCorrected_masked.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_masked_template0sub-01_ses-01_T1w_downsampled_biasCorrected_masked0WarpedToTemplate.nii.gz**: Like _sub-01_ses-01_T1w_downsampled_biasCorrected_masked.nii.gz_, but warped to _sub-01_ses-all_T1w_downsampled_biasCorrected_masked_template0.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked.nii.gz**: File that contains the final masked T1-weighted anatomical template across all sessions for subject 01. This template is based on _sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked_registered_to_sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0_0GenericAffine.mat**: File that contains transformation matrix coregistering _sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked.nii.gz_ to _sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked_registered_to_sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0_InverseWarped.nii.gz**: Like _sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked.nii.gz_, but inversely warped to _sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked_registered_to_sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0_Warped.nii.gz**: Like _sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked.nii.gz_, but warped to _sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz**: File that contains the unmasked T1-weighted anatomical template across all sessions for subject 01. This template is based on _sub-01_ses-[01-04]\_T1w_downsampled_biasCorrected_Warped.nii.gz_.

- **sub-01_ses-all_T1w_downsampled_biasCorrected_Warped_paths.txt**: File that contains paths to _sub-01_ses-[01-04]\_T1w_downsampled_biasCorrected_Warped.nii.gz_.

---

#### derivatives/sub-01/ses-01/func

The list below focuses on 'sub-01', 'ses-01', and 'run-01'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to 'ses-04'), and runs ('run-02' to 'run-10') are equivalent.

- **sub-01_ses-01_task-pRF_run-01_bold_mean_brainmask.nii.gz**: File that contains the brain mask calculated based on _sub-01_ses-01_task-pRF_run-01_bold_mean.nii.gz_.

- **sub-01_ses-01_task-pRF_run-01_bold_mean_masked.nii.gz**: Like _sub-01_ses-01_task-pRF_run-01_bold_mean.nii.gz_, but masked.

- **sub-01_ses-01_task-pRF_run-01_bold_mean.nii.gz**: File that contains the mean calculated across all images of _sub-01_ses-01_task-pRF_run-01_bold.nii.gz_.

- **sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz**: Like _sub-01_ses-01_task-pRF_run-01_bold.nii.gz_, but coarsely-coregistered to _sub-01_ses-all_T1w_downsampled_biasCorrected_template0_masked.nii.gz_. Note that we skipped the affix 'masked' in the file name to wipe the slate clean and omit potential confusion if further masking procedures were to be applied.

---

#### derivatives/sub-01/ses-all/func

The list below focuses on 'sub-01', 'ses-01', 'run-01', and 'job0'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to 'ses-04'), runs ('run-02' to 'run-10'), and jobs ('job1' to 'job39') are equivalent.

- **job0_r.sh**: File that contains a series of commands involving _sub-01_ses-01_task-pRF_run-01_bold_mean_masked.nii.gz_ necessary for generating _sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0.nii.gz_.

- **sub-01_ses-all_task-pRF_run-all_bold_mean_masked_sub-01_ses-01_task-pRF_run-01_bold_mean_masked00GenericAffine.mat**: File that contains the transformation matrix aligning _sub-01_ses-01_task-pRF_run-01_bold_mean_masked.nii.gz_ to _sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0.nii.gz_.

- **sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0GenericAffine.mat**: [...]

- **sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0.nii.gz**: File that contains the masked functional BOLD template across all sessions for subject 01. This template is based on _sub-01_ses-[01-04]\_task-pRF_run-[01-10]\_bold_mean_masked.nii.gz_.

- **sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0sub-01_ses-01_task-pRF_run-01_bold_mean_masked0WarpedToTemplate.nii.gz**: Like _sub-01_ses-01_task-pRF_run-01_bold_mean_masked.nii.gz_, but warped to _sub-01_ses-all_task-pRF_run-all_bold_mean_masked_template0.nii.gz_.

- **sub-01_ses-all_task-pRF_run-all_paths.txt**: File that contains paths to _sub-01_ses-[01-04]\_task-pRF_run-[01-10]\_bold_mean_masked.nii.gz_.

---

### Layers beyond the root directory — derivatives (FreeSurfer)

The derivatives ([FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall)) directory contains data resulting from preprocessing steps 9 to 10 and 17 to 18 (see manuscript).

---

#### derivatives/FreeSurfer/fsaverage

- **label**, **mri**, **mri.2mm**, **scripts**, **surf**, and **xhemi**: Subfolders that contain [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall)'s average template brain data.

---

#### derivatives/FreeSurfer/sub-01

The list below focuses on 'sub-01'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03') are equivalent.

- **label**, **mri**, **scripts**, **stats**, **surf**, **tmp**, **touch**, and **trash**: Subfolders that contain [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall)'s reconstruction outputs for subject 01 including the anatomical cortical surface model for the left and right brain hemisphere.

---

#### derivatives/FreeSurfer/sub-01/atlas

The list below focuses on 'sub-01' and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03') and brain hemispheres ('lh') are equivalent.

- **rh.\*.label**: Anatomical [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall/) labels including _rh.postcentral.label_ from the gyral-based Desikan-Killiany cortical atlas for the right brain hemisphere of subject 01.

---

#### derivatives/FreeSurfer/sub-01/vol2surf

The list below focuses on 'sub-01', 'ses-01', 'run-01', 'FWHM-1', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to'ses-04'), runs ('run-02' to 'run-10'), surface smoothing kernel widths ('FWHM-0'), and brain hemispheres ('lh') are equivalent.

- **rh_sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0_FWHM-1_BBR.mgh**: Like _sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_, but finely-coregistered to the unmasked anatomical template and resampled to surface vertices using the anatomical cortical surface model for the right brain hemisphere of subject 01, respectively. The fine coregistration consisted of BBR and the resampling was performed with surface smoothing (FWHM = 1 mm).

- **sub-01_ses-01_run-01.dat**: File that contains the transformation matrix from BBR associated with _sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_.

- **sub-01_ses-01_run-01.dat~**: File that contains a backup copy of _sub-01_ses-01_run-01.dat_.

- **sub-01_ses-01_run-01.dat.mincost**: File that contains the minimum costs achieved during BBR associated with _sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_.

- **sub-01_ses-01_run-01.dat.param**: File that contains the BBR transformation parameters associated with _sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_.

- **sub-01_ses-01_run-01.dat.sum**: File that contains a summary of the BBR registration process associated with _sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_.

- **sub-01_ses-01_run-01.log**: File that contains a log of the BBR registration process associated with _sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0.nii.gz_.

- **sub-01_ses-01_run-01.lta**: Like _sub-01_ses-01_run-01.dat_, but in LTA format.

---

### Layers beyond the root directory — derivatives (SamSrf)

The derivatives ([SamSrf](https://github.com/samsrf/samsrf/tree/4de3223950fc4cb995941b2041e2dcc73bb9bbd4)) directory contains data resulting from preprocessing steps 19 to 20, and any analyses performed thereafter (see manuscript).

---

#### derivatives/SamSrf/sub-01/anatomy

The list below focuses on 'sub-01' and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03') and brain hemispheres ('lh') are equivalent.

- **rh_surf.mat**: File that contains subset of reconstructed surfaces (as stored in _derivatives/FreeSurfer/sub-01/surf_) for the right brain hemisphere of subject 01, converted to [SamSrf](https://github.com/samsrf/samsrf/tree/4de3223950fc4cb995941b2041e2dcc73bb9bbd4) MAT format.

---

#### derivatives/SamSrf/sub-01/aperture

The list below focuses on 'sub-01'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03') are equivalent.

- **sub-01_task-prf_aperture-pins.mat**: File that contains a 2D movie aperture reflecting the position of the pins and blank periods per volume during the spatio-tactile pRF mapping task for subject 01.

- **sub-01_task-prf_aperture-pins_vec.mat**: Like _sub-01_task-prf_aperture-pins.mat_, but vectorized.

---

#### derivatives/SamSrf/sub-01/ses-01/FWHM-1

The list below focuses on 'sub-01', 'ses-01', 'run-01' or 'run-all', 'FWHM-1', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to 'ses-04'), runs ('run-02' to 'run-10'), surface smoothing kernel widths ('FWHM-0'), and brain hemispheres ('lh') are equivalent, if not indicated otherwise.

- **rh_sub-01_ses-01_task-pRF_run-01_FWHM-1_BBR_mgh2srf.mat**: Like _rh_sub-01_ses-01_task-pRF_run-01_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0_FWHM-1_BBR.mgh_, but converted to [SamSrf](https://github.com/samsrf/samsrf/tree/4de3223950fc4cb995941b2041e2dcc73bb9bbd4) MAT format, linearly detrended, and _z_-standardized.

- **rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_mean.mat**: Like _rh_sub-01_ses-01_task-pRF_run-01_FWHM-1_BBR_mgh2srf.mat_, but contains the mean calculated across all runs in session 01. The mean is based on _rh_sub-01_ses-01_task-pRF_run-[01-10]\_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0_FWHM-1_BBR.mgh_.

- **rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm_conts.mat**: File that contains the _t_-statistic map for the contrast stimulation vs baseline (rest) calculated based on _rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm.mat_.

- **rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm.mat**: File that contains the beta estimates and residuals of the general linear model analysis performed across all runs in session 01 and using [SPM12](https://www.fil.ion.ucl.ac.uk/spm/software/spm12/)'s canonical HRF. The beta estimates and residuals are based on _rh_sub-01_ses-01_task-pRF_run-[01-10]\_FWHM-1_BBR_mgh2srf.mat_.

- **del_rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_mean.mat** (only present for 'ses-01', 'rh', and 'FWHM-1'): File that contains the manual delineation for the identified fingertip cluster. The delineation was initialized using _rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_mean.mat_ (ergo the file name), but is based on _rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm_conts.mat_.

- **ROIs_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_mean/rh_D2a.label** (only present for 'ses-01', 'rh', and 'FWHM-1'): File in subfolder that contains a [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall)-compatible label called 'D2a' reflecting the delineation stored in _del_rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_mean.mat_.

---

#### derivatives/SamSrf/sub-01/ses-02+03+04/FWHM-1

The list below focuses on 'sub-01', 'FWHM-1', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), surface smoothing kernel widths ('FWHM-0'), and brain hemispheres ('lh') are equivalent, if not indicated otherwise.

- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat** (only present for 'FWHM-1' and 'rh'): File that contains results from the coarse fitting procedure (i.e., constrained grid search fit) for the 2dg model. The fitting was performed using  
  _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean.mat_, the vectorized aperture (see _sub-01_task-prf_aperture-pins_vec.mat_), and [SPM 12](https://www.fil.ion.ucl.ac.uk/spm/software/spm12/)'s canonical HRF.


- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_FneFit.mat** (only present for 'FWHM-1' and 'rh'): Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but contains results from the fine fitting procedure (i.e., unconstrained optimization procedure).

- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.mat** (only present for 'FWHM-1' and 'rh'): File that contains summary statistics associated with _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_FneFit.mat_.

- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the 2dg-fix model.

- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean.mat**: Like _rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_mean.mat_, but contains the mean calculated across all runs in session 02 to session 04. The mean is based on _rh_sub-01_ses-[02-04]\_task-pRF_run-[01-10]\_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0_FWHM-1_BBR.mgh_.

- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit.mat**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the onoff model.

- **src_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat** (only present for 'FWHM-1'): File that contains the search grid and predicted fMRI time series for the coarse fitting procedure (i.e., constrained grid search fit) associated with _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat_.

- **src_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_FneFit.mat** (only present for 'FWHM-1'): Like _src_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the coarse fitting procedure (i.e., constrained grid search fit) associated with _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_FneFit.mat_.

- **src_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat**: Like _src_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the coarse fitting procedure (i.e., constrained grid search fit) associated with _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

- **src_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit.mat**: Like _src_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the coarse fitting procedure (i.e., constrained grid search fit) associated with _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit.mat_.

---

#### derivatives/SamSrf/sub-01/ses-02+03+04-eve/FWHM-1

The list below focuses on 'sub-01', 'FWHM-1', 'ses-02+03+04-eve', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), surface smoothing kernel widths ('FWHM-0'), sessions ('ses-02+03+04-odd'), and brain hemispheres ('lh') are equivalent.

- The files are largely like those in _derivatives/SamSrf/sub-01/ses-02+03+04/FWHM-1_, but for the even-numbered runs of session 02 to session 04 and there are no files involving the 2dg model. Besides, there is a series of additional files:

- **rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_sumstat-cSNR-cR^2.mat**: File that contains summary statistics involving cSNR and cR^2 associated with _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

- **rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_sumstat-diff-cR^2.mat**: File that contains summary statistics involving diff-cR^2 (2dg-fix vs onoff model) associated with _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

- **rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit_sumstat-cSNR-cR^2.mat**: Like _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_sumstat-cSNR-cR^2.mat_, but for summary statistics associated with _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit.mat_ .

---

#### derivatives/SamSrf/sub-01/ses-all/FWHM-1

The list below focuses on 'sub-01', 'FWHM-1', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), surface smoothing kernel widths ('FWHM-0'), and brain hemispheres ('lh') are equivalent.

- **rh_sub-01_ses-all_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean.mat**: Like _rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_mean.mat_, but contains the mean calculated across all runs in all sessions. The mean is based on _rh_sub-01_ses-[01-04]\_task-pRF_run-[01-10]\_bold_registered_to_sub-01_ses-all_T1w_downsampled_biasCorrected_template0_FWHM-1_BBR.mgh_.

---

#### derivatives/SamSrf/simulations/ses-all/prfsize

The list below comprises data simulated using the 2dg model where pRF size was varied. This allowed us to investigate the implausibility of pRF estimates when fitting a 2dg model with unconstrained optimization to the data (see manuscript).

- **sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat**: File that contains results from the coarse fitting procedure (i.e., constrained grid search fit) for the 2dg model. The fitting was performed using _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix.mat_, the vectorized aperture (see _sub-01_task-prf_aperture-pins_vec.mat_), and [SPM 12](https://www.fil.ion.ucl.ac.uk/spm/software/spm12/)'s canonical HRF.

- **sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat**: Like _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but contains results from the fine fitting procedure (i.e., unconstrained optimization procedure).

- **sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.mat**: File that contains summary statistics associated with _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat_.

- **sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix.mat**: File that contains a full simulated data set (called 'ses-all' for consistency with empirical data) for the spatio-tactile pRF mapping task. This simulation is based on 100000 repeats (i.e., 100000 occurrences), a standard deviation for the noise of 2, the 2dg model, the vectorized aperture (see _sub-01_task-prf_aperture-pins_vec.mat_), [SPM 12](https://www.fil.ion.ucl.ac.uk/spm/software/spm12/)'s canonical HRF, and simulated pRFs that match and mismatch the search grid used for the coarse fitting procedure (i.e., constrained grid search fit).

- **sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat**: Like _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but the coarse fitting procedure (i.e., constrained grid search fit) was performed using _sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix.mat_.

- **sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat**: Like _sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but contains results from the fine fitting procedure (i.e., unconstrained optimization procedure).

- **sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.mat**: Like _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.mat_, but for summary statistics associated with _sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat_.

- **sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix.mat**: Like _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix.mat_, but with 1 repeat (i.e., 1 occurrence) and a standard deviation for the noise of 0 (i.e., no noise).
  
- **src_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat**: File that contains the search grid and predicted fMRI time series for the coarse fitting procedure (i.e., constrained grid search fit) associated with _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_.

- **src_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat**: Like _src_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the coarse fitting procedure (i.e., constrained grid search fit) associated with _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat_.

- **src_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat**: Like _src_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the coarse fitting procedure (i.e., constrained grid search fit) associated with _sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_.

- **src_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat**: Like _src_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_CrsFit.mat_, but for the coarse fitting procedure associated with _sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit.mat_.

---

#### derivatives/SamSrf/simulations/ses-eve/accuracy

The list below comprises data simulated using the 2dg-fix model where pRF center position was varied. This allowed us to investigate the computational accuracy of pRF estimates when fitting a 2dg-fix model with constrained grid search to the data (see manuscript).

The list below focuses on the even data set (called 'ses-eve' for consistency with empirical data) and 'sgrid-match', that is, simulated pRFs that match the search grid used for the coarse fitting procedure (i.e., constrained grid search fit). The directory structures and files for the remaining data sets (called 'ses-odd' for consistency with empirical data) and types of search grid alignment ('sgrid-mismatch'), that is, simulated pRFs that mismatch the search grid used for the coarse fitting procedure (i.e., constrained grid search fit), are equivalent.

- The files are largely like those in _derivatives/SamSrf/simulations/ses-all/prfsize_, but for the 2dg-fix model (simulation and fitting). However, there are no files containing general summary statistics or results from the fine fitting procedure (i.e., unconstrained optimization procedure). Besides, there is a series of additional files:

  
- **sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_count.mat**: File that contains count data (number of times a certain grid search value pair was recovered) associated with _sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

- **sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_sumstat-cSNR-cR^2.mat**: File that contains summary statistics involving cSNR and cR^2 associated with _sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

- **sim_ses-eve_task-prf_nrep-1_sd-0_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_count.mat**: Like
  _sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_count.mat_, but for count data associated with _sim_ses-eve_task-prf_nrep-1_sd-0_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

---

#### derivatives/SamSrf/simulations/ses-eve/gof

The list below comprises null data simulated using the onoff model to investigate the meaningfulness of the observed difference in cross-validated goodness-of-fit between the 2dg-fix and the onoff model (see manuscript).

The list below focuses on the even data set (called 'ses-eve' for consistency with empirical data). The directory structures and files for the remaining data sets (called 'ses-odd' for consistency with empirical data) are equivalent.

- The files are largely like those in _derivatives/SamSrf/simulations/ses-eve/accuracy_, but for both the onoff model (simulation and fitting) and the 2dg-fix model (fitting) as well as a simulated pRF that is not part of the search grid ('sgrid-none') used for the coarse fitting procedure (i.e., constrained grid search fit). The latter is a consequence of simulating data using the onoff model. However, there are no files containing count data. Besides, there is a series of additional files:

- **sim_ses-eve_task-prf_nrep-100000_sd-2_onoff_aperture-pins_vec_spmcan_sgrid-none_2dg-fix_aperture-pins_vec_spmcan_CrsFit_sumstat-diff-cR^2.mat**: File that contains summary statistics involving diff-cR^2 (2dg-fix vs onoff model) associated with _sim_ses-eve_task-prf_nrep-100000_sd-2_onoff_aperture-pins_vec_spmcan_sgrid-none_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.
  
---

### Layers beyond the root directory — derivatives (results)

The derivatives (results) directory contains visualizations of the information provided and analyses performed in our manuscript.

---

### derivatives/results/colormaps

- **colormap-generic.pdf**: File that displays [SamSrf](https://github.com/samsrf/samsrf/tree/4de3223950fc4cb995941b2041e2dcc73bb9bbd4)'s generic colormap.

---

### derivatives/results/prf2dg

- **2dgprf-2d.pdf**: File that displays a 2D Gaussian pRF in 2D format.
  
- **2dgprf-3d.pdf**: File that displays a 2D Gaussian pRF in 3D format.

---

### derivatives/results/prfworkflow

The list below focuses on 'aptframe-17' and '2dg-fix'. The directory structures and files for the remaining aperture frames ('aptframe-21', 'aptframe-25', and 'aptframe-29') and pRF models ('2dg' and 'onoff') are equivalent.

- **aptframe-17.pdf**: File that displays the 17th aperture frame.
  
- **prf-2dg-fix.pdf**: File that displays a pRF following the 2dg-fix model.
  
- **tc-hrf_prf-2dg-fix.pdf**: File that displays the HRF used for predicting or simulating fMRI time courses based on a pRF following the 2dg-fix model.
  
- **tc-noise_prf-2dg-fix.pdf**: File that displays the noise added when simulating a noise-tainted fMRI time course based on a pRF following the 2dg-fix model.
  
- **tc-obs_prf-2dg-fix.pdf**: File that displays the observed fMRI time course based on a pRF following the 2dg-fix model.
  
- **tc-pred-conv_prf-2dg-fix.pdf**: File that displays the predicted or (simulated noise-free) fMRI time course based on a pRF following the 2dg-fix model, that is, a predicted (or simulated noise-free) neuronal time course that was convolved with the HRF.

- **tc-sim_prf-2dg-fix.pdf**: File that displays the simulated noise-tainted fMRI time course based on a pRF following the 2dg-fix model.

---

### derivatives/results/simulations/ses-all/prfsize

- **sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.pdf**: File that displays summary statistics associated with _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.mat_.

- **sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.pdf**: Like _sim_ses-all_task-prf_nrep-100000_sd-2_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.pdf_, but for summary statistics associated with _sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_2dg_aperture-pins_vec_spmcan_FneFit_sumstats.mat_.

- **sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix_tc-sim.pdf**: File that displays simulated time courses associated with _sim_ses-all_task-prf_nrep-1_sd-0_2dg_aperture-pins_vec_spmcan_sgrid-mix.mat_.

---

### derivatives/results/simulations/ses-eve/accuracy

The list below focuses on the even data set (called 'ses-eve' for consistency with empirical data) and 'sgrid-match', that is, simulated pRFs that match the search grid used for the coarse fitting procedure (i.e., constrained grid search fit). The directory structures and files for the remaining data sets (called 'ses-odd' for consistency with empirical data) and types of search grid alignment ('sgrid-mismatch'), that is, simulated pRFs that mismatch the search grid used for the coarse fitting procedure (i.e., constrained grid search fit), are equivalent.

- **sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_counts-rec.pdf**: File that displays the recovered pRFs relative to the simulated ground truth pRFs as a frequency diagram. This visualization is associated with _sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_count.mat_, _sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_, and _src_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

- **sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_grids-sim.pdf**: File that displays the simulated ground truth pRFs relative to the search grid used for the coarse fitting procedure (i.e., constrained grid search fit) as a simple grid. This visualization is associated with _sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_ and _src_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

- **sim_ses-eve_task-prf_nrep-1_sd-0_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_grids-rec.pdf**: File that displays the recovered pRFs relative to the simulated ground truth pRFs as a simple grid. This visualization is associated with _sim_ses-eve_task-prf_nrep-1_sd-0_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.
  
- **sim_ses-eve_task-prf_nrep-1_sd-0_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_grids-sim.pdf**: Like _sim_ses-eve_task-prf_nrep-100000_sd-2_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit_grids-sim.pdf_, but the visualization is associated with _sim_ses-eve_task-prf_nrep-1_sd-0_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_ and _src_ses-eve_task-prf_nrep-1_sd-0_2dg-fix_aperture-pins_vec_spmcan_sgrid-match_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.
                         
---

### derivatives/results/simulations/ses-eve/gof

The list below focuses on the even data set (called 'ses-eve' for consistency with empirical data). The directory structures and files for the remaining data sets (called 'ses-odd' for consistency with empirical data) are equivalent.

- **sim_ses-eve_task-prf_nrep-100000_sd-2_onoff_aperture-pins_vec_spmcan_sgrid-none_2dg-fix_aperture-pins_vec_spmcan_CrsFit_sumstat-diff-cR^2.mat**: File that displays summary statistics involving diff-cR^2 (2dg-fix vs onoff model). This visualization is associated with _sim_ses-eve_task-prf_nrep-100000_sd-2_onoff_aperture-pins_vec_spmcan_sgrid-none_2dg-fix_aperture-pins_vec_spmcan_CrsFit_sumstat-diff-cR^2.mat_ and _sim_ses-eve_task-prf_nrep-100000_sd-2_onoff_aperture-pins_vec_spmcan_sgrid-none_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_.

---

### derivatives/results/sine

- **sine.pdf**: File displaying a sine wave (with a frequency of 25 Hz).
  
---

### derivatives/results/sub-01/ses-01/FWHM-1

The list below focuses on 'sub-01', 'ses-01', 'FWHM-1', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02' to 'ses-04'), surface smoothing kernel widths ('FWHM-0'), and brain hemispheres ('lh') are equivalent.

- **rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm_conts_map-Stim-Rest_masked-anat.png**: Like _rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm_conts_map-Stim-Rest.png_, but using an anatomical mask of SI (i.e., _rh.postcentral.label_) as well as delineations of BA3b (i.e., _rh.BA3b_exvivo.thresh.label_) and D2a (i.e., _rh_D2a.label_).

- **rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm_conts_map-Stim-Rest.png**: File that displays the _t_-statistic map for the contrast stimulation vs baseline (rest) along with a delineation of SI. The visualization is associated with _rh_sub-01_ses-01_task-pRF_run-all_FWHM-1_BBR_mgh2srf_spmcan_glm_conts.mat_ and _rh.postcentral.label_.

---

### derivatives/results/sub-01/ses-02+03+04/FWHM-1

The list below focuses on 'sub-01', 'FWHM-1', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), surface smoothing kernel widths ('FWHM-0'), and brain hemispheres ('lh') are equivalent.

- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-aR^2_masked-anat.png**: File that displays a map showing aR^2 using an anatomical mask and a delineation of D2a. The visualization is associated with _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_ and _rh_D2a.label_.
  
- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-Baseline_masked-anat.png**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-aR^2_masked-anat.png_, but for pRF baseline (i.e., beta 0).
  
- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-Beta_masked-anat.png**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-aR^2_masked-anat.png_, but for pRF amplitude (i.e., beta 1).
  
- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-diff-aR^2_masked-anat.png**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-aR^2_masked-anat.png_, but for diff-aR^2 (2dg-fix vs onoff model).
  
- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-R^2_masked-anat.png**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-aR^2_masked-anat.png_, but for R^2.
  
- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-x0_masked-anat.png**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-aR^2_masked-anat.png_, but for x0.
  
- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-y0_masked-anat.png**: Like _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-aR^2_masked-anat.png_, but for y0.
  
- **rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_tc-obsvsfit.png**: File displaying the observed and fit time courses for example vertices. The visualization is associated with _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_ and _rh_sub-01_ses-02+03+04_task-prf_run-all_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit.mat_.
  
---

### derivatives/results/sub-01/ses-02+03+04-eve/FWHM-1

The list below focuses on 'sub-01', 'ses-02+03+04-eve', 'FWHM-1', and 'rh'. The directory structures and files for the remaining subjects ('sub-02' to 'sub-03'), sessions ('ses-02+03+04-odd'), surface smoothing kernel widths ('FWHM-0'), and brain hemispheres ('lh') are equivalent.

- The files are largely like those in _derivatives/results/sub-01/ses-02+03+04/FWHM-1_, but for the even-numbered runs of session 02 to session 04. Besides, there is a series of additional files:

- **rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-cR^2_masked-anat.png**: File that displays a map showing cR^2 using an anatomical mask and a delineation of D2a. The visualization is associated with _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit.mat_ and _rh_D2a.label_.

  
- **rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-diff-cR^2_masked-anat.png**: Like _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-cR^2_masked-anat.png_, but for diff-cR^2 (2dg-fix vs onoff model).
  
- **rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit_map-cR^2_masked-anat.png**: Like _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_2dg-fix_aperture-pins_vec_spmcan_CrsFit_map-cR^2_masked-anat.png_, but the visualization is associated with _rh_sub-01_ses-02+03+04-eve_task-prf_run-eve_FWHM-1_BBR_mgh2srf_mean_onoff_aperture-pins_vec_spmcan_CrsFit.mat_.

---

![](Banner_Mandelkow2017_fMRI.jpg)
#### *How does the accuracy of machine-learning classifiers depend on fMRI resolution?*  
High-field (7T) high-resolution (1.2mm) fMRI and eye tracking data from human subjects repeatedly watching 5-minute clips of naturalistic (cinematic) movie content without sound. A high number of repeated stimulus presentations and fMRI acquisitions at two different resolutions (1.2mm and 2mm isotropic) were chosen to investigate the accuracy of machine-learning classifiers and to test its dependence on fMRI resolution. Please find details in below publication [Mandelkow et al. 2017](https://doi.org/10.1016/j.neuroimage.2017.08.053), which should be quoted as a reference. All data were acquired at the National Institutes of Health under NINDS protocol 00-N-0082 in 2012-2015.

**Effects of spatial fMRI resolution on the classification of naturalistic movies**,  
H. Mandelkow, J.A. de Zwart, J.H. Duyn, 2017, NeuroImage  
https://doi.org/10.1016/j.neuroimage.2017.08.053  

**Keywords**: fMRI; High-resolution; High-field; 7T; Multivariate pattern analysis; MVPA; Naturalistic stimuli; Movies; Eye tracking

**********************************************************************

### Data Files
*NOTE: This dataset comprises 7 subjects, 4 with >16 movie stimulus repetitions. Of the original 10 subjects three were discarded without analysis due to subsequent changes in the experimental protocol (MRI sequences).*

#### fMRI data
##### `sub-02_ses-05_task-Mx1_acq-Hr_run-2_bold.nii.gz`
One run of BOLD fMRI data in [Nifti](https://nifti.nimh.nih.gov) format (.nii.gz).
- `sub-##` : human subject number ##
- `ses-##` : experimental session number ## (1-5 separate sessions per subject)
- `task-*` : stimulus presented (5' movie clip)
	- `task-Mx1` : The Matrix I opening scene
	- `task-Mx2` : The Matrix II
	- `task-Gbu1` : The Good, the Bad, and the Ugly
	- `tast-ffMRI` : single-slice (fast) fMRI with high temporal resolution without stimulus e.g. for characterizing cardiac artifacts
- `acq-Hr` / `acq-Lr` : Higher- / Lower-resolution fMRI at 1.2mm / 2mm isotropic
- `run-#` : experimental run number within each fMRI session in temporal order

#### MRI anatomy
##### `sub-02_ses-05_acq-AnaGE_T2w.nii.gz` : gradient-echo anatomy (magnitude)
##### `sub-02_ses-05_acq-AnaGEp_T2w.nii.gz` : gradient-echo anatomy (phase)

#### Eye-tracking data
##### `sub-02_ses-05_task-Mx1_acq-Hr_run-2_vpdat.txt`
- `*_vpset0.txt` : calibration before movie start
- `*_vpset1.txt` : calibration at movie start
- **`*_vpdat.txt`** : eye-tracking data
- `*_vpset2.txt` : calibration at movie end
- `*_vpset3.txt` : calibration after movie end

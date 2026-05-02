# NODEAP: Distinct contributions of anterior and posterior OFC to outcome-guided behavior

**Summary**  
This dataset includes defaced anatomical T1-weighted MRI and raw multi-echo resting-state fMRI data from a study investigating the distinct roles of the anterior (aOFC) and posterior (pOFC) lateral orbitofrontal cortex in outcome-guided (goal-directed) behavior.  
Participants underwent odor–reward learning and outcome devaluation across multiple sessions. To probe causal contributions of OFC subregions, network-targeted TMS was applied to either aOFC or pOFC in separate sessions, and its effects on learning versus inference were assessed.

- For project code, behavioral data, and full analysis pipelines (including preprocessing of multi-echo resting-state fMRI), see:  
  👉 [project-nodeap-core](https://github.com/QingfangLiu/project-nodeap-core)

- For standalone analyses using functional connectivity derived from this dataset with deep learning methods (e.g., CVAEs), see:  
  👉 [project-nodeap-fmri-cvae](https://github.com/QingfangLiu/project-nodeap-fmri-cvae)

**Participants**  
- N = 48 healthy adults  
- See `participants.tsv` for sex, age, stimulation group (aOFC vs. pOFC), and counterbalanced TMS and meal orders  

**Sessions / tasks**  
Each subject may have several MRI sessions; session labels match the original collection schedule:  
- `ses-D0` – baseline/resting-state MRI (no devaluation).  
- `ses-S1D1`, `ses-S1D2`, `ses-S2D1`, `ses-S2D2`, `ses-S3D1`, `ses-S3D2` – study days spanning learning (Day 1) and post-meal devaluation/choice (Day 2). Some sessions include network-targeted TMS (aOFC or pOFC).  
- Functional scans are resting-state; multi-echo acquisitions are provided as separate echoes.

**What’s included**  
- `sub-*/anat/`  
  - Defaced T1w MRI: `sub-XX_T1w.nii.gz` (+ JSON sidecar if available).  
- `sub-*/ses-*/func/`  
  - Raw multi-echo BOLD: `sub-XX_ses-YY_task-rest_run-01_echo-{1,2,3}_bold.nii.gz` (+ matching JSON sidecars when available).  
- Top-level: `dataset_description.json`, `participants.tsv`, `participants.json`, `README.md`.

**Notes on data quality & privacy**  
- T1w images were defaced prior to sharing.  
- Functional files are raw (converted with dcm2niix); files with SPM-style prefixes (r/w/y/s*) were excluded.

**Folder conventions (BIDS)**  
```
nodeap-bids/
  sub-01/
    anat/sub-01_T1w.nii.gz
    ses-D0/func/sub-01_ses-D0_task-rest_run-01_echo-1_bold.nii.gz
    ses-D0/func/sub-01_ses-D0_task-rest_run-01_echo-2_bold.nii.gz
    ses-D0/func/sub-01_ses-D0_task-rest_run-01_echo-3_bold.nii.gz
    ses-S1D1/func/...
  sub-02/ ...
```

**How to cite**  
Please cite our paper: Liu et al., 'Distinct contributions of anterior and posterior orbitofrontal cortex to outcome-guided behavior', Current Biology (in press). Add DOI when available.

**Contacts**  
- Qingfang Liu — psychliuqf@gmail.com  
(You may also contact the corresponding author from the manuscript.)

**License**  
This dataset is shared under **CC0**.

Neuroimaging Data Collected During Kinesthetic Motor Imagery of Walking vs. Rest
-------------------------------------------------------------------------------
This dataset includes multimodal neuroimaging recordings from five participants performing kinesthetic motor imagery (KI) while viewing themselves walking in an exoskeleton. The dataset includes synchronized MRI (structural and functional) and EEG recordings organized according to the BIDS specification. Functional MRI data were acquired in two runs while participants viewed a 10-minute video, along with a separate baseline scan during which participants simulated a resting state for approximately 5 minutes.

MRI sessions were conducted after participants completed nine sessions of EEG‑controlled exoskeleton walking and standing experiments. 
Dataset link: <a href="https://openneuro.org/datasets/ds006940" target="_blank"> https://openneuro.org/datasets/ds006940 </a>

MRI Acquisition:
- Scanner: Philips Ingenia 3.0T (Koninklijke Philips N.V., The Netherlands)
- Structural scans: T1‑weighted anatomical images
- Functional scans (fMRI): Participants viewed a 10‑minute video of themselves walking in the exoskeleton, filmed from a first‑person perspective. The video contained 11 Stop‑Walk‑Stop (SWS) cycles. During viewing, participants were instructed to evoke KI in synchrony with the exoskeleton movements.
- Baseline condition: Participants mentally simulated resting state for approximately 5 minutes while fMRI data was recorded.

EEG Acquisition:
- MR‑compatible EEG cap (Brain Products GmbH, Gilching, Germany)
- Electrode locations are provided in EEGLAB format.
- 59 scalp channels + 4 EOG channels + 1 ECG channel

Stimuli:
- A video stimulus (`stimuli/walking_exoskeleton_S1.mp4`) was presented during walking tasks.

Participants:
Five healthy adults out of seven participated in the EEG‑controlled exoskeleton experiments.
Participants S6 and S7 did not undergo MRI scanning due to a pause in data collection during the COVID‑19 pandemic.

<h3>Folder Structure (Example: Participant S1)</h3>
<hr>

<pre>
├── dataset_description.json
├── README
├── derivatives
│   └── sub-01
│       └── ses-01
│           ├── anat
│           │   └── sub-01_ses-01_T1w.nii
│           ├── dwi
│           │   ├── sub-01_ses-01_run-001_dwi.json
│           │   ├── sub-01_ses-01_run-001_dwi.bval
│           │   ├── sub-01_ses-01_run-001_dwi.bvec
│           │   └── sub-01_ses-01_run-001_dwi.nii.gz
│           │
│           └── spm
│               ├── sub-01_ses-01_beta_0001.nii
│               ├── ...
│               ├── sub-01_ses-01_beta_0008.nii
│               ├── sub-01_ses-01_con_0001.nii
│               ├── ...
│               ├── sub-01_ses-01_con_0004.nii
│               ├── sub-01_ses-01_smpt_0001.nii
│               ├── ...
│               ├── sub-01_ses-01_smpt_0004.nii
│               ├── sub-01_ses-01_mask.mat
│               ├── sub-01_ses-01_resms.mat
│               ├── sub-01_ses-01_rpv.mat
│               └── sub-01_ses-01_spm.mat
│               
├── stimuli
│   └── walking_exoskeleton_S1.mp4
│
├── sub-01
│   └── ses-01
│       ├── anat
│       │   ├── sub-01_ses-01_T1w.json
│       │   └── sub-01_ses-01_T1w.nii
│       ├── eeg
│       │   ├── sub-01_ses-01_coordsystem.json
│       │   ├── sub-01_ses-01_electrodes.json
│       │   ├── sub-01_ses-01_electrodes.tsv
│       │   ├── sub-01_ses-01_task-baseline_eeg.eeg
│       │   ├── sub-01_ses-01_task-baseline_eeg.json
│       │   ├── sub-01_ses-01_task-baseline_eeg.vhdr
│       │   ├── sub-01_ses-01_task-baseline_eeg.vmrk
│       │   ├── sub-01_ses-01_task-walking1_eeg.eeg
│       │   ├── ...
│       │   └── sub-01_ses-01_task-walking2_eeg.vmrk
│       │
│       └── func
│           ├── sub-01_ses-01_task-baseline_run-001_bold.json
│           ├── sub-01_ses-01_task-baseline_run-001_bold.nii.gz
│           ├── sub-01_ses-01_task-walking1_run-001_bold.json
│           ├── sub-01_ses-01_task-walking1_run-001_bold.nii.gz
│           ├── sub-01_ses-01_task-walking2_run-001_bold.json
│           └── sub-01_ses-01_task-walking2_run-001_bold.nii.gz
</pre>

Validation Data
---------------
A validation file (`derivatives/MRI_DataValidation.xls`) is provided to summarize dataset completeness and quality checks.

- **Sheet: Files**  
  Lists presence/absence of EEG, MRI, and SPM outputs across subjects (S1–S5).  
  Includes counts for beta, con, spmT maps, and DTI volumes.

- **Sheet: VMRK-R128**  
  Reports event marker counts (R128 triggers) for baseline, walking1, and walking2 tasks.

- **Sheet: EEG-Duration**  
  Provides task durations (minutes) for 'baseline', 'walking1', and 'walking2' EEG recordings.

Notes on Organization
---------------------
* Raw data (anat, func, eeg) are stored under each subject directory (sub-XX/ses-YY).

* Derivatives: Preprocessed outputs are stored separately under derivatives/sub-XX/ses-YY, including:<br> 
&emsp;- Statistical Parametric Mapping (SPM) outputs<br> 
&emsp;- SPM-normalized (warped) anatomical scans<br> 
&emsp;- Diffusion Tensor Imaging (DTI) derivatives<br> 
&emsp;- Validation Excel file<br>

* The video stimulus is stored in the top-level stimuli/ folder.

* Naming conventions follow BIDS entities:<br>
&emsp;- sub-&lt;label&gt;  : subject identifier<br>
&emsp;- ses-&lt;label&gt;  : session identifier<br>
&emsp;- task-&lt;label&gt; : task name (baseline, walking1, walking2)<br>
&emsp;- run-&lt;index&gt;  : run number<br>


Citation
--------
If you use this dataset, please cite the associated study and acknowledge the contributors.
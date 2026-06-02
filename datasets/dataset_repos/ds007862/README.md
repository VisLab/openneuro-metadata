# OriSeg

## Change Log

Uploaded by Joseph Emerson 05/27/2026

## Description
This dataset measures blood-oxygenation-level-dependent (BOLD) responses from human visual cortex during a visual orientation-discrimination task under different image segmentation conditions. Data were acquired at 7T with 0.6 mm isotropic resolution for the purpose of measuring BOLD responses across the cortical depth. The experiment was designed to probe the effects of visual spatial context on the depth-dependent profiles of surround suppression in primary visual cortex (V1).

Authors: Emerson, Joseph H., Navarro, Karen, & Olman, Cheryl A.

Corresponding Author: Emerson, Joseph H.; Email: emers245@umn.edu

Citation: Emerson, Joseph H., Navarro, Karen, & Olman Cheryl A. "Orientation-tuned surround suppression exhibits a unique laminar signature in human primary visual cortex". Proc. Natl. Acad. Sci. U.S.A. (forthcoming).

Preprint: https://doi.org/10.64898/2025.12.12.694066

Funding: 
- HHS | NIH | NIH Office of the Director (OD), 1S10OD017974-01
- HHS | NIH | National Institute of Biomedical Imaging and Bioengineering (NIBIB), 5P41EB027061
- HHS | NIH | National Institute of Neurological Disorders and Stroke (NINDS), 5R01MH111447-05, 5R01NS123842
- HHS | NIH | National Institute on Drug Abuse (NIDA), 5T32MH115886-04, 5R01NS123842
- HHS | NIH | National Institute of Mental Health (NIMH), 5R01MH111447-05, 5T32MH115886-04

## Participants

Sixteen healthy adults (10 female, 5 male, 1 non-binary with undisclosed sex) participated in this study. Data from all sixteen participants are included without exclusion. See citation for details on exclusion criteria.

## Task

Please see our manuscript for full details about the task. A summary is provided below. Behavioral data are available upon request.

### Visual Stimuli
Participants fixated at center-screen while viewing stimuli constructed from sine-wave gratings. Stimuli consisted of three components:
- a large sine wave grating subtending 25 degrees visual angle
- a central grating subtending 1.25 degrees visual angle at fixation
- two target gratings subtending 2.5 degrees visual angle at 3.25 degrees eccentricity rotated 30 degrees below the horizontal meridian

All components were shown at 40% contrast and 1.6 cycles per degree for all conditions. Stimuli were presented in 12 sec. blocks with eight trials each. For each trial, the following stimulus sequence was used: 
1. all components flashed on screen simultaneously for 250 ms
2. gray screen with fixation point for 200 ms
3. all components flashed on screen simultaneously for 250 ms rotated uniformly relative to the first presentation
4. gray screen with fixation point during 300 ms response window
5. red (incorrect) or green (correct) circle flashed around fixation point indicating accuracy on previous response for 100 ms

In the second presentation of the stimulus within the trial, each component was rotated in the same clockwise or counterclockwise direction by the same amount relative to the first presentation. The average orientation within blocks was one of eight orientations arranged in equal intervals between 0 and 157.5 degrees. Participants performed a two-alternative forced choice (2AFC) task by responding in the subsequent 300 ms grayscreen window with a button press, indicating whether the orientation of the second presentation was shifted clockwise or counterclockwise relative to the first presentation. Orientation shifts between the first and second presentation ranged from 1 to 16 degrees. The size of the shifts were determined by a three-down, one-up staircase. Trials were interspersed with jitters of 0, 300, or 600 ms. Blocks are organized by condition and orientation, with the condition and mean orientation remaining constant within blocks.

### Experiment Conditions
This dataset contains two scan types: localizer and task. Participants performed the same orientation-discrimination task in both scan types and the stimulus sequence was identical in both. The localizer scan was used to identify the retinotopic representations of target and surround components in visual cortex. Localizer scans had two conditions:
1. *surround*: target gratings were replaced with gray disks 
2. *center*: the surround grating was replaced with neutral gray 

Total number of localizer blocks per session: 51 

Task scans were used to measure the effects of different contextual conditions on surround suppression. These scans included four experimental conditions plus a rest condition: 
1. *iso0*: the surround and target gratings were matched in orientation and phase, such that there was no discernable boundary between the surround and target disks
2. *iso90*: the surround was shifted 90-degrees in phase relative to the target inducing a perceptual boundary between the surround and target gratings
3. *orth*: the surround was rotated 90-degrees in orientation relative to the target orientation 
4. *sur*: identical to the *surround* condition from the localizer experiment.
5. *rest*: gray screen with fixation grating only

Total number of task blocks per session: 128

Within each session, there were three localizer scans and four task scans.

## MRI Acquisitions
All MRI data were acquired at the Center for Magnetic Resonance Research at the University of Minnesota.

### ses-01
Session 1 contains functional data from 7T.

#### func
Functional data can be found in the *func* datatype.  All functional data were acquired on two 7T Siemens scanners equipped with a custom head coil with a 32-channel transmit and 4-channel receive. The following participants were scanned on a Siemens MAGNETOM 7T Plus:
- sub-pnr102
- sub-pnr256
- sub-pnr328
- sub-pnr510
- sub-pnr739
- sub-pnr756

The following participants were scanned on a Siemens MAGNETOM 7T Terra:
- sub-pnr143
- sub-pnr161
- sub-pnr352
- sub-pnr495
- sub-pnr579
- sub-pnr668
- sub-pnr685
- sub-pnr713
- sub-pnr822
- sub-pnr947

We employed a T2\*-weighted gradient echo-planar imaging (GE EPI) with field of view covering the posterior occipital lobe: 
- TR: 2 sec 
- TE: 32.2 ms
- 24 or 25 coronal slices 
- Resolution: 0.6 mm isotropic
- FOV: 124.8 mm x 153.6 mm, posterior occipital 
- Matrix size: 208 x 256
- GRAPPA in-plane parallel acceleration imaging factor: 3
- 6/8 partial Fourier
- echo-spacing 1.2 ms 

The number of coronal slices depended on the SAR limits for the two scanners used. Participants scanned on the Siemens MAGNETOM 7T Plus had 25 coronal slices, while participants scanned on the Siemens MAGNETOM 7T Terra had 24 coronal slices. Phase-encoding was right-to-left in all participants except sub-pnr510, who had left-to-right phase encoding.

#### fmap
Each session also included a T1-weighted GE EPI matched to the functional space to delineate gray matter. These are included in the *fmap* datatype. A reverse phase encode T1-weighted GE EPI was used for distortion compensation. Since, the T1-weighted GE EPI was acquired at identical resolution, sampling, and echo spacing as the T2\*-weighted functional data, these acquisitions have matching distortions and the WARP field generated from the T1-weighted GE EPI can be used to compensate distortion in the T2\*-weighted data.

#### anat
Most participants also have in-session T1w anatomical scans used for initial registration and alignment of the 3T anatomical data. Three participants did not have these in-session anatomies: sub-pnr161, sub-pnr510, and sub-pnr947.

### ses-02
Session 2 contains anatomical data from 3T.

#### anat
Anatomical data were acquired on a Siemens 3T scanner. All participants have a full-brain T1-weighted MP-RAGE scan with 0.8 mm isotropic resolution. Several participants also have a T2-weighted SPACE scan with matching resolution. A few participants have multiple T1w scans within the same session. Unless otherwise specified, surface reconstruction was performed by averaging multiple T1w scans after between-scan motion compensation. However, the following subjects used only one of the T1w scans for surface reconstruction as indicated below:
- sub-pnr256: sub-pnr256_ses-02_run-04_T1w.nii.gz
- sub-pnr510: sub-pnr510_ses-02_run-01_T1w.nii.gz
- sub-pnr713: sub-pnr713_ses-02_run-02_T1w.nii.gz


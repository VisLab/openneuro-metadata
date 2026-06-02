This dataset has been converted using BrkRaw (vFalse)at 2026-03-30 15:50:38.142046.  https://doi.org/10.5281/zenodo.3818615

## Overview

Dataset title: Longitudinal whole-brain MRI of alpha-synuclein propagation following dorsal striatal injection in M83 hemizygous mice
MRI data collection ran from December 2019 to January 2022
Subset of data was used for publication: https://doi.org/10.1038/s42003-025-07680-1
Remainder used for preprint: https://doi.org/10.1101/2025.07.18.665565 

-   [ ] Brief overview of the tasks in the experiment

M83 hemizygous mice and their no-copies litter mates (wild-type; WT) mice, bred in-house via M83 hemizygous by hemizygous breeding, were injected with either phosphate-buffered saline (PBS), human preformed fibrils of alpha-synuclein (Hu-PFF), or mouse preformed fibrils (Ms-PFF) in 
the right dorsal striatum (co-ordinates: +0.2 mm relative to Bregma, +2.0 mm from midline, +2.6 mm beneath the dura). Mice underwent longitudinal magnetic resonance imaging (MRI) at four time points: -7, 30, 90 and 120 days post-injection, unless they reached a humane endpoint prior 
to any experimental timepoint. MRI acquisition was performed on 7.0-T Bruker Biospec 70/30 USR 30-cm inner bore diameter (with Bruker's MRI CryoProbe and AVANCE NEO electronics) at the Douglas Research Centre (Montreal, QC, Canada). High-resolution in vivo T1-weighted images (FLASH; 
Fast Low Angle SHot) were acquired for each subject (TE/TR of 4.5 ms/20 ms, 100 μm3 isotropic voxels, 2 averages, scan time= 14 min, flip angle=20°). For each time point acquisition, the mice were anaesthetized with isoflurane at 3% induction (with 1% oxygen flow rate) for 3:30 
minutes whereby a bolus injection of dexmedetomidine (1:240 dilution) was administered intraperitoneally. The mice remained in the induction chamber until 5:30 minutes elapsed by which the mice were transferred to the MRI scanner and placed under 1.5% isoflurane with a constant 
infusion of dexmedetomidine (0.05 mg/kg/hr).


-   [ ] Description of the contents of the dataset

A total of 401 mice were imaged at least twice and at most 5 times across standard timing intervals of approximately -7, 30, 90 and 120 days post-injection (dpi). Some subjects were scanned a couple days prior to the predetermined time points which results in an "early" session. The actual 
dpi can be calculated from the masterfile whereby injection date and date of MRI acquistion is provided. Fast Low Angle SHot described above can be found in the anat/ directory. Mice were siphoned off across experimental time point thereby leading to inconsistencies in number of sessions
across the subjects in this dataset. Moreover, if a mouse reached its humane endpoint prior to the experimental time point, it might have been scanned days prior to that timepoint or not scanned at all due to its condition.


-   [ ] Independent variables

Condition variables include 
1) injection which refers to the injection group (one of three options: PBS; Hu-PFF; Ms-PFF)
2) genotype (one of two options: WT or hemi)
3) sex (one of two options: male or female)

-   [ ] Dependent variables

Raw MRI data provided here; dependent variables would be generated from processing pipelines such as deformation-based morphometry for voxel-wise volume measures (https://github.com/CoBrALab/optimized_antsMultivariateTemplateConstruction; reference: http://dx.doi.org/10.52294/001c.133510) 

## Subjects

Species: mus musculus
Strain: C57BL/6 x C3H
JAX Strain Number: 004479
JAX URL: https://www.jax.org/strain/004479
Strain RRID: IMSR_JAX:004479

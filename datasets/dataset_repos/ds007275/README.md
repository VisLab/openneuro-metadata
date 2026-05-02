**Study overview**

This dataset accompanies a high-resolution fMRI study on hippocampal pattern separation (i.e., a process by which overlapping input is transformed into orthogonal representations in the hippocampus) based on semantic similarity. In humans, it is often studied with the Mnemonic Similarity Task (MST, https://faculty.sites.uci.edu/starklab/mnemonic-similarity-task-mst/), where neural repetition suppression for exact repeats is compared to that for similar lure items.

In session 1 thirty young adults (Mage = 21 years, 15 females) viewed adjective--noun phrases (e.g. *'exotic zoo'*). At later repetitions, phrases were either:

* Exact repeats (same adjective--noun combination, e.g. *'exotic zoo'*), or
* Semantically modified repeats in which the noun was repeated but the adjective was replaced with a semantically similar word (e.g. *'strange zoo'*).

Exact and modified repeats were presented both during an incidental encoding phase (smst\_enc) and a two-alternative forced-choice recognition phase (smst\_rec).

In repetition-sensitive clusters of hippocampus, we observed attenuated repetition suppression for semantically modified phrases compared to exact repeats, consistent with pattern separation. Across participants, the magnitude of this repetition suppression difference predicted mnemonic discrimination performance at recognition. Moreover, repetition-sensitive clusters identified during encoding were sensitive to discrimination success for lure items at recognition.

In session 2, thirty-one young adults (Mage = 21.19 years, 16 females) produced data for analysis, whereby they observed a subset of phrases (N=56) from session 1, containing multiple phrases that were incorrectly recognized at recognition. All three versions (baseline, close modified version, distant modified version) were repeated three times  across eight functional runs (smst\_map).

In an on-going analysis, we compare word2vec-based semantic similarity between phrases to voxel pattern similarity derived from the hippocampus, anterior temporal lobe and specifically the temporal pole. We predict semantic similarity representation in the anterior temporal lobe and the anterior hippocampus. We also predict that pattern similarity will be associated with mnemonic discrimination performance in the anterior hippocampus and the temporal pole.

**Data organization**

The dataset is organized according to the BIDS standard, and includes both **raw data** and several levels of **derivative data** and code used for preprocessing and analysis.

**Raw data**

All raw MRI and behavioral data necessary to reproduce the main analyses are included in standard BIDS folders (e.g. sub-*/ses-*).

**Derivatives and code**

The preprocessing and analysis pipeline is provided in code, together with intermediate derivatives (reduced in amount of files for compactness). Key derivative directories are:

* **anat-preprocess/** - N4-bias-corrected anatomical images (T1-weighted \[brain-extracted] and proton density \[PD]).
* **feat/** - Outputs of the fMRI preprocessing pipeline (FSL FEAT-based): specifically filtered for motion-correction outputs and the preprocessed functional data.
* **fieldmaps/** - Fieldmap images prepared for direct use in fMRI preprocessing (e.g. distortion correction).
* **masks/** - Hippocampal subfield masks in template space (e.g. dentate gyrus, subiculum, etc.); and group-level statistical clusters for contrasts of interest.
* **onsets/** - FEAT-formatted onset files for all experimental conditions (e.g. exact repeats, semantic lures, encoding vs. recognition) for use with FSL design files.
* **registrations/** - Transform matrices and warps for affine and SyN registrations (using ANTs) between various modalities.
* **templates/** - Group-specific templates derived from PD and T1 images (only including initial averages and the final templates)


**Related works (regularly updated)**

Experimental softwares and raw data is available at: https://doi.org/10.5281/zenodo.18395407

Data analysis pipelines: https://doi.org/10.5281/zenodo.18395334
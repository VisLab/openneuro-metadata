# UCSD Forehead Patch Sleep Validation Dataset

Curated EEG recordings for validating sleep staging from a three-electrode forehead patch against standard 33-channel polysomnography.

## What is included
- CGX patch `.set` files that contain `EEG.VisualHypnogram` and `EEG.SpectralScoring`. The 33-channel data is not included in this release -- this release only includes the three-electrode data. The 33-channel data will be released separately.

## Sleep stage labels
`EEG.VisualHypnogram` is manual scoring in 30-second epochs using the following integers

1 equals Wake  
2 equals REM  
3 equals N1  
4 equals N2  
5 equals N3  
0 equals unknown or movement

`EEG.SpectralScoring` is spectral staging from the forehead patch. One row per patch channel. One column per 30-second epoch (see publication).

## Alignment policy
The 33-channel cap data used to score polysomnography and the 3-channel patch EEG data do not always start and stop at the same clock times. CGX patch data were aligned to the cap start time based on a spreadsheet completed by the data collector, so the start may be off by a few seconds. The 3-channel EEG data were segmented into 30-second windows, and the number of these windows should approximately match the number of values in the EEG.VisualHypnogram for the same dataset. If the patch data ended up shorter than the visual hypnogram, the hypnogram was trimmed at the end to match the patch length. If the hypnogram was longer, it was left untrimmed. In general, the mismatch at the end of the recording is less than one 30-second window.

## Subject exclusions
113 and 121 are excluded. The CGX patch was inadequate or unavailable.

## Citation
Onton JA, Simon KC, Morehouse AB, Shuster AE, Zhang J, Peña AA, Mednick SC. Validation of spectral sleep scoring with polysomnography using forehead EEG device. Frontiers in Sleep. 2024. doi 10.3389/frsle.2024.1349537.  
American Academy of Sleep Medicine. The AASM manual for the scoring of sleep and associated events. 2007 and later.

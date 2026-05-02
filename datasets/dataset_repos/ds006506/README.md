# multipred-fmri - BIDS Dataset

## Description
In this study we investigated the neural mechanisms of sensory prediction in multisensory settings 

## Participants
- 26 university students (Granada, Spain).
- Normal or corrected-to-normal vision and hearing.

## Experimental Design
- **Training Phase:** Explicit learning of probabilistic associations between gabor patches and pure tones (within modality associations), and training of the main task .
- **Main Test Phase:** Testing in fMRI scanner the effects of the larned predictive associations during an orthogonal perceptual judgement task.
- **Localizers:** Perceptual judgement task without the predictive cues.


## Imaging Parameters
- **Scanner:** Siemens Magnetom Prisma_fit (3T)
- **Sequence:** T2*-weighted gradient echo EPI
- **Repetition Time (TR):** 1.5s
- **Echo Time (TE):** 40ms
- **Flip Angle:** 75°
- **Voxel Size:** 2.0 × 2.0 × 2.0 mm
- **Slices:** 68 (interleaved)
- **Phase Encoding Direction:** A>>P
  

## File Organization
- `/sub-*/anat/` contains structural MRI data.
- `/sub-*/func/` contains functional MRI data.
- `task-localizer_bold.json` and `task-main_bold.json` define the scanning parameters.


- `/derivatives/` contains preprocessed and analyzed data (`FEAT 6.0.0`), and files required for other analyses (mostly .nifti, .csv, and feat outputs)
- Preprocessed data: (`derivatives/fsl_preprocessed`)
- First-level: individual runs (`derivatives/fsl_firstlevel`)
- Second-level: within-subject (`derivatives/fsl_secondlevel`)
- Third-level: group analyses (`derivatives/fsl_thirdlevel`)

- `/code/` contains .py and .sh scripts to obtain the files in `derivates/`

## Citation
If using this dataset, please cite:

> Sabio-Albert, M. et al. (20XX). *title.* [DOI link]

## Reproducing results

All scripts for the analyses and figures can be found in our lab's github: [https://github.com/memory-formation/multipred-fmri]

## Contact
Marc Sabio-Albert ([marcsabioalbert@gmail.com](mailto:marcsabioalbert@gmail.com))


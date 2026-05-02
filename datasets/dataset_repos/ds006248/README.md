# Pituitary Adenoma Multimodal MRI Dataset  
*With Ground Truth and Benchmark Segmentations*

This dataset provides a comprehensive, BIDS-organized collection of **multiparametric MRI scans** and **expert-validated segmentations** from 50 patients with pituitary adenomas. It is designed to support development and evaluation of segmentation models targeting challenging, pathologically altered sellar anatomy.

The dataset includes:
- Up to 10 MRI sequences per subject
- Ground truth annotations for 5 anatomical structures
- Outputs from 5 segmentation models
- Full benchmarking metrics

For the accompanying data descriptior paper, please refer to

> Černý M, Májovský M, Valošek J, et al. *Open-access multiparametric MRI dataset of pituitary adenoma and benchmark analysis of five segmentation models*. *Scientific Data*. [Under review].

---

## Context

Accurate segmentation of pituitary adenomas and surrounding structures is critical for:
- Surgical planning and navigation  
- Radiosurgery targeting  
- Volumetric progression monitoring  

Until now, no large, openly available dataset with detailed annotations and benchmarked segmentation outputs existed in this clinical domain.

---

## Imaging Data

MRI scans were acquired using a **3T GE 750w system**. Data is stored in `.nii.gz` format and organized in compliance with the [BIDS standard](https://bids.neuroimaging.io/).

| Sequence type         | % of patients |
|-----------------------|---------------|
| COR CE-T1             | 100%          |
| COR T1                | 100%          |
| SAG CE-T1             | 98%           |
| COR T2                | 86%           |
| 3D AX T1+C            | 98%           |
| COR FIESTA            | 68%           |
| COR CE-FIESTA         | 70%           |
| AX ADC b=200          | 56%           |
| AX ADC b=1000         | 60%           |
| AX eADC b=1000        | 60%           |

---

## Ground Truth Segmentations

Each subject includes a multi-class segmentation mask with the following labels:

- `1` – Tumor  
- `2` – Normal pituitary gland  
- `3` – Left internal carotid artery (ICA)  
- `4` – Right ICA  
- `5` – Optic pathway  

Manual multi-class segmentation was performed on coronal CE-T1w scans using Brainlab Elements and refined in multiple review rounds, including an external reviewer. Each segmentation was saved as a single-label `.nii.gz` file with integer values from 0–5. Additional annotations—seed points for semi-automated segmentation and keyframe slice indices—were also created for each subject and are included in the dataset. For further details, please refer to the accompanying paper.

![A schematic overview of the process of dataset creation and model benchmarking](https://raw.githubusercontent.com/DrMartinCerny/pituitary_adenoma_multimodal_MRI_dataset/main/img/figure_2.png)  

_**A schematic overview of the process of dataset creation and model benchmarking.** The left and bottom part of the image (green arrows) depicts the ground truth creation. First, segmentation masks were drawn manually by the main author. They were then reviewed and refined if necessary by the second author and by a reviewer from an external institution, establishing ground truth segmentation masks. Seed points for semi-automated segmentation were placed manually. The upper right part of the image (blue arrows) depicts the benchmark analysis. Predicted segmentations were obtained from one semi-automated method and three models and compared with the ground truth. Segmentation accuracy was assessed quantitatively using the Dice similarity coefficient, intersection over union, and Hausdorff distance._

---

## Benchmark Study

We include predictions from five models:

- **Černý et al. 2025** – nnU-Net, full volume  
- **Da Mutten et al. 2025** – nnU-Net, full volume  
- **Da Mutten et al. 2024** – CNN ensemble  
- **Černý et al. 2023** – Keyframe-only CNN  
- **Egger et al. 2012** – GrowCut (semi-automated)  

All predictions are aligned to the CE-T1w space and located under:

```/derivatives/segmentations/```

---

### Benchmark Results

**Metrics used:**  
- Dice Similarity Coefficient (DSC)  
- Intersection over Union (IoU)  
- Hausdorff Distance (HD)  

| Model                     | DSC – Keyframes       | DSC – Full Volume     |
|---------------------------|------------------------|------------------------|
| Egger et al. 2012 [19]    | 0.836 ± 0.096          | 0.730 ± 0.124          |
| Černý et al. 2023 [24]    | 0.779 ± 0.233          | –                      |
| Da Mutten et al. 2024 [23]| 0.730 ± 0.136          | 0.667 ± 0.137          |
| Černý et al. 2025 [6]     | 0.863 ± 0.116          | 0.815 ± 0.110          |
| Da Mutten et al. 2025 [10]| 0.833 ± 0.098          | 0.794 ± 0.084          |

![4   A visual comparison of Dice similarity coefficient of assessed segmentation models for tumor label](https://raw.githubusercontent.com/DrMartinCerny/pituitary_adenoma_multimodal_MRI_dataset/main/img/figure_4.png)

_A visual comparison of Dice similarity coefficient of assessed segmentation models for tumor label class a) on key frames and b) full volume_

See the full article for a detailed analysis including other label classes.

---

## Tools and Code

This dataset includes scripts for:
- DICOM → NIfTI BIDS conversion  
- Segmentation benchmarking and label harmonization  
- Manual defacing of 3D scans  

The full codebase is available at:  
[github.com/DrMartinCerny/pituitary_adenoma_multimodal_MRI_dataset](https://github.com/DrMartinCerny/pituitary_adenoma_multimodal_MRI_dataset)

A copy of all code files is also included with the dataset.

---

## License

This dataset is licensed under a  
**Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)**.  

Use and adapt for non-commercial purposes with proper attribution.

[creativecommons.org/licenses/by-nc/4.0](https://creativecommons.org/licenses/by-nc/4.0)

---

## Citation

If you use this dataset in your work, please cite:

> Černý M, Májovský M, Valošek J, et al. *Open-access multiparametric MRI dataset of pituitary adenoma and benchmark analysis of five segmentation models*. *Scientific Data*. [Under review].

---

## Contact

For questions or collaboration, contact:  
**Martin Černý** – `cerny.martin@uvn.cz`
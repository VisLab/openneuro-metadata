# DMT-HAR-MED: Effects of DMT and harmine during meditation: Functional MRI dataset 

## Dataset Overview
This dataset contains raw and preprocessed structural and functional MRI data from a **double-blind, placebo-controlled, mixed-design** study investigating the effects of **N,N-dimethyltryptamine (DMT)** and **harmine** on brain connectivity during a **3-day meditation retreat**.

The dataset is organized according to the [BIDS specification](https://bids.neuroimaging.io/) (**version 1.10.1**).

---

## Study Description
Forty healthy meditation practitioners participated in one of two structurally identical meditation retreats. Participants were randomly assigned to receive either **DMT + harmine** or **placebo** on the second retreat day.

MRI scans were acquired at two time points:
- **Pre-retreat** (baseline, functional)
- **Post-retreat** (after pharmacological intervention, functional + anatomical)

Throughout the retreat, participants engaged in daily meditation practice. Subjective experiences and psychological measures were assessed using validated questionnaires, including:
- Mystical Experience Questionnaire (MEQ)
- Nondual Awareness Dimensional Assessment-State (NADA-S)
- Toronto Mindfulness Scale (TMS)
- Sussex-Oxford Compassion Scales (SOCS-S and SOCS-O)
- Psychological Insight Scale (PIS)
- Emotional Breakthrough Inventory (EBI)

For full methodological details, please refer to the corresponding publications:

> **Egger et al., 2025** — *Meditation, Psychedelics, and Brain Connectivity: A Randomised Controlled Resting-State fMRI Study of N,N-Dimethyltryptamine and Harmine in a Meditation Retreat.* Imaging Neuroscience (2025). https://doi.org/10.1162/IMAG.a.907

> **Meling et al., 2024** — *Meditating on psychedelics. A randomized placebo-controlled study of DMT and harmine in a mindfulness retreat.* Journal of Psychopharmacology (2024). https://doi.org/10.1177/02698811241282637


---

## Participants
- **Total participants:** 40
- **Group allocation:** 20 DMT + harmine, 20 placebo
- **Sex distribution:** 22 male, 18 female

---

## Experimental Design
- **Design:** Double-blind, placebo-controlled, mixed between- and within-subject design
- **Retreat structure:** Two separate 3-day meditation retreats
- **Conditions:**
  - Placebo
  - DMT + harmine (120 mg each, administered as four 30 mg tablets at 30-min intervals)
- **Sessions:**
  - **Pre:** Baseline scans before retreat
  - **Post:** Follow-up scans after pharmacological intervention

---

## Data Overview
The dataset includes:
- **Raw structural and functional MRI data**
- **resting-state scans**
- **Participant-level metadata** (`participants.tsv`)
- **Sidecar JSON files** with acquisition parameters
- **fMRIPrep outputs** (version **23.0.2**) for preprocessed functional data
- **Derivatives from physiological recordings** processed with the **physIO toolbox** 

---

## Ethics & Approvals
- Approved by the **Cantonal Ethics Committee of Zürich** (BASEC-ID: **2021-00180**)
- Exemption granted by the **Swiss Federal Office of Public Health (FOPH)** for DMT administration
- Registered on **ClinicalTrials.gov**: [NCT05780216](https://clinicaltrials.gov/study/NCT05780216)
- All participants provided **written informed consent**

---

## License
This dataset is released under the **Creative Commons Attribution 4.0 International License (CC-BY-4.0)**.  
You are free to share, reuse, and adapt the data, **provided that you cite both the dataset and the corresponding publication**.

---

## How to Acknowledge
When using these data, please cite **both**:

**Dataset:**
> Egger, K., Meling, D., & Scheidegger, M. (2025). *Effects of DMT and harmine during meditation: Functional MRI dataset* (Version 1.0.0) [Data set]. OpenNeuro. https://doi.org/10.18112/openneuro.ds006644.v1.0.0

**Publication:**
> Egger, K., Meling, D., Polat, F., Seifritz, E., Avram, M., & Scheidegger, M. (2025).  
> *Meditation, Psychedelics, and Brain Connectivity: A Randomised Controlled Resting-State fMRI Study of N,N-Dimethyltryptamine and Harmine in a Meditation Retreat*  
> Imaging Neuroscience (2025). https://doi.org/10.1162/IMAG.a.907

---

## Contact
For questions regarding the dataset, please contact:

**Klemens Egger**  
Psychedelic Research & Therapy Development Lab  
University Hospital of Psychiatry Zurich  
✉️ klemens.egger@bli.uzh.ch
# Dense longitudinal single-subject multimodal MRI dataset acquired via self-administered scanning

## Dataset Overview

This dataset comprises 85 hours of resting-state fMRI, 195 T1-weighted and 54 DTI scans acquired from a single participant across 11 months (321 days), with 51.6 hours from 128 standardized protocol sessions over 7.5 months. The data were collected predominantly through self-administered scanning (125/128 standard sessions) on a clinical 3T scanner without dedicated research infrastructure. Data were acquired during a period that included a venlafaxine taper; these longitudinal covariates are provided as metadata, but cannot be disentangled from time/season/procedural changes in this single-subject dataset.

**Key dataset features:**
- 85 hours of resting-state fMRI across 458 runs (243 sessions)
- 195 T1-weighted structural scans and 54 DTI sessions
- Detailed medication and taper logs (venlafaxine discontinuation)
- Pre-session psychological assessments (PANAS, Psychomotor Vigilance Task)
- Physiological monitoring (89 sessions, 170 runs)
- Daily lifestyle tracking (sleep, caffeine, alcohol, exercise, steps)
- Systematic vigilance state documentation (64% of runs)

## Main Intended Use

This dataset is primarily a **methods- and feasibility-focused resource** demonstrating the operational practicality, repeatability, and data quality achievable with predominantly self-administered MRI scanning in a clinical environment. It also provides an unusually dense, multimodal, longitudinal single-subject neuroimaging record.

Its greatest value lies in:
1. **Methodological and reliability studies**
2. **Testing preprocessing and analysis pipelines**
3. **Teaching and demonstration purposes**

Although extensive behavioral, physiological, and pharmacological variables are included, **the dataset is not suitable for isolating causal effects** of medication, seasonal factors, or procedural learning. These variables are highly collinear over time, and vigilance measures are subjective. Accordingly, the dataset should be interpreted as a **naturalistic longitudinal observation**, rather than a controlled pharmacological or seasonal study.

## Quick Start

### Finding the Core Standardized Data

Sessions marked with the **`std`** suffix contain the standardized protocol:
- **128 sessions** over 7.5 months (February 1 - September 22, 2025)
- Each session contains paired acquisitions:
  - 240-volume (10-minute) eyes-open run: `acq-3isoEOstd`
  - 340-volume (~14-minute) eyes-closed run: `acq-3isoECstd`
- Total: **51.6 hours** of consistent resting-state data

**Key metadata files:**
- `derivatives/sub-001_func_runs.tsv` - All functional run metadata with quality metrics
- `derivatives/sub-001_anat_runs.tsv` - All structural scan metadata and quality metrics
- `derivatives/sub-001_dwi_runs.tsv` - All diffusion scan metadata and quality metrics
- `sub-001/sub-001_sessions.tsv` - Session-level covariates, assessments, and pharmacological regressors

### Example: Quality-Based Filtering
```python
import pandas as pd

# Load functional runs metadata
func = pd.read_csv("derivatives/sub-001_func_runs.tsv", sep="\t")

# Filter standardized protocol runs
std_runs = func.query("stdEO == 1 | stdEC == 1")

# Apply quality threshold
low_motion = std_runs.query("fd_mean <= 0.2")

# Calculate hours (TR = 2.5s)
print(f"Standardized runs: {len(std_runs)} ({std_runs.num_volumes.sum() * 2.5 / 3600:.1f} hours)")
print(f"Low-motion subset: {len(low_motion)} ({low_motion.num_volumes.sum() * 2.5 / 3600:.1f} hours)")
```

**Expected output:** ~51.6 hours total, ~32.5 hours meeting strict motion criteria (mean FD ≤ 0.2mm)

### Example: Motion and Vigilance State

Motion characteristics vary systematically across vigilance states:
```python
import pandas as pd
import matplotlib.pyplot as plt

func = pd.read_csv("derivatives/sub-001_func_runs.tsv", sep="\t")

# Create state labels combining eyes and sleep
func["state"] = func["eyes_condition"].map({"open": "EO", "closed": "EC"}) + "/" + func["sleep"]
func["state"] = func["state"].str.replace("/No", "/Awake").replace("/A little", "/Partial sleep")

# Summary statistics
print("Motion (mean FD in mm) by vigilance state:")
print(func.groupby("state")["fd_mean"].agg(["mean", "count"]).round(3))

# Visualize
fig, ax = plt.subplots(figsize=(8, 5))
states = ["EO/Awake", "EC/Awake", "EC/Partial sleep", "EC/Yes"]
func[func["state"].isin(states)].boxplot(column="fd_mean", by="state", ax=ax)
ax.set_xlabel("Vigilance State")
ax.set_ylabel("Mean FD (mm)")
ax.set_title("Motion increases with decreased vigilance")
plt.suptitle("")
plt.tight_layout()
plt.show()
```

**Expected pattern:** Mean FD increases from ~0.13mm (eyes open/awake) to ~0.29mm (frank sleep).

## Dataset Structure

```
sub-001/
├── ses-YYYYMMDDNN(std)/          # Session directories
│   ├── func/                      # Resting-state fMRI
│   ├── anat/                      # T1-weighted scans
│   ├── dwi/                       # Diffusion tensor imaging
│   └── *_scans.tsv               # Per-session acquisition log
└── sub-001_sessions.tsv           # Session-level metadata and covariates

derivatives/
├── mriqc/                         # Quality control metrics (MRIQC v25.1.0)
├── medication/                    # Venlafaxine dosing logs and regressors
├── sleep/                         # Sleep timing events
├── caffeine/                      # Coffee consumption logs
├── alcohol/                       # Alcohol consumption logs
├── exercise/                      # Workout session logs
├── spatial_consistency/           # Between-session geometric positioning
├── steps/                         # Apple Health step counts
├── sub-001_func_runs.tsv          # All functional run metadata with quality metrics
├── sub-001_anat_runs.tsv          # All structural scan metadata and quality metrics
└── sub-001_dwi_runs.tsv           # All diffusion scan metadata and quality metrics

sourcedata/
├── sub-001_messages_raw.tsv       # Raw Telegram logging data
└── assessments/                   # Trial-level PVT and PANAS data
```

### Session Naming Convention

- `ses-YYYYMMDDNN`: Date (YYYYMMDD) + session order that day (NN: 01, 02)
- `ses-YYYYMMDDNNstd`: Sessions containing standardized paired protocol
- Example: `ses-2025031601std` = March 16, 2025, first session for the date, standardized protocol session

### Acquisition Labels

Functional runs use `acq-` labels encoding three properties:
- **Resolution**: `2p5iso` (2.5mm isotropic) or `3iso` (3mm isotropic)
- **Eyes condition**: `EO` (eyes open) or `EC` (eyes closed)
- **Protocol status**: `std` suffix indicates standardized protocol membership

Examples:
- `acq-3isoECstd` = 3mm isotropic, eyes closed, standardized protocol
- `acq-2p5isoEO` = 2.5mm isotropic, eyes open, developmental phase

## Important Technical Notes

### No Susceptibility Distortion Correction

**Field maps and reversed phase-encoding acquisitions were not obtained**. Functional and diffusion data are provided **without susceptibility distortion correction**.

### Defacing

All T1-weighted anatomical images were defaced prior to public release using *pydeface* (poldracklab/pydeface, v2.0.0, Docker).  
Only defaced images are included in the shared dataset.

### T1-Weighted Slice Interpolation

All T1-weighted scans were reconstructed with **Philips −50% slice gap**, interpolating intermediate slices at half-step positions (e.g., 1mm nominal slices positioned every 0.5mm).

- NIfTI headers correctly report geometric spacing
- Approximately **half the through-plane resolution is interpolated** rather than independently acquired
- For most applications (registration, morphometry), data are suitable as-is
- **Optional preprocessing**: Users requiring spatially independent voxels can apply:
  ```
  code/preprocessing/fix_philips_slice_interpolation.py
  ```
  before bias correction or segmentation to drop every second slice. Note that this procedure has not been thoroughly tested.

### Physiological Monitoring

Scanner console SCANPHYSLOG files did not contain reliable per-volume triggers. **Trigger timing was derived** by detecting gradient-active periods and calculating backwards from acquisition endpoints using known TR and volume counts.

- Available for 89 sessions (170 functional runs)
- Format: BIDS-compliant `*_physio.tsv.gz` with respiratory, pulse, and synthesized triggers
- Sampling frequency: 500 Hz
- Suitable for physiological noise modeling with accurate volume alignment

### Self-Scanning Methodology

**189 of 243 total sessions** (78%) were conducted using self-administered protocols without operator presence, including **125 of 128 standard protocol sessions** (98%).

Key technique: Laser crosshair positioning to participant's eyes provided reproducible head placement starting June 10, 2025:

| Metric                      | Before laser (≤ June 2025) | After laser (> June 2025) |
| :-------------------------- | :------------------------: | :-----------------------: |
| x-translation SD            |           1.74 mm          |        **1.59 mm**        |
| y-translation SD            |           5.04 mm          |        **2.59 mm**        |
| z-translation SD            |          13.87 mm          |        **2.14 mm**        |
| pitch SD                    |            6.43°           |         **1.11°**         |
| roll SD                     |            1.25°           |         **0.62°**         |
| yaw SD                      |            1.42°           |         **0.69°**         |

High variation in head placement before the introduction of the Laser-to-eyes technique should be partly attributed to variations in scan geometry parameters rather than real misplacements (e.g. high pitch SD - highly unlikely to be a positioning error).

## Data Completeness

| Data Type | Coverage | Notes |
|-----------|----------|-------|
| **Functional MRI** | 458 runs, 85 hours | 256 runs (51.6h) from standardized protocol |
| **T1-weighted** | 195 scans, 84 sessions | Multiple acquisitions per session enable reliability analysis |
| **DTI** | 54 sessions | Consistent protocol (32 directions, b=800) |
| **Physiological monitoring** | 89 sessions (170 runs) | 73 standard protocol sessions (57% coverage) |
| **Pre-scan PVT** | 146 sessions | 87% standard protocol, 60% overall |
| **Pre-scan PANAS** | 131 sessions | 80% standard protocol, 54% overall |
| **Vigilance state** | 384/458 runs (84%) SSS, 64% sleep | Stanford Sleepiness Scale + sleep occurrence |
| **Sleep logs** | 277/321 nights (86%) | Missing nights marked; synthetic events flagged |
| **Medication logs** | Complete record | 286 dose events spanning entire study |

## Recommended Use Cases

### Methodological Development
Single-subject design eliminates between-subject variance, enabling focused testing of:
- Preprocessing pipeline optimization
- Motion correction strategies
- Connectivity measure reliability
- Analysis approaches under non-ideal but realistic acquisition conditions (no fieldmaps, standard clinical sequences)

### Within-Subject Connectivity Reliability
Extended temporal coverage with consistent protocol enables assessment of connectivity measure stability across timescales from hours to months, eliminating between-subject variance.

### State-Dependent Connectivity Analysis
Systematic vigilance state documentation across 59 hours enables investigation of arousal-dependent network dynamics:
- Eyes-open/awake: 34.1h (mean FD = 0.13mm)
- Eyes-closed/awake: 10.0h (mean FD = 0.18mm)
- Partial sleep: 7.3h (mean FD = 0.20mm)
- Frank sleep: 17.8h (mean FD = 0.29mm)

### Naturalistic Longitudinal Observation
The dataset documents co-occurring physiological, behavioral, and environmental transitions during antidepressant discontinuation that coincided with seasonal change. Detailed dosing logs and session-level regressors are provided:
- Recent dose amount (mg, 48h window)
- 21-day rolling average dose (therapeutic timescale)
- Acute withdrawal indicator (>28h since last dose)
- Withdrawal burden (accumulated stress from irregular dosing)

**Important limitation**: Medication taper, photoperiod, and procedural improvements are strongly correlated and cannot be analytically disentangled within this single-subject design. The dataset provides a resource for exploratory analysis rather than causal inference.

See `derivatives/medication/` for complete logs and `sub-001_sessions.tsv` for session-level regressors.

### Personalized Neuroimaging
Dense temporal sampling demonstrates feasibility of individual-level network characterization and tracking neural dynamics within a single person across extended timescales.

## Key Files for Getting Started

### Essential Metadata
- **`derivatives/sub-001_func_runs.tsv`** - Comprehensive metadata for all 458 functional runs
  - Includes: sequence protocol, volume counts, eyes condition, standardized protocol indicators, vigilance state
  - Boolean columns `stdEO` and `stdEC` for efficient filtering
  
- **`sub-001/sub-001_sessions.tsv`** - Session-level covariates and summary statistics
  - Pharmacological regressors (recent dose, 21-day average, withdrawal metrics)
  - PVT performance (median RT, lapse count)
  - PANAS scores (positive/negative affect)
 
  
### Quality Control
- **`derivatives/mriqc/`** - Complete MRIQC v25.1.0 outputs
  - Per-run JSON files with comprehensive image quality metrics
  - Functional: framewise displacement, DVARS, temporal SNR, artifact statistics
  - Structural: CNR, SNR, tissue contrast, TPM overlaps
  - DTI: signal-to-noise, noise estimates, artifact detection

### Geometric Positioning Data
   - **`derivatives/spatial_consistency/sub-001_3iso_spatial_consistency.tsv`** - Between-session positioning metrics
     - Rigid-body alignment parameters for first volume of each 3iso run
     - Enables assessment of self-scanning reproducibility across sessions

### Pharmacological Data
- **`derivatives/medication/sub-001_venlafaxine_doses.tsv`** - Complete dosing record
  - 286 dose events with timestamps (ISO 8601)
  - Dosage amounts and administration methods
  - Source provenance (logged vs. synthetically generated for baseline)
  
### Behavioral and Lifestyle Data
- **`derivatives/sleep/sub-001_sleep_events.tsv`** - Sleep timing (86% coverage)
- **`derivatives/caffeine/sub-001_coffee_events.tsv`** - Coffee consumption
- **`derivatives/alcohol/sub-001_alcohol_events.tsv`** - Alcohol intake (0.5L beer-equivalents)
- **`derivatives/exercise/sub-001_exercise_sessions.tsv`** - Intentional workout logs
- **`derivatives/steps/sub-001_steps_events.tsv`** - Apple Health step records

### Source Data
- **`sourcedata/sub-001_messages_raw.tsv`** - Raw Telegram logging export
- **`sourcedata/assessments/sub-001_pre_session_PVT_PANAS.tsv`** - Trial-level assessment data

All files include JSON sidecars following BIDS conventions.

## Processing Code

Reproducible scripts for all data derivations are provided in `code/`:
- SCANPHYSLOG to BIDS conversion
- PVT/PANAS scoring and summary computation
- Pharmacokinetic modeling and session-level regressor calculation
- Philips slice interpolation preprocessing helper

**PVT/PANAS testing interface:** https://eugenpt.github.io/ep_fmri_tests/pvt.html

All code released under CC0 license.

## Protocol Evolution

Data collection spanned three phases:

1. **Protocol Development** (November 2024 - January 2025, 3 months)
   - Optimization of scan protocols and self-scanning procedures
   - High geometric variability before standardized positioning technique
   - Testing of 2.5mm isotropic high-resolution protocol (discontinued)

2. **Standardized Data Collection** (February - September 2025, 7.5 months)
   - 128 sessions with consistent paired acquisition protocol
   - Concurrent gradual antidepressant discontinuation
   - 98% self-administered (125/128 sessions)
   - Geometric reproducibility substantially improved from June 10, 2025 onward

    2.1. **Laser-to-eyes technique introduction** (June 10, 2025)
    - Implementation of laser crosshair projected onto participant's eyes
    - Marked reduction in geometric variability (translation SD <3mm, rotation SD <1.5°)
    - Enabled increased frequency of T1w and DTI acquisitions

    2.2. **T1w slice thickness tests** (June - early July 2025)
    - Evaluation of 1.0–2.0 mm slice thickness in 0.25 mm increments
    - Resulted in adoption of 1 mm protocol for subsequent scans

Users comparing data across phases should note increased geometric variability during early development sessions and during mid-study T1-weighted slice-thickness tests (1.0–2.0 mm).

## Data Quality Summary

### Functional MRI

* **58 hours** meet *strict* motion criteria (mean FD < 0.2 mm)
* **75.4 hours** meet *moderate* motion criteria (mean FD < 0.3 mm)
* Temporal SNR: **36 ± 8** (median 37, range 12–54)

**Between-session geometric reproducibility:**
Following the introduction of the *Laser-to-eyes* alignment technique (June 2025), between-session head positioning variability decreased several-fold, achieving **sub-3 mm and sub-degree reproducibility** across axes - **comparable to operator-assisted acquisitions**.
Earlier variability likely includes both aiming/positioning variations and minor geometry or prescription differences.
Detailed statistics are provided in the [Self-Scanning Methodology](#self-scanning-methodology) section.

**Self-administered vs. operator-assisted acquisitions:**
Unadjusted comparisons of 3 mm isotropic EPI runs show higher mean framewise displacement (FD) in self-administered sessions than in operator-assisted sessions (0.187 vs. 0.137 mm), reflecting systematic differences in behavioral state. Self-administered sessions were more frequently conducted during periods of reduced alertness.

In regression analyses controlling for vigilance state (sleep), eyes-open vs. eyes-closed condition, and run duration, self-administration was not an independent predictor of either motion (FD) or temporal SNR. Instead, vigilance state, eyes condition, and motion were the dominant predictors of data quality. Quantitative stratified summaries and run-level covariates are provided in `derivatives/sub-001_func_runs.tsv`.

### Structural MRI
- CNR: 2.20 ± 0.11
- Total SNR: 7.48 ± 0.62
- TPM overlaps: GM 0.52 ± 0.01, WM 0.54 ± 0.01
- 1mm slice acquisitions (n=56) show improved metrics vs. 2mm (n=98)

### Diffusion MRI
- SNR (b=0): median 7.64 (IQR 1.49)
- SNR (b=800): median 7.87 (IQR 1.86)
- NDC: median 0.592 (all sessions > 0.10 exclusion threshold)
- Stable noise characteristics across 11 months

### Pre-Scan Assessments
- **PVT**: Median RT 299 ± 18ms, 78% of sessions with ≤1 lapse
- **PANAS**: Positive affect 28.8 ± 4.5, Negative affect 16.9 ± 3.5

## Usage Notes

### Key Limitations

- **Single-subject, time-locked design (N = 1):** Medication dose, season/photoperiod, vigilance, and procedural optimization are strongly correlated over time and cannot be disentangled. Causal inference regarding pharmacological, seasonal, or learning-related effects is not supported.

- **No susceptibility distortion correction:** No field maps or reversed phase-encoding acquisitions were obtained. Functional and diffusion data are provided without distortion correction, limiting anatomical localization in susceptibility-prone regions.

- **Minimal diffusion MRI protocol:** Diffusion data (32 directions, single shell, b = 800 s/mm²) support basic tensor-level analyses and longitudinal consistency assessment, but are not suitable for advanced microstructural modeling or robust tractography.

- **Subjective behavioral annotations:** Vigilance, sleep, and fatigue measures are primarily self-reported and should be treated as subjective estimates rather than objective ground truth.

- **Potential scanner drift:** No phantom scans were acquired; longitudinal trends in image quality may reflect scanner or reconstruction drift, procedural optimization, or physiological factors.

- **Self-administered scanning context:** A substantial portion of the dataset was acquired via self-administered scanning under institution-specific safety conditions and should not be interpreted as a generally applicable acquisition protocol.

### Self-Scanning Generalizability and Safety Considerations

⚠️ Safety warning: self-administered scanning is not a general recommendation.

The self-administered scanning procedures described here were conducted under institutional safety regulations at the International Tomography Center SB RAS, with approval for autonomous operation limited to this individual case. This methodology may not generalize to all populations. The participant was a researcher with extensive prior fMRI experience, high tolerance for confined spaces, and familiarity with scanner operation and MRI safety procedures. Self-administered scanning involves non-trivial risks, including independent verification of MRI safety, operation of bed controls while positioned inside the bore, and autonomous recognition of abnormal or emergency situations.

During all self-administered sessions, standard emergency stop mechanisms, intercom communication, and bore exit controls were available to the participant, consistent with institutional MRI safety procedures.

This approach should only be considered under exceptional circumstances by individuals with demonstrated competence in scanner operation and only after formal institutional safety review and authorization. Institutional safety protocols and operator oversight remain essential for any broader application. Accordingly, this dataset documents a case-specific, institution-approved implementation and should not be interpreted as a generally applicable or recommended scanning paradigm.

### Temporal and Environmental Considerations

Data collection spanned 11 months (November 2024 - September 2025) across seasonal transitions in the Northern hemisphere (Novosibirsk, 55°N), with photoperiod ranging from ~7 hours (winter solstice) to ~17 hours (summer solstice). **Venlafaxine dose, photoperiod, and procedural refinements are tightly correlated over time** (see draft Technical Validation section). Analyses exploring pharmacological or seasonal influences should therefore be interpreted with caution.

### Quality Control Recommendations

Run-level quality metrics from MRIQC are provided in `derivatives/mriqc/`. Users can apply flexible quality thresholds based on their analysis approach: 58 hours meet strict criteria (mean FD < 0.2mm), 75.4 hours meet moderate criteria (mean FD < 0.3mm). Motion varies systematically with vigilance state, enabling both stringent connectivity analyses using high-quality awake data and investigation of state-dependent dynamics across the arousal spectrum.

### Behavioral and Physiological Data Interpretation

PVT was conducted via web browser with some timing overhead; relative within-subject comparisons should remain valid for assessing alertness fluctuations. Trial-level logs are available as raw data. Physiological trigger timing was derived by detecting gradient-active periods (see Methods). Medication regressors for the pre-taper baseline use synthetically generated 08:00 dose events (flagged as source="generated"). Sleep data coverage is 86% overall with missing nights marked in `derivatives/sleep/`; sleep logs are self-reported and reflect subjective timing estimates. Exercise logs reflect intentional workouts; step counts provide complementary objective activity measures. 

**Vigilance-state labels should be treated as subjective estimates**; users are encouraged to derive complementary arousal proxies from the provided physiological recordings (e.g., HRV or respiratory variability) or head-motion patterns if objective state classification is required. Raw data and complete derivation code are provided for all measures.

### Protocol Evolution and Cross-Phase Comparisons

The scanning protocol evolved over 11 months: a 3-month development phase optimized self-scanning procedures, followed by 7.5 months of standardized data collection (128 sessions marked with `std` suffix). T1-weighted slice thickness testing (1.0-2.0mm) occurred mid-study; most sessions used 1.0mm (n=56) or 2.0mm (n=98) acquisitions.

## Citation

Please cite this dataset as:

> **Petrovskiy, E.D.** (2025). *Dense longitudinal single-subject multimodal MRI dataset with self-administered acquisition.* OpenNeuro, [Dataset](https://openneuro.org/datasets/ds006772), DOI: [10.18112/openneuro.ds006772.v1.0.5](https://doi.org/10.18112/openneuro.ds006772.v1.0.5)


## License

This dataset is released under **CC0** (Creative Commons Zero v1.0 Universal) - dedicated to the public domain. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

## Contact

**Evgeny D. Petrovskiy**
[petrovskiy@tomo.nsc.ru](mailto:petrovskiy@tomo.nsc.ru)
International Tomography Center SB RAS  
Novosibirsk, Russia

For questions or issues regarding this dataset, please contact the author directly.

The participant (author) provided written informed consent for data acquisition and unrestricted public data sharing.

## Acknowledgements

The author thanks the Ministry of Science and Higher Education of the Russian Federation for granting access to the equipment at the Center of Collective Use "Mass Spectrometric Investigations" SB RAS, International Tomography Center, Novosibirsk, Russian Federation.

---

**Dataset Version:** 1.0.3
**BIDS Version:** 1.9.0  
**Last Updated:** [2025-10-15]
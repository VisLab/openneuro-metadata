## **EEG-Controlled Exoskeleton for Walking and Standing – A Longitudinal Motor Imagery Study in Healthy Adults**

### **Dataset Overview**
This dataset comprises multimodal recordings from a brain–machine interface (BMI) training study involving seven healthy adult participants (ages 20–30 years; mean = 24.3, SD = 3.8). The study investigated both open-loop and closed-loop control of a lower-limb exoskeleton (Rex Bionics). The dataset includes 60-channel EEG, 4-channel EOG, motion data from two IMU sensors (mounted on the participant's forehead and the exoskeleton), and exoskeleton control and feedback signals. Each participant completed nine sessions over several weeks, with each session structured into a training phase followed by a closed-loop trial phase.

### **Experimental Design**

- **Participants:** 7 healthy adults (4 male, 3 female)
- **Sessions:** 9 per participant
- **Training Phase:** Motor imagery calibration
- **Trial Phase:** Closed-loop BMI control (walk/stop)
- **Conditions:** Walk / Stop (motor imagery)

### **Task Structure**

**Training:**
Participants perform motor imagery tasks without feedback to calibrate the BMI decoder.

**TrialXX:**
Each session includes 12 closed-loop BMI trials (trial01–trial12), during which participants use motor imagery to control the exoskeleton in real time.

- **Block 1:** Trials 1–4
- **Block 2:** Trials 5–8
- **Block 3:** Trials 9–12

**walk6min / stop6min:**
After the 12 trials, participants complete two extended motor imagery tasks:

- **walk6min:** Imagining continuous walking for 6 minutes
- **stop6min:** Imagining standing still for 6 minutes

### **Data Modalities**

- **EEG:** 60 scalp channels + 4 EOG channels
- **IMU:** 3-axis accelerometer, gyroscope, magnetometer, and quaternion
- **Sensor Placement:** IMUs mounted on the participant's forehead and the exosuit back brace
- **Decoder Signals / Feedback:** Logged control signals and BMI predictions

### **Additional Materials**

- **MIQ‑RS:** Motor Imagery Questionnaire – Revised Second Version (PDFs in `derivatives/MIQ-RS/`)
- **Validation Tables:** Data availability, synchronization, and electrode placement (`derivatives/validation/`)
- **Raw Data:** Provided without filtering or artifact removal

### **Folder Structure**

---

```
dataset-root/
│
├── sub-{SubNo}/
│   └── ses-{SesNo}/
│       ├── eeg/
│       │   ├── sub-{SubNo}_ses-{SesNo}_coordsystem.json
│       │   ├── sub-{SubNo}_ses-{SesNo}_electrodes.tsv
│       │   ├── sub-{SubNo}_ses-{SesNo}_electrodes.json
│       │   │
│       │   ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_eeg.edf
│       │   ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_eeg.json
│       │   │
│       │   ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_acq-{AcqLabel}_events.tsv
│       │   ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_acq-{AcqLabel}_events.json
│       │   │
│       │   ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_recording-{StimLabel}_stim.tsv.gz
│       │   └── sub-{SubNo}_ses-{SesNo}_task-{Task}_recording-{StimLabel}_stim.json
│       │
│       └── motion/
│           ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_tracksys-{IMUPos}_motion.tsv
│           ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_tracksys-{IMUPos}_motion.json
│           ├── sub-{SubNo}_ses-{SesNo}_task-{Task}_tracksys-{IMUPos}_channels.tsv
│           └── sub-{SubNo}_ses-{SesNo}_task-{Task}_tracksys-{IMUPos}_channels.json
│
└── derivatives/
    ├── MIQ-RS/
    │   └── sub-{SubNo}_MIQ-RS.pdf
    │
    └── validation/
        ├── BeepValidation.xls
        ├── ExoIMU_Stats.xls
        ├── ExoIMU_W_vs_S.xls
        ├── HeadIMU_Stats.xls
        ├── HeadIMU_W_vs_S.xls
        ├── IMU_Orientation.xls
        ├── Training-OpenLoop-Stats.xls
        ├── Trial-CloseLoop-Stats.xls
        ├── failCounterValidation.xls
        ├── infoClosedLoopValidation.xls
        ├── rexCommandValidation.xls
        └── rexStateValidation.xls
```

### **Naming Convention**

| Placeholder | Description | Values |
|---|---|---|
| `{SubNo}` | Participant ID | 01–07 |
| `{SesNo}` | Session Number | 01–09 |
| `{Task}` | Task name | `training`, `trial01–trial12`, `stop6min`, `walk6min` |
| `{AcqLabel}` | Acquisition label | `infoclosedloop`, `rexcommand`, `rexstate` |
| `{StimLabel}` | Stimulus label | `beep`, `failcounter` |
| `{IMUPos}` | IMU position | `head`, `exo` |

### **Citation**
If you use this dataset, please cite the associated study and acknowledge the contributors.

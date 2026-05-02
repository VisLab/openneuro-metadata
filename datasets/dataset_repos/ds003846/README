
# Readme

In case of any questions, please contact: Lukas Gehrke, lukas.gehrke@tu-berlin.de, orcid: 0000-0003-3661-1973

## Overview

Cyber-Physical Systems: Prediction Error

These data were collected at https://www.tu.berlin/bpn. Data collection occurred either between 10:00 and 12:00 or between 14:00 and 18:00.

To learn about the task, independent-, dependent-, and control variables, please consult the methods sections of the following two publications:

https://dl.acm.org/doi/abs/10.1145/3290605.3300657
https://iopscience.iop.org/article/10.1088/1741-2552/ac69bc/meta

- Contents of the dataset: Output from BIDS-validator

Summary
324 Files, 9.76GB
19 - Subjects
5 - Sessions

Available Tasks
PredictionError

Available Modalities
EEG

- [ ] Quality assessment of the data: Link to data paper, once done

## Methods

### Subjects

The study sample consists of 19 participants (participant_id 1 to 19) with ages ranging from 18 to 34 years and varying cap sizes from 54 to 60. Stimulation is delivered in three blocks: Block_1, Block_2, and Block_3, utilizing different combinations of Visual, Vibro, and EMS.

Participant Information:
Age: Ranges from 18 to 34 years.
Cap Size: Varied, with sizes ranging from 54 to 60.
Stimulation Blocks:
Block_1 and Block_2 include Visual, Visual + Vibro, and Visual + Vibro + EMS.
Block_3 primarily involves Visual + Vibro + EMS.
Usage of Stimulation Blocks:
Most participants experience Visual stimulation in all blocks.
Visual + Vibro is common in Block_1 and Block_2.
Visual + Vibro + EMS is prevalent in Block_3.
Some participants did not experience certain blocks (indicated by "0").
Other Observations:
Cap size variation doesn't show a clear pattern in relation to stimulation blocks.
Participants exhibit diverse stimulation patterns, showcasing individualized experiences.

### Task, Environment and Variables

This set of variables outlines key parameters in a neuroscience experiment involving a haptic task. Here's a summary:

box:
Description: Represents the target object to be touched following its spawn.
Units: String (presumably indicating the characteristics or identity of the object).
normal_or_conflict:
Description: Describes the behavior of the target object in the current trial, distinguishing between oddball and non-oddball conditions.
Units: String (presumably indicating the nature of the trial).
condition:
Description: Indicates the level of haptic realism in the experiment.
Units: String (presumably representing different levels of realism).
cube:
Description: Specifies the position of the target object, whether it is located on the left, right, or center.
Units: String (presumably indicating spatial orientation).
trial_nr:
Description: Denotes the number of the current trial in the experiment.
Units: Integer.

### Apparatus

Here's a summary of the recording environment:

- **EEG Stream Name:** BrainVision
- **EEG Reference and Ground:** FCz and AFz, respectively
- **EEG Channel Locations:** 63 channels with specific names (e.g., Fp1, Fz, Pz) and types (EEG)
- **Additional Channels:** 1 EOG (Electrooculogram)
- **Power Line Frequency:** 50 Hz
- **Manufacturer:** Brain Products
- **Manufacturer's Model Name:** BrainAmp DC
- **Cap Manufacturer:** EasyCap
- **Cap Model Name:** actiCap 64ch CACS-64
- **EEG Placement Scheme:** Positions chosen from a 10% system
- **Channel Counts:**
  - EEG Channels: 63
  - EOG Channels: 1
  - ECG Channels: 0
  - EMG Channels: 0
  - Miscellaneous Channels: 0
  - Trigger Channels: 0

This configuration indicates a high-density EEG setup with specific electrode placements, utilizing Brain Products' BrainAmp DC model. The electrode cap is manufactured by EasyCap, with the specific model name actiCap 64ch CACS-64. The EEG data is sampled at an unspecified frequency, and the system is designed to capture electrical brain activity across a comprehensive set of channels. The recording includes an additional channel for recording eye movements (EOG). Overall, the setup appears suitable for detailed EEG investigations in neurophysiological research.

The motion capture recording environment uses two devices: "rigid_head" and "rigid_handr," which correspond to "HTCViveHead" and "HTCViveRightHand" in the BIDS (Brain Imaging Data Structure) naming convention. The tracked points include "Head" and "handR." The motion data is captured using quaternions with channels named "quat_X," "quat_Y," "quat_Z," and "quat_W." Positional data includes channels "_X," "_Y," and "_Z." The system is manufactured by HTC, with the model name "Vive," and the recording has a sampling frequency of 90 Hz. Additional information such as software versions is not provided.
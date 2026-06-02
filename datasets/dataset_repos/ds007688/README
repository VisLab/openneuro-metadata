# The Temporal Sequence of Party Leader Incongruence: A multitask EEG dataset

## Introduction
This dataset contains high-density EEG (and linked behavioral data) from a preregistered study investigating how partisans process political incongruence. The study tests the **'Hot Cognition'** hypothesis by disentangling the temporal sequence of neural responses to party leaders (identity incongruence) and their messages (source-content incongruence). 

Data was collected in the Netherlands, using supporters of the progressive **GreenLeft/Labour (GL/PvdA)** party as the in-party group and the far-right **Party for Freedom (PVV)** as the out-party group.

## Dataset Content
The dataset includes data from 44 healthy adult participants. It is organized according to BIDS v1.8.0.
The release includes:
1. **Raw EEG recordings** in EDF format with BIDS-compliant JSON sidecars. Find original downsampled fif. files in \sourcedata.
2. **Behavioral data**: Subjective ratings of agreement, surprise, and upset (Likert scales) and reaction times. You can find it in https://osf.io/xrtcy/overview
3. **Event Annotations**: Trial-by-trial logs including stimulus onsets, durations, trial types (congruent/incongruent), and specific stimulus file references.
4. **Stimuli**: A root-level `/stimuli` folder containing the facial cut-outs (JPG) of the political leaders used.
5. **Code**: Companion preprocessing and analysis scripts.
6. **Derivatives**: Preprocessed data
6. **Metadata**: Additional information

## Experimental Design
The study utilized two primary tasks to isolate different stages of political information processing:

### 1. Just Faces Task (Identity Incongruence)
* **Goal**: To measure automatic neural responses to political social identity.
* **Stimuli**: Four political leaders (Frans Timmermans & Jesse Klaver for GL/PvdA; Geert Wilders & Fleur Agema for PVV) and two unfamiliar control faces.
* **Procedure**: 260 trials. Faces were presented for 700ms.
* **Task**: Participants pressed a key only for unfamiliar faces to ensure attention during Just Faces task.

### 2. Statements & Faces Task (Source-Content Incongruence)
* **Goal**: To investigate how source identity of a political message is processed given source-content congruent and incongruent messages
* **Design**: 2x2 factorial design (Face: In-party vs. Out-party; Statement: Pro-attitudinal vs. Counter-attitudinal).
* **Stimuli**: 240 trials. A statement (1830–2880ms) was followed by a politician's face (1200–1400ms).
* **Issues**: Immigration, climate change, EU expansion, gender equality, vegetarianism, and cultural integration.
* **Task**: In ~18% of trials, participants rated their agreement, surprise, or upset.

## Data Acquisition
* **EEG System**: 64-channel BioSemi ActiveTwo system.
* **Electrodes**: International 10-20 layout, including EOG, ECG, and mastoid leads.
* **Reference**: Recorded with CMS/DRL; re-referenced to average reference during preprocessing.
* **Filtering**: Data were band-pass filtered offline (0.5–40 Hz).
* **Software**: Stimuli were presented and analysed using PsychoPy and MNE-Python.

## Technical Validation
* **Behavioral**: Analysis confirmed strong in-party favoritism. Participants agreed more with in-party leaders and felt greater surprise/upset when in-party leaders were paired with counter-attitudinal statements.
* **Neural (ERP)**: Cluster-based permutation tests revealed an enhanced early posterior positivity (Visual P2) for out-party stimuli emerging as early as 148ms, suggesting rapid, pre-conscious detection of political opponents.

## Data Quality Notes
* **Participant Exclusions**: 
    * Just Faces (H1): n=37 included after excluding for EEG noise/bad channels.
    * Statements & Faces (H3): n=36 included due to technical issues in trial recording for some participants.
* **Bad Channels**: Frequently interpolated channels included AF7, F7, FT8, FC5, and C2.
* **Demographics**: The sample consists primarily of young, progressive-leaning university students (Mean age = 21.4).

## Usage Recommendations
* **Citing this dataset**: Please search associated the preprint or paper with the following name:
  > Couto de Jesus, G., Bakker, B. N., Schumacher, G., & Bathelt, J. (2026). The Temporal Sequence of Party Leader Incongruence: a data-driven ERP study.
* **Running its code**
  > The python scripts stored in \code were built to analyse downsampled fif. files (see \sourcedata). 

## Acknowledgements
Funding was provided by:
* **IP-PAD**: European Union’s Horizon Europe MSCA Doctoral Networks (Grant No. 101072992).
* **POLEMIC**: European Research Council (ERC) (Grant No. 759079).
* **NWO**: Talent Programme VIDI (Project No. VI.Vidi.211.055).

Special thanks to Anna Mae van Dooren, Lois van Petegem, and Rayna Akil for data collection assistance.

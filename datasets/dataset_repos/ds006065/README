# iEEG Dataset: Theta-synchronized Stimulation of Human Hippocampal Networks

## Information
This folder contains intracranial EEG (iEEG) data from **7 participants** undergoing closed-loop stimulation as part of a study on hippocampal network connectivity, as used in the following publication:  

**Kragel et al., 2025, Nature Communications:**  
*“Closed-loop control of theta oscillations enhances human hippocampal network connectivity”*  

For questions or further information, contact:  
- **James Kragel:** [jkragel@uchicago.edu](mailto:jkragel@uchicago.edu)  
- **Joel Voss:** [joelvoss@uchicago.edu](mailto:joelvoss@uchicago.edu)  

---

## License
This dataset is made available under the **Public Domain Dedication and License v1.0**.  
Full text: [http://www.opendatacommons.org/licenses/pddl/1.0](http://www.opendatacommons.org/licenses/pddl/1.0)

---

## Dataset and Protocol
The data are organized according to the **Brain Imaging Data Structure (BIDS)** iEEG specification, a community-driven standard for organizing neurophysiology data along with its metadata.  

### Structure
Each subject folder contains the raw iEEG data for that subject, segmented into different periods of the stimulation protocol:
- **Pre-stimulation evoked potentials**
- **Post-stimulation evoked potentials**
- **Pre-stimulation rest**
- **Post-stimulation rest**
- **Closed-loop stimulation**
- **Control stimulation**

---

## Raw Data
The raw data are stored in **BrainVision format** (`vhdr`, `vmrk`, and `eeg` files). You can read these files into memory using the following tools:

- **MATLAB:** [FieldTrip toolbox](https://www.fieldtriptoolbox.org/getting_started/eeg/brainvision/)  
- **Python:** [`pybv` package](https://github.com/bids-standard/pybv)  

### Electrode Coordinates
Electrode coordinates are provided in **MNI space**, registered to the **MNI152 2009c asymmetrical template**.

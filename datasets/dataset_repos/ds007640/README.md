# Dataset of Emotion Recognition Using Validated Video Stimuli with Large-scale Behavioral Survey and MEG Recordings

## General Description
This dataset was developed as part of research focused on brain signal-based emotion recognition by capturing high-fidelity Magnetoencephalography (MEG) signals during induced different emotional states. The dataset is organized into three primary components: 

1. **Phenotype (Online Survey)**: Stored within the 'phenotype' directory, this component contains the results of a large-scale subjective emotional assessment of the set of 40 video stimuli. It includes responses from 500 participants, providing robust behavioral baseline.  
2. **Source Data (Head Digitization)**: Located in 'sourcedata' directory, this component contains head position information measured prior to each recording session. The resulting configuration files ('.cfg') store the 3D spatial coordinates (x, y, z) for anatomical landmarks and Head Position Indicator (HPI) coils, essential for accurate co-registration. 
3. **MEG Recording**: Comprehensive MEG neural recordings from 23 participants, who viewed the same 40 validated video clips used in the online survey. These recordings enable the investigation of emotion-specific neural signal patterns and are organized into subject-specific directories (e.g., 'sub-01'). 

To capture the richness of emotional experiences, we employed a multi-faceted assessment paradigm. Beyond the standard Self-Assessment Manikin (SAM) responses for Valence and Arousal, our labels include discrete emotion categories (PrEmo) and temporal highlight scene selections, providing a more granular ‘ground truth’ for affective states. 

## Citation
For a detailed description of the stimulus selection, experimental design, and data acquisition process, please refer to the publication listed below. We kindly request that any research utilizing this dataset cites the following paper: 
[Add on Reference/DOI]

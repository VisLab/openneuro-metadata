Dataset description
===================

This dataset was collected for the study "Diagnostic ultrasound enhances, then reduces, exogenously induced brain activity of mice" by Tan et al. (2024). The research demonstrates how transcranially delivered diagnostic ultrasound (tDUS) modulates the brain's receptivity to external stimuli, using a blinking light stimulus in a mouse model.
The study findings highlight the potential for diagnostic ultrasound to intentionally modulate brain function, paving the way for possible future clinical and therapeutic applications.
Please cite the following paper when using this dataset:

Tan H, Griggs DJ, Chen L, et al. Diagnostic ultrasound enhances, then reduces, exogenously induced brain activity of mice. Frontiers in Neuroscience. 2024. DOI: [in peer review].


License
-------

This dataset is proprietary to the Department of Neurological Surgery, University of Washington, Seattle, WA, USA.  
Usage is restricted to academic and non-commercial research. Redistribution, modification, or commercial use is prohibited without prior permission.  
For inquiries, contact: Pierre D. Mourad (doumitt@uw.edu).


Acknowledgements
----------------

We thank the Department of Neurological Surgery, University of Washington, for internal funding.  
This research was supported by R01 NS119395 and P51 OD010425 (DJG) and the Mary Gates Research Scholarship** (HT).


Dataset Overview
-----------------

This dataset comprises electrocorticography (ECoG) recordings from three cohorts of C57BL/6 mice exposed to combinations of diagnostic ultrasound (tDUS) and blinking light stimuli. The study investigates how tDUS influences the visual cortex's response to external visual stimulation.

Key Features:
- Subjects: 20 C57BL/6 mice divided into three experimental cohorts:
  1. Light-only cohort: Exposed to blinking light only.
  2. US-only cohort: Exposed to tDUS without light.
  3. US+Light cohort: Exposed to blinking light combined with tDUS.
- Electrode Placement: ECoG electrodes targeted visual and somatosensory cortices.
- Recording Conditions: Data recorded at 20 kS/s, filtered (5–55 Hz), and analyzed with MATLAB.


Data Structure
---------------

Data Files:
- Raw ECoG Data: Continuous brain activity recordings.
- Event-Triggered Data: Segment-specific RMS values for blinking light events.
- Processed Data: Filtered and normalized brain activity traces.

Metadata:
- Experimental conditions, cohort allocation, and baseline brain activity.


Methodology
-----------

- Stimulation Protocols: Mice were exposed to blinking light stimuli (10 seconds per event) and tDUS delivered through a P21x5-1 scan head (Sonosite MicroMaxx system).
- Data Collection: Baseline and event-triggered ECoG signals were recorded using LabChart software.
- Analysis: RMS values normalized to baseline activity for comparative statistical analysis.


Outcomes
________

Key Findings:
1. Enhanced Brain Activity: Simultaneous tDUS and blinking light increased cortical activity compared to light alone.
2. Persistent Effects: tDUS effects on brain activity persisted after stimulation ceased.
3. No Effect of tDUS Alone: tDUS without light did not activate cortical activity but reduced subsequent activity.


References
___________

For a complete list of references, please consult the manuscript.





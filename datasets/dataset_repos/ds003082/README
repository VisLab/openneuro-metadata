# Brainstorm - Auditory Cortex Mapping Dataset

## License

This dataset (MEG and MRI data) was collected by Jonathan Cote of the Neuroplasticity and Sensory Biomarking Lab, Montreal Neurological Institute, McGill University, Canada. Its purpose is to serve as a data example to be used with our MEG-based auditory cortex mapping technique. It is presently released in the Public Domain, and is not subject to copyright in any jurisdiction.

We would appreciate though that you reference this dataset in your publications: please acknowledge its authors (Jonathan Cote and Etienne de Villers-Sidani) and cite the mapping technique publication (under review)
 
This dataset will first be a single subject, but might be expanded up to the 10 participants in the future.

## Presentation of the experiment

#### Experiment

* One subject, one acquisition run of around 12 minutes
* Subject stimulated binaurally with intra-aural earphones (air tubes+transducers)
* The run contains:
    * 1795 iso-intensity pure tones (IIPT)
    * The frequency of these ranges between 100 Hz and 21527 Hz, spaced by 1/4 octave.
* Random inter-stimulus interval: randomized but averaging at a presentation rate of 3Hz
* The subject passively listened while looking at a fixation cross
* Auditory stimuli generated with the Matlab Psychophysics toolbox


#### MEG acquisition

* Acquisition at **120000Hz**, with a **CTF 275** system, subject in seating position
* Recorded at the Montreal Neurological Institute in January 2015
* Anti-aliasing low-pass filter at 3000Hz, files saved with the 3rd order gradient
* Recorded channels (340):
    * 1 Trigger channel indicating the presentation times of the audio stimuli: UADC001 (#306)
    * 26 MEG reference sensors (#4-#29)
    * 272 MEG axial gradiometers (#30-#302)
    * 1 ECG bipolar (#303)
    * 2 EOG bipolar (vertical #304, horizontal #305)
    * 3 Unused channels (#1-#3)
* 3 datasets:
    * **sub-0001_ses-0001_task-mapping_run-01_meg.ds**: Run #1, 653s, 1795 IIPT, sampled at 12000 Hz

    * **sub-emptyroom_ses-0001_emptyroom_run-01_meg.ds**: Empty room recording, 120s long, sampled at 12000 Hz

    * **sub-emptyroom_ses-0001_emptyroom_run-02_meg.ds**: Empty room recording, 120s long, sampled at 2400 Hz

* Use of the .ds, not the AUX (standard at the MNI) because they are easier to manipulate in FieldTrip

#### Stimulation delays


* **Delay #1**: Transmission of the sound.   
Between when the sound card plays the sound and when the subject receives the sound in the ears. This is the time it takes for the transducer to convert the analog audio signal into a sound, plus the time it takes to the sound to travel through the air tubes from the transducer to the subject's ears. This delay cannot be estimated from the recorded signals: before the acquisition, we placed a sound meter at the extremity of the tubes to record when the sound is delivered. Delay **between 4.8ms and 5.0ms** (std = 0.08ms). At a sampling rate of 2400Hz, this delay can be considered **constant**, we will not compensate for it.
* **Delay #2**: Recording of the signals.   
The CTF MEG systems have a constant delay of **4 samples** between the MEG/EEG channels and the analog channels (such as the audio signal UADC001), because of an anti-aliasing filtered that is applied to the first and not the second. This translate here to a **constant delay** of **1.7ms**.
* **Uncorrected delays**: We will  keep the delays. We decide not to compensate for these delays because they do not introduce any jitter in the responses and they are not going to change anything in the interpretation of the data.

#### Head shape and fiducial points

* 3D digitization using a Polhemus Fastrak device driven by Brainstorm (S01_20131218_*.pos)
* More information: [Digitize EEG electrodes and head shape][1]
* The output file is copied to each .ds folder and contains the following entries:
    * The position of the center of CTF coils
    * The position of the anatomical references we use in Brainstorm: Nasion and connections tragus/helix, as illustrated [here][2].

* Around 150 head points distributed on the hard parts of the head (no soft tissues)

#### Subject anatomy
* Subject with 1.5T MRI
* Processed with FreeSurfer 5.3


[1]: http://neuroimage.usc.edu/brainstorm/Tutorials/TutDigitize
[2]: http://neuroimage.usc.edu/brainstorm/CoordinateSystems#Pre-auricular_points_.28LPA.2C_RPA.29
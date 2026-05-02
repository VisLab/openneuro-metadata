# README
## Details related to access to the data

-   [ ] Contact person

Name: Hong Chen
Email: hongchen@wustl.edu

-   [ ] Practical information to access the data

The data includes acquired field map images measure the temperature of the brain in response to ultrasound stimulation. The acquired MR field maps (magnitude and phase) were then converted to temperature maps using Image Guided Therapy Thermoguide software.
(http://www.imageguidedtherapy.com/Software/Software-for-real-time-monitoring-and-control-of-thermal-ablation.html).

This dataset only includes the raw magnitude and phase files acquired from the MR scanner.

## Overview
-   [ ] Brief overview of the tasks in the experiment

The purpose of the experiment is to measure the temperature of the brain in response to focused ultrasound stimulation of the brain.
To measure the temperature of the brain, we utilized MR-thermometry, which can non-invasively measure relative changes temperatures in the brain in response to an event.
In this case, the event is a stimuli of focused ultrasound applied to the brain.

-   [ ] Description of the contents of the dataset

The dataset contains:
(1) an anatomical T1-MPRAGE image acquired at the beginning of the scan,
(2) magnitude and phase field map images which are needed to create a temperature map of the brain,
(3) accompanying T2-FLAIR images to assess the safety of the stimulation before proceeding with further scans.

For (2) and (3), there are multiple runs (i.e. run-01 through run-09).
run-01 corresponds to the baseline / sham condition.
run-02, -03, and -04 correspond to stimulation at 150 mVpp, or 1.05 MPa.
run-05, -06, and -07 correspond to stimulation at 200 mVpp, or 1.40 MPa.

-   [ ] Independent variables

Ultrasound is a type of energy that can be manipulated in several ways to alter the amount of energy delivered to the brain at any given time.
For this experiment, we manipulated the acoustic pressure by changing the input voltage to drive the ultrasound transducer.
The acoustic pressure is proportional to the ultrasound power and intensity delivered.

-   [ ] Dependent variables

The temperature of the brain in the target region was measured in response to changes in acoustic pressure.

-   [ ] Control variables

N/A.

-   [ ] Quality assessment of the data

Quality assessment of the data was performed by evaluating the temperature maps on Thermoguide to see if the temperature rise in response to FUS follows reasonable heating and cooling kinetics consistent with literature.

## Methods

### Subjects

A brief sentence about the subject pool in this experiment.

The subject was a male rhesus macaque, aged 11 at the time of data acquisition.
The subject had two recording chambers with craniotomy on each hemisphere to enable access to the brain for electrophysiological recording and stimulation.
All procedures conducted to the subject was approved by the IACUC protocol.

### Apparatus

The subject was placed in the prone position with the head fixed in an MR-compatible large animal stereotaxic frame.
The ultrasound system contained:
(1) a function generator that generates the ultrasound waveform,
(2) a power amplifier to amplifier the energy from the function generator,
(3) the ultrasound device + housing which delivers ultrasound energy to the subject's brain.

(1) and (2) are not MR-compatible and placed inside the MR control room. (3) is connected to (1) and (2) via a long wire that is passed through a small hole that connects the MR scanner room with the MR control room.

### Initial setup

Prior to the experiment, the subject's recording chambers were cleaned thoroughly with aseptic technique. The subject was then anesthetized in the home cage and transported to the MR-scanning bay.
The subject was brought to the MR-scanner bed and placed in the prone position. The anesthesia system was promptly switched from the animal transport cart to the MR-compatible anesthesia system. A pulse-oximeter sensor was attached to the subject's fingers to ensure proper anesthesia depth throughout the whole experiment. The subject's vitals were checked to ensure the subject was under stable anesthesia before proceeding with other procedures.
The subject's head was fixed in an MR-compatible large animal stereotaxic frame to reduce motion during the data acquisition period.
Sterilized ultrasound gel was applied inside the recording chambers. A sterile syringe was used to remove any bubbles present from loading the ultrasound gel.
The ultrasound device was sterilized using sterile alcohol swabs. Sterilized ultrasound gel was also applied to the surface of the device (the transducer) to ensure adequate coupling.
The ultrasound device was inserted into the chamber and fixed via the device housing fitting tightly to the subject's recording chamber.
The ultrasound device was then connected to the rest of the ultrasound system via a long wire.
The subject was covered with warm blankets.

### Task organization

No task was performed during the acquisition of this dataset.

### Task details

No task was performed during the acquisition of this dataset.
The ultrasound device contained a transducer with the following properties:
DL-47 (DeL Piezo Specialties, LLC), 15 mm diameter, 25 mm radius of curvature, 1.5 MHz resonance frequency.

Ultrasound stimulation was delivered with the following parameters:
1.5 MHz frequency, 10 HZ PRF, 50% duty cycle, 15s stimulation duration, acoustic pressure 0 - 1.4 MPa.
At 0 mVpp, the acoustic pressure is 0 MPa.
At 150 mVpp, the acoustic pressure was approximately 1.05 MPa.
At 200 mVpp, the acoustic pressure was approximately 1.40 MPa.

The stimulation was triggered by a TTL signal from the MR control room to the function generator. The stimulation always started on frame 10 out of 100 total acquisition frames.

### Additional data acquired

No additional data was acquired.

### Experimental location

Please refer to JSON files for more details.

### Missing data

N/A.

### Notes

N/A.
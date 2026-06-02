This dataset contains multimodal physiological recordings acquired during smartphone interaction and video viewing conditions. The dataset includes simultaneous electroencephalography (EEG), eye-tracking, photoplethysmography (PPG), and galvanic skin response (GSR) signals.

## **Experimental Protocol**

Participants complete two experimental conditions while wearing a 64-channel EEG cap and a head-mounted eye tracker, with simultaneous PPG and GSR recordings:

**Smartphone Monitor condition (10 min):**
Participants engage in naturalistic smartphone use using their personal devices. They are instructed to interact freely with one of their most frequently used applications (e.g., browsing, reading, or app interaction). No constraints are imposed on interaction style.

**Video Monitor  condition (5 min):** 
Participants view a standardized video presented on a monitor.

## **Participants**
Number of participants: 23 (sub-01 to sub-23)
Participants are healthy adults. Detailed demographic and experimental information (age, sex, and smartphone application type) is provided on participants.tsv at the root of the dataset.

## **Hardware Synchronization and Event Markers**

Session boundaries are marked using hardware-based transistor–transistor logic (TTL) synchronization pulses. Five TTL pulses are delivered at ~1-second intervals to mark session onset and offset. Additional TTL pulses are generated every 20 seconds during the session. These triggers are embedded in both EEG and eye-tracking data streams, enabling precise temporal alignment across all modalities.

EEG event markers are defined for two conditions: Smartphone Monitor (onset: S 12; offset: S 13) and Video Monitor (onset: S 22; offset: S 23).

In the eye-tracking data, session boundaries are identified using TTL bursts consisting of five pulses occuring at ~1-second intervals
with pulse characteristics (Type: sig; Direction: in; Value: 1.0). Additional synchronization pulses are present at ~20-second intervals during sessions. 
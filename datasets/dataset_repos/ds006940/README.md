EEG-Controlled Exoskeleton for Walking and Standing
A Longitudinal Motor Imagery Study in Healthy Adults

Dataset Overview
This dataset contains multimodal recordings from a brain–machine interface (BMI) training study involving seven healthy adult participants (ages 20–30, Mean = 24.3, SD = 3.8). The study focused on open-loop and closed-loop control of a lower-limb exoskeleton (Rex Bionics) using EEG and inertial sensor data. Each participant completed nine sessions over several weeks, structured into training and trial phases.

Experimental Design
* Participants: 7 healthy adults (4 male, 3 female)
* Sessions: 9 per participant
* Training Phase: Motor imagery calibration
* Trial Phase: Closed-loop BMI control (walk/stop)
* Conditions: Walk / Stop (motor imagery)

Task Structure and Naming Convention

Each session includes multiple motor imagery tasks organized as follows:

Training: The training phase is used to calibrate the BMI decoder. Participants perform motor imagery tasks without feedback.

TrialXX:
The trial phase consists of 12 closed-loop BMI trials per session, labeled trial01 to trial12. During these trials, participants use motor imagery to control the exoskeleton in real time.

Block 1: Trials 1–4  
Block 2: Trials 5–8  
Block 3: Trials 9–12  

walk6min / stop6min:
After completing the 12 trials, participants perform two extended motor imagery tasks:

walk6min – Imagining continuous walking for 6 minutes  
stop6min – Imagining standing still for 6 minutes  


Data Modalities
* EEG: 60 scalp channels + 4 EOG channels
* IMU: 3-axis accelerometer, gyroscope, magnetometer, and quaternion
* Sensor Placement: IMUs mounted on participant forehead and exosuit back brace
* Decoder Signals/Feedback: Logged control signals and BMI predictions

Additional Materials
* MIQ-RS: Motor Imagery Questionnaire – Revised Second Version (PDFs in derivatives/MIQ-RS/)
* Validation Tables: Data availability, synchronization, and electrode placement (derivatives/validation/)
* Raw Data: Provided without filtering or artifact removal

BIDS Structure
* dataset_description.json: Metadata and provenance
* sub-XX/ses-YY/: EEG and IMU recordings per session
* derivatives/: MIQ-RS responses and validation spreadsheets

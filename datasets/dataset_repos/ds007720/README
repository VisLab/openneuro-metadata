BCI-FIT: A customization protocol for communication brain-computer interface systems.
============================================================

Dataset Overview
-----------------

The BCI Functional Implementation Toolkit (BCI-FIT) is a flexible, user-centered, interdisciplinary customization protocol for non-implantable communication brain-computer interface (cBCI) systems. Five participants with speech and/or physical impairments resulting from amyotrophic lateral sclerosis (ALS) completed calibration and copy-spelling tasks with both customized and non-customized versions of a non-implantable cBCI over multiple visits. Starting from a predetermined default, system customization was iteratively adjusted after each visit based on typing performance, participant preferences, clinical observations, brain signal characteristics, and results of simulations and other offline exploration. 

- N=5
- Participants had speech and/or physical impairments
- All tasks were proctored using BciPy [1]
- The dataset is organized in accordance with the Brain Imaging Data Structure (BIDS) specification (version 1.7.0).

Methodology
--------------------------------

Testing was conducted on an MSI Trident 3 desktop computer running Windows 11 Professional (64-bit) with an Nvidia GeForce RTX 3060 GPU, 12th-gen Intel i7-12700 CPU (2.10 GHz), and 16 GB RAM. Participants viewed tasks on a 24” monitor with 1920x1080 resolution cycling at 144 Hz. Participants were seated (in a recliner chair or wheelchair, according to their preference) at 50-60 cm from the computer screen, which was mounted on an adjustable table or a floor mount (Rehadapt, Kassel, Germany). Screen distance was approximated using calibration positioning with a Tobii Nano eye-tracking system (Tobii, Stockholm, Sweden). For switch input, participants activated a Jelly Bean switch (AbleNet, Roseville, MN, USA) that they either held in their hand or rested on their lap. EEG activity was recorded from one of two different dry electrode caps (Wearable Sensing, San Diego, CA, USA): DSI-Flex (FCz, Pz, Oz, P3, P4, PO7, and PO8) or DSI-24 (Fp1/2, Fz, F3/4, F7/8, Cz, C3/4, T3/T4 [T7/T8], T5/T6 [P7/P8], Pz, P3/P4, O1/2), accessed in BciPy via Lab Streaming Layer. The cap was chosen based on user preference and a review of signal quality related to cap fit and comfort. Both caps employ a hardware filter permitting a collection bandwidth of 0.003-150 Hz. Recordings were collected with an averaged linked-ear reference ((A1 + A2) / 2) and an active common-mode follower; the ground electrode was located at FCz on the DSI-Flex and at FPz on the DSI-24. All recordings were sampled at 300 Hz. All data were downsampled to 150 Hz and filtered between 1 and 20 Hz (2nd-order) with a 60 Hz notch. 
Participants used Matrix and RSVP typing layouts included in BciPy 2.0 [1]. For each calibration task, participants completed 55 test inquiries, each consisting of a target character prompt, a presentation cue, and a sequence of 14 characters. The prompt target characters were displayed in yellow text within the matrix, or in the center of the screen for RSVP, for 1 second. For the presentation cue, the entire matrix was flashed in red, or a red fixation cross was displayed in the center of the screen for RSVP, for 0.5 seconds to alert participants that the flashing letter sequence was about to begin. The 14 characters in the letter stream were then intensified one at a time in the matrix, or flashed in the center of the screen for RSVP, at 5 Hz. Participants were instructed to watch for the intensification or presentation of the target character (in 10% of inquiries, the target was not intensified). A blank interval of 4 seconds separated each inquiry. Presentation timing, color, and number of characters listed above are default values; these parameters were adjusted as part of system customization.

Copy-spelling was similar to calibration, with the key difference that there were no target prompts in test inquiries. Rather, participants were presented with a partially completed phrase at the top of the screen and asked to copy the final word. All target words were five letters long, and phrases were drawn randomly, without replacement, from a preselected list. Participants were asked to watch for the letter they wanted to type and keep noticing that character until the system made a typing decision. If the decision was correct, they were to begin watching the next letter in the word. If it was incorrect, they were to look for the “<” character to select a backspace and delete the error, then try again to type the next letter in the target word. Each character selection was made after a series of inquiries. In the first inquiry of a series, characters were presented in random order with uniform likelihood probability. In subsequent inquiries, character probabilities were updated based on EEG evidence from classifier-adjusted likelihood estimates. The system showed a minimum of two and a maximum of eight inquiries per series before making a selection, which occurred either when the classifier surpassed a confidence threshold of 0.8 probability or if the maximum inquiry count was reached (in which case the character with the highest probability was selected). Participants attempted to copy four five-letter words per condition per visit. A copy-spelling session would end when the target word was successfully completed, when 10 selections were made, when five erroneous selections occurred in a row, or after 10 minutes had passed.

Directory Structure
------------------------------------------

The dataset follows the BIDS convention with the following structure: `sub-<label>/ses-<label>/eeg/`. Files within each `eeg/` directory follow the pattern `sub-<label>_ses-<label>_task-<TaskName>_run-<index>_eeg.<ext>` (e.g., `sub-P1_ses-1_task-MatrixCalibration_run-1_eeg.vhdr`). EEG signals are stored in BrainVision format due to the high data resoultion available (`.vhdr`/`.vmrk`/`.eeg`). The data may also be shared via EDF or converted to other formats using MNE-BIDS [2] or similar tools, please contact if help is needed in the conversion process.


Paradigms
----------------------------------------
- Paradigms: Matrix, RSVP
- Task types: Calibration, CopyPhrase
- Stimulus alphabet: A–Z, backspace ("<"), and space ("_"), for 28 selectable characters


Participants
----------------------------------------
Five participants are included (sub-P1 through sub-P5). To protect participant privacy given the small sample size and the nature of the disability (ALS), demographic information (age, sex, handedness, clinical measures) is intentionally not distributed with this dataset. The same participant identifiers (P1 ... P5) are used in associated publications and conference presentations, so group demographics and clinical details can be referenced from the BCI-FIT poster (Peters et al., 2025) and forthcoming publication. Researchers requiring demographic, clinical, or otherwise restricted data should contact Betts Peters (petersbe@ohsu.edu) to discuss a separate data-sharing agreement through OHSU.


License
----------------------------------------
This dataset is released under the Creative Commons Zero (CC0 1.0) public-domain dedication. See `dataset_description.json` for the canonical license declaration.


Software
----------------------------------------
- Data collected with BciPy v2.0 (https://github.com/CAMBI-tech/BciPy)
- Converted to BIDS using a custom script relying on BciPy and MNE-BIDS
- BIDS writing via MNE-BIDS v0.14


Contact Information
----------------------------------------

For questions or issues regarding this dataset, please contact the corresponding author, Betts Peters (petersbe@ohsu.edu).


How to Acknowledge / Cite
----------------------------------------
When using this dataset, please cite the BCI-FIT poster:

Peters, B., Kinsella, M., Klee, D., Lawhead, M., Memmott, T., Spaulding, S., Oken, B., & Fried-Oken, M. (2025, June 2–5). BCI-FIT: Effects of cBCI customization on performance [Poster presentation]. 11th International BCI Meeting, Banff, AB, Canada. https://bcisociety.org/wp-content/uploads/2025/05/DeArmond-BCI-2025-program-v106.pdf


References
----------------------------------------

[1] Memmott, T., Koçanaoğulları, A., Lawhead, M., Klee, D., Dudy, S., Fried-Oken, M., & Oken, B. (2021). BciPy: brain-computer interface software in Python. Brain-Computer Interfaces, 8(4), 137–153. https://doi.org/10.1080/2326263X.2021.1878727

[2] Appelhoff, S., Sanderson, M., Brooks, T., Vliet, M., Quentin, R., Holdgraf, C., Chaumon, M., Mikulan, E., Tavabi, K., Höchenberger, R., Welke, D., Brunner, C., Rockhill, A., Larson, E., Gramfort, A., & Jas, M. (2019). MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis. Journal of Open Source Software, 4, 1896. https://doi.org/10.21105/joss.01896

[3] Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., Flandin, G., Phillips, C., Delorme, A., & Oostenveld, R. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Scientific Data, 6, 103. https://doi.org/10.1038/s41597-019-0104-8

[4] Peters, B., Kinsella, M., Klee, D., Lawhead, M., Memmott, T., Spaulding, S., Oken, B., & Fried-Oken, M. (2025, June 2–5). BCI-FIT: Effects of cBCI customization on performance [Poster presentation]. 11th International BCI Meeting, Banff, AB, Canada. https://bcisociety.org/wp-content/uploads/2025/05/DeArmond-BCI-2025-program-v106.pdf

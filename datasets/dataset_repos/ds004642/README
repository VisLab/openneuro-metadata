 ## Intraoperative recordings of medianus stimulation with low and high impedance ECoG
This dataset of medianus SEP was first analyzed in publication [1]. There we investigated whether the low impedance ECoG electrode (LoZ) improves fast ripple detection over a standard electrode with high impedance contacts (HiZ).
There are 10 patients (median age 40 y, range 19-56 y, 6 female) who underwent brain tumor resections in the perirolandic region at our institution. The data includes the continuous raw data from the ECoG contacts of both electrodes. We recorded medianus SEP intraoperatively (stimulation rate = 4.7 Hz) from two 4-contacts ECoG strips simultaneously (LoZ: a contacts, HiZ: b contacts) that had different median impedance (LoZ: 3.4 kΩ, HiZ: 6.9 kΩ).

### Repository structure

### Main directory (LoZ HFO)

Contains metadata files in the BIDS standard about the participants and the study. Folders are explained below.

### Subfolders

-   LoZ HFO/sub-/ Contains folders for each subject, named sub-  and session information.
-   LoZ HFO/sub-/ses-01/ieeg/ Contains the raw ieeg data in .edf format for each subject. Each *ieeg.edf file contains continuous iEEG data from one stimulation rate recorded at the hand area Ω from both the electrodes simultaneously . Details about the channels are given in the corresponding .tsv file.

### Note from the paper

"The offline data processing used the continuous ECoG that was recorded in parallel to the SEP recordings. Data analysis was performed with custom scripts in Matlab. To detect the SEP stimulation artefact, we first filtered the ECoG (high pass cutoff = 200 Hz) and performed local peak detection (minimum peak prominence between peaks = 30 ms, minimum peak width = 4 ms, samples = 0.2 ms). We used the times of the detected stimulus artifact as triggers to define sweeps with post-stimulus recording sweep length 50 ms. We classified sweeps with amplitude ±100 µV as artefact-ridden and excluded them from further analysis.

We averaged 100 sweeps and filtered the averaged trace (bandpass [30 300] Hz, IIR filter, response roll-off -12 db per octave, forward and reverse filtering to avoid phase distortion). We visually inspected the data and selected one optimal channel with high N20 amplitude (positive or negative) for further analysis. From the averaged N20 trace, we determined the N20 peak latency. To obtain the N20 peak amplitude and the SNR, we inspected the latency of the N20 peak. If the N20 latency was >20 ms, we selected a signal window [20 25] ms. If the N20 latency was ≤ 20 ms, we selected a signal window [17 22] ms. In the same way, we filtered the averaged trace in the [250 500] Hz band to obtain the evoked FR and in the [500 1000] Hz band to obtain the evoked HFO. We doubled the largest deflection in the signal window of the N20 frequency band to define the N20 signal amplitude. In the FR and HFO bands we used the peak-to-peak amplitude."

### BIDS Conversion

bids-starter-kid and custom Matlab scripts were used to convert the dataset into BIDS format.

### References
[1] Vasileios Dimakopoulos, Marian C. Neidert, Johannes Sarnthein, Low impedance electrodes improve detection of high frequency oscillations in the intracranial EEG, Clinical Neurophysiology, 2023, ISSN 1388-2457, https://doi.org/10.1016/j.clinph.2023.07.002

If you have any inquiries or questions, contact:

* Vasileios Dimakopoulos (vasileios.dimakopoulos@usz.ch)
* Johannes Sarnthein (johannes.sarnthein@usz.ch)
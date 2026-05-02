DESCRIPTION

Here we share the unprocessed multi-echo GRE data obtained at both 10.5 and 7 T alongside T1w MP2RAGE collected at 7 T, all reported in the following paper: Mesoscale whole-brain T2*-weighted and associated quantitative MRI in humans at 10.5 T. Jiaen Liu, Peter van Gelderen, Jacco A. de Zwart, Jeff H. Duyn, Yujia Huang, Shuxian Qu, Andrea Grant, Edward Auerbach, Matt Waks, Russell Lagore, Lance Delabarre, Alireza Sadeghi-Tarakameh, Yigitcan Eryaman, Gregor Adriany, Kamil Ugurbil and Xiaoping Wu. Magnetic Resonance in Medicine (2026): 1–9, https://doi.org/10.1002/mrm.70366.

Below we provide a brief description of the data. A detailed description of the data including acquisition, reconstruction, processing and analysis can be found in the paper cited above.

PARTICIPANTS

Four healthy adults who signed a consent form were scanned.

DATA ACQUISITION

We performed human experiments on a Siemens Magnetom 10.5 T MR scanner (Siemens Healthineers, Erlangen, Germany) retrofitted with 16-channel RF transmission and 128-channel signal reception systems, and equipped with a whole-body gradient (70 mT/m maximum strength and 200 T/m/s maximum slew rate). A custom-built 16Tx80Rx RF head array, with an FDA-approved investigational device exemption, was used to acquire human brain images. The same human volunteers were scanned at 7 T on a Siemens Terra MR scanner (Siemens Healthineers, Erlangen, Germany), using the commercial Nova single-channel transmit 32-channel receive RF coil (Nova Medical, Wilmington, MA, USA).

At 10.5 T, a 3D ME-GRE sequence with embedded volumetric navigators was used for T2*w data acquisition. Relevant imaging parameters included 0.5 mm isotropic resolution, 240×180×128 mm3 field of view (FOV), 35 ms repetition time (TR), 4 echo times (TEs), TE1 of 10.2 ms, echo spacing (ES) of 4.9 ms, 12° nominal flip angle (i.e., the Ernst angle assuming T1 of 1.75 s for the mean value across gray and white matter at 10.5 T33) and 208 Hz/pixel readout receiver bandwidth. Parallel imaging with controlled aliasing (CAIPI) was applied with an acceleration factor of 2 in the phase-encoding (left-right) direction and 3 in the slice-encoding (head-foot) direction, leading to a total scan time of ~13.3 min.

At 7 T, T2* w data acquisition was performed using the same 3D ME-GRE sequence as the 10.5 T experiments. Imaging parameters including FOV, resolution, 2D acceleration, TE1 and ES were matched to the 10.5 T protocol. Due to the longer T2* values, the 7 T data acquisition employed a 6-echo protocol, leading to a longer TR of 45 ms, a higher nominal flip angle of 14° (using mean 7 T T1 of 1.5 s), and a longer total scan time of ~17.2 min. The volumetric navigator images were collected using the same imaging parameters as those of the 10.5 T protocol, except that their temporal resolution increased to 540 ms due to the increased TR.

For each volunteer, we acquired fully sampled calibration data in a separate reference scan using a multi-echo 2D GRE sequence. This data was used for estimating multi-coil sensitivity maps needed for parallel image reconstruction. Specifically, multi-slice 2D GRE images with whole brain coverage were obtained with the following parameters: 4 mm isotropic in-plane resolution, 256×192 mm2 FOV, 4 mm slice thickness and 50 axial slices. At each field strength, TE was set to the minimum water-fat in-phase TE, 2.56 ms for 10.5 T and 2.88 ms for 7 T, for improved sensitivity map estimation. TR was set to 315 ms for 10.5 T and 500 ms for 7 T, and nominal flip angle to 30° for 10.5 T and 38° for 7 T, leading to a total scan time of less than 25 s.

For image processing and analysis, whole-brain anatomical reference images were collected using T1-weighted (T1w) 3D magnetization prepared two rapid acquisition gradient echoes (MP2RAGE) at 7 T. MP2RAGE parameters included 0.7 mm isotropic resolution, 2.36 ms TE, 4 s TR, and TI1/TI2= 740/2430 ms.

All 3D T2*w ME-GRE images were reconstructed using in-house MATLAB software made publicly available at https://github.com/jiaen-liu/moco. The reconstruction was based on a unified signal model incorporating intra-scan rigid-body motion and B0 changes for motion and B0 correction, and coil sensitivity maps for SENSE-based parallel imaging reconstruction.

PREPROCESSING


USAGE NOTES

If you use the data, please consider citing the paper mentioned above.

CONTACT

If you have any questions about the data, please reach out to Shuxian Qu at qu000109@umn.edu
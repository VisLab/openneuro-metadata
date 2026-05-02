# Tracking ongoing cognition in individuals using brief, whole-brain functional connectivity patterns

## Original Paper

This data was originally published in the manuscript: "Tracking ongoing cognition in individuals using brief, whole-brain functional connectivity patterns" (2015). Gonzalez-Castillo, J., Hoy, C.W., Handwerker, D.A., Robinson, M.E., Buchanan, L.C., Saad, Z.S., Bandettini, P.A. PNAS 112(28) 8762-8767. [https://doi.org/10.1073/pnas.1501242112](https://doi.org/10.1073/pnas.1501242112).

## Dataset

This dataset comprises of 18 healthy volunteers performing one run of a continuous multi-task paradigm. Note that the original paper included data from 20 participants; 2 participants did not provide consent to share data, so only the 18 participants who did consent are included here. Data were originally collected from 2012-2013.

### Task Paradigm

In this paradigm, participants performed pseudo-randomly interleaved blocks of the following tasks:

- Math: evaluate a short arithmetic problem.
- Memory: 2-back task with shapes.
- Video: watch a video of a fish tank and press a button when an 'x' appears on a clown fish
- Rest: passively stare at a fixation cross

Each task block lasted 3 minutes (180 seconds), preceded by 12 seconds of instructions. The order of task blocks was randomized so that each task was always preceded and followed by a different task. This pseudo-random order of the task blocks was consistent across participants. 

### Scanning Parameters

Data were collected on a 7T Siemens scanner with a 32-channel head coil at the NIH. Functional runs were collected with a gre-EPI sequence (TR: 1.5s, TE: 25ms, FA: 50°; 36 interleaved slices, voxel size 2mm<sup>3</sup>, FOV 192mm, GRAPPA 2).

For one subject (sub-006), functional data were collected with a slightly different sequence (TR: 1.5s, TE: 25ms, FA: 70°, 35 oblique interleaved slices, slice thickness 2mm with 0.3mm gap and in-plane resolution of 1.4mm<sup>2</sup>, FOV 200mm, GRAPPA 4).

Additionally, each subject underwent T1-weighted magnetization-prepared rapid gradient-echo and proton density (PD) sequences were acquired for presentation and alignment purposes (axial prescription, 192 number of slices per slab, 1mm slice thickness; square FOV, 256 mm; image matrix, 256 × 256). All anatomical data shared here have been de-faced.

## Note

1. The "de-faced" anatomical data are all extracted (masked) brains.
1. The instructions for the first resting-state block were on the screen while the scanner was being prepared. Once the first trigger came from the MRI, the experiment clock was reset and the resting-state task started. So, resting-state instruction time varied across participants but the scan didn’t start until the rest block actually began.
1. The math mental arithmetic task stimuli all take the form "(X +/- Y) +/- Z = | A,B", where X, Y, and Z are whole numbers adding or subtracting from one another and there are two solutions (A or B) to choose between. The task-ctask_events.json file has MANY entries in the `stimulus` field's `Levels` to satisfy the BIDS validator.

## Contact

Javier Gonzalez-Castillo: javier.gonzalez-castillo@nih.gov

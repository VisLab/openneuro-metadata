# Dataset overview

This OpenNeuro release contains two fMRI datasets acquired on a 3 T Siemens Prisma scanner as part of a study characterising the auditory hemodynamic response function (HRF) using fast fMRI.

The two datasets differ in acquisition parameters but employ the same experimental paradigm, enabling assessment of reproducibility across sessions and acquisition protocols.

---

## MRI acquisition

Both datasets were acquired with a repetition time (TR) of 1 s and whole-brain coverage (48 slices), but differed in several parameters:

- Bandwidth: 2620 Hz (Original dataset) vs. 1985 Hz (Replication dataset)
- Voxel resolution: 2 mm vs. 2.5 mm isotropic
- Echo time (TE): 35.2 ms vs. 28 ms

---

## Experimental task

Participants passively listened to brief (500 ms) environmental sounds presented with long inter-stimulus intervals (>18.5 s), designed to allow characterisation of the full auditory HRF. Each fMRI session consisted of 6 runs of this passive listening paradigm.

---

## Datasets

### Original dataset
- Participants completed 2 fMRI sessions.
- Each session included 6 functional runs.
- Participants additionally completed one multi-parameter mapping (MPM) session.

### Replication dataset
- Participants completed 4 fMRI sessions.
- Each session included 6 functional runs using the same auditory stimuli.

Participants 1–4 in the Original dataset are the same individuals as Participants 1–4 in the Replication dataset.

---

## Data quality and notes

- Participants were scanned using a head fixation device to minimise motion. Each participant has one MPM available.
- `sub-rep05` is missing a fieldmap for `ses-01`.

---

## Intended use

The dataset is intended for methodological work on HRF estimation, fast fMRI, and auditory cortex, as well as for reuse in studies of auditory perception and hemodynamic modelling.
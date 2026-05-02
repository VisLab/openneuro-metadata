# Overview

This is the "Tilt Illusion" dataset.

In brief, it contains EEG data for 36 subjects responding to the percieved orientation 
of a central target grating, that is titrated to appear vertical on average, and is 
surrounded by an anular grating of +-30 degrees. We then looked at the prestimulus 
EEG correlates of an increased or decreased tilt illusion.

# Citing this dataset

Please cite as follows:

> Williams, J.G., Harrison, W.J., Beale, H.A., Mattingley, J.B., & Harris, A.M. (2024). Effects of alpha oscillation power and phase on discrimination performance in a visual tilt illusion. Current Biology.

For more information, see the `dataset_description.json` file.

# License

The `tilt illusion` dataset is made available under the CC BY 4.0 license.

Copyright (c) 2024, Jessica Williams, William Harrison, Henry Beale, Jason Mattingley, & Anthony Harris

A human readable information can be found at:

https://creativecommons.org/licenses/by/4.0/deed.en

# Format

The dataset is formatted according to the Brain Imaging Data Structure (BIDS).
See the `dataset_description.json` file for the specific version used.

Generally, you can find metadata in the `.tsv` files and documentation thereof in the accompanying `.json` files.

An important BIDS definition to consider is the "Inheritance Principle", which
is described in the BIDS specification under the following link:

https://bids-specification.readthedocs.io/en/latest/common-principles.html#the-inheritance-principle

In brief, the Inheritance Pinciple states that any metadata file (such as `.json`, `.tsv`)
may be defined at any directory level, but no more than one applicable file may be defined at a given level [...],
and the values from the top level are inherited by all lower levels --
unless they are overridden by a file at the lower level.

# Details about the experiment

For a detailed description of the task, see Williams et al. (2024)
What follows is a brief summary.

Participants were seated in front of a computer screen placed on a desk.
On each trial they were presented with a central target grating, surrounded by 
an annular grating of +-30 degrees. This induced a 'tilt illusion' whereby the 
percieved angle of the central grating was biased away from the angle of the 
surround. We first titrated the angle of the central grating to each participant's
percieved vertical angle, separately for each surround. Percieved vertical was 
defined as the angle at which the participant reported the grating as tilted 
leftward and rightward equally often. Participants responded with their right 
hand by pressing the left and right arrow keys on a standard USB keyboard. Stimuli
were presented very briefly (8.3ms) at 60% contrast, and were clearly visible.
Between trials, a mask made from the combination of several gratings was presented
to prevent the buildup of tilt aftereffects across trials.

Throughout the experiment, EEG data was recorded using a Biosemi Active 2 system
with 64 scalp electrods and 6 EOG electrodes (left and right HEOG, VEOG on left
eye, and left and right mastoids - in positions EXG 3-8). 

For more information, you can also consult the events.tsv and events.json files.

The original data was recorded in `.bdf` format using Actiview. It is stored in 
the `/sourcedata` directory. To comply with the BIDS format, the .bdf format was 
converted to EEGLab format, constituting a '.set' file and a 'fdt' file for each 
dataset. 

Participant 1's data was corrupted by large artefacts that could not be corrected.
Participants 8, 16, and 28 had no EEG data recorded, as their pre-task titration
failed to converge. As such, the data for these 4 participants are not included 
in this dataset.
Whole-Head Cocktail Party fNIRS

Whole-head functional near-infrared spectroscopy (fNIRS) recordings from
38 subjects performing covert and overt spatial-attention tasks in a
cocktail-party paradigm, with simultaneous eye-tracking.

fNIRS: 56 sources, 144 detectors, 1134 measurement channels at ~8.99 Hz.

Tasks
-----
overt:            Spatial attention with overt eye movements: subjects move
                  their eyes to attend to audiovisual stimuli (videos) on the
                  cued side.

covert:           Covert auditory attention: audio-only stimuli; subjects
                  fixate the central plus sign and attend to left or right
                  without moving their eyes.

visualorient:     Eye-movement-only baseline. Subjects make ~5 s eye orienting
                  and fixation movements with no audiovisual stimuli and no
                  fixation cross. Matches the overt task structure.

resting:          Resting-state recording: 5 minutes of central-fixation on a
                  plus sign with no task.

longvisualorient: Orienting + visual attention recording with events.tsv
                  aligned to the audiovisual orienting cue. Subjects orient
                  their eyes to the cue; ~15-17 s later a video clip appears
                  on the attended side. Same SNIRF recording as videoattend;
                  only the events.tsv differs.

videoattend:      Same SNIRF recording as longvisualorient, with events.tsv
                  aligned to the onset of the video clip (~15-17 s after the
                  orienting cue) for video-locked GLM analysis.

Privacy
-------
This dataset contains only fNIRS optical measurements and eye-tracking time
series; no anatomical scans (MRI, CT, photographs, or otherwise) are
included. Facial defacing is therefore not applicable to this dataset.
Data were acquired and shared under approved IRB consent.

Companion analysis code: https://github.com/duwadisudan/wholehead-cocktail-party-fnirs

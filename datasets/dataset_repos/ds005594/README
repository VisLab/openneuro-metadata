Generated from raw data by MNE-BIDS (Appelhoff et al., 2019) and custom code to join to behavioural data, stimulus information, and metadata.

## Notes on the Data

For full details on this dataset, see our preprint: Taylor et al. (2024) https://doi.org/10.1101/2024.11.11.622929

General notes:

* An issue during recording meant that sub-05 completed the first block without data being saved. The experiment was restarted from the beginning for this participant. This participant was not included in our analyses, but the data are included in this dataset. They are also identified with the `recording_restarted` field in `participants.tsv`.

* A separate issue during recording meant that EEG data for some trials were lost for `sub-01`, though enough trials were recorded in total to meet our criteria for inclusion in the analysis. The raw data comprised two separate recordings. In this dataset, the two recordings are concatenated end-to-end into one file. The point at which the files are joined is marked with a boundary event. This participant is identified with the `recording_interrupted` field in `participants.tsv`.

* During the course of the experiment, we identified an issue with the wiring in one splitter box, which meant that voltages from channels FT7 and FC3 were swapped in the raw recorded data. We elected to keep the wiring as it was for the duration of the experiment, and then swapped the data from the two channels in the code that generated this BIDS dataset. This means that this issue has been corrected in this BIDS version of the data.

* "BAD" periods (MNE term) for key presses and break periods are included in the events files.

* Recording dates/times have been anonymised by shifting all recordings backwards in time by a constant number of days (same constant for all participants). This obscures information that may be used to identify participants, but preserves time-of-day information, and the relative times elapsed between different recordings.

## References

Appelhoff, S., Sanderson, M., Brooks, T., Vliet, M., Quentin, R., Holdgraf, C., Chaumon, M., Mikulan, E., Tavabi, K., Höchenberger, R., Welke, D., Brunner, C., Rockhill, A., Larson, E., Gramfort, A. and Jas, M. (2019). MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis. Journal of Open Source Software 4: (1896). https://doi.org/10.21105/joss.01896

Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., Flandin, G., Phillips, C., Delorme, A., Oostenveld, R. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Scientific Data, 6, 103. https://doi.org/10.1038/s41597-019-0104-8


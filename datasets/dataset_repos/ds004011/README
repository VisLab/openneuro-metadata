The main folder contains the raw MEG data for all participants in standard bids format. See references.
 

The ‘sourcedata’ folder contains the behavioural data collected during the MEG session as well as the eyetracking data. The data in this folder follows the following trial structure:
 

- sourcedata
	- beh
		- sub-[participant number]
			- sub-[participant number]_task-occlusion_run-[run number]_events.csv: contains all the events for each trial in the MEG session, detailing what was shown on the screen.
			- sub-[participant number]_task-occlusion_run-[run number]_occframes.csv: contains all the stimulus positions for each occlusion trial in the MEG session.
			- sub-[participant number]_task-occlusion_run-[run number]_disframes.csv: contains all the stimulus positions for each disappearance trial in the MEG session.
	- eyetracking
		- sub-[participant number]_Occ.edf: edf file containing the eye positions during the MEG session.

The ‘derivatives’ folder contains the pre-processed MEG data for each participant. The data in this folder follows the following trial structure:


- derivatives
	- preprocessed
		- cosmo_p[participant number].mat: cosmomvpa formatted file with the pre-processed data, epoched for each trial, containing the following variables:
			- ds_diss: cosmo data struct containing the disappearance trials epoched relative to stimulus onset (MEG channels)
			- ds_occ: cosmo data struct containing the disappearance trials epoched relative to stimulus onset (MEG channels)
			- ds_loc: cosmo data struct containing the unpredictable position stream trials epoched relative to stimulus onset (MEG channels)
			- ds_eyes_diss: cosmo data struct containing the disappearance trials epoched relative to stimulus onset (eye-x, eye-y, pupil size)
			- ds_eyes_occ: cosmo data struct containing the disappearance trials epoched relative to stimulus onset (eye-x, eye-y, pupil size)
			- ds_eyes_loc: cosmo data struct containing the unpredictable position stream trials epoched relative to stimulus onset (eye-x, eye-y, pupil size)
		-  cosmo_p[participant number]_position_epochs.mat: cosmomvpa formatted file with the pre-processed data, epoched relative to each position change, containing the following variables:
			- ds_tiny: cell with two entries. First entry contains the disappearance trials epoched relative to position change. Second entry contains the occlusion trials epoched relative to position change. (MEG channels)
			- ds_tiny_eyes: cell with two entries. First entry contains the disappearance trials epoched relative to position change. Second entry contains the occlusion trials epoched relative to position change. (eye-x, eye-y, pupil size)


------------

References:

Appelhoff, S., Sanderson, M., Brooks, T., Vliet, M., Quentin, R., Holdgraf, C., Chaumon, M., Mikulan, E., Tavabi, K., Höchenberger, R., Welke, D., Brunner, C., Rockhill, A., Larson, E., Gramfort, A. and Jas, M. (2019). MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis. Journal of Open Source Software 4: (1896). https://doi.org/10.21105/joss.01896

Niso, G., Gorgolewski, K. J., Bock, E., Brooks, T. L., Flandin, G., Gramfort, A., Henson, R. N., Jas, M., Litvak, V., Moreau, J., Oostenveld, R., Schoffelen, J., Tadel, F., Wexler, J., Baillet, S. (2018). MEG-BIDS, the brain imaging data structure extended to magnetoencephalography. Scientific Data, 5, 180110. https://doi.org/10.1038/sdata.2018.110

This dataset contains the fMRI and EEG data for E.A. McDevitt, G. Kim, N.B. Turk-Browne, K.A. Norman (2026). The role of rapid eye movement sleep in neural differentiation of memories in the hippocampus. Journal of Cognitive Neuroscience, 10.1162/jocn.a.82

Please refer to the paper for detailed methods. 

The dataset includes 69 participants with three fMRI scans and one EEG session per participant. Depending on the participant's condition, the EEG session either contains sleep data from a nap or data recorded during a quiet wake session.  

Please contact Elizabeth McDevitt (emcdevitt@princeton.edu) if you have any questions. 

Notes about the dataset: 

The following subjects/sessions do not include a T1w anatomical scan: sub-160 ses-00; sub-170 ses-00; sub-178 ses-01

- sub-107/ses-02/func: There are three runs of the decision task included instead of two. During decision_run-01, the participant did not respond to 'B' trials (coded in column trial_type). Therefore, there are many trials with no response_accuracy or response_times recorded in task-decision_run-01_events.tsv. Immediately following this run, the same task was re-run as decision_run-03 to collect behavioral responses; therefore the data associated with task-decision_run-03 can be considered a "repeat" of task-decision_run-01. Decision_run-02 was run as expected during the second cycle of the reward prediction task.  

- sub-108_ses-02_task-reward_run-01_events.tsv: Many trials have no response_accuracy or response_time recorded. The participant misunderstood instructions and did not respond on trials where they predicted a "neutral" outcome. 

- sub-182_ses-01_task-study_run-01_events.tsv: There was an issue with Matlab not recording "2" button presses during this run of the task. The experimenter recoded all "no response" trials as "2" and used this to code response_accuracy. However, there were no response_times recorded for these trials. 
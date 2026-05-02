Here, we present a densely sampled fMRI dataset wherein 31 participants provided subjective value ratings for over 500 food images across three separate days.

## Experimental Task

Participants rated subjective values for 568 food images across three separate days. On each day, they underwent four fMRI runs, each consisting of 47 or 48 trials, and were asked to refrain from eating or drinking anything besides the water for 3 hours before the experiment. Note that, due to a technical issue, one participant (ID: sub-016) completed only 2 runs on day 3.

On each trial, participants rated one food image in terms of “How much do you want to eat this food?” using a 4-point Likert scale (a rating of 4 represents high value). They were first presented with a food image (Valuation phase: 4 seconds), and made a rating by pressing the corresponding key on a keypad within 2.5 seconds (Rating phase), followed by the feedback (Feedback phase: 0.5 seconds). Durations of the inter-trial-intervals (ITI) were randomly sampled from the unform distribution between 2 and 8 seconds. Here, participants were instructed to evaluate a food item during the Valuation phase, as the Rating phase was too short for decision-making. Furthermore, to dissociate the rating value from spatial attentions and motor-related responses, the mapping between rating values (1, 2, 3, and 4) and the spatial key positions was randomized across trials.

## Stimuli
We used 568 out of the 896 food images from the Food-pics dataset (<https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00307/full>), for which nutritional information was available. These images were presented to participants in a random order.

## Data Records

All data are organized according to the Brain Imaging Data Structure (BIDS). Each participant is assigned a unique identifier (e.g., sub-001), and demographic information is provided in the participants.tsv file. The dataset consists of three sessions per participant, corresponding to the three experimental days (labeled ses-01, ses-02, and ses-03). Each session directory contains three subdirectories: *anat*, *fmap*, and *func*, housing anatomical, field-map, and functional images, respectively. Typically, the func directory contains four experimental runs; however, due to a technical issue, one participant (sub-016) completed only two runs in the third session (ses-03).

Detailed behavioral data are provided in event files (e.g., sub-001_ses-01_task-food_run-01_events.tsv) located within the *func* directory. These event files contain trial-wise information, including: stimulus properties (the food image presented, along with its visual and nutritional features); participant responses (the subjective rating submitted by the participant); and timing (onsets and durations for the Valuation, Rating, and Feedback phases, as well as the timing of key-press responses).
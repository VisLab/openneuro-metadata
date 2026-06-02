# FOODEEG: An open dataset of human electroencephalographic and behavioural responses to food images

## Overview

The FOODEEG dataset comprises of human electroencephalographic (EEG) and behavioural responses to food images for 117 participants. This repository contains raw and processed EEG recordings collected during a food categorisation task and behavioural responses collected during a food go/no-go task and a food paired choice task.

More information, including custom code, food image stimuli, normative ratings, and questionnaire data, can be found via the Open Science Framework (doi.org/10.17605/OSF.IO/Y9PMF/).

## Experiment details

Neural and behavioural data were collected over two testing sessions (N = 117).

In Session 1, participants completed a food categorisation task while EEG was recorded. Participants viewed food images for 2 s and categorised the food (yes/no) as quickly as possible on whether it was healthy, tasty, or whether they were willing to eat it. Each food image was presented three times, once across healthiness, tastiness, and willingness to eat trials. After the food categorisation task, participants provided continuous ratings (0-100) for each food image on healthiness, tastiness, and willingness to eat.

In Session 2, participants completed two behavioural tasks. The food go/no-go task involved participants making responses to Go food images (e.g., healthy foods) and withholding responses to No-go food images (e.g., not-healthy foods). In the food paired choice task, participants viewed pairs of food images and selected the food that they preferred to eat more out of the pair. Participants' dietary style, eating motivations, general motivational tendencies and hedonism were assessed using questionnaires.

Separately, normative ratings on the food image stimuli were collected from online samples (total N = 624). We collected continuous ratings (0-100) on 22 food attributes that encompassed nutritive, hedonic, familiarity, taste, and emotional properties of foods.

## Data descriptor

For more details about the dataset please see the corresponding paper:

Chae, V. J., Grootswagers, T., Bode, S., & Feuerriegel, D. (2025). FOODEEG: An open dataset of human electroencephalographic and behavioural responses to food images (p. 2025.11.07.687287). bioRxiv. https://doi.org/10.1101/2025.11.07.687287

## Main files

This dataset was formatted according to the Brain Imaging Data Structure (BIDS). See the `dataset_description.json` file for the specific version used.

**`sub-*/eeg`**: contains the raw continuous EEG recording (`.bdf`) during the food categorisation task and the corresponding metadata file (`events.tsv`).

**`sub-*/beh`**: contains the behavioural responses during the food go/no-go task (`task-gonogo_beh.tsv`) and the food paired choice task (`task-pairedchoice_beh.tsv`). A copy of each file in `.csv` format is also contained here.

**`derivatives`**: contains the cleaned continuous EEG data (`.set`) for 110 participants used in the technical validation analyses in the data descriptor. Seven participants were excluded from the analyses. The participant IDs and the reason for exclusion are outlined in the metadata file for the participants (`participants.tsv`).

## Additional data

At the end of Session 1, participants rated each food image on healthiness, tastiness, and willingness to eat on a continuous scale (0-100). At the end of Session 2, participants completed questionnaires assessing dietary styles, food motivations, general motivational tendencies, and hedonism.

Separately from online samples (total N = 624), we collected continuous ratings (0-100) for the food images on 22 food attributes, including nutritive properties (healthiness, calorie content, edibility, and level of transformation), hedonic properties (tastiness, willingness to eat, negative and positive valence, and arousal), taste properties (sweetness, saltiness, sourness, bitterness, and savouriness), familiarity (previous exposure, recognisability, and typicality), and elicited emotions (happiness, surprise, disgust, craving, and guilt).

Questionnaire responses and continuous rating data can be found via the Open Science Framework (doi.org/10.17605/OSF.IO/Y9PMF/).

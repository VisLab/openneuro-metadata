### Categorized Free Recall with Open-Loop Stimulation at Encoding

#### Description
This dataset contains behavioral events and intracranial electrophysiological recordings from a categorized free recall task with open-loop stimulation at encoding.  The experiment consists of participants studying a list of words, presented visually one at a time, completing simple arithmetic problems that function as a distractor, and then freely recalling the words from the just-presented list in any order.  The data was collected at clinical sites across the country as part of a collaboration with the Computational Memory Lab at the University of Pennsylvania.

The word lists in this paradigm follow a specific semantic construction.  Each word comes from one of 25 semantic categories, and each list of 12 items contains 6 pairs of same-category words from 3 different categories.  This means that each list has 4 words from 3 semantic categories, and in each half of the list there will be 1 pair of words from each category.  For example, if a list contains words from categories A, B, and C, a possible list construction would be: 

**A1 - A2 - B1 - B2 - C1 - C2 - A3 - A4 - C3 - C4 - B3 - B4**

This study contains open-loop electrical stimulation of the brain during encoding.  There is no stimulation during the distractor or retrieval phases.  Stimulation is delivered to a single electrode at a time, with locations chosen in the hippocampus and entorhinal cortex.  Stimulation parameters are included in the behavioral events tsv files, denoting the anode/cathode labels, amplitude, pulse frequency, pulse width, and pulse count.  

20 of the 25 lists in a session are randomly assigned as stimulation lists.  On these lists, stimulation occurs on alternating two-word blocks, meaning 6 of the 12 words are presented with stimulation.  Stimulation starts 200 ms prior to the onset of the first word in the block and lasts for 4.6 seconds, ending 200-450 ms after the offset of the second word (depending on the inter-stimulus interval).  Half of the stimulation lists begin with a stimulation on pair and half begin with a stumulation off pair, but the order of these conditions is random.  A stimulation list that begins with a stimulation on pair would look as follows (with bold indicating stimulation):

**1 - 2** | 3 - 4 | **5 - 6** | 7 - 8 | **9 - 10** | 11 - 12

#### To Note
* The iEEG recordings are labeled either "monopolar" or "bipolar."  The monopolar recordings are referenced (typically a mastoid reference), but should always be re-referenced before analysis.  The bipolar recordings are referenced according to a paired scheme indicated by the accompanying bipolar channels tables.
* Each subject has a unique montage of electrode locations.  MNI and Talairach coordinates are provided when available.
* Recordings done with the Blackrock system are in units of 250 nV, while recordings done with the Medtronic system are estimated through testing to have units of 0.1 uV.  We have completed the scaling to provide values in V.

#### Contact
For questions or inquiries, please contact sas-kahana-sysadmin@sas.upenn.edu.
Dataset title: Bilingual speech production with functional localizers
This dataset was created to explore neural mechanisms of bilingual speech production.

It includes data from forty-two Polish-English bilinguals who completed a series of tasks:

1. Picture naming in L1 and L2 (overt production)
2. Verbal Fluency in L1 (overt production)
3. Stroop in L1 (overt production)
4. Language localizer in L1 (Alice version, see Malik Moraleda, Ayyash et al., 2020)
5. Multiple Demand localizer (based on visual working memory task, see Fedorenko et al., 2013)
6. Articulation task, used as a localizer of functional network supporting articulation

Each participant completed two sessions. Picture naming task was included in each session (4 runs per session) and the remaining tasks were distributed between the two sessions (2 runs per task). The first run of the picture naming task was completed in L1 or L2, with the two conditions counterbalanced between sessions. The remaining 3 runs were always completed in L1. The language of naming for the first run can be derived from the event files: trial_type L1L1 corresponds to naming in L1 and trial_type L2L1 corresponds to naming in L2.

Details of all tasks and the experimental design are described in https://direct.mit.edu/nol/article/5/2/315/118227.

The dataset includes anatomical (T1 and T2 weighted), functional, and fieldmap scans for each participant. Anatomical and fieldmap scans were acquired for each session separately. Note! PE-polar fieldmaps were acquired at the beginning (acq-start) and in the end (acq-end) of each session. In the cases when the scanning session needed to be interrupted, some of the tasks functional scans should be corrected using the acq-end scans (see IntendedFor specification in the .json files accompanying fieldmaps).

In case of any questions please contact Agata Wolna (agata.wolna@uj.edu.pl) or Zofia Wodniecka (zofia.wodniecka@uj.edu.pl).

# Manual review worksheet — Phase 2.5E (29 rows)

_Generated: 2026-05-11. Companion to `manual_review_2026-05-11.json`._

## Instructions

For each entry below, replace the **`decision:`** line with ONE of these formats:

- **`decision: doi 10.xxxx/yyyy`** — when you find a working DOI (the resolver will hit Crossref/OpenAlex for it)
- **`decision: bib Lastname | 2020 | Full paper title`** — when no DOI exists or Crossref doesn't index it (resolver computes `pub_id` locally from these three fields; no network needed)
- **`decision: rejected reason text`** — when the URL is broken / not a publication / etc.
- **Leave `(pending)`** to skip this row for the current iteration

When done (or after handling some chunk), **paste this whole file back into the chat** and I'll convert your decisions into the registry. You don't need to edit the JSON directly.

Each entry lists the three or four most useful checks (`doi.org` lookup, the original URL, Google Scholar search when a title is available). Click whichever helps you decide fastest.

---

## cit_000106 — Nature Neuroscience 2024 (clean-shape DOI, Crossref miss)

- existing doi: `10.1038/s41593-024-01564-3`
- doi.org check: https://doi.org/10.1038/s41593-024-01564-3
- diagnosis: DOI shape is normal Nature Neuroscience format. Either Crossref indexing lag, or `-3` suffix is a transcription typo (modern Nature uses letter suffixes like `-w`, `-x`).

**decision:** (pending)
I cannot resolve this as is.  Give me the cit_id and the dataset that it came from.
---

## cit_000187 — PNAS 2017 (OSF source private)

- existing doi: `10.1073/pnas.1711571115`
- original url: https://osf.io/er5u7 (returned 401, private)
- your earlier resolved_url: https://www.pnas.org/doi/10.1073/pnas.1711571115
- title (from notes): "The neural basis of the effect of computational complexity on search"
- doi.org check: https://doi.org/10.1073/pnas.1711571115
- Google Scholar: https://scholar.google.com/scholar?q=%22The+neural+basis+of+the+effect+of+computational+complexity+on+search%22

**decision:** (pending)
I cannot resolve this without going back to original links.  give me cit_id and datasets
---

## cit_000194 — F1000Research

- existing doi: `10.12688/f1000research.12142.2`
- original url: https://f1000research.com/articles/6-1262/v2
- doi.org check: https://doi.org/10.12688/f1000research.12142.2
- diagnosis: F1000 versioned DOI; should be valid. Verify at doi.org.

**decision:** (pending)
Gorgolewski KJ, Durnez J and Poldrack RA. Preprocessed Consortium for Neuropsychiatric Phenomics dataset [version 2; peer review: 2 approved]. F1000Research 2017, 6:1262 (https://doi.org/10.12688/f1000research.11964.2)
---

## cit_000265 — Scientific Reports 2018 (OSF source)

- existing doi: `10.1038/s41598-018-24312-0`
- original url: https://osf.io/dm47y
- OSF project title: "Do activations and representations differ for episodic versus semantic memory?"
- your earlier resolved_url: https://www.nature.com/articles/s41598-018-24312-0
- doi.org check: https://doi.org/10.1038/s41598-018-24312-0
- diagnosis: clean shape; verify it actually resolves.

**decision:** (pending)
https://www.nature.com/articles/s41562-025-02390-4
Tibon, R., Greve, A., Humphreys, G. et al. Neural activations and representations during episodic versus semantic memory retrieval. Nat Hum Behav 10, 803–821 (2026). https://doi.org/10.1038/s41562-025-02390-4
---

## cit_000381 — PNAS article URL (no DOI)

- url: https://www.pnas.org/content/117/11/6170
- diagnosis: PNAS 117(11) 6170 → likely 2020. Open the URL, find the DOI on the article page (usually shown prominently).

**decision:** (pending)
L.R. Mujica-Parodi,A. Amgalan,S.F. Sultan,B. Antal,X. Sun,S. Skiena,A. Lithen,N. Adra,E. Ratai,C. Weistuch,S.T. Govindarajan,H.H. Strey,K.A. Dill,S.M. Stufflebeam,R.L. Veech, & K. Clarke,  Diet modulates brain network stability, a biomarker for brain aging, in young adults, Proc. Natl. Acad. Sci. U.S.A. 117 (11) 6170-6177, https://doi.org/10.1073/pnas.1913042117 (2020).
---

## cit_000395 — F1000Research

- existing doi: `10.12688/f1000research.6911.1`
- original url: https://f1000research.com/articles/4-174/v1
- doi.org check: https://doi.org/10.12688/f1000research.6911.1

**decision:** (pending)
Hanke M, Dinga R, Häusler C et al. High-resolution 7-Tesla fMRI data on the perception of musical genres – an extension to the studyforrest dataset [version 1; peer review: 2 approved with reservations]. F1000Research 2015, 4:174 (https://doi.org/10.12688/f1000research.6679.1)
---

## cit_000451 — MIT JoCN article (no DOI)

- url: https://direct.mit.edu/jocn/article/29/1/95/28621/Fluctuations-of-Attentional-Networks-and-Default
- diagnosis: JoCN 29(1) 95 → 2017. Title from URL slug: "Fluctuations of Attentional Networks and Default..." Open the URL, copy the DOI shown on the article page.

**decision:** (pending)
Citation
Laurens Van Calster, Arnaud D'Argembeau, Eric Salmon, Frédéric Peters, Steve Majerus; Fluctuations of Attentional Networks and Default Mode Network during the Resting State Reflect Variations in Cognitive States: Evidence from a Novel Resting-state Experience Sampling Method. J Cogn Neurosci 2017; 29 (1): 95–113. doi: https://doi.org/10.1162/jocn_a_01025

---

## cit_000615 — PsycNet record (no DOI)

- url: https://psycnet.apa.org/record/2020-66677-001
- diagnosis: APA PsycNet record from 2020. Open the URL, find the DOI in the record (APA papers always have one).

**decision:** (pending)
Brandt, E., Wilson, J. K., Rieger, R. E., Gill, D., Mayer, A. R., & Cavanagh, J. F. (2021). Respiratory sinus arrhythmia correlates with depressive symptoms following mild traumatic brain injury. Journal of Psychophysiology, 35(3), 139–151. https://doi.org/10.1027/0269-8803/a000268
---

## cit_000702 — MIT JoCN article (no DOI)

- url: https://direct.mit.edu/jocn/article/33/9/1990/106990/The-Dual-Mechanisms-of-Cognitive-Control-Project
- diagnosis: JoCN 33(9) 1990 → 2021. Title from URL slug: "The Dual Mechanisms of Cognitive Control Project". Open the URL, copy DOI from the article page.

**decision:** (pending)
Todd S. Braver, Alexander Kizhner, Rongxiang Tang, Michael C. Freund, Joset A. Etzel; The Dual Mechanisms of Cognitive Control Project. J Cogn Neurosci 2021; 33 (9): 1990–2015. doi: https://doi.org/10.1162/jocn_a_01768
---

## cit_000746 — J. Psychiatry and Brain Sci (specialized publisher)

- existing doi: `10.20900/jpbs.20200024`
- doi.org check: https://doi.org/10.20900/jpbs.20200024
- diagnosis: Hapres publisher (mEDRA, not Crossref). DOI likely valid via doi.org. If yes, use `bib` form to compute `pub_id` locally from author/year/title.

**decision:** (pending)
The Role of Social Reward and Corticostriatal Connectivity in Substance Use
Daniel Sazhin 1, Angelique M. Frazier 1, Caleb R. Haynes 1, Camille R. Johnston 1, Iris Ka-Yi Chat 1, Jeffrey B. Dennison 1, Corinne P. Bart 1, Michael E. McCloskey 1, Jason M. Chein 1, Dominic S. Fareri 2, Lauren B. Alloy 1, Johanna M. Jarcho 1, David V. Smith 1,* 
J Psychiatry Brain Sci. 2020;5:e200024. https://doi.org/10.20900/jpbs.20200024
---

## cit_000902 — Nature Communications (shortDOI in url)

- existing doi: `10.1038/s41467-019-10641-z`
- url was a shortDOI: https://doi.org/10/gjf3tx
- doi.org check: https://doi.org/10.1038/s41467-019-10641-z
- diagnosis: clean Nature Communications DOI; verify.

**decision:** (pending)
Pavlov, Y. G., & Kotchoubey, B. (2021). Temporally distinct oscillatory codes of retention and manipulation of verbal working memory. European Journal of Neuroscience, 54(7), 6497–6511. https://doi.org/10.1111/ejn.15457
---

## cit_001189 — Truncated DOI from a paper reference (Elsevier)

- existing doi: `10.1016/s0911-6044(03`
- diagnosis: **TRUNCATED.** Extraction stopped mid-DOI; full form is `10.1016/S0911-6044(03)00012-X` or similar. Journal is "Journal of Neurolinguistics" (S0911-6044). No source URL, no title — likely irreducible without manual research. Consider `rejected`.

**decision:** (pending)
Cannot be resolved as is:  Need original cit_id and information to see what dataset it was associated with.
---

## cit_001212 — Network Neuroscience (malformed; fixable)

- existing doi: `10.1162/netna00056`
- diagnosis: **MALFORMED.** MIT Press journals use `netn_a_NNNNN` (underscores). Try `10.1162/netn_a_00056`.
- doi.org check (fixed): https://doi.org/10.1162/netn_a_00056

**decision:** (pending)
Douglas H. Schultz, Takuya Ito, Levi I. Solomyak, Richard H. Chen, Ravi D. Mill, Alan Anticevic, Michael W. Cole; Global connectivity of the fronto-parietal cognitive control network is related to depression symptoms in the general population. Network Neuroscience 2018; 3 (1): 107–123. doi: https://doi.org/10.1162/netn_a_00056
---

## cit_001224 — OUP SCAN article (no DOI)

- url: https://academic.oup.com/scan/article/15/4/383/5831854
- diagnosis: Social Cognitive and Affective Neuroscience 15(4) 383 → 2020. Open the URL; OUP shows DOI on article page.

**decision:** (pending)
Kelsey R McDonald, John M Pearson, Scott A Huettel, Dorsolateral and dorsomedial prefrontal cortex track distinct properties of dynamic social behavior, Social Cognitive and Affective Neuroscience, Volume 15, Issue 4, April 2020, Pages 383–393, https://doi.org/10.1093/scan/nsaa053
---

## cit_001251 — arXiv → PNAS 2020 (verified by you earlier)

- existing doi: `10.1073/pnas.2001151117`
- original url: https://arxiv.org/abs/2001.09857
- your earlier resolved_url: https://www.pnas.org/doi/10.1073/pnas.2001151117
- doi.org check: https://doi.org/10.1073/pnas.2001151117

**decision:** (pending)
Diao Y, Yin T, Gruetter R, Jelescu IO. PIRACY: An Optimized Pipeline for Functional Connectivity Analysis in the Rat Brain. Front Neurosci. 2021 Mar 26;15:602170. doi: 10.3389/fnins.2021.602170. PMID: 33841071; PMCID: PMC8032956.
---

## cit_001293 — Translational Psychiatry (malformed; fixable)

- existing doi: `10.1038/tp201792`
- diagnosis: **MALFORMED.** Missing dots, same family as the Sci Data correction. Try `10.1038/tp.2017.92`.
- doi.org check (fixed): https://doi.org/10.1038/tp.2017.92

**decision:** (pending)
Garza-Villarreal, E., Chakravarty, M., Hansen, B. et al. The effect of crack cocaine addiction and age on the microstructure and morphology of the human striatum and thalamus using shape analysis and fast diffusion kurtosis imaging. Transl Psychiatry 7, e1122 (2017). https://doi.org/10.1038/tp.2017.92
---

## cit_001389 — J. Neurosci PDF URL

- url: https://www.jneurosci.org/content/jneuro/39/49/9716.full.pdf
- diagnosis: J Neurosci 39(49) 9716 → 2019. Trim `.full.pdf` and open https://www.jneurosci.org/content/39/49/9716 — DOI is on the article page.

**decision:** (pending)
Functional Connectome of the Fetal Brain
Elise Turk, Marion I. van den Heuvel, Manon J. Benders, Roel de Heus, Arie Franx, Janessa H. Manning, Jasmine L. Hect, Edgar Hernandez-Andrade, Sonia S. Hassan, Roberto Romero, René S. Kahn, Moriah E. Thomason and Martijn P. van den Heuvel
Journal of Neuroscience 4 December 2019, 39 (49) 9716-9724; https://doi.org/10.1523/JNEUROSCI.2891-18.2019
---

## cit_001420 — PNAS article URL

- url: https://www.pnas.org/content/113/17/4853.short
- diagnosis: PNAS 113(17) 4853 → 2016. Open without `.short` suffix; DOI is on the article page.

**decision:** (pending)
https://www.pnas.org/doi/10.1073/pnas.1518377113
R.L. Carhart-Harris,S. Muthukumaraswamy,L. Roseman,M. Kaelen,W. Droog,K. Murphy,E. Tagliazucchi,E.E. Schenberg,T. Nest,C. Orban,R. Leech,L.T. Williams,T.M. Williams,M. Bolstridge,B. Sessa,J. McGonigle,M.I. Sereno,D. Nichols,P.J. Hellyer,[...] & D.J. Nutt,  Neural correlates of the LSD experience revealed by multimodal neuroimaging, Proc. Natl. Acad. Sci. U.S.A. 113 (17) 4853-4858, https://doi.org/10.1073/pnas.1518377113 (2016).

---

## cit_001429 — Truncated Elsevier DOI

- existing doi: `10.1016/s1053-8119(03`
- diagnosis: **TRUNCATED**, same pattern as cit_001189. Full form looks like `10.1016/S1053-8119(03)...`. Journal is NeuroImage (S1053-8119). Likely irreducible without manual research. Consider `rejected`.

**decision:** (pending)
Cannot decide as is:  Give me original cit_id and dataset associated with it.
---

## cit_001431 — arXiv → IEEE TPAMI 2019 (verified by you earlier)

- existing doi: `10.1109/TPAMI.2019.2937788`
- original url: https://arxiv.org/abs/1810.03856
- your earlier resolved_url: https://ieeexplore.ieee.org/document/8816668
- doi.org check: https://doi.org/10.1109/TPAMI.2019.2937788

**decision:** (pending)
VanRullen, R., Reddy, L. Reconstructing faces from fMRI patterns using deep generative neural networks. Commun Biol 2, 193 (2019). https://doi.org/10.1038/s42003-019-0438-y
---

## cit_001460 — OUP SCAN article (no DOI)

- url: https://academic.oup.com/scan/article/12/7/1025/3798709
- diagnosis: SCAN 12(7) 1025 → 2017. Open the URL; copy DOI from article page.

**decision:** (pending)
Suzanne Oosterwijk, Lukas Snoek, Mark Rotteveel, Lisa Feldman Barrett, H. Steven Scholte, Shared states: using MVPA to test neural overlap between self-focused emotion imagery and other-focused emotion understanding, Social Cognitive and Affective Neuroscience, Volume 12, Issue 7, July 2017, Pages 1025–1035, https://doi.org/10.1093/scan/nsx037
---

## cit_001490 — Cerebral Cortex (URL slug appended to DOI)

- existing doi: `10.1093/cercor/bhx202/4080827/how-we-transmit-memories-to-other-brains`
- diagnosis: **MALFORMED.** URL slug was appended. Actual DOI is `10.1093/cercor/bhx202`.
- doi.org check (fixed): https://doi.org/10.1093/cercor/bhx202

**decision:** (pending)
A. Zadbood, J. Chen, Y.C. Leong, K.A. Norman, U. Hasson, How We Transmit Memories to Other Brains: Constructing Shared Neural Representations Via Communication, Cerebral Cortex, Volume 27, Issue 10, October 2017, Pages 4988–5000, https://doi.org/10.1093/cercor/bhx202

---

## cit_001503 — Zenodo badge URL (probably not a publication)

- existing doi: `10.5281/zenodo.3524401.svg`
- diagnosis: **MALFORMED** — `.svg` is from a badge image URL. Actual Zenodo DOI is `10.5281/zenodo.3524401`. But Zenodo deposits are usually datasets/software, not publications — likely `rejected` like the other Zenodo entries from earlier in this session.
- doi.org check (fixed): https://doi.org/10.5281/zenodo.3524401

**decision:** (pending)
Cannot decide as is.  Give me the original cit_id and dataset.
---

## cit_001517 — PNAS article URL

- url: https://www.pnas.org/content/114/35/9475.short
- diagnosis: PNAS 114(35) 9475 → 2017. Open without `.short`; copy DOI from article page.

**decision:** (pending)
Y. Yeshurun,M. Nguyen, & U. Hasson,  Amplification of local changes along the timescale processing hierarchy, Proc. Natl. Acad. Sci. U.S.A. 114 (35) 9475-9480, https://doi.org/10.1073/pnas.1701652114 (2017).
---

## cit_001546 — Cerebral Cortex article URL

- url: https://cercor.oxfordjournals.org/content/18/11/2505.short
- diagnosis: Cereb Cortex 18(11) 2505 → 2008. Note: `cercor.oxfordjournals.org` is the legacy hostname; the article is now at `academic.oup.com/cercor/...`. Try https://academic.oup.com/cercor/article/18/11/2505 — copy DOI.

**decision:** (pending)
Cannot resolve -- give me the original cit_id and dataset id.
---

## cit_001580 — J. Neurosci article URL

- url: https://www.jneurosci.org/content/36/7/2212.short
- diagnosis: J Neurosci 36(7) 2212 → 2016. Open without `.short`; copy DOI.

**decision:** (pending)
Distinct β Band Oscillatory Networks Subserving Motor and Cognitive Control during Gait Adaptation
Johanna Wagner, Scott Makeig, Mateusz Gola, Christa Neuper and Gernot Müller-Putz
Journal of Neuroscience 17 February 2016, 36 (7) 2212-2226; https://doi.org/10.1523/JNEUROSCI.3543-15.2016
---

## cit_001588 — bioRxiv DOI (missing date prefix)

- existing doi: `10.1101/48905`
- diagnosis: **MALFORMED** bioRxiv DOI. Modern format is `10.1101/YYYY.MM.DD.NNNNN`; this is missing the date prefix. Likely an early-2014 bioRxiv preprint where IDs were just numeric. Try doi.org with the existing DOI — if it resolves, use `bib`; if not, `rejected`.
- doi.org check: https://doi.org/10.1101/048905

**decision:** (pending)
Cannot resolve as is:  Give me the cit_id and dataset_id
---

## cit_001629 — eLife DOI (looks short)

- existing doi: `10.7554/eLife.1607`
- diagnosis: eLife DOIs are typically `10.7554/eLife.NNNNN` (5 digits). `1607` is 4 digits — could be a valid early-era eLife DOI or truncated. Try doi.org.
- doi.org check: https://doi.org/10.7554/eLife.01607
- diagnosis (fixed): also try with leading zero `01607`

**decision:** (pending)
This is not likely the right article.  Give me the original cit_id and dataset ID.
---

## cit_001657 — Wellcome Open Research (verified by you earlier)

- existing doi: `10.12688/wellcomeopenres.10444.1`
- original url: https://wellcomeopenresearch.org/articles/1-33/v1
- doi.org check: https://doi.org/10.12688/wellcomeopenres.10444.1

**decision:** (pending)
Romaniuk L, Pope M, Nicol K et al. Neural correlates of fears of abandonment and rejection in borderline personality disorder [version 1; peer review: 2 not approved]. Wellcome Open Res 2016, 1:33 (https://doi.org/10.12688/wellcomeopenres.10331.1)
---

## Summary by diagnostic category

| Category | cit_ids | Suggested action |
|---|---|---|
| Clean shape, just needs doi.org verify | cit_000106, cit_000187, cit_000194, cit_000265, cit_000395, cit_000746, cit_000902, cit_001251, cit_001431, cit_001657 | Click doi.org link; if resolves, fill `bib` with author/year/title from page |
| Malformed-but-fixable | cit_001212 (netn_a_), cit_001293 (Transl Psych dots), cit_001490 (slug), cit_001503 (.svg), cit_001629 (eLife leading zero) | Use the "fixed" DOI in `decision: doi …` |
| URL only — open page, copy DOI | cit_000381, cit_000451, cit_000615, cit_000702, cit_001224, cit_001389, cit_001420, cit_001460, cit_001517, cit_001546, cit_001580 | Open URL, find DOI on the page, `decision: doi …` |
| Truncated / probably irreducible | cit_001189, cit_001429, cit_001588 | Likely `rejected` unless you happen to know the source paper |
| Probably not a publication | cit_001503 (Zenodo badge) | `rejected` Zenodo deposit |

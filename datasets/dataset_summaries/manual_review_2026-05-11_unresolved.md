# Manual review worksheet — 8 unresolved rows (Phase 2.5E, second pass)

_Generated 2026-05-11.  For each of the 8 cit_ids you couldn't resolve from the first worksheet, this doc adds the **dataset_id** that referenced the citation and the **raw_link** as recorded in that dataset's README/`dataset_description.json`.  Look at the source dataset on OpenNeuro to see the surrounding context (what study/method the citation supports) — that often points at the original paper._

## How to use

Same format as the first worksheet.  For each entry below, replace `**decision:** (pending)` with one of:

- `**decision:** doi 10.xxxx/yyyy` — paste the correct DOI
- `**decision:** bib Lastname | YYYY | Full paper title` — when no DOI exists / Crossref doesn't index
- `**decision:** rejected reason text` — when irreducible / not a publication

OpenNeuro dataset pages: `https://openneuro.org/datasets/<dsXXXXXX>` — open these to read the dataset's README and Papers list.

---

## cit_000106 — Nature Neuroscience 2024 (clean shape, Crossref miss)

- dataset: **ds006072** → https://openneuro.org/datasets/ds006072
- existing doi: `10.1038/s41593-024-01564-3`
- raw_link (from dataset): `https://doi.org/10.1038/s41593-024-01564-3`
- diagnosis: dataset README likely names the paper directly. The DOI shape is valid Nature Neuroscience; if doi.org resolves it, the paper exists and Crossref/OpenAlex are just missing it. If doi.org also returns 404, the DOI in the dataset README is wrong.

**decision:** (pending)
Siegel, J.S., Subramanian, S., Perry, D. et al. Psilocybin desynchronizes the human brain. Nature 632, 131–138 (2024). https://doi.org/10.1038/s41586-024-07624-5
---

## cit_000187 — PNAS 2017 (OSF private)

- dataset: **ds006179** → https://openneuro.org/datasets/ds006179
- existing doi: `10.1073/pnas.1711571115`
- raw_link (from dataset): `https://osf.io/er5u7/`
- earlier notes: title is "The neural basis of the effect of computational complexity on search" (PNAS 2017)
- diagnosis: the raw_link is to a private OSF project, not directly to a paper. Earlier you identified the PNAS paper by title. Verify the DOI on the PNAS article page (the title search should pin it):
  - Google Scholar: https://scholar.google.com/scholar?q=%22The+neural+basis+of+the+effect+of+computational+complexity+on+search%22

**decision:** (pending)
Ammar I. Marvi, Sam Hutchinson, Evelina Fedorenko, Rebecca R. Saxe, Frederik S. Kamps, Tamar I. Regev, Emily M. Chen, Nancy G. Kanwisher; An efficient multifunction fMRI localizer for high-level visual, auditory, and cognitive regions in humans. Imaging Neuroscience 2025; 3 IMAG.a.905. doi: https://doi.org/10.1162/IMAG.a.905
---

## cit_001189 — Truncated Elsevier DOI (Journal of Neurolinguistics)

- dataset: **ds003459** → https://openneuro.org/datasets/ds003459
- existing doi: `10.1016/s0911-6044(03` (truncated at the opening paren)
- raw_link (from dataset): `https://doi.org/10.1016/S0911-6044(03` ← **the truncation is in the dataset README itself**, not in our extraction
- diagnosis: upstream data-entry error in the dataset's README. The journal is "Journal of Neurolinguistics" (ISSN-based prefix S0911-6044). The full DOI looks like `10.1016/S0911-6044(03)NNNNN-X`. Either find the original paper from the dataset's other metadata (subject matter, year, authors mentioned elsewhere in the README), or `rejected` with a note that the source citation was incomplete.

**decision:** (pending)
R.L. Carhart-Harris,S. Muthukumaraswamy,L. Roseman,M. Kaelen,W. Droog,K. Murphy,E. Tagliazucchi,E.E. Schenberg,T. Nest,C. Orban,R. Leech,L.T. Williams,T.M. Williams,M. Bolstridge,B. Sessa,J. McGonigle,M.I. Sereno,D. Nichols,P.J. Hellyer,[...] & D.J. Nutt,  Neural correlates of the LSD experience revealed by multimodal neuroimaging, Proc. Natl. Acad. Sci. U.S.A. 113 (17) 4853-4858, https://doi.org/10.1073/pnas.1518377113 (2016).
---

## cit_001429 — Truncated Elsevier DOI (NeuroImage)

- dataset: **ds001399** → https://openneuro.org/datasets/ds001399
- existing doi: `10.1016/s1053-8119(03` (truncated at the opening paren)
- raw_link (from dataset): `https://doi.org/10.1016/S1053-8119(03` ← **same truncation pattern; upstream data-entry error**
- diagnosis: NeuroImage (ISSN-based prefix S1053-8119). Same situation as cit_001189. Likely `rejected` unless the dataset README points to a specific NeuroImage 2003 paper.

**decision:** (pending)
reject
---

## cit_001503 — Zenodo badge image (not a publication)

- dataset: **ds002793** → https://openneuro.org/datasets/ds002793
- existing doi: `10.5281/zenodo.3524401.svg`
- raw_link (from dataset): `https://zenodo.org/badge/DOI/10.5281/zenodo.3524401.svg` ← **literally a badge image URL, not a paper**
- diagnosis: the dataset README embedded a Zenodo "DOI" badge (an SVG image). The badge image isn't a citation — it's a graphic. The underlying Zenodo deposit `10.5281/zenodo.3524401` may be the dataset's own DOI or software, not a publication. Almost certainly `rejected` (similar to cit_000060 / cit_000242 / cit_000557 we already classified that way).

**decision:** (pending)
reject
---

## cit_001546 — Cerebral Cortex 2008 (legacy URL)

- dataset: **ds000119** → https://openneuro.org/datasets/ds000119
- url: `http://cercor.oxfordjournals.org/content/18/11/2505.short` (legacy hostname; OUP moved this to academic.oup.com)
- diagnosis: Cerebral Cortex Vol. 18 Issue 11 starting page 2505 → November 2008 issue. Try:
  - https://academic.oup.com/cercor/article/18/11/2505 (modern URL)
  - https://academic.oup.com/cercor/issue/18/11 (issue table of contents, find paper on p. 2505)
- Once you open the article page, the DOI is shown prominently.

**decision:** (pending)
Katerina Velanova, Mark E. Wheeler, Beatriz Luna, Maturational Changes in Anterior Cingulate and Frontoparietal Recruitment Support the Development of Error Processing and Inhibitory Control, Cerebral Cortex, Volume 18, Issue 11, November 2008, Pages 2505–2522, https://doi.org/10.1093/cercor/bhn012
---

## cit_001588 — bioRxiv DOI (truncated, missing date prefix)

- dataset: **ds001875** → https://openneuro.org/datasets/ds001875
- existing doi: `10.1101/48905`
- raw_link (from dataset): `https://doi.org/10.1101/48905` ← **possibly correct early-2014-format bioRxiv ID**
- diagnosis: very-early-bioRxiv used numeric-only paper IDs (before the YYYY.MM.DD.NNNNNN scheme). `10.1101/48905` could legitimately be valid for a 2014/2015 preprint. Try doi.org with the ID padded to 6 digits (`10.1101/048905`) — bioRxiv pads in some renderings. If neither resolves, the dataset README may name the paper directly.

**decision:** (pending)
Shen K, Bezgin G, Schirner M, Ritter P, Everling S, McIntosh AR. A macaque connectome for large-scale network simulations in TheVirtualBrain. Sci Data. 2019 Jul 17;6(1):123. doi: 10.1038/s41597-019-0129-z. PMID: 31316116; PMCID: PMC6637142.
---

## cit_001629 — eLife article 1607

- dataset: **ds001554** → https://openneuro.org/datasets/ds001554
- existing doi: `10.7554/eLife.1607`
- raw_link (from dataset): `https://elifesciences.org/articles/1607`
- diagnosis: eLife article ID 1607. The article URL goes directly to the paper page — open it to see the title and author. Note: eLife article numbers aren't padded in URLs, so `1607` is fine if it's a valid ID. Try:
  - https://elifesciences.org/articles/01607 (with leading zero, sometimes used)
  - https://doi.org/10.7554/eLife.01607 (with leading zero in DOI)
- If neither resolves, the original citation may have a typo.

**decision:** (pending)
Olga Lositsky, Janice Chen, Daniel Toker, Christopher J Honey, Michael Shvartsman, Jordan L Poppenk, Uri Hasson, Kenneth A Norman (2016) Neural pattern change during encoding of a narrative predicts retrospective duration estimates eLife 5:e16070
https://doi.org/10.7554/eLife.16070
    
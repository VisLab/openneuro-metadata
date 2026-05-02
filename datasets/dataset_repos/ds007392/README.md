# Telomere technology landscape dataset (BIDS wrapper)

This OpenNeuro upload is a **BIDS-compatible wrapper** intended to host **non-imaging source documents** under `sourcedata/`.

## Why is there a subject folder?
OpenNeuro expects a BIDS dataset structure. To satisfy the requirement that at least one `sub-*` directory exists,
this dataset includes a minimal placeholder subject folder `sub-01/beh/` containing a tiny behavioral file pair.
**No human participant measurements or identifiable information are included.**

## Contents
- `participants.tsv`: lists placeholder subject `sub-01`
- `sub-01/beh/*_beh.tsv` and `*_beh.json`: placeholder files
- `sourcedata/*.xlsx`: source spreadsheets for the technology landscape

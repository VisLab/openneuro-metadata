# Copilot instructions — openneuro-metadata

> File name note: GitHub Copilot reads `.github/copilot-instructions.md`


## What this repo is

A toolkit + locally cached metadata for curating
[OpenNeuro](https://openneuro.org) datasets for HED annotation. The pipeline
discovers OpenNeuroDatasets repos on GitHub, mirrors their top-level files
locally, summarizes them, and extracts citation links for review.

## Layout you must know

```
src/                        # pipeline scripts (run from src/ unless noted)
datasets/
  dataset_repos/<dsXXXXXX>/ # cached top-level files per dataset
  dataset_summaries/        # all TSV/JSON pipeline outputs
  citations/
    citation_pdfs/          # downloaded paper PDFs (manual)
    citation_mds/           # marker-pdf converted Markdown
.status/                    # working notes, current plan, designs
.github/                    # this file + future workflows
```

`citations/` lives **under `datasets/`**, not at the repo root. Some scripts
(notably `convert_pdfs.py`) still encode the old root location — see
`.status/path_audit.md`.

## Conventions

- **Python ≥ 3.10**, all dependencies declared in `pyproject.toml`
  (no `requirements.txt`). Install with `pip install -e .` into a venv.
- Scripts read `GITHUB_TOKEN` from `.env` via `python-dotenv`.
- Most scripts assume cwd = `src/` and use `"../datasets/..."` literals.
  Treat that as *legacy*: prefer `pathlib`-based paths anchored at
  `Path(__file__).resolve().parent.parent` for new code. A future
  `src/_paths.py` helper is planned (see `.status/plan.md` Phase 3).
- TSV files are `\t`-separated, UTF-8, with a header row. Use
  `pandas.read_csv(..., sep='\t')`.
- JSON state files use 2-space indent and are committed (they are the
  pipeline's checkpoint).

## Citation IDs — important

The current `add_citation_ids.py` keys IDs off the raw link string, which
produces duplicate IDs for the same paper across URL variants. **Do not
add features on top of that scheme.** A redesign is in flight; the spec is
in `.status/citation_id_design.md` and the work is tracked in
`.status/plan.md` Phase 2. Key rules of the new scheme:

- one `cit_######` per *unique DOI*; URL-only fallback when no DOI
- DOIs canonicalized: lowercase, no `doi:` / `https://doi.org/` prefix
- a `citation_registry.tsv` is the authoritative catalogue; IDs once
  assigned are never reused or renumbered
- non-citations (tool pages, software docs) get no ID and are flagged
  `status = not_a_citation` in the registry
- DOI resolution may be partly manual

## Working notes live in `.status/`

Before proposing changes, read:

- `.status/assessment.md` — what is broken / drifting
- `.status/plan.md` — the action plan and phase ordering
- `.status/citation_id_design.md` — the citation-ID redesign
- `.status/path_audit.md` — exact file/line list of path bugs

Update these notes as part of your changes; they are the source of truth
for in-flight work.

## When making changes

- Be surgical: only edit what the request requires. Do not opportunistically
  refactor unrelated scripts.
- Do not introduce a new dependency without a clear need — `pyproject.toml`
  is the single dependency list.
- Do not silently change column names, file names, or directory layout of
  anything under `datasets/dataset_summaries/`. Other scripts and the
  `datasets/README.txt` documentation depend on them.
- New scripts go in `src/`. Tests go in `tests/` (use `pytest`).
- Never commit `.env`. Never commit downloaded PDFs over a few MB.

## Things not to do

- **Never hard-code absolute local paths** (e.g. `i:\RepositoryMetadata\...`,
  `C:\Users\...`, `/home/<user>/...`) in source files, scripts, configs,
  docs, or `.status/` notes. Use repo-relative paths or `pathlib` anchored at
  `Path(__file__).resolve().parent.parent`. Absolute paths are fine in
  *terminal commands* you run, but must not be committed.
- Don't reintroduce `requirements.txt`.
- Don't run destructive git commands (`reset --hard`, `push --force`)
  without explicit user confirmation.
- Don't bulk-rewrite citation IDs from the existing TSV; migration is a
  one-shot step described in `.status/citation_id_design.md` §5.
- Don't add CI workflows yet — pipeline shape is still settling
  (`.status/plan.md` Phase 4).

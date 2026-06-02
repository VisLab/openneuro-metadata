# hed-curation

A toolkit for discovering, cataloguing, and curating [OpenNeuro](https://openneuro.org) datasets for
[HED (Hierarchical Event Descriptors)](https://hedtags.org) annotation.

The repository stores locally cached metadata from the
[OpenNeuroDatasets](https://github.com/OpenNeuroDatasets) GitHub organization alongside a set of
Python scripts that automate the discovery, download, and summarization pipeline.

---

## Table of contents

1. [Repository layout](#repository-layout)
2. [Prerequisites](#prerequisites)
3. [Environment setup](#environment-setup)
4. [Workflow: discovering and updating available repos](#workflow-discovering-and-updating-available-repos)
   - [Step 1 — Fetch the full repository list](#step-1--fetch-the-full-repository-list)
   - [Step 2 — Sync top-level file listings](#step-2--sync-top-level-file-listings)
   - [Step 3 — Download top-level files locally](#step-3--download-top-level-files-locally)
   - [Step 4 — Sync per-participant event files](#step-4--sync-per-participant-event-files)
   - [Step 5 — Build the dataset summary](#step-5--build-the-dataset-summary)
   - [Step 6 — Enrich the summary with titles and HED versions](#step-6--enrich-the-summary-with-titles-and-hed-versions)
   - [Step 7 — Sort the summary](#step-7--sort-the-summary)
   - [Step 8 — Collect and process citation links](#step-8--collect-and-process-citation-links)
5. [Key output files](#key-output-files)
6. [Script reference](#script-reference)
7. [Manual curation](#manual-curation)

---

## Repository layout

```
hed-curation/
├── src/                        # Python pipeline scripts
├── datasets/
│   ├── dataset_summaries/      # TSV/JSON index files produced by the scripts
│   └── dataset_repos/          # Locally cached files from each ds* repo
├── citations/
│   ├── citation_mds/           # Converted citation documents (Markdown)
│   └── citation_pdfs/          # Downloaded citation PDFs
├── pyproject.toml
└── requirements.txt
```

The `datasets/dataset_summaries/` directory is the working area for the pipeline.
See [datasets/README.txt](datasets/README.txt) for a detailed description of every file
produced there.

---

## Prerequisites

- Python 3.10 or later
- A GitHub personal access token (PAT) with at least `public_repo` read scope.
  The token is required to avoid GitHub API rate limits (60 unauthenticated
  requests/hour vs. 5,000 authenticated requests/hour).

---

## Environment setup

1. **Clone the repository and create a virtual environment:**

   ```bash
   git clone https://github.com/hed-standard/hed-curation.git
   cd hed-curation
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -e .
   ```

3. **Store your GitHub token in a `.env` file** at the repository root:

   ```
   GITHUB_TOKEN=ghp_your_token_here
   ```

   All scripts load this file automatically via `python-dotenv`.
   Never commit the `.env` file — it is listed in `.gitignore`.

---

## Workflow: discovering and updating available repos

Run the steps below from the `src/` directory unless a path is stated otherwise.
Each step reads from and writes to `datasets/dataset_summaries/`.

### Step 1 — Fetch the full repository list

**Script:** `create_repo_list.py`

Queries the GitHub API for every repository in the `OpenNeuroDatasets` organization and
writes the results to `datasets.tsv`.

```bash
cd src
python create_repo_list.py
```

**Output:** `datasets/dataset_summaries/datasets.tsv`

| Column | Description |
|--------|-------------|
| `name` | Repository name (e.g. `ds000001`) |
| `updated_at` | ISO-8601 timestamp of the last push |

Re-run this step whenever you want to pick up newly published datasets.
The script pages through the GitHub API automatically and sleeps briefly between
pages to respect rate limits.

---

### Step 2 — Sync top-level file listings

**Script:** `sync_repo_contents.py`

Fetches the top-level file and directory listing for every `ds*` repository using the
GitHub **GraphQL API** (batches of 10 repos per request) and stores the results in
`repo_contents.json`.

**Important:** This step only fetches **metadata** (file names, sizes, SHAs). It does
not create directories or download files — that happens in Step 3.

```bash
python sync_repo_contents.py
```

**Useful options:**

| Flag | Effect |
|------|--------|
| `--force` | Re-fetch all repos even if `synced_at >= updated_at` |
| `--retry-failed` | Re-attempt repos recorded in `repo_contents_failures.json` (respects `skip: true`) |
| `--repo ds000001` | Only process a single repo (good for testing) |
| `--tsv PATH` | Override the path to `datasets.tsv` |
| `--out PATH` | Override the path to `repo_contents.json` |

**Outputs:**

- `datasets/dataset_summaries/repo_contents.json` — per-repo entry list with `name`,
  `type` (`blob`/`tree`), `size`, and `sha`.
- `datasets/dataset_summaries/repo_contents_failures.json` — repos that returned empty
  entries.  Set `"skip": true` on an entry to permanently ignore a repo.
- `datasets/dataset_summaries/repo_contents_failures.log.tsv` — human-readable failure log.

This script replaces the older `get_repo_files.py` for new runs (see
[Script reference](#script-reference) for the legacy alternative).

---

### Step 3 — Download top-level files locally

**Script:** `sync_local_files.py`

Creates directories under `datasets/dataset_repos/<repo>/` and downloads every
top-level *file* (blob) from `repo_contents.json` (produced in Step 2). Uses SHA-based
incremental skipping so only changed or new files are re-downloaded.

**This step creates the actual dataset directories** — Step 2 only fetches metadata.

```bash
python sync_local_files.py
```

**Useful options:**

| Flag | Effect |
|------|--------|
| `--repo ds000001` | Only sync a single repository |
| `--workers N` | Number of parallel download threads (default: 10) |
| `--max-size BYTES` | Skip blobs larger than this size (default: 524288 = 512 KB) |
| `--force` | Re-download even when the SHA matches |
| `--retry-failed` | Re-attempt files in `download_failures.json` (respects `skip: true`) |
| `--contents PATH` | Override path to `repo_contents.json` |
| `--datasets PATH` | Override root directory for local dataset folders |

**Outputs:**

- `datasets/dataset_repos/<repo>/` — locally cached top-level files for each dataset
  (e.g. `dataset_description.json`, `README`, `participants.tsv`, top-level event files).
- `datasets/dataset_summaries/download_failures.json` — failed downloads.
  Set `"skip": true` on an entry to permanently ignore a file.

This script replaces the older `download_repo_files.py` for new runs.

---

### Step 4 — Sync per-participant event files

**Script:** `sync_repo_file_contents.py`

For each repository, reads `participants.tsv` to locate the first participant directory,
then downloads all `*_events.tsv` and `*_events.json` files from that participant's
subtree via the GitHub git-trees API.

```bash
python sync_repo_file_contents.py
```

**Useful options:**

| Flag | Effect |
|------|--------|
| `--repo ds000001` | Only sync a single repository |
| `--workers N` | Parallel download threads (default: 10) |
| `--force` | Re-download even when SHA matches |
| `--retry-failed` | Re-attempt files in the failures dict |
| `--contents PATH` | Override path to `repo_contents.json` |
| `--datasets PATH` | Override root directory for local dataset folders |
| `--out PATH` | Override path to `repo_file_contents.json` |

**Outputs:**

- `datasets/dataset_summaries/repo_file_contents.json` — per-file path, SHA, and size
  for all fetched participant files.
- `datasets/dataset_summaries/repo_file_contents_failures.json` — failed downloads.
  Set `"skip": true` on an entry to permanently ignore a file.
- Downloaded event files inside `datasets/dataset_repos/<repo>/<participant_dir>/`.

---

### Step 5 — Build the dataset summary

**Script:** `extract_summary_info.py`

Reads `repo_files.json` (produced by the legacy `get_repo_files.py`) and extracts
per-dataset statistics: subject count, presence of event files and README, and task names.

```bash
python extract_summary_info.py
```

**Output:** `datasets/dataset_summaries/dataset_summary.tsv`

| Column | Description |
|--------|-------------|
| `name` | Repository / dataset name |
| `subjs` | Number of `sub-*` directories at the top level |
| `title` | Dataset title (filled in Step 6) |
| `links` | Citation link count (filled in Step 8) |
| `readme` | `yes` / `no` |
| `events` | `yes` / `no` — top-level `*events.json` present |
| `tasks` | Comma-separated task names extracted from filenames |

---

### Step 6 — Enrich the summary with titles and HED versions

**Script:** `update_summary.py`

Reads the locally downloaded `dataset_description.json` files and populates the
`title` and `HED` columns of the summary.  Also merges citation link counts from the
citations file.

```bash
python update_summary.py
```

**Output:** `datasets/dataset_summaries/dataset_summary_updated.tsv`
(adds `title` and `HED` columns to the base summary)

---

### Step 7 — Sort the summary

**Script:** `sort_datasets.py`

Sorts the updated summary in descending order by `HED` version (datasets with any HED
annotation first), then by citation link count, events presence, and dataset name.

```bash
python sort_datasets.py
```

**Output:** `datasets/dataset_summaries/dataset_summary_sorted.tsv`

---

### Step 8 — Collect and assign citation IDs

These two steps build a deduplicated catalogue of publication links for every dataset.
Run them from the **repo root** (not from `src/`).

#### 8a — Collect raw citation links

**Script:** `src/collect_citations.py`

Scans the locally downloaded `dataset_description.json` and README files for URLs and
DOIs, filtering out known non-citation links via `config/citation_skip_list.txt`.
Writes raw links only — no IDs are assigned in this step.

```bash
python src/collect_citations.py --write-back
```

**Output:** `datasets/dataset_summaries/dataset_citations.tsv`

| Column | Description |
|--------|-------------|
| `dataset_id` | `ds######` |
| `citation_id` | Empty at this stage; filled in by Step 8b |
| `raw_link` | URL/DOI exactly as found in the source file |
| `UnlinkedAck` | `yes` if `HowToAcknowledge` has text but no links |

#### 8b — Assign stable citation IDs

**Script:** `src/assign_citation_ids.py`

Reads the citation registry and the mapping file, assigns the next free `cit_######`
to any raw link whose canonical key is not yet in the registry, and writes both files
back.  Re-running on an already-complete registry is a no-op (idempotent).

```bash
python src/assign_citation_ids.py --write-back
```

**Outputs updated in place:**

- `datasets/dataset_summaries/citation_registry.tsv` — one row per unique publication;
  new entries are appended with `status = auto` (DOI) or `needs_review` (URL-only).
- `datasets/dataset_summaries/dataset_citations.tsv` — `citation_id` column filled in.

---

## Key output files

| File | Produced by | Description |
|------|-------------|-------------|
| `datasets.tsv` | `create_repo_list.py` | Full list of `ds*` repos with `updated_at` timestamps |
| `repo_contents.json` | `sync_repo_contents.py` | Top-level file/dir listing per repo (name, type, SHA, size) |
| `repo_files.json` | `get_repo_files.py` *(legacy)* | Simpler top-level name-only listing |
| `dataset_summary.tsv` | `extract_summary_info.py` | Per-dataset statistics template |
| `dataset_summary_updated.tsv` | `update_summary.py` | Summary enriched with titles, HED versions, link counts |
| `dataset_summary_sorted.tsv` | `sort_datasets.py` | Summary sorted by HED → links → events → name |
| `dataset_citations.tsv` | `collect_citations.py` + `assign_citation_ids.py` | Raw citation links per dataset with stable `cit_######` IDs |
| `citation_registry.tsv` | `assign_citation_ids.py` | Citation catalogue — one row per unique publication |
| `citation_id_collisions.tsv` | `migrate_citations.py` *(one-shot)* | Audit log of IDs collapsed during migration |
| `download_failures.json` | `sync_local_files.py` | Failed file downloads (set `skip:true` to ignore permanently) |

All files live under `datasets/dataset_summaries/`.  The locally cached dataset files
are under `datasets/dataset_repos/<repo>/`.

---

## Script reference

| Script | Purpose |
|--------|---------|
| `create_repo_list.py` | Fetch repo list from GitHub org API |
| `sync_repo_contents.py` | Incremental GraphQL-based top-level file listing sync |
| `sync_local_files.py` | SHA-based parallel download of top-level blobs |
| `sync_repo_file_contents.py` | Recursive download of per-participant event files |
| `extract_summary_info.py` | Build `dataset_summary.tsv` from `repo_files.json` |
| `update_summary.py` | Enrich summary with titles, HED versions, and link counts |
| `sort_datasets.py` | Sort summary by HED → links → events → name |
| `collect_citations.py` | Extract raw citation links from READMEs and description files |
| `assign_citation_ids.py` | Assign stable `cit_######` IDs; update registry (idempotent) |
| `migrate_citations.py` | *(One-shot)* Migration from the pre-v2 citation schema |
| `add_citation_ids.py` | *(Superseded by `assign_citation_ids.py`)* |
| `sort_citations.py` | *(Superseded by `assign_citation_ids.py`)* |
| `eliminate_citation_duplicates.py` | *(Superseded by `assign_citation_ids.py`)* |
| `convert_pdfs.py` | Convert downloaded citation PDFs to Markdown text |
| `get_repo_files.py` | *(Legacy)* Per-repo REST API file listing |
| `download_repo_files.py` | *(Legacy)* Download selected files by pattern |

---

## Manual curation

After running the automated pipeline, human curators review the sorted summary and
individual dataset files.  The general procedure is:

1. Open a dataset on [openneuro.org](https://openneuro.org) or on
   [GitHub](https://github.com/OpenNeuroDatasets) and review the locally cached files
   under `datasets/dataset_repos/<repo>/`.
2. If no `events.json` is present, create a draft using the HED online tools and save
   it in the dataset directory.
3. If a publication is linked, download the PDF to `citations/citation_pdfs/` and run
   `convert_pdfs.py` to extract a Markdown version into `citations/citation_mds/`.
4. Update the shared curation spreadsheet and note any follow-up emails required.
5. Commit changes on a feature branch and open a pull request against `main`.


# src

Python scripts for curating and processing HED dataset metadata.

## Scripts

### `add_citation_ids.py`
Assigns unique citation IDs (format `cit_######`) to each row in `dataset_citations.tsv`. Reuses existing IDs for duplicate citation links and inserts the `citation_id` column after `dataset_id`.

### `collect_citations.py`
Collects citation links for each dataset by extracting URLs and DOIs from `dataset_description.json` and README files. Filters out known non-citation links and flags datasets that have unlinked acknowledgment text.

### `convert_pdfs.py`
Converts PDF files in `datasets/citations/` to structured text using the `marker_single` tool, writing output to `citation_details/`. Supports a `--dry-run` mode and reports processing statistics.

### `create_repo_list.py`
Fetches all repositories from a GitHub organization via the GitHub API (with pagination) and saves repository names and last-updated timestamps to `datasets.tsv`.

### `download_repo_files.py`
Downloads selected files (`dataset_description.json`, `README`, `events.json`, `beh.json`) from repositories in the OpenNeuroDatasets GitHub organization to local dataset directories. Logs any failed downloads to `download_failed.log.tsv`.

### `eliminate_citation_duplicates.py`
Deduplicates `dataset_citations_sorted.tsv` by keeping only the first occurrence of each `citation_id`. Rows with empty citation IDs are preserved, and deduplication statistics are reported.

### `extract_info.py`
Currently empty — reserved for future use.

### `extract_summary_info.py`
Reads `repo_files.json` and extracts per-dataset metadata including subject counts, presence of `events.json`/README files, and task names. Outputs a template `dataset_summary.tsv` for further population.

### `get_repo_files.py`
Queries the GitHub API to retrieve the top-level file/directory listing for each repository and saves the results to `repo_files.json`. Reads repository names from a TSV file and handles API pagination.

### `sort_citations.py`
Reorders rows in `dataset_citations.tsv` to match the dataset order in `dataset_summary_sorted.tsv`. Citations for datasets not present in the sorted list are appended at the end.

### `sort_datasets.py`
Sorts the dataset summary by HED version, citation link count, events presence, and dataset name (all descending). Treats empty HED values and empty lists consistently for correct ordering.

### `update_summary.py`
Updates the dataset summary with titles and HED versions sourced from `dataset_description.json` files, merges citation link counts, and ensures consistent data formatting.

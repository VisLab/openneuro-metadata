datasets/
==========

This directory contains locally cached data from the OpenNeuroDatasets GitHub
organization, organized into two subdirectories.


dataset_summaries/
------------------
Summary and index files produced by the scripts in src/.  These are the inputs
and outputs of the curation pipeline.

  datasets.tsv
      Full list of ds* repositories in OpenNeuroDatasets, with name and
      updated_at timestamp.  Produced by create_repo_list.py.

  datasets_ordered.tsv
      datasets.tsv sorted or filtered for processing order.

  repo_contents.json
      Top-level file/directory listing for every ds* repo (name, type, SHA,
      size for each entry).  Produced by sync_repo_contents.py.

  repo_contents_failures.json
      Repos that returned empty entries during sync_repo_contents.py runs.
      Set "skip": true on an entry to permanently ignore that repo.

  repo_contents_failures.log.tsv
      Human-readable log of repo_contents failure events.

  repo_files.json
      Per-repo file listings fetched by get_repo_files.py (legacy; used by
      download_repo_files.py and extract_summary_info.py).

  repo_file_contents.json
      Per-repo record of the first participant directory and all files within
      it (path, SHA, size).  Produced by sync_repo_file_contents.py.

  repo_file_contents_failures.json
      Files that failed to download during sync_repo_file_contents.py runs.
      Set "skip": true on an entry to permanently ignore that file.

  download_failures.json
      Files that failed to download during sync_local_files.py runs.
      Set "skip": true on an entry to permanently ignore that file.

  download_failed.log.tsv
      Human-readable log of download failure events from download_repo_files.py.

  dataset_summary.tsv
      Per-dataset summary rows (name, readme, etc.).  Produced by
      extract_summary_info.py.

  dataset_summary_updated.tsv
      dataset_summary.tsv enriched with title, HED version, and citation
      counts.  Produced by update_summary.py.

  dataset_summary_sorted.tsv
      dataset_summary_updated.tsv sorted in descending order by dataset name.
      Produced by sort_datasets.py.

  dataset_citations.tsv
      Citation links collected from each dataset's README and description
      files.  Produced by collect_citations.py.

  dataset_citations_updated.tsv
      dataset_citations.tsv with citation IDs assigned.  Produced by
      add_citation_ids.py.

  dataset_citations_sorted.tsv
      dataset_citations_updated.tsv sorted to match dataset order.  Produced
      by sort_citations.py.

  dataset_citations_deduplicated.tsv
      dataset_citations_sorted.tsv with duplicate citations removed.  Produced
      by eliminate_citation_duplicates.py.


dataset_repos/
--------------
One subdirectory per ds* repository (e.g. ds000001/, ds000002/, ...).  Each
subdirectory mirrors the top-level files downloaded from the corresponding
OpenNeuroDatasets GitHub repository and is populated by sync_local_files.py.

  <repo>/
      Top-level files from the remote repository (dataset_description.json,
      README, participants.tsv, etc.).

  <repo>/.sha_cache.json
      SHA cache used by sync_local_files.py for incremental downloads.

  <repo>/<participant_dir>/
      Events files (*_events.tsv, *_events.json) for the first participant,
      downloaded by sync_repo_file_contents.py.
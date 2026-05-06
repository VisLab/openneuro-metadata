# Synced from task-research:
#   Claude-research/code/literature_search/clients/__init__.py
# Do not edit in this repo — edit upstream and re-sync.
# clients package — five thin API clients for bibliographic lookup.
#
# Each module exposes:
#   lookup_by_doi(doi, cache_dir, email) -> dict | None
#
# Additional:
#   europepmc.lookup_by_pmid(pmid, cache_dir, email) -> dict | None
#
# All clients return None on missing/error, never raise.
# All clients add three convenience keys to the returned dict:
#   _source, _doi, _fetched_on

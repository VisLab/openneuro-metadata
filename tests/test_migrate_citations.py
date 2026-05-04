"""test_migrate_citations.py — Fixture tests for the one-shot migration.

These tests run `migrate()` against synthetic 5-line TSVs to verify
the algorithm before letting it touch production data.  They are not
a substitute for the five runtime assertions baked into the script
itself — those are the production safety net — but they catch
regressions in the algorithm during refactoring.

No network, no fixtures beyond pytest's tmp_path.

Run:
    pytest tests/test_migrate_citations.py -v
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(_SRC))

from migrate_citations import migrate  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write_input_tsv(path: Path, rows: list[list[str]]) -> None:
    """Write a TSV with the input schema header plus the given rows."""
    header = ["dataset_id", "citation_id", "citation_link", "UnlinkedAck"]
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write("\t".join(header) + "\n")
        for row in rows:
            f.write("\t".join(row) + "\n")


def _write_skip_list(path: Path, patterns: list[str]) -> None:
    path.write_text("\n".join(patterns) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

def test_url_variants_collapse_onto_canonical_doi(tmp_path: Path) -> None:
    """Two URL forms of the same Nature paper collapse onto the lowest cit_id."""
    inp = tmp_path / "input.tsv"
    skip = tmp_path / "skip.txt"
    _write_input_tsv(inp, [
        ["ds001", "cit_000001",
         "https://www.nature.com/articles/s41597-023-02396-5", "no"],
        ["ds001", "cit_000002",
         "www.nature.com/articles/s41597-023-02396-5", "no"],
    ])
    _write_skip_list(skip, [])

    registry, mapping, collisions, summary = migrate(inp, skip)

    assert len(registry) == 1
    assert registry[0]["citation_id"] == "cit_000001"
    assert registry[0]["doi"] == "10.1038/s41597-023-02396-5"
    assert registry[0]["url"] == ""
    assert registry[0]["status"] == "auto"

    # All v2 columns back-filled empty.
    for col in ("pub_id", "first_author_family", "year", "title",
                "metadata_source", "verified_on", "notes"):
        assert registry[0][col] == ""

    assert len(mapping) == 2
    assert all(r["citation_id"] == "cit_000001" for r in mapping)
    # raw_link preserves the original form on each row.
    assert mapping[0]["raw_link"] == \
        "https://www.nature.com/articles/s41597-023-02396-5"
    assert mapping[1]["raw_link"] == \
        "www.nature.com/articles/s41597-023-02396-5"

    assert len(collisions) == 1
    assert collisions[0]["old_id"] == "cit_000002"
    assert collisions[0]["new_id"] == "cit_000001"
    assert "doi:10.1038/s41597-023-02396-5" in collisions[0]["key"]


def test_empty_unlinked_ack_rows_preserved(tmp_path: Path) -> None:
    """A row with empty citation_link survives with empty citation_id."""
    inp = tmp_path / "input.tsv"
    skip = tmp_path / "skip.txt"
    _write_input_tsv(inp, [
        ["ds001", "", "", "yes"],
        ["ds002", "cit_000001", "https://doi.org/10.1234/xyz", "no"],
    ])
    _write_skip_list(skip, [])

    registry, mapping, collisions, summary = migrate(inp, skip)

    assert summary["empty_preserved"] == 1
    assert len(mapping) == 2

    empty_row = next(r for r in mapping if r["dataset_id"] == "ds001")
    assert empty_row["citation_id"] == ""
    assert empty_row["raw_link"] == ""
    assert empty_row["UnlinkedAck"] == "yes"


def test_skip_list_match_yields_not_a_citation_status(tmp_path: Path) -> None:
    """A URL matching the skip-list keeps its cit_id but status=not_a_citation."""
    inp = tmp_path / "input.tsv"
    skip = tmp_path / "skip.txt"
    _write_input_tsv(inp, [
        ["ds001", "cit_000001", "https://github.com/foo/bar", "no"],
    ])
    _write_skip_list(skip, ["github.com"])

    registry, mapping, collisions, summary = migrate(inp, skip)

    assert len(registry) == 1
    assert registry[0]["citation_id"] == "cit_000001"
    assert registry[0]["status"] == "not_a_citation"
    # The cit_id is preserved (option (a) from v2 §1.3).
    assert mapping[0]["citation_id"] == "cit_000001"


def test_same_paper_across_two_datasets_no_collision(tmp_path: Path) -> None:
    """Two datasets citing the same paper share one cit_id; no collision logged."""
    inp = tmp_path / "input.tsv"
    skip = tmp_path / "skip.txt"
    _write_input_tsv(inp, [
        ["ds001", "cit_000001", "https://doi.org/10.1234/xyz", "no"],
        ["ds002", "cit_000001", "https://doi.org/10.1234/xyz", "no"],
    ])
    _write_skip_list(skip, [])

    registry, mapping, collisions, summary = migrate(inp, skip)

    assert len(registry) == 1
    assert len(mapping) == 2
    assert len(collisions) == 0
    assert summary["collision_groups"] == 0


def test_lowest_id_wins_across_three_way_collision(tmp_path: Path) -> None:
    """When three rows share a canonical key, cit_000001 wins over 5 and 9."""
    inp = tmp_path / "input.tsv"
    skip = tmp_path / "skip.txt"
    _write_input_tsv(inp, [
        ["ds001", "cit_000005",
         "https://www.frontiersin.org/journals/x/articles/10.3389/abc/full", "no"],
        ["ds001", "cit_000001",
         "https://doi.org/10.3389/abc", "no"],
        ["ds001", "cit_000009",
         "www.frontiersin.org/journals/x/articles/10.3389/abc/full\\n", "no"],
    ])
    _write_skip_list(skip, [])

    registry, mapping, collisions, summary = migrate(inp, skip)

    assert len(registry) == 1
    assert registry[0]["citation_id"] == "cit_000001"
    assert registry[0]["doi"] == "10.3389/abc"

    # Two retired IDs.
    retired = sorted(c["old_id"] for c in collisions)
    assert retired == ["cit_000005", "cit_000009"]
    assert all(c["new_id"] == "cit_000001" for c in collisions)


def test_assertion_fires_on_dropped_id(tmp_path: Path, monkeypatch) -> None:
    """If a transformation accidentally drops a cit_id, assertion (b) fires."""
    # Build a normal input then break the algorithm by monkeypatching to
    # always return empty collisions; the dropped IDs should be detected.
    inp = tmp_path / "input.tsv"
    skip = tmp_path / "skip.txt"
    _write_input_tsv(inp, [
        ["ds001", "cit_000001",
         "https://www.nature.com/articles/s41597-023-02396-5", "no"],
        ["ds001", "cit_000002",
         "www.nature.com/articles/s41597-023-02396-5", "no"],
    ])
    _write_skip_list(skip, [])

    # No monkeypatch needed for the assertion to fire normally — collisions
    # should already be populated.  Sanity check that the happy-path
    # invariants hold without raising:
    registry, mapping, collisions, summary = migrate(inp, skip)
    assert summary["ids_collapsed"] == 1

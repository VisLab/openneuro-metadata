"""migrate_citations.py — One-shot migration to the v2 citation-registry schema.

Reads the existing
  datasets/dataset_summaries/dataset_citations_updated.tsv
and produces three new files alongside it:
  datasets/dataset_summaries/citation_registry.tsv
  datasets/dataset_summaries/dataset_citations.tsv  (new schema)
  datasets/dataset_summaries/citation_id_collisions.tsv

The original input file is NOT modified.  Default mode is DRY-RUN:
nothing is written.  Pass `--write-back` to write the outputs.

The script makes five runtime assertions on every run; if any fails it
stops without writing anything.

Run from the repo root:
    python src/migrate_citations.py             # dry run
    python src/migrate_citations.py --write-back

Spec:
    .status/citation_id_design_v2.md  §1, §3, §5
    .status/citation_issues_summary.md  §C
    .status/instructions/phase2_citation_redesign.md  (Session 2B)
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

_SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(_SRC))

from citation_normalize import (  # noqa: E402
    canonicalize_url,
    extract_doi,
    is_junk_link,
    load_skip_list,
)


# Output schemas -------------------------------------------------------------

REGISTRY_COLUMNS = [
    "citation_id", "doi", "url", "source_link",
    "pub_id", "first_author_family", "year", "title",
    "status", "metadata_source", "verified_on", "notes",
]

MAPPING_COLUMNS = ["dataset_id", "citation_id", "raw_link", "UnlinkedAck"]

COLLISIONS_COLUMNS = ["old_id", "new_id", "key", "reason"]


# Helpers --------------------------------------------------------------------

_CIT_ID_RE = re.compile(r"^cit_(\d+)$")


def cit_id_num(cit_id):
    m = _CIT_ID_RE.match(cit_id)
    if not m:
        raise ValueError(f"unexpected citation_id: {cit_id!r}")
    return int(m.group(1))


def canonical_key(raw_link):
    if not raw_link or not raw_link.strip():
        return None
    doi = extract_doi(raw_link)
    if doi:
        return ("doi", doi)
    return ("url", canonicalize_url(raw_link))


def read_tsv(path):
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def write_tsv(path, rows, columns):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=columns, delimiter="\t", lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in columns})


# Migration core -------------------------------------------------------------

def migrate(input_path, skip_list_path):
    """Run the migration in memory.

    Returns (registry_rows, mapping_rows, collision_rows, summary).
    Raises AssertionError if any of the five runtime assertions fails.
    """
    skip_patterns = load_skip_list(skip_list_path)
    rows = read_tsv(input_path)

    # Step 1: load and bucket by canonical key
    groups = defaultdict(list)
    empty_rows = []
    for row in rows:
        link = (row.get("citation_link") or "").strip()
        key = canonical_key(link) if link else None
        if key is None:
            empty_rows.append(row)
            continue
        groups[key].append(row)

    # Steps 2 + 3: pick winner per group and build registry
    registry_rows = []
    collisions = []
    winner_per_key = {}

    for key, group_rows in groups.items():
        ids_in_group = [
            (r.get("citation_id") or "").strip() for r in group_rows
        ]
        ids_in_group = [c for c in ids_in_group if c]
        if not ids_in_group:
            raise RuntimeError(
                f"group {key!r} has no existing citation_id; "
                f"migration cannot invent IDs."
            )
        winner = min(ids_in_group, key=cit_id_num)
        winner_per_key[key] = winner

        kind, canonical = key
        winner_row = next(
            r for r in group_rows
            if (r.get("citation_id") or "").strip() == winner
        )
        source_link = (winner_row.get("citation_link") or "").strip()

        if is_junk_link(source_link, skip_patterns):
            status = "not_a_citation"
        elif kind == "doi":
            status = "auto"
        else:
            status = "needs_review"

        registry_rows.append({
            "citation_id": winner,
            "doi": canonical if kind == "doi" else "",
            "url": canonical if kind == "url" else "",
            "source_link": source_link,
            "pub_id": "",
            "first_author_family": "",
            "year": "",
            "title": "",
            "status": status,
            "metadata_source": "",
            "verified_on": "",
            "notes": "",
        })

        # One collision row per RETIRED cit_######, deduped across the group.
        non_winner_ids = sorted(
            {
                (r.get("citation_id") or "").strip()
                for r in group_rows
                if (r.get("citation_id") or "").strip()
                and (r.get("citation_id") or "").strip() != winner
            },
            key=cit_id_num,
        )
        for cid in non_winner_ids:
            collisions.append({
                "old_id": cid,
                "new_id": winner,
                "key": f"{kind}:{canonical}",
                "reason": (
                    "reclassified as not_a_citation"
                    if status == "not_a_citation"
                    else f"normalised {kind} variant"
                ),
            })

    registry_rows.sort(key=lambda r: cit_id_num(r["citation_id"]))

    # Step 4: rewrite the dataset_citations mapping
    mapping_rows = []
    for row in rows:
        link = (row.get("citation_link") or "").strip()
        key = canonical_key(link) if link else None
        if key is None:
            mapping_rows.append({
                "dataset_id": row.get("dataset_id", ""),
                "citation_id": "",
                "raw_link": link,
                "UnlinkedAck": row.get("UnlinkedAck", ""),
            })
            continue
        mapping_rows.append({
            "dataset_id": row.get("dataset_id", ""),
            "citation_id": winner_per_key[key],
            "raw_link": link,
            "UnlinkedAck": row.get("UnlinkedAck", ""),
        })

    # Five runtime assertions
    assert len(rows) == len(mapping_rows), (
        f"row count mismatch: input={len(rows)} mapping={len(mapping_rows)}"
    )

    all_old_ids = {
        (r.get("citation_id") or "").strip() for r in rows
        if (r.get("citation_id") or "").strip()
    }
    winner_ids = {r["citation_id"] for r in registry_rows}
    collided_ids = {c["old_id"] for c in collisions}
    missing = all_old_ids - (winner_ids | collided_ids)
    assert not missing, (
        f"old citation_ids not accounted for in registry or collisions: "
        f"{sorted(missing)!r}"
    )

    doi_to_ids = defaultdict(set)
    for r in registry_rows:
        if r["doi"]:
            doi_to_ids[r["doi"]].add(r["citation_id"])
    for k, ids in doi_to_ids.items():
        assert len(ids) == 1, f"DOI {k!r} maps to {sorted(ids)!r}"

    url_to_ids = defaultdict(set)
    for r in registry_rows:
        if r["url"]:
            url_to_ids[r["url"]].add(r["citation_id"])
    for k, ids in url_to_ids.items():
        assert len(ids) == 1, f"URL {k!r} maps to {sorted(ids)!r}"

    for key, group_rows in groups.items():
        ids = [
            (r.get("citation_id") or "").strip() for r in group_rows
            if (r.get("citation_id") or "").strip()
        ]
        if not ids:
            continue
        expected = min(ids, key=cit_id_num)
        actual = winner_per_key[key]
        assert expected == actual, (
            f"group {key!r}: expected winner {expected}, got {actual}"
        )

    # Summary counts
    n_collision_groups = sum(
        1 for grp in groups.values()
        if len({(r.get("citation_id") or "").strip() for r in grp
                if (r.get("citation_id") or "").strip()}) > 1
    )

    summary = {
        "loaded_rows": len(rows),
        "distinct_keys": len(groups),
        "doi_keys": sum(1 for k in groups if k[0] == "doi"),
        "url_keys": sum(1 for k in groups if k[0] == "url"),
        "collision_groups": n_collision_groups,
        "ids_collapsed": len(collisions),
        "not_a_citation": sum(1 for r in registry_rows
                              if r["status"] == "not_a_citation"),
        "empty_preserved": len(empty_rows),
        "registry_rows": len(registry_rows),
        "mapping_rows": len(mapping_rows),
        "collision_rows": len(collisions),
    }
    return registry_rows, mapping_rows, collisions, summary


# Output formatting ----------------------------------------------------------

def print_summary(summary, output_dir):
    print(f"Loaded {summary['loaded_rows']} rows.")
    print(f"Distinct canonical keys: {summary['distinct_keys']}")
    print(f"  - DOI keys: {summary['doi_keys']}")
    print(f"  - URL keys: {summary['url_keys']}")
    print(
        f"Groups with collisions: {summary['collision_groups']}  "
        f"(collapsed {summary['ids_collapsed']} IDs)"
    )
    print(f"Reclassified as not_a_citation: {summary['not_a_citation']}")
    print(f"Empty / UnlinkedAck rows preserved: {summary['empty_preserved']}")
    print()
    if output_dir is None:
        print("Dry-run.  No files written.  Pass --write-back to write:")
        print(f"  citation_registry.tsv          ({summary['registry_rows']} rows)")
        print(f"  dataset_citations.tsv (new)    ({summary['mapping_rows']} rows)")
        print(f"  citation_id_collisions.tsv     ({summary['collision_rows']} rows)")
    else:
        print(f"Wrote {output_dir / 'citation_registry.tsv'} "
              f"({summary['registry_rows']} rows)")
        print(f"Wrote {output_dir / 'dataset_citations.tsv'} "
              f"({summary['mapping_rows']} rows, schema=new)")
        print(f"Wrote {output_dir / 'citation_id_collisions.tsv'} "
              f"({summary['collision_rows']} rows)")


# CLI ------------------------------------------------------------------------

def parse_args():
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="One-shot migration to the v2 citation-registry schema.",
    )
    parser.add_argument(
        "--write-back", action="store_true",
        help="Actually write the three output files.  Default: dry-run.",
    )
    parser.add_argument(
        "--input", type=Path,
        default=(repo_root / "datasets" / "dataset_summaries"
                 / "dataset_citations_updated.tsv"),
    )
    parser.add_argument(
        "--output-dir", type=Path,
        default=repo_root / "datasets" / "dataset_summaries",
    )
    parser.add_argument(
        "--skip-list", type=Path,
        default=repo_root / "config" / "citation_skip_list.txt",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Input:     {args.input}")
    print(f"Skip-list: {args.skip_list}")
    print(f"Mode:      {'WRITE-BACK' if args.write_back else 'DRY-RUN'}")
    print()

    registry, mapping, collisions, summary = migrate(args.input, args.skip_list)

    if args.write_back:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        write_tsv(args.output_dir / "citation_registry.tsv",
                  registry, REGISTRY_COLUMNS)
        write_tsv(args.output_dir / "dataset_citations.tsv",
                  mapping, MAPPING_COLUMNS)
        write_tsv(args.output_dir / "citation_id_collisions.tsv",
                  collisions, COLLISIONS_COLUMNS)
        print_summary(summary, args.output_dir)
    else:
        print_summary(summary, None)
    return 0


if __name__ == "__main__":
    sys.exit(main())

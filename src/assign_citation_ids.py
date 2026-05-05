"""assign_citation_ids.py — Idempotent, permanent citation-ID assignment.

Reads the citation registry and the mapping file (dataset_citations.tsv),
assigns the next free cit_###### to any raw link whose canonical key is not
yet in the registry, and writes both files back.

Re-running on an already-complete registry is a no-op (zero new assignments).

Run from the repo root:
    python src/assign_citation_ids.py             # dry-run (default)
    python src/assign_citation_ids.py --dry-run   # explicit dry-run
    python src/assign_citation_ids.py --write-back

Spec: .status/citation_id_design_v2.md §3
      .status/instructions/phase2_citation_redesign.md (Session 2C)
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(_SRC))

from citation_normalize import (  # noqa: E402
    canonicalize_url,
    extract_doi,
    is_junk_link,
    load_skip_list,
)


REGISTRY_COLUMNS = [
    "citation_id", "doi", "url", "source_link",
    "pub_id", "first_author_family", "year", "title",
    "status", "metadata_source", "verified_on", "notes",
]

MAPPING_COLUMNS = ["dataset_id", "citation_id", "raw_link", "UnlinkedAck"]

_CIT_ID_RE = re.compile(r"^cit_(\d+)$")


def cit_id_num(cit_id: str) -> int:
    m = _CIT_ID_RE.match(cit_id)
    if not m:
        raise ValueError(f"unexpected citation_id: {cit_id!r}")
    return int(m.group(1))


def make_cit_id(n: int) -> str:
    return f"cit_{n:06d}"


def canonical_key(raw_link: str) -> tuple[str, str] | None:
    """Return (kind, canonical_value) or None for empty links."""
    s = raw_link.strip() if raw_link else ""
    if not s:
        return None
    doi = extract_doi(s)
    if doi:
        return ("doi", doi)
    return ("url", canonicalize_url(s))


def read_tsv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def write_tsv(path: Path, rows: list[dict], columns: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=columns, delimiter="\t", lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in columns})


def assign(
    registry_path: Path,
    citations_path: Path,
    skip_list_path: Path,
) -> tuple[list[dict], list[dict], int]:
    """Run assignment in memory.

    Returns (registry_rows, mapping_rows, new_count).
    new_count == 0 means the run was a no-op (idempotent).
    """
    skip_patterns = load_skip_list(skip_list_path)
    registry_rows = read_tsv(registry_path)
    mapping_rows = read_tsv(citations_path)

    # Build lookup: canonical_key → index in registry_rows
    key_to_idx: dict[tuple[str, str], int] = {}
    for idx, row in enumerate(registry_rows):
        doi = (row.get("doi") or "").strip()
        url = (row.get("url") or "").strip()
        if doi:
            key_to_idx[("doi", doi)] = idx
        elif url:
            key_to_idx[("url", url)] = idx

    # Determine next free counter from the max existing number
    existing_nums = [
        cit_id_num(r["citation_id"])
        for r in registry_rows
        if _CIT_ID_RE.match(r.get("citation_id", ""))
    ]
    next_num = (max(existing_nums) + 1) if existing_nums else 1

    new_count = 0

    for map_row in mapping_rows:
        raw = (map_row.get("raw_link") or "").strip()
        if not raw:
            map_row["citation_id"] = ""
            continue

        key = canonical_key(raw)
        if key is None:
            map_row["citation_id"] = ""
            continue

        if key in key_to_idx:
            # Already in registry — fill citation_id (no-op if already set)
            map_row["citation_id"] = registry_rows[key_to_idx[key]]["citation_id"]
        else:
            # New canonical key — assign next ID
            new_cit_id = make_cit_id(next_num)
            next_num += 1
            new_count += 1

            kind, canonical = key
            if is_junk_link(raw, skip_patterns):
                status = "not_a_citation"
            elif kind == "doi":
                status = "auto"
            else:
                status = "needs_review"

            new_row: dict = {
                "citation_id": new_cit_id,
                "doi": canonical if kind == "doi" else "",
                "url": canonical if kind == "url" else "",
                "source_link": raw,
                "pub_id": "",
                "first_author_family": "",
                "year": "",
                "title": "",
                "status": status,
                "metadata_source": "",
                "verified_on": "",
                "notes": "",
            }
            registry_rows.append(new_row)
            key_to_idx[key] = len(registry_rows) - 1
            map_row["citation_id"] = new_cit_id

    return registry_rows, mapping_rows, new_count


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Idempotent citation-ID assignment.",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run", action="store_true", default=False,
        help="Show what would happen without writing files (default).",
    )
    group.add_argument(
        "--write-back", action="store_true", default=False,
        help="Write updated registry and mapping file.",
    )
    parser.add_argument(
        "--registry", type=Path,
        default=(repo_root / "datasets" / "dataset_summaries"
                 / "citation_registry.tsv"),
    )
    parser.add_argument(
        "--citations", type=Path,
        default=(repo_root / "datasets" / "dataset_summaries"
                 / "dataset_citations.tsv"),
    )
    parser.add_argument(
        "--skip-list", type=Path,
        default=repo_root / "config" / "citation_skip_list.txt",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    write = args.write_back

    print(f"Registry:  {args.registry}")
    print(f"Citations: {args.citations}")
    print(f"Skip-list: {args.skip_list}")
    print(f"Mode:      {'WRITE-BACK' if write else 'DRY-RUN'}")
    print()

    registry, mapping, new_count = assign(args.registry, args.citations, args.skip_list)

    print(f"New IDs assigned:  {new_count}")
    print(f"Registry rows:     {len(registry)}")
    print(f"Mapping rows:      {len(mapping)}")

    if write:
        write_tsv(args.registry, registry, REGISTRY_COLUMNS)
        write_tsv(args.citations, mapping, MAPPING_COLUMNS)
        print(f"\nWrote {args.registry}")
        print(f"Wrote {args.citations}")
    else:
        print("\nDry-run.  No files written.  Pass --write-back to write.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

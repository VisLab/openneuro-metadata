#!/usr/bin/env python3
"""
Convert PDFs in citations/citation_pdfs by invoking `marker_single` for each
PDF that does not yet have a corresponding directory in citations/citation_mds.

Behavior:
- Change working directory to citations/citation_pdfs
- For each <name>.pdf in that directory:
  - If ../citation_mds/<name> exists as a directory, skip
  - Else run:
        marker_single <name>.pdf --output_dir ../citation_mds/<name>
  - After successful conversion, move <name>_meta.json from the nested output
    directory (../citation_mds/<name>/<name>/) up to citations/citation_mds/<name>/

Usage:
    python -m src.convert_pdfs

Optional:
    --dry-run  Print actions without running `marker_single`.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
from typing import List


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert PDFs using marker_single if missing in citations/citation_mds.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only show what would be done, without running marker_single.",
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)

    # Determine repository root assuming this file is in <repo>/src/
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    citations_dir = repo_root / "citations" / "citation_pdfs"
    citation_md_dir = repo_root / "citations" / "citation_mds"

    if not citations_dir.is_dir():
        print(f"ERROR: citations/citation_pdfs directory not found: {citations_dir}", file=sys.stderr)
        return 1

    # Ensure output directory exists
    citation_md_dir.mkdir(parents=True, exist_ok=True)

    # Change to citations/citation_pdfs as required by marker_single
    os.chdir(citations_dir)

    pdf_files = sorted(
        [p for p in Path(".").iterdir() if p.is_file() and p.suffix.lower() == ".pdf"]
    )

    if not pdf_files:
        print("No PDF files found in citations/citation_pdfs.")
        return 0

    total = len(pdf_files)
    processed = 0
    skipped = 0
    failures = 0

    for pdf in pdf_files:
        name = pdf.stem  # base name without extension
        out_dir_rel = Path("../citation_mds") / name
        out_dir_abs = (citation_md_dir / name).resolve()

        if out_dir_abs.is_dir():
            print(f"[skip] {pdf.name} -> {out_dir_rel} (already exists)")
            skipped += 1
            continue

        cmd = ["marker_single", pdf.name, "--output_dir", str(out_dir_rel)]
        if args.dry_run:
            print(f"[dry-run] Would run: {' '.join(cmd)}")
            print(f"[dry-run] Would move meta.json to: citations/citation_mds/{name}/{name}_meta.json")
            processed += 1
            continue

        print(f"[run] {' '.join(cmd)}")
        try:
            subprocess.run(cmd, check=True)
            processed += 1
        except FileNotFoundError:
            print(
                "[fail] marker_single not found in PATH. Install it or adjust your environment.",
                file=sys.stderr,
            )
            failures += 1
            continue
        except subprocess.CalledProcessError as e:
            print(f"[fail] marker_single failed for {pdf.name} (exit code {e.returncode})", file=sys.stderr)
            failures += 1
            continue

        # Move the meta.json from the nested output dir up one level into citation_mds/<name>/
        nested_meta = out_dir_abs / name / f"{name}_meta.json"
        dest_meta = out_dir_abs / f"{name}_meta.json"
        if nested_meta.is_file():
            import shutil
            shutil.move(str(nested_meta), dest_meta)
            print(f"[meta] Moved {nested_meta.name} -> citations/citation_mds/{name}/")
        else:
            print(f"[warn] meta.json not found at expected path: {nested_meta}", file=sys.stderr)

    print(
        f"Done. Total PDFs: {total}, processed: {processed}, skipped: {skipped}, failures: {failures}"
    )
    return 0 if failures == 0 else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# CLAUDE.md — Project conventions for Claude sessions

This file sits at the repository root and is read at the start of every
Claude session.  It describes the things that matter for working in this
repo from the Cowork / Windows sandbox, and points at the canonical
docs for everything else.

For repo intent and conventions that apply equally to Copilot and to
Claude, see [`.github/copilot-instructions.md`](.github/copilot-instructions.md)
— **read it first**.  This file only adds what is Claude-specific.

---

## What this repo is (one-liner)

A Python pipeline + locally cached metadata for curating OpenNeuro
datasets for HED annotation.  Discovers repos on GitHub, mirrors their
top-level files, summarises them, and extracts citation links.  The
citation-curation workstream is in active redesign — see
`.status/citation_id_design_v2.md` for the current spec.

---

## Repository layout (quick map)

```
src/                          pipeline scripts
datasets/
  dataset_repos/<dsXXXXXX>/   cached top-level files per dataset
  dataset_summaries/          all TSV/JSON pipeline outputs
  citations/
    citation_pdfs/            downloaded paper PDFs (manual)
    citation_mds/             marker-pdf converted Markdown
.status/                      working notes, plans, designs (read these)
.github/                      copilot-instructions.md + future workflows
tests/                        currently empty
```

`citations/` lives under `datasets/`, **not** at the repo root — some
older scripts still encode the wrong path.  See `.status/path_audit.md`.

---

## Where to look first in `.status/`

In rough order of "read this before changing anything":

| File                                       | What it is |
|--------------------------------------------|------------|
| `assessment.md`                            | What is broken / drifting |
| `plan.md`                                  | Phased action plan |
| `citation_id_design_v2.md`                 | Current citation-ID spec (cross-repo) |
| `citation_id_design.md`                    | v1 of the citation-ID spec (superseded; kept for diff) |
| `citation_issues_summary.md`               | Narrative of the citation-ID problem (v1) |
| `cross_repo_id_thinking_2026-05-01.md`     | Why v2 looks the way it does |
| `path_audit.md`                            | Hard-coded path bugs |
| `README.md`                                | Index of `.status/` itself |

When making non-trivial changes, **update the relevant `.status/` doc
in the same commit**.  These notes are the source of truth for in-flight
work; if they get stale, the next session repeats lost discussion.

---

## Cross-repo relationship — `task-research`

This repo's citations are intended to feed into the `task-research`
project (a separate repo, typically at `H:\Research\task-research` on
the maintainer's machine).  The bridge is the `pub_id` column described
in `citation_id_design_v2.md`:

- `task-research` defines the deterministic ID
  `pub_<8-hex-of-sha1(lastname+year+title)>` in
  `Claude-research/code/literature_search/identity.py`.
- This repo will copy that file verbatim into `src/citation_identity.py`
  and pin three known hashes in `tests/test_citation_identity.py`.
  Those tests catch any drift if either side is edited locally.

When working on the cross-repo path, read both
`citation_id_design_v2.md` (here) and the §11.7 / Phase 6 sections of
`task-research/Claude-research/instructions/literature_search_plan_2026-04-21.md`
(there).  Do not invent a third ID scheme.

---

## Session reporting

Every session that writes, moves, or deletes files must produce a
session report under `.status/`:

```
.status/session_YYYY-MM-DD_<short-topic>.md
```

Minimum content: what was done, what files changed, what decisions were
made, what's left for the next session.

Also write a thinking/design summary to `.status/` (same date
convention) for any non-trivial design decision.  These complement the
session report and explain the *why*.  The pattern in
`cross_repo_id_thinking_2026-05-01.md` is the reference template.

---

## Cowork / Windows sandbox quirks

The sandbox has two ways to read files, and they don't always agree.

### Use Read for workspace files (Windows path)
- Always shows current contents, including files just written by Write
  or Edit tools.
- Use for `.tsv`, `.json`, `.md` lookups in this repo.

### Use bash for code execution and system ops (Linux mount)
- Reads files via VirtioFS, which can show a stale snapshot of files
  just written by Write or Edit.
- Use bash for running Python, `wc`, `awk`, `diff`, `cp`, etc.  Do
  **not** use `cat` to fetch workspace file contents you'll then reason
  about — Read is safer.
- The Linux mount of this repo is
  `/sessions/<session-id>/mnt/openneuro-metadata/`.  The session ID
  changes between sessions; use `mcp__cowork__request_cowork_directory`
  to confirm.

### Write vs Edit
- **Write**: creates or fully rewrites a file.  Immediately visible to
  bash.
- **Edit**: targeted diff-style change.  May NOT be immediately visible
  to subsequent bash reads (cache lag).  Prefer Write for new files;
  use Edit for small in-place changes that bash doesn't need to read
  back immediately.

### Rule of thumb
```
Read  workspace files  →  Read tool (Windows path)
Write workspace files  →  Write or Edit (Windows path)
Run code / shell ops   →  bash (Linux mount path)
```

---

## Things to avoid (Claude-specific)

- **Do not hard-code absolute Windows paths** (e.g. `I:\RepositoryMetadata\…`,
  `C:\Users\…`) in committed files.  This applies to source, scripts,
  configs, docs, and `.status/` notes.  Use repo-relative paths or
  `pathlib` anchored at `Path(__file__).resolve().parent.parent`.
  Absolute paths are only acceptable in throw-away terminal commands.
- **Do not bulk-renumber `cit_######` IDs.**  v2 of the citation
  redesign is explicit: existing IDs survive the migration; the lowest
  ID per canonical key wins.  Numbers are not allowed to shift just
  because alphabetical or other orderings would be cleaner.
- **Do not edit `src/citation_identity.py` (once added).**  It is
  synced from `task-research`.  Edit upstream; copy here.
- **Do not commit `.env`, downloaded PDFs over a few MB, or anything
  under `outputs/cache/`.**

---

## When in doubt, ask

If a request requires reorganising directories, renaming columns in
`datasets/dataset_summaries/`, or introducing a third ID scheme,
**stop and ask** before writing code.  The pipeline is settling but
not yet stable, and the maintainer prefers small reversible changes.

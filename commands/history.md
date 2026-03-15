---
description: Browse past analyses and pipeline runs
argument-hint: "[search=<term>] [--all]"
---

# /history

## Analysis History

### Usage
- `/history` — list recent analyses (last 10)
- `/history {id}` — show full details for a specific analysis
- `/history search={term}` — search by title, question, or tags
- `/history --all` — list all analyses across all datasets

### Instructions

1. Read `.knowledge/analyses/index.yaml`. If empty: "No analyses archived yet."
2. Filter to active dataset unless `--all` flag.
3. Sort by date descending.

**List:** Show table: date, title, level, key finding count, dataset. "Showing 10 of {total}."

**Detail (`/history {id}`):** Show title, date, question, level, all key findings, metrics used, agents used, output files, confidence.

**Search:** Case-insensitive search across title, question, key_findings, tags.

After displaying, suggest: "Re-run with fresh data?" or "Build on finding #N?"

## Pipeline Runs

### Usage
- `/runs` or `/runs list` — list all pipeline runs
- `/runs latest` — most recent run details
- `/runs {id}` — specific run details (partial match supported)
- `/runs clean` — remove runs older than 30 days (confirmation required)
- `/runs compare {id1} {id2}` — side-by-side comparison

### Instructions

1. Scan `working/runs/` — each subdirectory is a run named `{YYYY-MM-DD}_{DATASET}_{TITLE}/`
2. Read `pipeline_state.json` from each for: pipeline_id, dataset, question, status, timing, agent counts.

**List:** Table sorted by date: #, Date, Dataset, Title, Status, Agents (completed/total).

**Detail:** Show directory name, status, dataset, question, timing, agent status map (completed/failed/skipped/pending), output files, confidence grade.

**Clean:** List runs >30 days old, require confirmation before deletion.

**Compare:** Load both runs' state. Show table: Date, Dataset, Status, Agents, Confidence, Charts, Findings, Duration.

## Edge Cases
- No archive → "No analyses archived. Complete one first."
- No runs directory → "No pipeline runs found. Use `/run-pipeline`."
- Corrupted state → Show with `status: unknown`
- Partial match ambiguity → List matches, ask user to be specific

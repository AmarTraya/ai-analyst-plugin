---
description: End-to-end analysis — from business question to validated slide deck
argument-hint: "<question>"
---

# /run-pipeline

## Usage

```
/run-pipeline <question>
/run-pipeline question="..." data_path=... [theme=analytics|analytics-dark] [audience=...]
/run-pipeline plan=deep_dive|quick_chart|refresh_deck|validate_only
/run-pipeline dry-run=true
```

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `question` | Yes | — | Business question to answer |
| `data_path` | Yes | — | Path to CSV, parquet, or data directory |
| `theme` | No | `analytics` | `analytics` (light) or `analytics-dark` |
| `audience` | No | `senior stakeholders` | Controls content density |
| `plan` | No | `full_presentation` | Execution plan (see Plans below) |
| `context` | No | `stakeholder readout` | `workshop`, `talk`, `team standup` |

## Workflow

### Phase 1: Frame the Question

1. Parse business question into the Question Ladder: goal → decision → metric → hypothesis
2. Generate 3+ testable hypotheses across cause categories (product, technical, external, mix shift)
3. Create analysis design spec: question, decision, data needed, dimensions, time range, output format, success criteria
4. **Output:** `outputs/question_brief_{DATE}.md`, `outputs/hypothesis_doc_{DATE}.md`

**Checkpoint 1 (user-facing):** Review framing before proceeding. Skip if user said "just do it."

### Phase 2: Explore & Verify Data

1. Profile schema via `helpers/schema_profiler.py` — tables, columns, types, row counts
2. Run data quality checks: completeness, consistency, coverage, statistical sanity (use data-exploration skill)
3. Classify issues as BLOCKER/WARNING/INFO. **HALT on any BLOCKER.**
4. Run source tie-out: compare pandas direct-read vs DuckDB SQL on row counts, nulls, numeric sums. **HALT on mismatch.**
5. **Output:** `outputs/data_inventory_{DATE}.md`, `working/tieout_{DATASET}.md`

### Phase 3: Analyze

1. Run segmentation, funnel decomposition, trend detection (descriptive analytics or overtime/cohort agent)
2. Drill iteratively through dimensions for root cause until reaching a specific, actionable cause
3. Apply triangulation skill: segment-first Simpson's check, internal consistency, cross-reference, plausibility
4. Assign confidence grade (A-F) via 4-layer validation
5. Estimate business impact with sensitivity ranges (opportunity sizer)
6. **Output:** `outputs/analysis_report_{DATE}.md`, `working/investigation_{DATASET}.md`, `outputs/validation_{DATASET}_{DATE}.md`

**Checkpoint 2 (automated):** Verify tie-out passed, root cause is specific, findings validated, opportunity sized.

### Phase 4: Build Story & Charts

1. Design storyboard with Context → Tension → Resolution arc
2. Map each narrative beat to a visual format and HTML component type
3. Review storyboard coherence — verify no gaps before charting
4. Generate charts: `swd_style()`, `(10,6)` figsize, action titles, direct labels
5. Review each chart against SWD checklist. Fix loop: APPROVED → continue, APPROVED WITH FIXES → re-generate listed charts (1 iteration max), NEEDS REVISION → HALT
6. **Output:** `working/storyboard_{DATASET}.md`, `outputs/charts/*.png`

**Checkpoint 3 (automated):** Verify R2 (title≠headline), R3 (backgrounds), R5 (no banned words), R7 (figsize).

### Phase 5: Create Deck

1. Read `templates/marp_components.md` for the HTML component library
2. Read `templates/deck_skeleton.marp.md` for deck structure
3. Write stakeholder narrative (Storytelling agent + Stakeholder Communication skill)
4. Build Marp deck with ≥3 HTML component types, speaker notes, correct theme
5. Frontmatter must include: `marp`, `theme`, `size`, `paginate`, `html`, `footer`
6. Run `helpers/marp_linter.py` to validate
7. **Output:** `outputs/deck_{DATASET}_{DATE}.marp.md`

**Checkpoint 4 (automated):** Verify R1 (theme), R2, R3, R4 (rec order), R5, R6 (breathing slides every 3-4), R7, R10 (HTML components), deck 8-22 slides, speaker notes, lint pass.

### Phase 6: Export & Close

1. Export PDF and HTML via `helpers/marp_export.py` (non-blocking — skip if Marp CLI unavailable)
2. Archive analysis to `.knowledge/analyses/index.yaml`
3. **Output:** `outputs/deck_{DATASET}_{DATE}.pdf`, `outputs/deck_{DATASET}_{DATE}.html`

## Rules (Non-Negotiable)

| # | Rule |
|---|------|
| R1 | Theme default is light. Dark only for workshop/talk or explicit override. |
| R2 | Chart title ≠ slide headline. Chart title = data claim. Headline = narrative. |
| R3 | Chart background is `#F7F6F2`. Verify `swd_style()` called. |
| R4 | Recommendations ordered by confidence: High → Medium → Low. |
| R5 | Banned words in headlines: surgical, devastating, exploded, ticking time bomb, smoking gun, unprecedented, unleash, supercharge, game-changing, skyrocketed. |
| R6 | Breathing slide every 3-4 insight slides. Classes: `impact`, `dark-impact`, `section-opener`, `takeaway`. |
| R7 | Charts at `(10, 6)` figsize, 150 DPI. CSS `object-fit: contain` handles containment. |
| R8 | Read agent files from disk at each phase. Do not rely on cached knowledge. |
| R9 | Source tie-out before analysis. HALT on mismatch. |
| R10 | Marp decks must use ≥3 HTML component types. Plain-markdown-only insight slides are a failure. |
| R11 | Export both PDF and HTML after Checkpoint 4. Non-blocking if Marp CLI unavailable. |

## Plans

| Plan | When | What Runs |
|------|------|-----------|
| `full_presentation` | End-to-end | All phases |
| `deep_dive` | Analysis without deck | Phases 1-3 only |
| `quick_chart` | Just a chart | Phase 4 chart generation + review |
| `refresh_deck` | Re-do presentation | Phases 4-5 (reuses analysis) |
| `validate_only` | Re-check existing work | Validation only |

## Resume

If a previous run was interrupted, read `working/pipeline_state.json` (or `working/latest/pipeline_state.json`) to identify completed phases. Reset failed/interrupted agents to pending. Compute READY set from dependency graph. Continue from the next ready agent.

Present resume plan before executing:
```
Resuming pipeline {run_id}
Completed: {list}
Will retry: {list}
Next: {ready agents}
```

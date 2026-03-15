---
description: Interactive onboarding — configure profile, data, business context, and preferences
argument-hint: "[status] [reset] [reset everything]"
---

# /setup

4-phase conversational interview that populates the knowledge system from the user's context.

## Design Principles

1. **Conversational, not interrogative** — react to answers, weave context forward
2. **2-3 questions at a time** — never dump all questions at once
3. **Validate responses** — confirm paths exist, normalize synonyms
4. **Allow skipping** — optional fields accept "skip" or "later"
5. **Show progress** — summary after each phase

## State File

`.knowledge/setup-state.yaml` tracks phase completion status.

## Phase 1: Role & Team

Ask (in 1-2 groups):
1. Role (PM, DS, Engineer, Analyst, exec)
2. Technical level (Beginner / Intermediate / Advanced)
3. Team/department (optional)
4. Domain (e-commerce, SaaS, fintech, etc.) (optional)

Write to `.knowledge/user/profile.md`. Map synonyms: "PM"→Product Manager, "DS"→Data Scientist.

## Phase 2: Data Connection

Ask: CSV files / DuckDB / Cloud warehouse / Sample dataset?

- **CSV:** Ask path, verify exists, invoke `/connect-data type=csv`
- **DuckDB:** Ask path, verify, invoke `/connect-data type=duckdb`
- **Cloud:** Route to `/connect-data`, mark phase as `partial`
- **Sample:** List `data/examples/`, let user pick

Don't block on partial — continue to Phase 3.

## Phase 3: Business Context

Ask (in 2-3 groups):
1. Company/product description
2. Top 2-3 metrics
3. Current business question (optional)
4. OKRs/goals (optional)
5. Key segments (optional)
6. Seasonality (optional)

Write to `.knowledge/user/business-context.md`. Seed metric stubs if dataset connected.

## Phase 4: Preferences

Ask:
1. Detail level: Executive summary / Standard / Deep dive
2. Chart preference: Minimal / Standard / Chart-heavy
3. Sharing format: Deck / Email / Slack / Brief / Notebook (optional)
4. Anything else (optional)

Update profile.md with Communication Preferences section.

## Setup Complete

```
=== SETUP COMPLETE ===
Role: {role} ({tech_level})  |  Data: {dataset} — {N} tables
Key metrics: {list}  |  Detail: {level}  |  Charts: {pref}

Get started: Ask a question, /explore, or /run-pipeline
```

## Subcommands

### `/setup status`
Read `.knowledge/setup-state.yaml`, show phase completion table.

### `/setup reset`
Tier 1: Clear profile + preferences (Phase 1 & 4). Keeps data connections. Confirmation required.

### `/setup reset everything`
Tier 2: Clear everything — profile, business context, dataset connections. User must type `reset everything` to confirm.

## Resume Logic

If setup-state.yaml exists: find first pending phase, resume from there. If all complete: "Setup is already complete. Use `/setup status` or `/setup reset`."

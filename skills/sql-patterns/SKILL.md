---
name: sql-patterns
description: Retrieve proven SQL patterns and table cheatsheets from query archaeology before writing new queries. Use automatically before any analysis agent writes SQL.
---

# SQL Patterns & Query Archaeology

## When to Use
- **Automatically** before any analysis agent writes SQL (pre-flight step)
- **Manually** when asking about known patterns for a table or join

## Instructions

### Step 1: Check the Index

Read `.knowledge/query-archaeology/curated/index.yaml`. Parse counters: `cookbook_entries`, `table_cheatsheets`, `join_patterns`.

**If all three are zero (or missing), stop here.** Return nothing, do not mention archaeology.

### Step 2: Identify Search Terms

From the current analysis context, extract:
- **Table names** the agent is about to query (e.g., `orders`, `events`)
- **Query intent tags** (e.g., `funnel`, `retention`, `revenue`, `cohort`)

### Step 3: Search the Three Stores

Match using case-insensitive substring.

**Cookbook** (`curated/cookbook/*.yaml`): Match `tables` or `tags` arrays. Extract: `title`, `sql`, `tables`, `tags`, `caveats`.

**Table Cheatsheets** (`curated/tables/*.yaml`): Match `table_name`. Extract: `table_name`, `grain`, `primary_key`, `common_filters`, `gotchas`, `common_joins`.

**Join Patterns** (`curated/joins/*.yaml`): Match if ≥2 `tables` match search terms. Extract: `tables`, `join_sql`, `cardinality`, `notes`, `validated`.

### Step 4: Format & Hand Off

Return matched entries as context block. The analysis agent should prefer archaeology SQL over writing from scratch and respect any gotchas listed.

## Rules
1. Never mention archaeology when the store is empty — silent skip
2. Never require exact matches — always substring
3. Never load all files eagerly — check index counts first
4. Never modify archaeology files — read-only
5. Never block analysis if retrieval fails — archaeology is additive

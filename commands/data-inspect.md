---
description: Inspect active dataset schema, list all datasets, or switch the active dataset
argument-hint: "[table] | list | switch <name>"
---

# /data-inspect

## Schema Inspection

### `/data` — Full schema overview
1. Read `.knowledge/active.yaml` for the active dataset
2. Read `.knowledge/datasets/{active}/schema.md`
3. Display condensed summary: table name, row count, column count, primary key

### `/data {table}` — Table detail
1. Find the table section in schema.md
2. Show full column listing with types and descriptions
3. Show key relationships (FKs to/from this table)

### `/data` with no active dataset
"No active dataset. Run `/connect-data` to connect one, or `/data list` to see available options."

## Dataset Listing

### `/data list` or `/datasets`
1. Read `data_sources.yaml` for registered sources
2. Read `.knowledge/active.yaml` for active pointer
3. For each source, check `.knowledge/datasets/{name}/manifest.yaml` for summary stats

Display:
```
Connected Datasets:
  * active_dataset (active)
    Display Name — N tables, date_range
    Connection: type (database)
  - other_dataset
    Display Name — N tables
    Connection: type (details)
```

Mark active with `*`, others with `-`.

## Rules
1. Never query the database just to show schema — read from cached schema.md
2. Never show connection credentials — type and database only
3. Never show the full schema.md raw — format into condensed table view

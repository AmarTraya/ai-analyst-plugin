---
description: Browse organization knowledge — glossary, metrics, products, teams, objectives
argument-hint: "[glossary|products|metrics|objectives|teams|lookup <term>]"
---

# /business

Interactive browser for your organization's knowledge system.

## Prerequisites
- Organization context at `.knowledge/organizations/{org}/`
- If none: "No organization context found. Run `/setup` Phase 3."

## Subcommands

### `/business` — Overview
Display summary: glossary term count, products, metrics, objectives, teams.
Use `helpers/business_context.py` → `load_business_context(org_path)`.

### `/business glossary`
Load `business/glossary/terms.yaml`. Sort alphabetically. Show first 20, offer "Show all" if more.

### `/business products`
Load `business/products/index.yaml`. Display: Product, Category, Status, Key Metrics.

### `/business metrics`
Load `business/metrics/index.yaml`. Cross-reference with `.knowledge/datasets/{active}/metrics/`. Show definition, type, owner.

### `/business objectives`
Load `business/objectives/index.yaml`. Show: Objective, Key Results, Status (On Track / At Risk / Behind).

### `/business teams`
Load `business/teams/index.yaml`. Show: Team, Lead, Focus Area, Analysts.

### `/business lookup {term}`
Search all categories (case-insensitive substring). Rank: exact > starts-with > contains. Show top 10 with category badge.

## Display Rules
- Tables for structured data (align columns)
- Limit initial display to 20 rows with pagination
- Show file paths so users know where to edit
- Adapt detail: summary for `/business`, detail for subcommands

## Error Handling
- Missing org → suggest `/setup`
- Empty categories → show "how to add" with file path
- Malformed YAML → show parse error

---
name: data-exploration
description: Profile datasets, assess data quality, and compare across sources. Use when encountering new data, checking quality before analysis, or comparing datasets.
---

# Data Exploration

Systematic methodology for profiling datasets, assessing data quality, and comparing data sources.

## Data Profiling

### Step 1: Profile Schema

```python
from helpers.data_helpers import get_connection_for_profiling
from helpers.schema_profiler import profile_source

conn_info = get_connection_for_profiling()
schema = profile_source(conn_info)
```

Identify: tables and row counts, date columns, numeric columns, null rates.

### Step 2: Deep Profile per Table

```python
from helpers.data_helpers import read_table
from helpers.deep_profiler import (
    profile_distributions, profile_temporal_patterns, profile_completeness,
)

for table_info in schema["tables"]:
    df = read_table(table_info["name"])
    if len(df) > 100_000:
        df = df.sample(n=100_000, random_state=42)
    distributions = profile_distributions(df)
    completeness = profile_completeness(df)
    if table_info.get("date_columns"):
        temporal = profile_temporal_patterns(df, table_info["date_columns"][0], freq="D")
```

### Step 3: Correlations & Anomalies

Run on tables with key business metrics (revenue, counts, rates):

```python
from helpers.deep_profiler import profile_correlations, profile_anomalies
correlations = profile_correlations(df, threshold=0.5)
# Aggregate to daily before anomaly detection — never run on raw event rows
anomalies = profile_anomalies(daily_df, date_col=primary_date, metric_cols=metric_cols, window=14)
```

### Step 4: Write Profile Report

Write to `.knowledge/datasets/{active}/last_profile.md` with severity summary.

## Data Quality Check

Run these checks in order at the start of every analysis. Stop on BLOCKERs.

### 1. Completeness

- Null rates per column (SQL or pandas)
- Missing date ranges for time-series data
- Unexpected zeros in numeric columns

### 2. Consistency

- Duplicate primary keys
- Referential integrity (FK → PK)
- Date format consistency, casing inconsistency

### 3. Coverage

```python
from helpers.sql_helpers import check_temporal_coverage, check_value_domain
coverage = check_temporal_coverage(df, "order_date", freq="D")
domain = check_value_domain(df["device_type"], ["desktop", "mobile", "tablet"])
```

### 4. Statistical Sanity

```python
from helpers.tieout_helpers import check_null_concentration, check_outliers
null_results = check_null_concentration(df)
for col in numeric_columns:
    check_outliers(df[col], method="iqr")
```

Check for impossible values (negative revenue, rates >100%, future dates).

### 5. Data Freshness

Infer cadence from median gap between consecutive dates. Flag if stale relative to cadence.

## Severity Classification

| Severity | Condition |
|----------|-----------|
| **BLOCKER** | >50% nulls in key metric, PK has nulls/dupes, entire date ranges missing, coverage <50%, impossible values |
| **WARNING** | 5-50% nulls, mixed date formats, coverage 50-95%, extreme outliers, stale data |
| **INFO** | <5% nulls, minor casing issues, weekend gaps in business-day data |

## Output Format

```markdown
# Data Quality Report: [Dataset]
## Summary
| Severity | Count | Details |
| BLOCKER  | X     | ...     |
| WARNING  | X     | ...     |
| INFO     | X     | ...     |

## Recommendation
PROCEED / PROCEED WITH CAUTION / BLOCKED
```

## Cross-Dataset Comparison

When comparing datasets (`/compare-datasets`):
1. Enumerate `.knowledge/datasets/` — require at least 2
2. Build union of metric IDs, identify shared vs. dataset-specific
3. Compare definitions, typical ranges, guardrail alignment
4. Flag discrepancies and generate cross-dataset observations
5. Write to `.knowledge/global/cross_dataset_observations.yaml`

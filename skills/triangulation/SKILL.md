---
name: triangulation
description: Cross-reference findings against multiple sources, detect common analytical errors, and run 4-layer validation with confidence scoring. Use after every analysis before presenting to stakeholders.
---

# Triangulation & Validation

## Triangulation Framework

Every finding gets checked through four lenses:

```
CHECK 0: SEGMENT-FIRST  → Simpson's Paradox check (MANDATORY)
CHECK 1: INTERNAL        → Do the numbers add up?
CHECK 2: CROSS-REFERENCE → Does another data source agree?
CHECK 3: PLAUSIBILITY    → Does this make sense?
```

### Check 0: Segment-First (Mandatory)

Run BEFORE accepting any aggregate finding. Default segments to check:
1. Platform/device  2. User type/plan tier  3. Geography  4. Acquisition channel

For each aggregate finding: compute metric at aggregate AND segment level. If ANY segment shows the **opposite** trend → flag Simpson's Paradox. Report segment-level findings instead.

### Check 1: Internal Consistency

- Percentages sum to 100% (±1%)?
- Segment sums equal total?
- Funnel monotonically decreasing?
- Rates between 0-100%?
- Denominator stable? (a "drop" in conversion might be a traffic spike)

### Check 2: Cross-Reference

- Calculate the same thing two different ways
- If conversion rate went up, did absolute conversions also go up?
- Does daily data sum to weekly?

### Check 3: External Plausibility

| Metric | Typical Range |
|--------|--------------|
| SaaS free→paid conversion | 2-5% |
| E-commerce conversion | 1-4% |
| Email open rate | 15-30% |
| Monthly churn (SaaS) | 3-8% |
| DAU/MAU ratio (B2B SaaS) | 10-25% |
| NPS (good SaaS) | 20-50 |
| Bounce rate | 40-60% |

## Common Analytical Errors

| Error | How to Check |
|-------|-------------|
| **Simpson's Paradox** | Check aggregate vs. segments — if they disagree, investigate segment sizes |
| **Survivorship Bias** | Ask "what's NOT in this dataset?" — churned users, failed transactions? |
| **Incomplete Windows** | Verify data range is complete — don't compare full January to partial February |
| **Denominator Changes** | Look at numerator AND denominator separately before interpreting ratios |
| **Correlation ≠ Causation** | Look for confounders, ask "what else changed?" |

## 4-Layer Semantic Validation

### Layer 1: Structural
```python
from helpers.structural_validator import validate_schema, validate_primary_key, validate_completeness
```
FAIL → BLOCKER (halt analysis)

### Layer 2: Logical
```python
from helpers.logical_validator import validate_aggregation_consistency, validate_trend_continuity
```
FAIL → WARNING (check calculations)

### Layer 3: Business Rules
```python
from helpers.business_rules import validate_ranges, validate_rates, validate_yoy_change
```
FAIL → WARNING (explain outliers)

### Layer 4: Simpson's Paradox
```python
from helpers.simpsons_paradox import check_simpsons_paradox, scan_dimensions
```
FAIL → BLOCKER (disaggregate findings)

## Confidence Scoring

```python
from helpers.confidence_scoring import score_confidence, format_confidence_badge
score = score_confidence(validation_results)
badge = format_confidence_badge(score)  # "A (92/100)" or "C (58/100) — 2 warnings"
```

Include badge in executive summary and synthesis slide.

## Validation Report Output

```markdown
# Validation Report: [Analysis Name]
### Overall Confidence: [HIGH / MEDIUM / LOW]

### Finding-by-Finding Validation
| Check | Result | Detail |
| Internal consistency | PASS/WARN/FAIL | ... |
| Cross-reference | PASS/WARN/FAIL | ... |
| External plausibility | PASS/WARN/FAIL | ... |
| Analytical errors | PASS/WARN/FAIL | ... |
| **Confidence** | **HIGH/MEDIUM/LOW** | ... |

### Caveats for Stakeholders
### Recommended Additional Validation
```

---
name: metric-definition
description: Define metrics clearly with standardized templates and guardrail pairing. Use when defining new metrics, resolving ambiguous metric names, or checking that success metrics have guardrails.
---

# Metric Definition & Guardrails

## Metric Spec Template

```markdown
## Metric: [Name]

### Definition
**Plain English:** [One sentence a non-technical person can understand]
**Formula:** [Exact calculation]

### Components
| Component | Definition | Source |
| **Numerator** | [What's counted/summed] | [Table.column] |
| **Denominator** | [Bottom of ratio, if applicable] | [Table.column] |
| **Unit of analysis** | [per user, per session, per order] | |

### Segmentation Dimensions
| Dimension | Values | Why |

### Data Source
- **Primary table:** [schema.table]
- **Key columns:** [list]
- **Refresh cadence / Latency**

### Thresholds
| Condition | Value | Action |
| Healthy | ... | No action |
| Watch | ... | Monitor weekly |
| Investigate | ... | Root cause within 48h |
| Alert | ... | Immediate escalation |

### Known Limitations
- [Each caveat that affects interpretation]

### Driver Decomposition (Optional)
Revenue = Active Users × Orders per User × AOV
[Table: Driver | Formula | Relationship | Source]
```

## Writing Rules

1. **Definition must be unambiguous** — two analysts should write the same SQL
2. **Always specify the denominator** — "conversion rate" alone is meaningless
3. **Always specify the time window** — DAU daily ≠ DAU 7-day average
4. **Always specify exclusions** — test accounts, bots, internal users
5. **Thresholds based on historical data** — not gut feel

## Auto-Registration

After writing a spec, register in `.knowledge/datasets/{active}/metrics/`:
1. Generate ID from name (lowercase, hyphens)
2. Write `{id}.yaml` with definition, source, dimensions, guardrails
3. Update `index.yaml`

## Guardrails

A **guardrail metric** must not degrade while optimizing a success metric.

### Common Guardrail Pairs

| Success Metric | Guardrail(s) |
|---------------|-------------|
| Conversion rate | AOV, Return rate |
| Signup rate | Activation rate, 7-day retention |
| Revenue per user | NPS/CSAT, Support ticket volume |
| Feature adoption | Core workflow completion |
| Speed (time to complete) | Error rate, Quality score |
| Engagement (DAU) | Revenue per user, Churn rate |

### Guardrail Check Process

Before presenting any "[metric] improved by X%":

1. Identify guardrail metric(s)
2. Compute guardrail over the same time period
3. Compare to baseline/acceptable range
4. Assign verdict:

| Verdict | Status | How to Present |
|---------|--------|----------------|
| **CLEAR** | Guardrail stable/improved | Present as a win |
| **TRADE-OFF** | Guardrail degraded <10% | Present improvement AND trade-off with net impact |
| **DEGRADED** | Guardrail degraded >10% | Do NOT present as a win — flag for investigation |

When degraded: quantify both sides in the same units, compute net impact, flag delayed effects, recommend investigation.

---
name: question-framing
description: Structure analytical questions using the Question Ladder framework and create analysis design specs. Use when starting any analysis, when questions are vague, or when analysis lacks decision context.
---

# Question Framing & Analysis Design

## The Question Ladder

Every analytical question climbs four rungs:

```
GOAL        → What business outcome are we trying to achieve?
DECISION    → What specific decision will this analysis inform?
METRIC      → What will we measure to inform that decision?
HYPOTHESIS  → What do we expect to find, and why?
```

**Rule:** Never start analyzing data until you can state all four rungs.

## Framing Process

1. **Extract the decision** — "What will you DO differently based on the answer?" If "nothing" → redirect to reporting.
2. **Define success criteria** — Specific conditions, not vague understanding goals.
3. **Form testable hypotheses** — "I think X happened because Y" not "I think things are bad."
4. **Identify data requirements** — Map each hypothesis to metrics, segments, time ranges. Flag gaps early.

## Good vs. Bad Questions

| Bad | Problem | Good |
|-----|---------|------|
| "How are our users doing?" | No decision context | "Did the onboarding redesign improve Day-7 retention?" |
| "Analyze our funnel" | No hypothesis or scope | "Where in signup-to-purchase are we losing users, by channel?" |
| "What's our conversion rate?" | Reporting, not analysis | "Why did conversion drop 15% in March, across segments?" |

## Impact × Feasibility

When multiple questions emerge, prioritize by:
- **High impact:** Revenue >$100K, affects >10% users, informs this-quarter decision
- **High feasibility:** Data exists and clean, answerable in <4 hours
- **Do first:** High impact + high feasibility. **Skip:** Low impact + low feasibility.

## Analysis Design Spec

Before touching data, fill in all 7 fields:

```markdown
## Analysis Design Spec
### 1. Question — [Specific, testable]
### 2. Decision — [Concrete action informed by this]
### 3. Data Needed — [Table with: Data | Source | Available? | Notes]
### 4. Dimensions — [2-4 segmentation dimensions with justification]
### 5. Time Range & Granularity — [Period, granularity, comparison]
### 6. Output Format — [Quick answer | Analysis report | Deck | Data table]
### 7. Success Criteria — [Falsifiable conditions]
```

### Scope Calibration

| Request Type | Depth | Typical Agents | Time |
|-------------|-------|----------------|------|
| Number pull | Single stat | Data Explorer only | Minutes |
| Monitoring | Trend check | Overtime/Trend | 15-30 min |
| Exploration | Open investigation | Descriptive Analytics | 30-60 min |
| Deep dive | Root cause | Full pipeline | 1-2 hours |

## Question Brief Output

```markdown
# Question Brief: [Title]
## Date: [YYYY-MM-DD]

### Business Context
[2-3 sentences]

### The Question Ladder
| Rung | Statement |
| Goal | ... |
| Decision | ... |
| Metric | ... |
| Hypothesis | ... |

### Success Criteria
[Specific thresholds or conditions]

### Data Requirements
[Table: Data | Source | Available? | Notes]

### Scope
- Time range, Segments, Exclusions

### Priority
- Impact, Feasibility, Recommendation
```

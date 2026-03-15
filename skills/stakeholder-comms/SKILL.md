---
name: stakeholder-comms
description: Adapt findings to the audience and ensure every recommendation has a follow-up plan. Use when producing narratives, decks, or any stakeholder-facing output.
---

# Stakeholder Communication & Close the Loop

## The Stakeholder Matrix

| Dimension | Executive | Product Team | Engineering | Data Team |
|-----------|----------|-------------|-------------|-----------|
| **Lead with** | Business impact ($, users) | What to do about it | What's broken and where | How we found it |
| **Detail level** | Bottom line + 1 fact | Findings + next steps | Root cause + fix scope | Methodology + caveats |
| **Format** | 3 slides / 1 paragraph | Report with charts | Investigation log | Full report + validation |
| **Metrics** | Revenue, growth rate | Conversion, retention | Error rate, latency | Significance, CI |
| **Recommendation** | "We should X" | "I recommend X because Y" | "Fix is X, effort Y" | "Data supports X, caveats Y" |

## How to Adapt

1. **Identify audience** — signals: "for leadership" → Executive; "what to do?" → Product; "root cause?" → Engineering; "how confident?" → Data
2. **Select the lead** — same finding, different first sentence per audience
3. **Calibrate detail** — pyramid principle: conclusion first, add depth per audience level
4. **Adapt recommendation style** — decisive for exec, reasoned for PM, scoped for eng, qualified for data

## Multi-Audience Documents

1. Executive Summary (3-5 sentences, bottom line first)
2. Key Findings for Product
3. Technical Details for Engineering
4. Methodology for Data

Label sections clearly so readers jump to their level.

## Close the Loop

Append to every analysis with a recommendation:

```markdown
## Close the Loop

### Decision
- **Recommendation:** [What the analysis recommends]
- **Decision maker:** [Who — name or role]
- **Decision deadline:** [When]

### Success Tracking
- **Success metric:** [What tells us it worked]
- **Current baseline:** [Value today]
- **Target:** [Expected value if recommendation works]
- **Measurement window:** [How long before evaluation]

### Follow-Up
- **Check-in date:** [When to evaluate]
- **Owner:** [Who checks]
- **If successful:** [Next step]
- **If unsuccessful:** [Fallback plan]
- **If inconclusive:** [What additional data/time needed]

### Analysis Provenance
- **Date / Analyst / Key assumptions / Confidence / What would change the recommendation**
```

### Why Each Field Matters

| Field | Why |
|-------|-----|
| Decision maker | Without an owner, recommendations float |
| Decision deadline | Insights have a shelf life |
| Success metric | Can't tell if recommendation worked without one |
| Baseline | "Improved" means nothing without "from what?" |
| Target | Any change looks like success without a bar |
| If unsuccessful | Pre-commit to fallback to avoid sunk-cost rationalization |

### What You Fill In (as analyst)

Recommendation, success metric, baseline, target, measurement window, key assumptions, confidence, what would change recommendation.

### What User Must Fill In (prompt them)

Decision maker, decision deadline, follow-up owner, check-in date.

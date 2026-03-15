---
name: visualization
description: Create charts following SWD methodology and build slide decks with consistent themes. Use when generating any chart, graph, or presentation.
---

# Visualization & Presentation

## SWD Chart Methodology

> Gray everything first. Color is reserved for the one data point that tells the story.

- Maximum **2 colors + gray** per chart. Action Amber (`#D97706`) for focus, Accent Red (`#DC2626`) for secondary.
- **Titles state the takeaway** — "iOS drove the June spike" not "Tickets by Platform"
- Prefer text over charts for single numbers. Prefer horizontal bars over pie charts. Prefer direct labels over legends.

### Always Apply SWD Style

```python
from helpers.chart_helpers import swd_style, highlight_bar, highlight_line, action_title, save_chart
colors = swd_style()  # Loads .mplstyle + returns color palette
```

### Declutter Checklist

- [ ] Chart border/box — removed
- [ ] Top and right spines — removed
- [ ] Heavy gridlines — light gray y-axis only or none
- [ ] Data markers — removed from line charts
- [ ] Legend — replaced with direct labels
- [ ] Rotated axis text — switch to horizontal bars instead
- [ ] Background — warm off-white `#F7F6F2`
- [ ] Trailing zeros — `$45` not `$45.00`, `12%` not `12.0%`
- [ ] 3D effects — never
- [ ] Max 4-6 tick marks

### Chart Type Selection

| Data Relationship | Chart Type |
|---|---|
| Comparison (≤12 categories) | Vertical bar |
| Comparison (>7 / long labels) | Horizontal bar |
| Parts of whole | Stacked bar |
| Change over time (continuous) | Line chart |
| Change over time (discrete) | Bar chart |
| Correlation | Scatter plot |
| Distribution | Histogram |
| Flow/process | Funnel chart |
| Intensity (2 dimensions) | Heatmap |
| Contributions | Waterfall chart |

### Chart Sequencing

Follow **Context → Tension → Resolution** for multi-chart analyses:
- Context (1-2 charts): Set the baseline
- Tension (2-3 charts): Reveal and zoom into the problem
- Resolution (1-2 charts): Explain why, recommend action

## Presentation Themes

### Slide Structure

Every deck follows: `Title → Executive Summary → Context → Insights → Synthesis → Recommendations → Appendix`

### Content Density Rules

1. Max 3 bullet points per slide
2. One chart per slide
3. Headlines are takeaways, not labels
4. No full sentences in bullets — fragments with key numbers
5. 5-8 slides for 10 min, 10-15 for 30 min
6. The "headline test": headlines read in sequence should tell the complete story

### Theme: `analytics` (light — default)

- Title: Inter/system sans-serif Bold 36pt, `#1F2937`
- Body: 16pt, `#4B5563`
- Accent: `#D97706` (amber)
- Background: `#F7F6F2`, Surface: `#FFFFFF`
- 3px amber left border on every slide
- Marp CSS: `themes/analytics-light.css`
- Components: `.metric-callout`, `.kpi-row > .kpi-card`, `.finding`, `.chart-container`, `.rec-row`, `.callout`, `.so-what`, `.delta`, `.badge`, `.data-source`
- Slide variants: `insight`, `chart-left`, `chart-right`, `impact`

### Theme: `analytics-dark` (for workshops/talks)

- Background: `#1A1A17`, Surface: `#222220`
- Text: `#F5F5F0`, Accent: `#D97706`
- Marp CSS: `themes/analytics-dark.css`
- Slide variants: `dark-title`, `dark-impact`, `two-col`, `diagram`, `insight`, `chart-left`, `chart-right`

### Automatic Theme Selection

| Condition | Theme |
|-----------|-------|
| Explicit `theme=` | Use as-is |
| Context is "workshop"/"talk" | `analytics-dark` |
| Marp (no context) | `analytics` (light) |
| Otherwise | `corporate` |

### Font Size Minimums

| Element | Minimum |
|---------|---------|
| h1 (title slides) | 48px |
| h1 (content) | 44px |
| Body/paragraphs | 24px |
| List items | 22px |
| Nothing except footers | below 16px |

### Marp Export

```bash
npx @marp-team/marp-cli --no-stdin --pdf --html --allow-local-files \
  --theme themes/analytics-light.css deck.marp.md -o deck.pdf
```

### Anti-Patterns (Banned)

| Anti-Pattern | Use Instead |
|-------------|-------------|
| Pie charts | Horizontal bar chart |
| Rainbow palettes | Gray + 1 highlight color |
| Spaghetti lines | `highlight_line()` |
| Dual y-axes | Two separate charts |
| 3D charts | Flat 2D |
| Descriptive titles | Action titles |
| Legend boxes | Direct labels |
| Default matplotlib style | Always `swd_style()` |

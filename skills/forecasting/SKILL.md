---
name: forecasting
description: Generate time-series forecasts using naive baselines, seasonality detection, and exponential smoothing. Use when projecting metrics forward or sizing opportunities.
---

# Forecasting

## When to Use
- "What will revenue look like next month?" or "forecast DAU"
- After trend analysis reveals a pattern worth projecting
- When sizing opportunities that depend on future values

## Instructions

### Step 1: Prepare Data
1. Identify metric and source table from metric dictionary
2. Query aggregated to appropriate granularity (daily/weekly/monthly)
3. Create pandas Series with DatetimeIndex
4. Clean: forward-fill NaN, drop leading nulls
5. Require at least 14 data points

### Step 2: Detect Seasonality
Run `detect_seasonality()` from `helpers/forecast_helpers.py`. Store dominant period.

### Step 3: Generate Forecasts
Run multiple methods and compare MSE:
1. **Naive (last value):** `naive_forecast(series, periods, method='last')`
2. **Naive (seasonal):** `naive_forecast(series, periods, method='seasonal_naive')`
3. **Exponential smoothing:** `exponential_smoothing(series)`
4. **Holt-Winters:** `exponential_smoothing(series, seasonal_period=dominant_period)` (if seasonality detected)

### Step 4: Chart
1. `swd_style()` → solid line for history, dashed for forecast
2. Confidence band (±1 std residuals) as shaded area
3. Vertical dashed line at historical/forecast boundary
4. `action_title()` with forward-looking title
5. Save to `working/forecast_{metric}_{DATE}.png`

### Step 5: Present
Report: best method + why, forecast values for key periods, seasonality summary, confidence, caveats.

## Rules
1. Always run at least 2 methods for comparison
2. Never present forecast without stating assumptions
3. Always include naive baseline
4. Flag if residuals show systematic patterns
5. Warn if structural break detected

## Edge Cases
- Constant series → report constant value
- Strong trend, no seasonality → Holt's double exponential
- Short history (<30 points) → naive only, warn about accuracy

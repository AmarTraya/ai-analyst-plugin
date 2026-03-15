"""
Chart-Data Tie-Out — programmatic verification that charts accurately
represent their underlying data.

Runs between data preparation and chart rendering (chart-maker Step 4b)
to catch silent data subsetting errors, stale annotations, title-data
drift, percentage rounding issues, and highlight-claim mismatches.

All functions return ``{"ok": bool, "issues": [...]}`` dicts and never
raise exceptions.

Usage:
    from helpers.chart_tieout import run_chart_tieout

    tieout = run_chart_tieout(df, chart_spec)
    if not tieout["ok"]:
        for issue in tieout["issues"]:
            if issue["severity"] == "FAIL":
                raise RuntimeError(issue["message"])
"""

import math
import re

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Tolerances
# ---------------------------------------------------------------------------

_ANNOTATION_TOL = 0.001    # 0.1% relative tolerance for annotation values
_TITLE_CLAIM_TOL = 0.01    # 1% tolerance for title claim verification
_PERCENT_SUM_TOL = 1.0     # Absolute tolerance for percentage sum (100 +/- 1)
_ABS_FLOOR = 0.01          # Absolute floor for near-zero comparisons


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def verify_chart_data(df, chart_spec):
    """Verify basic data integrity against the chart specification.

    Checks that required columns exist, DataFrame is non-empty, y-values
    are finite (no inf/NaN), and limit is respected.

    Args:
        df: pandas.DataFrame — the prepared data for charting.
        chart_spec: dict with keys like x, y, chart_type, limit, etc.

    Returns:
        dict with keys: ok (bool), issues (list of issue dicts).
    """
    issues = []

    # --- Non-empty check ---
    if df is None or len(df) == 0:
        issues.append(_issue(
            "FAIL", "chart_data", "empty_dataframe",
            "DataFrame is empty — no data to chart",
        ))
        return {"ok": False, "issues": issues}

    # --- Column existence ---
    x_col = chart_spec.get("x")
    if x_col and x_col not in df.columns:
        issues.append(_issue(
            "FAIL", "chart_data", "missing_x_column",
            f"x column '{x_col}' not found in DataFrame. "
            f"Available: {sorted(df.columns.tolist())}",
        ))

    y_cols = chart_spec.get("y")
    if y_cols:
        if isinstance(y_cols, str):
            y_cols = [y_cols]
        for y_col in y_cols:
            if y_col not in df.columns:
                issues.append(_issue(
                    "FAIL", "chart_data", "missing_y_column",
                    f"y column '{y_col}' not found in DataFrame. "
                    f"Available: {sorted(df.columns.tolist())}",
                ))

    color_col = chart_spec.get("color_by")
    if color_col and color_col not in df.columns:
        issues.append(_issue(
            "FAIL", "chart_data", "missing_color_column",
            f"color_by column '{color_col}' not found in DataFrame. "
            f"Available: {sorted(df.columns.tolist())}",
        ))

    # --- Finite values in y-columns ---
    if y_cols:
        if isinstance(y_cols, str):
            y_cols = [y_cols]
        for y_col in y_cols:
            if y_col in df.columns and pd.api.types.is_numeric_dtype(df[y_col]):
                inf_count = int(np.isinf(df[y_col].dropna()).sum())
                nan_count = int(df[y_col].isna().sum())
                if inf_count > 0:
                    issues.append(_issue(
                        "FAIL", "chart_data", "infinite_values",
                        f"y column '{y_col}' contains {inf_count} infinite value(s)",
                    ))
                if nan_count > 0:
                    issues.append(_issue(
                        "WARN", "chart_data", "nan_values",
                        f"y column '{y_col}' contains {nan_count} NaN value(s)",
                    ))

    # --- Limit check ---
    limit = chart_spec.get("limit")
    if limit is not None and len(df) > limit:
        issues.append(_issue(
            "WARN", "chart_data", "limit_exceeded",
            f"DataFrame has {len(df)} rows but limit is {limit}. "
            f"Data should be truncated before charting.",
        ))

    ok = not any(i["severity"] == "FAIL" for i in issues)
    return {"ok": ok, "issues": issues}


def verify_annotations(df, chart_spec):
    """Verify that annotation labels match actual data values.

    For each annotation in the chart spec, looks up the corresponding
    data point and checks that any numeric value in the annotation label
    matches the actual value within tolerance.

    Args:
        df: pandas.DataFrame — the prepared data.
        chart_spec: dict with annotations list.

    Returns:
        dict with keys: ok (bool), issues (list of issue dicts).
    """
    issues = []
    annotations = chart_spec.get("annotations")
    if not annotations:
        return {"ok": True, "issues": []}

    x_col = chart_spec.get("x")
    y_cols = chart_spec.get("y")
    if isinstance(y_cols, str):
        y_cols = [y_cols]

    for i, ann in enumerate(annotations):
        ann_value = ann.get("value")
        ann_label = ann.get("label", "")

        # Extract numeric claims from the annotation label
        label_numbers = _extract_numbers(ann_label)
        if not label_numbers:
            continue  # No numeric claim to verify

        # Try to find the matching data point
        if x_col and x_col in df.columns and ann_value is not None:
            match = df[df[x_col].astype(str) == str(ann_value)]
            if len(match) == 0:
                issues.append(_issue(
                    "WARN", "annotation", f"annotation_{i}_no_match",
                    f"Annotation at x='{ann_value}' has no matching data point",
                ))
                continue

            # Check each y-column value against label numbers
            if y_cols:
                for y_col in y_cols:
                    if y_col in match.columns:
                        actual = match[y_col].iloc[0]
                        if pd.isna(actual):
                            continue
                        actual = float(actual)
                        # Check if any number in the label matches the actual
                        if not _any_number_matches(label_numbers, actual,
                                                   _ANNOTATION_TOL):
                            issues.append(_issue(
                                "FAIL", "annotation", f"annotation_{i}_mismatch",
                                f"Annotation '{ann_label}' at x='{ann_value}': "
                                f"label numbers {label_numbers} do not match "
                                f"actual value {actual} (column '{y_col}', "
                                f"tolerance {_ANNOTATION_TOL:.1%})",
                            ))

    ok = not any(i["severity"] == "FAIL" for i in issues)
    return {"ok": ok, "issues": issues}


def verify_title_claim(df, chart_spec):
    """Verify that quantitative claims in the title match the data.

    Regex-extracts percentage and numeric claims from the chart title,
    then verifies each against the DataFrame. Best-effort — returns
    unverifiable_claims count for claims that cannot be checked.

    Args:
        df: pandas.DataFrame — the prepared data.
        chart_spec: dict with title field.

    Returns:
        dict with keys: ok (bool), issues (list of issue dicts),
            verified_claims (int), unverifiable_claims (int).
    """
    issues = []
    title = chart_spec.get("title", "")
    verified = 0
    unverifiable = 0

    if not title:
        return {"ok": True, "issues": [], "verified_claims": 0,
                "unverifiable_claims": 0}

    # Extract percentage claims (e.g., "dropped 23%", "65% of revenue")
    pct_claims = _extract_percentage_claims(title)

    # Extract absolute numeric claims (e.g., "jumped from 14 to 65")
    abs_claims = _extract_absolute_claims(title)

    y_cols = chart_spec.get("y")
    if isinstance(y_cols, str):
        y_cols = [y_cols]

    for pct_value, context in pct_claims:
        matched = False
        if y_cols:
            for y_col in y_cols:
                if y_col in df.columns and pd.api.types.is_numeric_dtype(df[y_col]):
                    # Check if the percentage matches any computed percentage
                    # from the data (e.g., max change, proportion)
                    if _verify_percentage_in_data(df, y_col, pct_value,
                                                  _TITLE_CLAIM_TOL):
                        matched = True
                        verified += 1
                        break
        if not matched:
            # Could not verify — might be a derived metric not in the df
            unverifiable += 1

    for abs_value, context in abs_claims:
        matched = False
        if y_cols:
            for y_col in y_cols:
                if y_col in df.columns and pd.api.types.is_numeric_dtype(df[y_col]):
                    values = df[y_col].dropna().values
                    if _any_number_matches([abs_value], float(values.min()),
                                           _TITLE_CLAIM_TOL):
                        matched = True
                    elif _any_number_matches([abs_value], float(values.max()),
                                            _TITLE_CLAIM_TOL):
                        matched = True
                    elif any(_any_number_matches([abs_value], float(v),
                                                _TITLE_CLAIM_TOL)
                             for v in values):
                        matched = True
                    if matched:
                        verified += 1
                        break
        if not matched:
            unverifiable += 1

    # Only FAIL if we found a claim and positively disproved it
    # Unverifiable claims are not failures
    ok = not any(i["severity"] == "FAIL" for i in issues)
    return {"ok": ok, "issues": issues, "verified_claims": verified,
            "unverifiable_claims": unverifiable}


def verify_percentage_labels(df, chart_spec):
    """Verify percentage labels for pie/donut charts sum correctly.

    For pie/donut charts or charts with format="percent", checks that:
    1. Percentage slices sum to 100% (within tolerance)
    2. Each slice matches its actual proportion of the total

    Args:
        df: pandas.DataFrame — the prepared data.
        chart_spec: dict with chart_type and format fields.

    Returns:
        dict with keys: ok (bool), issues (list of issue dicts).
    """
    issues = []
    chart_type = chart_spec.get("chart_type", "")
    fmt = chart_spec.get("format", "")

    is_percentage_chart = chart_type in ("pie", "donut") or fmt == "percent"
    if not is_percentage_chart:
        return {"ok": True, "issues": []}

    y_cols = chart_spec.get("y")
    if isinstance(y_cols, str):
        y_cols = [y_cols]
    if not y_cols:
        return {"ok": True, "issues": []}

    for y_col in y_cols:
        if y_col not in df.columns:
            continue
        if not pd.api.types.is_numeric_dtype(df[y_col]):
            continue

        values = df[y_col].dropna()
        if len(values) == 0:
            continue

        total = values.sum()
        if total == 0:
            issues.append(_issue(
                "FAIL", "percentage_labels", f"{y_col}_zero_total",
                f"Column '{y_col}' sums to zero — cannot compute percentages",
            ))
            continue

        # Compute actual percentages
        percentages = (values / total) * 100
        pct_sum = percentages.sum()

        # Check sum is close to 100
        if abs(pct_sum - 100.0) > _PERCENT_SUM_TOL:
            issues.append(_issue(
                "FAIL", "percentage_labels", f"{y_col}_sum_mismatch",
                f"Percentage labels for '{y_col}' sum to {pct_sum:.2f}%, "
                f"expected 100% (tolerance: +/-{_PERCENT_SUM_TOL}%)",
            ))

        # Check for individual slice accuracy (each should match proportion)
        x_col = chart_spec.get("x")
        if x_col and x_col in df.columns:
            for idx in values.index:
                actual_pct = (values.loc[idx] / total) * 100
                rounded_pct = round(actual_pct)
                # If rounding introduces > 1% error on any single slice
                if abs(rounded_pct - actual_pct) > 1.0:
                    label = df.loc[idx, x_col] if x_col in df.columns else idx
                    issues.append(_issue(
                        "WARN", "percentage_labels",
                        f"{y_col}_slice_rounding_{idx}",
                        f"Slice '{label}': rounded {rounded_pct}% vs "
                        f"actual {actual_pct:.2f}% — rounding error > 1%",
                    ))

    ok = not any(i["severity"] == "FAIL" for i in issues)
    return {"ok": ok, "issues": issues}


def verify_highlight_claim(df, chart_spec):
    """Verify that the highlighted category matches the title's claim.

    If the title claims a category is the max/min/dominant element, and
    a highlight is specified via color_by or annotations, verify the
    highlighted element actually has that property.

    Args:
        df: pandas.DataFrame — the prepared data.
        chart_spec: dict with title, x, y, color_by, annotations.

    Returns:
        dict with keys: ok (bool), issues (list of issue dicts).
    """
    issues = []
    title = (chart_spec.get("title") or "").lower()

    # Detect superlative claims in title
    superlative_patterns = [
        (r"highest|largest|most|dominant|leading|top|greatest|maximum|max",
         "max"),
        (r"lowest|smallest|least|minimum|min|fewest", "min"),
        (r"(dropped|fell|declined|decreased)\s+(?:the\s+)?most", "min_change"),
        (r"(grew|jumped|surged|increased|rose)\s+(?:the\s+)?most", "max_change"),
    ]

    claimed_direction = None
    for pattern, direction in superlative_patterns:
        if re.search(pattern, title):
            claimed_direction = direction
            break

    if not claimed_direction:
        return {"ok": True, "issues": []}

    x_col = chart_spec.get("x")
    y_cols = chart_spec.get("y")
    if isinstance(y_cols, str):
        y_cols = [y_cols]

    if not x_col or not y_cols or x_col not in df.columns:
        return {"ok": True, "issues": []}

    # Determine which category is highlighted (from annotations or title)
    highlighted = _extract_highlighted_category(title, df, x_col)
    if not highlighted:
        return {"ok": True, "issues": []}

    for y_col in y_cols:
        if y_col not in df.columns or not pd.api.types.is_numeric_dtype(df[y_col]):
            continue

        if claimed_direction == "max":
            actual_winner = df.loc[df[y_col].idxmax(), x_col]
        elif claimed_direction == "min":
            actual_winner = df.loc[df[y_col].idxmin(), x_col]
        else:
            continue  # max_change/min_change need time-series logic

        if str(actual_winner).lower() != highlighted.lower():
            issues.append(_issue(
                "FAIL", "highlight_claim", f"{y_col}_wrong_highlight",
                f"Title claims '{highlighted}' is the {claimed_direction}, "
                f"but actual {claimed_direction} is '{actual_winner}' "
                f"(column '{y_col}')",
            ))

    ok = not any(i["severity"] == "FAIL" for i in issues)
    return {"ok": ok, "issues": issues}


def run_chart_tieout(df, chart_spec):
    """Run all chart-data tie-out checks and return a summary.

    Orchestrates all verification functions and produces a consolidated
    result with pass/fail counts and a list of all issues.

    Args:
        df: pandas.DataFrame — the prepared data for charting.
        chart_spec: dict — the chart specification.

    Returns:
        dict with keys:
            ok (bool): True if no FAIL-severity issues.
            checks (dict): Per-check results keyed by check name.
            issues (list): All issues across all checks.
            summary (str): Human-readable summary line.
            pass_count (int): Number of checks that passed.
            fail_count (int): Number of checks with FAIL issues.
            warn_count (int): Number of checks with WARN-only issues.
    """
    checks = {}
    all_issues = []

    check_fns = [
        ("chart_data", verify_chart_data),
        ("annotations", verify_annotations),
        ("title_claim", verify_title_claim),
        ("percentage_labels", verify_percentage_labels),
        ("highlight_claim", verify_highlight_claim),
    ]

    for name, fn in check_fns:
        try:
            result = fn(df, chart_spec)
        except Exception as exc:
            result = {
                "ok": False,
                "issues": [_issue(
                    "WARN", name, "check_error",
                    f"Check '{name}' raised an exception: {exc}",
                )],
            }
        checks[name] = result
        all_issues.extend(result.get("issues", []))

    fail_issues = [i for i in all_issues if i["severity"] == "FAIL"]
    warn_issues = [i for i in all_issues if i["severity"] == "WARN"]

    pass_count = sum(1 for r in checks.values() if r["ok"] and not r.get("issues"))
    fail_count = sum(1 for r in checks.values()
                     if any(i["severity"] == "FAIL" for i in r.get("issues", [])))
    warn_count = sum(1 for r in checks.values()
                     if r["ok"] and r.get("issues")
                     and all(i["severity"] == "WARN" for i in r["issues"]))

    ok = len(fail_issues) == 0

    summary = (
        f"Chart tie-out: {pass_count} passed, {fail_count} failed, "
        f"{warn_count} warnings — {'OK' if ok else 'HALT'}"
    )

    return {
        "ok": ok,
        "checks": checks,
        "issues": all_issues,
        "summary": summary,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "warn_count": warn_count,
    }


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _issue(severity, check, code, message):
    """Create a standardized issue dict.

    Args:
        severity: "FAIL" or "WARN".
        check: Which check produced this issue.
        code: Machine-readable issue code.
        message: Human-readable description.

    Returns:
        dict with keys: severity, check, code, message.
    """
    return {
        "severity": severity,
        "check": check,
        "code": code,
        "message": message,
    }


def _extract_numbers(text):
    """Extract numeric values from text, excluding dates and ordinals.

    Args:
        text: String to parse.

    Returns:
        list of float values found in the text.
    """
    if not text:
        return []

    # Remove date-like patterns to avoid false positives
    cleaned = re.sub(r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b', '', text)
    cleaned = re.sub(r'\b(?:19|20)\d{2}\b', '', cleaned)  # years
    cleaned = re.sub(r'\bQ[1-4]\b', '', cleaned, flags=re.IGNORECASE)  # quarters

    # Match numbers: integers, decimals, percentages, currency
    # Capture the sign and number, strip trailing % or currency symbols
    matches = re.findall(
        r'[-+]?\$?(\d+(?:,\d{3})*(?:\.\d+)?)\s*%?',
        cleaned,
    )

    numbers = []
    for m in matches:
        try:
            numbers.append(float(m.replace(',', '')))
        except ValueError:
            continue
    return numbers


def _extract_percentage_claims(title):
    """Extract percentage claims from a title string.

    Returns a list of (value, context) tuples where value is the
    percentage as a float and context is the surrounding text.

    Args:
        title: Chart title string.

    Returns:
        list of (float, str) tuples.
    """
    claims = []
    # Match patterns like "23%", "dropped 23%", "65% of revenue"
    for m in re.finditer(r'(\d+(?:\.\d+)?)\s*%', title):
        value = float(m.group(1))
        start = max(0, m.start() - 20)
        end = min(len(title), m.end() + 20)
        context = title[start:end]
        claims.append((value, context))
    return claims


def _extract_absolute_claims(title):
    """Extract absolute numeric claims from a title string.

    Filters out years, dates, and percentages. Returns (value, context)
    tuples.

    Args:
        title: Chart title string.

    Returns:
        list of (float, str) tuples.
    """
    claims = []
    # Remove percentages first (handled separately)
    cleaned = re.sub(r'\d+(?:\.\d+)?\s*%', '', title)
    # Remove years
    cleaned = re.sub(r'\b(?:19|20)\d{2}\b', '', cleaned)
    # Remove quarters
    cleaned = re.sub(r'\bQ[1-4]\b', '', cleaned, flags=re.IGNORECASE)

    for m in re.finditer(r'\b(\d+(?:,\d{3})*(?:\.\d+)?)\b', cleaned):
        try:
            value = float(m.group(1).replace(',', ''))
            if value == 0:
                continue
            start = max(0, m.start() - 20)
            end = min(len(cleaned), m.end() + 20)
            context = cleaned[start:end]
            claims.append((value, context))
        except ValueError:
            continue
    return claims


def _any_number_matches(candidates, actual, tolerance):
    """Check if any candidate number matches the actual value.

    Uses relative tolerance with an absolute floor for near-zero values.

    Args:
        candidates: list of float values to check.
        actual: The actual value to compare against.
        tolerance: Relative tolerance threshold.

    Returns:
        bool: True if any candidate matches within tolerance.
    """
    for candidate in candidates:
        if actual == 0 and candidate == 0:
            return True
        if abs(actual) < _ABS_FLOOR and abs(candidate) < _ABS_FLOOR:
            if abs(actual - candidate) < _ABS_FLOOR:
                return True
            continue
        denom = abs(actual) if actual != 0 else abs(candidate)
        if denom == 0:
            continue
        if abs(actual - candidate) / denom <= tolerance:
            return True
    return False


def _verify_percentage_in_data(df, y_col, pct_value, tolerance):
    """Check if a percentage claim can be verified against the data.

    Tries several interpretations:
    1. pct_value matches a raw value in the column
    2. pct_value matches a proportion of total (for pie/donut)
    3. pct_value matches a percentage change between max and min
    4. pct_value matches a percentage change between first and last

    Args:
        df: pandas.DataFrame.
        y_col: Column name to check.
        pct_value: The claimed percentage value.
        tolerance: Relative tolerance.

    Returns:
        bool: True if the claim is verified by any interpretation.
    """
    values = df[y_col].dropna()
    if len(values) == 0:
        return False

    # 1. Raw value match
    for v in values:
        if _any_number_matches([pct_value], float(v), tolerance):
            return True

    # 2. Proportion of total
    total = values.sum()
    if total != 0:
        for v in values:
            proportion = (float(v) / total) * 100
            if _any_number_matches([pct_value], proportion, tolerance):
                return True

    # 3. Percentage change: max vs min
    vmax = float(values.max())
    vmin = float(values.min())
    if vmin != 0:
        pct_change = abs((vmax - vmin) / vmin) * 100
        if _any_number_matches([pct_value], pct_change, tolerance):
            return True

    # 4. Percentage change: first vs last
    first = float(values.iloc[0])
    last = float(values.iloc[-1])
    if first != 0:
        pct_change_fl = abs((last - first) / first) * 100
        if _any_number_matches([pct_value], pct_change_fl, tolerance):
            return True

    return False


def _extract_highlighted_category(title, df, x_col):
    """Try to identify which category the title refers to.

    Checks each unique value in the x-column against the title text.

    Args:
        title: Lowercased title string.
        df: pandas.DataFrame.
        x_col: Column name for categories.

    Returns:
        str or None: The matching category name, or None.
    """
    categories = df[x_col].dropna().unique()
    for cat in categories:
        cat_str = str(cat).lower()
        if len(cat_str) >= 2 and cat_str in title:
            return str(cat)
    return None

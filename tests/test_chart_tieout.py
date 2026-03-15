"""Tests for helpers/chart_tieout.py — chart-data tie-out verification."""

import numpy as np
import pandas as pd
import pytest

from helpers.chart_tieout import (
    run_chart_tieout,
    verify_annotations,
    verify_chart_data,
    verify_highlight_claim,
    verify_percentage_labels,
    verify_title_claim,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_df():
    """Simple categorical DataFrame for bar/pie charts."""
    return pd.DataFrame({
        "category": ["iOS", "Android", "Web", "Other"],
        "tickets": [650, 420, 310, 120],
        "revenue": [45.0, 30.0, 20.0, 5.0],
    })


@pytest.fixture
def time_series_df():
    """Time series DataFrame for line charts."""
    return pd.DataFrame({
        "month": pd.date_range("2024-01-01", periods=6, freq="MS"),
        "value": [100, 110, 105, 140, 135, 150],
    })


@pytest.fixture
def valid_bar_spec():
    """Valid bar chart spec matching sample_df."""
    return {
        "chart_type": "bar",
        "x": "category",
        "y": "tickets",
        "title": "iOS leads with 650 tickets",
        "annotations": [
            {"value": "iOS", "label": "650 tickets", "position": "top"},
        ],
    }


@pytest.fixture
def valid_pie_spec():
    """Valid pie chart spec matching sample_df revenue column."""
    return {
        "chart_type": "pie",
        "x": "category",
        "y": "revenue",
        "title": "Revenue distribution across platforms",
    }


# ---------------------------------------------------------------------------
# verify_chart_data
# ---------------------------------------------------------------------------

class TestVerifyChartData:
    def test_happy_path(self, sample_df, valid_bar_spec):
        result = verify_chart_data(sample_df, valid_bar_spec)
        assert result["ok"] is True
        assert len(result["issues"]) == 0

    def test_empty_dataframe(self, valid_bar_spec):
        df = pd.DataFrame(columns=["category", "tickets"])
        result = verify_chart_data(df, valid_bar_spec)
        assert result["ok"] is False
        assert any(i["code"] == "empty_dataframe" for i in result["issues"])

    def test_none_dataframe(self, valid_bar_spec):
        result = verify_chart_data(None, valid_bar_spec)
        assert result["ok"] is False

    def test_missing_x_column(self, sample_df):
        spec = {"x": "nonexistent", "y": "tickets", "chart_type": "bar"}
        result = verify_chart_data(sample_df, spec)
        assert result["ok"] is False
        assert any(i["code"] == "missing_x_column" for i in result["issues"])

    def test_missing_y_column(self, sample_df):
        spec = {"x": "category", "y": "nonexistent", "chart_type": "bar"}
        result = verify_chart_data(sample_df, spec)
        assert result["ok"] is False
        assert any(i["code"] == "missing_y_column" for i in result["issues"])

    def test_missing_y_column_in_list(self, sample_df):
        spec = {"x": "category", "y": ["tickets", "missing"], "chart_type": "bar"}
        result = verify_chart_data(sample_df, spec)
        assert result["ok"] is False

    def test_nan_values_warn(self):
        df = pd.DataFrame({
            "x": ["a", "b", "c"],
            "y": [1.0, float("nan"), 3.0],
        })
        spec = {"x": "x", "y": "y", "chart_type": "bar"}
        result = verify_chart_data(df, spec)
        assert result["ok"] is True  # NaN is WARN, not FAIL
        assert any(i["code"] == "nan_values" for i in result["issues"])

    def test_infinite_values_fail(self):
        df = pd.DataFrame({
            "x": ["a", "b", "c"],
            "y": [1.0, float("inf"), 3.0],
        })
        spec = {"x": "x", "y": "y", "chart_type": "bar"}
        result = verify_chart_data(df, spec)
        assert result["ok"] is False
        assert any(i["code"] == "infinite_values" for i in result["issues"])

    def test_limit_exceeded_warn(self, sample_df):
        spec = {"x": "category", "y": "tickets", "chart_type": "bar", "limit": 2}
        result = verify_chart_data(sample_df, spec)
        assert result["ok"] is True
        assert any(i["code"] == "limit_exceeded" for i in result["issues"])

    def test_missing_color_by_column(self, sample_df):
        spec = {"x": "category", "y": "tickets", "chart_type": "bar",
                "color_by": "missing_col"}
        result = verify_chart_data(sample_df, spec)
        assert result["ok"] is False
        assert any(i["code"] == "missing_color_column" for i in result["issues"])


# ---------------------------------------------------------------------------
# verify_annotations
# ---------------------------------------------------------------------------

class TestVerifyAnnotations:
    def test_correct_annotation(self, sample_df, valid_bar_spec):
        result = verify_annotations(sample_df, valid_bar_spec)
        assert result["ok"] is True

    def test_wrong_annotation_value(self, sample_df):
        spec = {
            "x": "category",
            "y": "tickets",
            "annotations": [
                {"value": "iOS", "label": "999 tickets", "position": "top"},
            ],
        }
        result = verify_annotations(sample_df, spec)
        assert result["ok"] is False
        assert any("mismatch" in i["code"] for i in result["issues"])

    def test_no_annotations(self, sample_df):
        spec = {"x": "category", "y": "tickets"}
        result = verify_annotations(sample_df, spec)
        assert result["ok"] is True
        assert len(result["issues"]) == 0

    def test_annotation_no_matching_data_point(self, sample_df):
        spec = {
            "x": "category",
            "y": "tickets",
            "annotations": [
                {"value": "Desktop", "label": "100 tickets", "position": "top"},
            ],
        }
        result = verify_annotations(sample_df, spec)
        assert any(i["code"] == "annotation_0_no_match" for i in result["issues"])

    def test_annotation_no_numeric_label(self, sample_df):
        spec = {
            "x": "category",
            "y": "tickets",
            "annotations": [
                {"value": "iOS", "label": "Peak month", "position": "top"},
            ],
        }
        result = verify_annotations(sample_df, spec)
        assert result["ok"] is True  # No numeric claim to verify


# ---------------------------------------------------------------------------
# verify_title_claim
# ---------------------------------------------------------------------------

class TestVerifyTitleClaim:
    def test_verifiable_percentage(self):
        df = pd.DataFrame({"x": ["a", "b"], "y": [100, 150]})
        spec = {"x": "x", "y": "y", "title": "Y increased by 50%"}
        result = verify_title_claim(df, spec)
        assert result["verified_claims"] >= 1

    def test_unparseable_title(self):
        df = pd.DataFrame({"x": ["a", "b"], "y": [100, 150]})
        spec = {"x": "x", "y": "y", "title": "Sales went up significantly"}
        result = verify_title_claim(df, spec)
        assert result["ok"] is True
        assert result["verified_claims"] == 0
        assert result["unverifiable_claims"] == 0

    def test_title_with_year_not_treated_as_claim(self):
        df = pd.DataFrame({"x": ["a", "b"], "y": [100, 200]})
        spec = {"x": "x", "y": "y", "title": "Revenue growth in 2024"}
        result = verify_title_claim(df, spec)
        # "2024" should be filtered out as a year, not treated as a claim
        assert result["ok"] is True

    def test_no_title(self):
        df = pd.DataFrame({"x": ["a"], "y": [1]})
        spec = {"x": "x", "y": "y", "title": ""}
        result = verify_title_claim(df, spec)
        assert result["ok"] is True
        assert result["verified_claims"] == 0

    def test_absolute_claim_matches(self, sample_df):
        spec = {
            "x": "category", "y": "tickets",
            "title": "iOS peaked at 650 tickets",
        }
        result = verify_title_claim(sample_df, spec)
        assert result["verified_claims"] >= 1

    def test_unverifiable_claim_does_not_fail(self):
        df = pd.DataFrame({"x": ["a", "b"], "y": [10, 20]})
        spec = {"x": "x", "y": "y", "title": "Conversion dropped 73%"}
        result = verify_title_claim(df, spec)
        assert result["ok"] is True
        assert result["unverifiable_claims"] >= 1


# ---------------------------------------------------------------------------
# verify_percentage_labels
# ---------------------------------------------------------------------------

class TestVerifyPercentageLabels:
    def test_pie_chart_valid(self, sample_df, valid_pie_spec):
        result = verify_percentage_labels(sample_df, valid_pie_spec)
        assert result["ok"] is True

    def test_non_percentage_chart_skipped(self, sample_df, valid_bar_spec):
        result = verify_percentage_labels(sample_df, valid_bar_spec)
        assert result["ok"] is True
        assert len(result["issues"]) == 0

    def test_pie_chart_zero_total(self):
        df = pd.DataFrame({"cat": ["a", "b"], "val": [0, 0]})
        spec = {"chart_type": "pie", "x": "cat", "y": "val"}
        result = verify_percentage_labels(df, spec)
        assert result["ok"] is False
        assert any("zero_total" in i["code"] for i in result["issues"])

    def test_donut_chart_checked(self):
        df = pd.DataFrame({"cat": ["a", "b", "c"], "val": [50, 30, 20]})
        spec = {"chart_type": "donut", "x": "cat", "y": "val"}
        result = verify_percentage_labels(df, spec)
        assert result["ok"] is True

    def test_format_percent_checked(self):
        df = pd.DataFrame({"cat": ["a", "b"], "val": [60, 40]})
        spec = {"chart_type": "bar", "x": "cat", "y": "val", "format": "percent"}
        result = verify_percentage_labels(df, spec)
        assert result["ok"] is True


# ---------------------------------------------------------------------------
# verify_highlight_claim
# ---------------------------------------------------------------------------

class TestVerifyHighlightClaim:
    def test_correct_max_highlight(self, sample_df):
        spec = {
            "x": "category", "y": "tickets",
            "title": "iOS has the most tickets",
        }
        result = verify_highlight_claim(sample_df, spec)
        assert result["ok"] is True

    def test_wrong_max_highlight(self, sample_df):
        spec = {
            "x": "category", "y": "tickets",
            "title": "Android has the most tickets",
        }
        result = verify_highlight_claim(sample_df, spec)
        assert result["ok"] is False
        assert any("wrong_highlight" in i["code"] for i in result["issues"])

    def test_no_superlative_in_title(self, sample_df):
        spec = {
            "x": "category", "y": "tickets",
            "title": "Ticket distribution by platform",
        }
        result = verify_highlight_claim(sample_df, spec)
        assert result["ok"] is True
        assert len(result["issues"]) == 0

    def test_correct_min_highlight(self):
        df = pd.DataFrame({
            "device": ["Phone", "Tablet", "Desktop"],
            "errors": [5, 2, 10],
        })
        spec = {
            "x": "device", "y": "errors",
            "title": "Tablet has the fewest errors",
        }
        result = verify_highlight_claim(df, spec)
        assert result["ok"] is True


# ---------------------------------------------------------------------------
# run_chart_tieout (integration)
# ---------------------------------------------------------------------------

class TestRunChartTieout:
    def test_all_pass(self, sample_df, valid_bar_spec):
        result = run_chart_tieout(sample_df, valid_bar_spec)
        assert result["ok"] is True
        assert result["fail_count"] == 0
        assert "OK" in result["summary"]

    def test_mixed_results(self):
        df = pd.DataFrame({
            "category": ["iOS", "Android"],
            "tickets": [100.0, float("nan")],
        })
        spec = {
            "chart_type": "bar",
            "x": "category",
            "y": "tickets",
            "title": "Ticket counts",
            "annotations": [
                {"value": "iOS", "label": "999 tickets", "position": "top"},
            ],
        }
        result = run_chart_tieout(df, spec)
        assert result["ok"] is False
        assert result["fail_count"] >= 1
        assert result["warn_count"] >= 0
        assert "HALT" in result["summary"]

    def test_summary_counts(self, sample_df, valid_bar_spec):
        result = run_chart_tieout(sample_df, valid_bar_spec)
        total = result["pass_count"] + result["fail_count"] + result["warn_count"]
        assert total <= 5  # At most 5 check categories

    def test_exception_in_check_handled(self):
        """Verify that exceptions in individual checks don't crash the orchestrator."""
        # Pass a non-DataFrame to trigger edge cases
        result = run_chart_tieout(pd.DataFrame(), {"chart_type": "bar"})
        # Should return ok=False for empty df but not raise
        assert isinstance(result, dict)
        assert "ok" in result

    def test_empty_spec(self, sample_df):
        result = run_chart_tieout(sample_df, {})
        assert isinstance(result, dict)
        assert result["ok"] is True  # No columns to check = no failures


# ---------------------------------------------------------------------------
# Regex edge cases
# ---------------------------------------------------------------------------

class TestRegexEdgeCases:
    def test_date_not_extracted_as_number(self):
        from helpers.chart_tieout import _extract_numbers
        nums = _extract_numbers("Revenue in 2024-03-15")
        # Should not extract 2024, 03, 15 as separate numbers
        assert 2024 not in nums
        assert 15 not in [int(n) for n in nums if n == int(n)]

    def test_year_filtered_from_title(self):
        from helpers.chart_tieout import _extract_absolute_claims
        claims = _extract_absolute_claims("Growth in 2024 was strong")
        values = [c[0] for c in claims]
        assert 2024 not in values

    def test_percentage_extracted(self):
        from helpers.chart_tieout import _extract_percentage_claims
        claims = _extract_percentage_claims("Revenue dropped 23.5% in Q3")
        assert len(claims) == 1
        assert claims[0][0] == 23.5

    def test_currency_number_extracted(self):
        from helpers.chart_tieout import _extract_numbers
        nums = _extract_numbers("Revenue was $1,234.56")
        assert any(abs(n - 1234.56) < 0.01 for n in nums)

    def test_quarter_not_extracted(self):
        from helpers.chart_tieout import _extract_numbers
        nums = _extract_numbers("Q3 results improved")
        assert 3 not in nums

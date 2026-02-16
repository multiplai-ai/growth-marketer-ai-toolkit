#!/usr/bin/env python3
"""
Time Comparison Calculations

Implements MTD pacing, weekly pace, and period-over-period comparisons
for engagement metrics.

Comparison Types:
- MTD Pacing: Project full-month value from MTD actuals
- Weekly Pace: Project weekly value from WTD actuals
- vs Prior Week: Compare weekly pace to prior week
- vs P3MA: Compare to prior 3-month average
- vs PY: Compare to prior year same period
"""

from datetime import date, datetime, timedelta
from typing import Dict, Any, Optional, List, Union
import calendar
import pandas as pd
import numpy as np


def get_period_context(
    report_date: Optional[date] = None
) -> Dict[str, Any]:
    """
    Get period context for calculations.

    Args:
        report_date: Date to calculate context for (default: today)

    Returns:
        Dict with period details:
        - report_date: The date being reported
        - month_start: First day of month
        - month_end: Last day of month
        - days_in_month: Total days in month
        - days_elapsed: Days from month start through report_date
        - week_start: Monday of current week
        - days_this_week: Days from Monday through report_date (1-7)
        - prior_week_start: Monday of prior week
        - prior_week_end: Sunday of prior week
    """
    if report_date is None:
        report_date = date.today()

    # Month context
    month_start = report_date.replace(day=1)
    days_in_month = calendar.monthrange(report_date.year, report_date.month)[1]
    month_end = report_date.replace(day=days_in_month)
    days_elapsed = report_date.day

    # Week context (Monday = 0)
    days_since_monday = report_date.weekday()
    week_start = report_date - timedelta(days=days_since_monday)
    days_this_week = days_since_monday + 1  # 1 = Monday, 7 = Sunday

    prior_week_start = week_start - timedelta(days=7)
    prior_week_end = week_start - timedelta(days=1)

    return {
        "report_date": report_date,
        "month_start": month_start,
        "month_end": month_end,
        "days_in_month": days_in_month,
        "days_elapsed": days_elapsed,
        "week_start": week_start,
        "days_this_week": days_this_week,
        "prior_week_start": prior_week_start,
        "prior_week_end": prior_week_end,
        "month_name": report_date.strftime("%B"),
        "year": report_date.year
    }


def calculate_mtd_pacing(
    mtd_value: float,
    days_elapsed: int,
    days_in_month: int
) -> float:
    """
    Calculate MTD pacing (projected full-month value).

    Formula: MTD_value / days_elapsed * days_in_month

    Args:
        mtd_value: Current MTD value
        days_elapsed: Days elapsed in month
        days_in_month: Total days in month

    Returns:
        Projected full-month value
    """
    if days_elapsed <= 0:
        return 0.0

    return (mtd_value / days_elapsed) * days_in_month


def calculate_weekly_pace(
    wtd_value: float,
    days_this_week: int
) -> float:
    """
    Calculate weekly pace (projected 7-day value).

    Formula: WTD_value / days_this_week * 7

    Args:
        wtd_value: Current week-to-date value
        days_this_week: Days elapsed this week (1-7)

    Returns:
        Projected weekly value
    """
    if days_this_week <= 0:
        return 0.0

    return (wtd_value / days_this_week) * 7


def calculate_delta(
    current: float,
    prior: float,
    as_percent: bool = False
) -> Optional[float]:
    """
    Calculate delta (change) between values.

    Args:
        current: Current/comparison value
        prior: Prior/baseline value
        as_percent: Return as percentage change

    Returns:
        Delta value (absolute or percent), None if prior is 0/NaN
    """
    if pd.isna(current) or pd.isna(prior):
        return None

    if as_percent:
        if prior == 0:
            return None
        return ((current - prior) / prior) * 100
    else:
        return current - prior


def calculate_p3ma(
    prior_month_values: List[float]
) -> Optional[float]:
    """
    Calculate Prior 3-Month Average.

    Args:
        prior_month_values: List of values for prior 3 months

    Returns:
        Average value, None if insufficient data
    """
    valid_values = [v for v in prior_month_values if pd.notna(v)]

    if len(valid_values) < 3:
        return None

    return sum(valid_values) / len(valid_values)


class TimeComparisonCalculator:
    """
    Calculator for time-based metric comparisons.

    Handles multiple comparison types and formats results
    for reporting.
    """

    def __init__(
        self,
        report_date: Optional[date] = None,
        days_elapsed: Optional[int] = None
    ):
        """
        Initialize calculator.

        Args:
            report_date: Date to calculate for
            days_elapsed: Override days elapsed (from data)
        """
        self.context = get_period_context(report_date)

        # Allow override from actual data
        if days_elapsed is not None:
            self.context["days_elapsed"] = days_elapsed

    def calculate_mtd_metrics(
        self,
        current_mtd: Dict[str, float],
        p3ma: Optional[Dict[str, float]] = None,
        prior_year: Optional[Dict[str, float]] = None,
        prior_month: Optional[Dict[str, float]] = None,
        plan: Optional[Dict[str, float]] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Calculate full set of MTD comparisons for metrics.

        Args:
            current_mtd: Dict of metric name -> MTD value
            p3ma: Dict of metric name -> P3MA value
            prior_year: Dict of metric name -> prior year value
            prior_month: Dict of metric name -> prior month value
            plan: Dict of metric name -> plan/target value

        Returns:
            Dict of metric name -> comparison dict with:
            - current_mtd: Raw MTD value
            - mtd_paced: Projected full month
            - p3ma: Prior 3-month average
            - delta_p3ma_abs: Absolute delta vs P3MA
            - delta_p3ma_pct: Percent delta vs P3MA
            - prior_year: Prior year value
            - delta_py_abs: Absolute delta vs PY
            - delta_py_pct: Percent delta vs PY
            - prior_month: Prior month value
            - delta_pm_abs: Absolute delta vs prior month
            - delta_pm_pct: Percent delta vs prior month
            - plan: Plan/target value
            - delta_plan_abs: Absolute delta vs plan
            - delta_plan_pct: Percent delta vs plan
        """
        p3ma = p3ma or {}
        prior_year = prior_year or {}
        prior_month = prior_month or {}
        plan = plan or {}

        results = {}

        for metric, mtd_value in current_mtd.items():
            # Calculate paced value
            paced = calculate_mtd_pacing(
                mtd_value,
                self.context["days_elapsed"],
                self.context["days_in_month"]
            )

            result = {
                "current_mtd": mtd_value,
                "mtd_paced": paced,
                "days_elapsed": self.context["days_elapsed"],
                "days_in_month": self.context["days_in_month"]
            }

            # P3MA comparison
            if metric in p3ma and pd.notna(p3ma[metric]):
                result["p3ma"] = p3ma[metric]
                result["delta_p3ma_abs"] = calculate_delta(paced, p3ma[metric])
                result["delta_p3ma_pct"] = calculate_delta(paced, p3ma[metric], as_percent=True)
            else:
                result["p3ma"] = None
                result["delta_p3ma_abs"] = None
                result["delta_p3ma_pct"] = None

            # Prior year comparison
            if metric in prior_year and pd.notna(prior_year[metric]):
                result["prior_year"] = prior_year[metric]
                result["delta_py_abs"] = calculate_delta(paced, prior_year[metric])
                result["delta_py_pct"] = calculate_delta(paced, prior_year[metric], as_percent=True)
            else:
                result["prior_year"] = None
                result["delta_py_abs"] = None
                result["delta_py_pct"] = None

            # Prior month comparison
            if metric in prior_month and pd.notna(prior_month[metric]):
                result["prior_month"] = prior_month[metric]
                result["delta_pm_abs"] = calculate_delta(paced, prior_month[metric])
                result["delta_pm_pct"] = calculate_delta(paced, prior_month[metric], as_percent=True)
            else:
                result["prior_month"] = None
                result["delta_pm_abs"] = None
                result["delta_pm_pct"] = None

            # Plan comparison
            if metric in plan and pd.notna(plan[metric]):
                result["plan"] = plan[metric]
                result["delta_plan_abs"] = calculate_delta(paced, plan[metric])
                result["delta_plan_pct"] = calculate_delta(paced, plan[metric], as_percent=True)
            else:
                result["plan"] = None
                result["delta_plan_abs"] = None
                result["delta_plan_pct"] = None

            results[metric] = result

        return results

    def calculate_weekly_metrics(
        self,
        current_wtd: Dict[str, float],
        prior_week: Optional[Dict[str, float]] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Calculate weekly pace and vs prior week.

        Args:
            current_wtd: Dict of metric name -> WTD value
            prior_week: Dict of metric name -> prior week value

        Returns:
            Dict of metric name -> comparison dict
        """
        prior_week = prior_week or {}
        results = {}

        for metric, wtd_value in current_wtd.items():
            pace = calculate_weekly_pace(
                wtd_value,
                self.context["days_this_week"]
            )

            result = {
                "current_wtd": wtd_value,
                "weekly_pace": pace,
                "days_this_week": self.context["days_this_week"]
            }

            if metric in prior_week and pd.notna(prior_week[metric]):
                result["prior_week"] = prior_week[metric]
                result["delta_pw_abs"] = calculate_delta(pace, prior_week[metric])
                result["delta_pw_pct"] = calculate_delta(pace, prior_week[metric], as_percent=True)
            else:
                result["prior_week"] = None
                result["delta_pw_abs"] = None
                result["delta_pw_pct"] = None

            results[metric] = result

        return results

    def format_comparison_table(
        self,
        metrics: Dict[str, Dict[str, Any]],
        include_weekly: bool = True
    ) -> pd.DataFrame:
        """
        Format comparisons into a display table.

        Args:
            metrics: Output from calculate_mtd_metrics
            include_weekly: Include weekly pace columns

        Returns:
            DataFrame formatted for display
        """
        rows = []

        for metric_name, values in metrics.items():
            row = {
                "Metric": metric_name,
                "Current MTD": values.get("current_mtd"),
                "MTD Paced": values.get("mtd_paced"),
                "P3MA": values.get("p3ma"),
                "vs P3MA": values.get("delta_p3ma_abs"),
                "vs P3MA %": values.get("delta_p3ma_pct"),
                "PY": values.get("prior_year"),
                "vs PY": values.get("delta_py_abs"),
                "vs PY %": values.get("delta_py_pct")
            }

            if include_weekly:
                row["Weekly Pace"] = values.get("weekly_pace")
                row["Prior Week"] = values.get("prior_week")
                row["vs PW %"] = values.get("delta_pw_pct")

            if values.get("plan") is not None:
                row["Plan"] = values.get("plan")
                row["vs Plan %"] = values.get("delta_plan_pct")

            rows.append(row)

        return pd.DataFrame(rows)


def format_number(
    value: Optional[float],
    format_type: str = "count",
    na_display: str = "—"
) -> str:
    """
    Format number for display.

    Args:
        value: Value to format
        format_type: "count", "rate", "percent", "delta_pct"
        na_display: String to show for None/NaN values

    Returns:
        Formatted string
    """
    if value is None or pd.isna(value):
        return na_display

    if format_type == "count":
        return f"{value:,.0f}"

    elif format_type == "rate":
        return f"{value:.2f}"

    elif format_type == "percent":
        return f"{value:.1f}%"

    elif format_type == "delta_pct":
        prefix = "+" if value > 0 else ""
        return f"{prefix}{value:.1f}%"

    else:
        return str(value)


def get_signal_color(
    delta_p3ma_pct: Optional[float],
    delta_py_pct: Optional[float]
) -> str:
    """
    Determine signal color based on comparisons.

    Args:
        delta_p3ma_pct: Percent change vs P3MA
        delta_py_pct: Percent change vs PY

    Returns:
        "green", "red", or "yellow"
    """
    if delta_p3ma_pct is None or delta_py_pct is None:
        return "yellow"

    if delta_p3ma_pct > 0 and delta_py_pct > 0:
        return "green"
    elif delta_p3ma_pct < 0 and delta_py_pct < 0:
        return "red"
    else:
        return "yellow"


def main():
    """Demo/test calculations."""
    print("=" * 60)
    print("Time Comparison Calculator Demo")
    print("=" * 60)

    # Example data
    report_date = date(2026, 1, 23)
    calc = TimeComparisonCalculator(report_date, days_elapsed=23)

    print(f"\nPeriod Context for {report_date}:")
    for key, value in calc.context.items():
        print(f"  {key}: {value}")

    # Example MTD metrics
    current_mtd = {
        "minutes_total": 3_500_000,
        "users_manpi": 125_000,
        "starts_total": 450_000
    }

    p3ma = {
        "minutes_total": 4_800_000,
        "users_manpi": 120_000,
        "starts_total": 480_000
    }

    prior_year = {
        "minutes_total": 4_200_000,
        "users_manpi": 100_000,
        "starts_total": 420_000
    }

    print("\n--- MTD Comparisons ---")
    results = calc.calculate_mtd_metrics(current_mtd, p3ma, prior_year)

    for metric, values in results.items():
        print(f"\n{metric}:")
        print(f"  MTD: {format_number(values['current_mtd'], 'count')}")
        print(f"  Paced: {format_number(values['mtd_paced'], 'count')}")
        print(f"  P3MA: {format_number(values['p3ma'], 'count')}")
        print(f"  vs P3MA: {format_number(values['delta_p3ma_pct'], 'delta_pct')}")
        print(f"  vs PY: {format_number(values['delta_py_pct'], 'delta_pct')}")
        color = get_signal_color(values['delta_p3ma_pct'], values['delta_py_pct'])
        print(f"  Signal: {color}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

"""
Mutual Fund Recommendation System

Recommends the top three mutual fund schemes for a selected
risk appetite using Sharpe ratio as the ranking metric.
"""

from pathlib import Path

import pandas as pd


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "07_scheme_performance.csv"


def load_performance_data():
    """Load mutual fund performance data."""

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Performance dataset not found: {DATA_PATH}"
        )

    return pd.read_csv(DATA_PATH)


def map_risk_appetite(risk_grade):
    """Map detailed risk grades to simplified risk appetites."""

    if risk_grade == "Low":
        return "Low"

    if risk_grade == "Moderate":
        return "Moderate"

    return "High"


def recommend_funds(performance, risk_appetite):
    """Return the top three funds for a selected risk appetite."""

    valid_risk_levels = {"low", "moderate", "high"}

    if risk_appetite.lower() not in valid_risk_levels:
        raise ValueError(
            "Risk appetite must be Low, Moderate, or High."
        )

    result = (
        performance[
            performance["risk_appetite"].str.lower()
            == risk_appetite.lower()
        ]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    return result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_1yr_pct",
            "return_3yr_pct",
            "max_drawdown_pct",
        ]
    ]


def main():
    """Run the interactive fund recommendation system."""

    performance = load_performance_data()

    performance["risk_appetite"] = (
        performance["risk_grade"]
        .apply(map_risk_appetite)
    )

    print("\nMutual Fund Recommendation System")
    print("---------------------------------")

    risk = input(
        "Enter risk appetite (Low / Moderate / High): "
    ).strip()

    recommendations = recommend_funds(
        performance,
        risk
    )

    if recommendations.empty:
        print("\nNo funds found for the selected risk appetite.")
        return

    print("\nTop 3 Recommended Funds:\n")
    print(recommendations.to_string(index=False))


if __name__ == "__main__":
    main()
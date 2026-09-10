"""
Fund Master Exploration

Displays unique fund houses, categories, sub-categories,
risk categories, and the total number of schemes.
"""

from pathlib import Path

import pandas as pd


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def explore_fund_master():
    """Explore key categorical fields in the Fund Master dataset."""

    file_path = RAW_DIR / "01_fund_master.csv"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Fund Master file not found: {file_path}"
        )

    fund = pd.read_csv(file_path)

    print("Unique Fund Houses:")
    print(fund["fund_house"].dropna().unique())

    print("\nCategories:")
    print(fund["category"].dropna().unique())

    print("\nSub Categories:")
    print(fund["sub_category"].dropna().unique())

    print("\nRisk Categories:")
    print(fund["risk_category"].dropna().unique())

    print(f"\nTotal Schemes: {len(fund):,}")


def main():
    """Run Fund Master exploration."""

    print("\nStarting Fund Master exploration...\n")
    explore_fund_master()
    print("\n✓ Fund Master exploration completed.")


if __name__ == "__main__":
    main()
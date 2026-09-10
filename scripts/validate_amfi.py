"""
AMFI Code Validation

Validates that every AMFI code present in the Fund Master dataset
also exists in the NAV History dataset.
"""

from pathlib import Path

import pandas as pd


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def validate_amfi_codes():
    """Compare AMFI codes between Fund Master and NAV History."""

    fund_path = RAW_DIR / "01_fund_master.csv"
    nav_path = RAW_DIR / "02_nav_history.csv"

    if not fund_path.exists():
        raise FileNotFoundError(f"Fund Master file not found: {fund_path}")

    if not nav_path.exists():
        raise FileNotFoundError(f"NAV History file not found: {nav_path}")

    fund = pd.read_csv(fund_path)
    nav = pd.read_csv(nav_path)

    fund_codes = set(fund["amfi_code"].dropna())
    nav_codes = set(nav["amfi_code"].dropna())

    missing_codes = fund_codes - nav_codes

    print(f"Fund Master Codes: {len(fund_codes):,}")
    print(f"NAV Codes: {len(nav_codes):,}")
    print(f"Missing Codes: {len(missing_codes):,}")

    if missing_codes:
        print("\nMissing AMFI Codes:")
        for code in sorted(missing_codes):
            print(code)

        raise ValueError(
            f"AMFI validation failed: {len(missing_codes)} "
            "Fund Master codes are missing from NAV History."
        )

    print("\n✓ All AMFI codes validated successfully.")


def main():
    """Run AMFI code validation."""

    print("\nStarting AMFI code validation...\n")
    validate_amfi_codes()
    print("\n✓ AMFI validation completed.")


if __name__ == "__main__":
    main()
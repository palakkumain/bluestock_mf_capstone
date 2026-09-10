"""
Data Cleaning Pipeline

Cleans the main Bluestock Mutual Fund datasets:
- NAV history
- Investor transactions
- Scheme performance

Cleaned files are saved to data/processed/.
"""

from pathlib import Path

import pandas as pd


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def find_file(prefix):
    """Find a raw CSV file using its dataset prefix."""
    matches = list(RAW_DIR.glob(f"*{prefix}*.csv"))

    if not matches:
        raise FileNotFoundError(
            f"No raw CSV file found for dataset: {prefix}"
        )

    return matches[0]


def clean_nav_history():
    """Clean NAV history data."""
    file_path = find_file("02_nav_history")
    nav = pd.read_csv(file_path)

    nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
    nav = nav.sort_values(["amfi_code", "date"])

    # Forward-fill missing NAV values within each fund
    nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

    nav = nav.drop_duplicates()
    nav = nav[nav["nav"] > 0]

    output_path = PROCESSED_DIR / "02_nav_history_clean.csv"
    nav.to_csv(output_path, index=False)

    print(f"✓ NAV history cleaned: {len(nav):,} rows")


def clean_investor_transactions():
    """Clean investor transaction data."""
    file_path = find_file("08_investor_transactions")
    tx = pd.read_csv(file_path)

    tx["transaction_date"] = pd.to_datetime(
        tx["transaction_date"],
        errors="coerce"
    )

    tx["transaction_type"] = (
        tx["transaction_type"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    tx["transaction_type"] = tx["transaction_type"].replace({
        "Sip": "SIP",
        "Lump Sum": "Lumpsum",
        "Redeem": "Redemption"
    })

    tx = tx[tx["amount_inr"] > 0]

    tx["kyc_status"] = (
        tx["kyc_status"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    output_path = PROCESSED_DIR / "08_investor_transactions_clean.csv"
    tx.to_csv(output_path, index=False)

    print(f"✓ Investor transactions cleaned: {len(tx):,} rows")


def clean_scheme_performance():
    """Clean scheme performance data."""
    file_path = find_file("07_scheme_performance")
    perf = pd.read_csv(file_path)

    numeric_columns = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "sharpe_ratio",
        "expense_ratio_pct"
    ]

    for column in numeric_columns:
        perf[column] = pd.to_numeric(
            perf[column],
            errors="coerce"
        )

    # Quality flags
    perf["negative_sharpe"] = perf["sharpe_ratio"] < 0

    perf["expense_issue"] = ~perf[
        "expense_ratio_pct"
    ].between(0.1, 2.5)

    output_path = PROCESSED_DIR / "07_scheme_performance_clean.csv"
    perf.to_csv(output_path, index=False)

    print(f"✓ Scheme performance cleaned: {len(perf):,} rows")


def main():
    """Run all dataset cleaning tasks."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    print("\nStarting data cleaning...\n")

    clean_nav_history()
    clean_investor_transactions()
    clean_scheme_performance()

    print("\n✓ Data cleaning completed successfully.")


if __name__ == "__main__":
    main()
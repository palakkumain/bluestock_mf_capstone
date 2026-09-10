"""
Data Ingestion and Initial Inspection

Reads all CSV files from data/raw and performs basic
validation and inspection of their structure.
"""

from pathlib import Path

import pandas as pd


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def inspect_csv(file_path):
    """Load and inspect a single CSV file."""
    print("=" * 60)
    print(file_path.name)
    print("=" * 60)

    df = pd.read_csv(file_path)

    print(f"Shape: {df.shape}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    return df


def main():
    """Inspect all CSV files in the raw data directory."""
    if not RAW_DIR.exists():
        raise FileNotFoundError(f"Raw data directory not found: {RAW_DIR}")

    csv_files = sorted(RAW_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {RAW_DIR}")

    for file_path in csv_files:
        inspect_csv(file_path)

    print("\nData ingestion and inspection completed successfully.")


if __name__ == "__main__":
    main()
"""
SQLite Database Creation

Loads cleaned CSV datasets from data/processed/ into a SQLite
database and verifies the created tables.
"""

import sqlite3
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DB_DIR = PROJECT_ROOT / "data" / "db"
DB_PATH = DB_DIR / "bluestock_mf.db"


FILES = {
    "fact_nav": "02_nav_history_clean.csv",
    "fact_transactions": "08_investor_transactions_clean.csv",
    "fact_performance": "07_scheme_performance_clean.csv",
}


def create_database():
    """Create the SQLite database and load cleaned datasets."""

    if not PROCESSED_DIR.exists():
        raise FileNotFoundError(
            f"Processed data directory not found: {PROCESSED_DIR}"
        )

    DB_DIR.mkdir(parents=True, exist_ok=True)

    engine = create_engine(f"sqlite:///{DB_PATH}")

    try:
        for table_name, file_name in FILES.items():
            file_path = PROCESSED_DIR / file_name

            if not file_path.exists():
                raise FileNotFoundError(
                    f"Required file not found: {file_path}"
                )

            df = pd.read_csv(file_path)

            df.to_sql(
                table_name,
                engine,
                if_exists="replace",
                index=False
            )

            print(
                f"✓ Loaded {table_name}: "
                f"{len(df):,} rows"
            )

    finally:
        engine.dispose()


def verify_database():
    """Verify that all expected tables were created."""

    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database was not created: {DB_PATH}"
        )

    with sqlite3.connect(DB_PATH) as connection:
        print("\nDatabase verification:")

        for table_name in FILES:
            query = f"SELECT COUNT(*) FROM {table_name}"
            count = connection.execute(query).fetchone()[0]

            print(f"✓ {table_name}: {count:,} rows")


def main():
    """Run database creation and verification."""

    print("\nStarting database creation...\n")

    create_database()
    verify_database()

    print("\n✓ Database created and verified successfully.")


if __name__ == "__main__":
    main()
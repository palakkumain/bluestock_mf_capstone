import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import os

print("Starting database creation...")

engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "fact_nav": "02_nav_history_clean.csv",
    "fact_transactions": "08_investor_transactions_clean.csv",
    "fact_performance": "07_scheme_performance_clean.csv"
}

try:
    for table, file in files.items():
        path = f"data/processed/{file}"
        print(f"Reading: {path}")

        if not os.path.exists(path):
            print(f"❌ File not found: {path}")
            continue

        df = pd.read_csv(path)
        df.to_sql(table, engine, if_exists="replace", index=False)
        print(f"✅ Loaded {table}: {len(df)} rows")

    conn = sqlite3.connect("bluestock_mf.db")
    print("\nVerification:")

    for table in files.keys():
        try:
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"{table}: {count} rows")
        except Exception as e:
            print(f"Error checking {table}: {e}")

    conn.close()
    print("\n🎉 Database created successfully!")

except Exception as e:
    print("ERROR:", e)
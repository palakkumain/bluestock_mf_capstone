#  Task 1: Clean NAV History  


import pandas as pd
import os

RAW = "data/raw"
OUT = "data/processed"

os.makedirs(OUT, exist_ok=True)

# Read NAV file
nav = pd.read_csv(f"{RAW}/1788499983331-4389156d-02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

# Sort by fund and date
nav = nav.sort_values(["amfi_code", "date"])

# Forward fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
nav = nav.drop_duplicates()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(f"{OUT}/02_nav_history_clean.csv", index=False)

print("Done! Cleaned rows:", len(nav))

#  Task 2: Clean Investor Transactions 

tx = pd.read_csv(f"{RAW}/1788499980509-304c1255-08_investor_transactions.csv")

# Convert date format
tx["transaction_date"] = pd.to_datetime(tx["transaction_date"], errors="coerce")

# Standardize transaction types
tx["transaction_type"] = tx["transaction_type"].str.strip().str.title()

tx["transaction_type"] = tx["transaction_type"].replace({
    "Sip": "SIP",
    "Lump Sum": "Lumpsum",
    "Redeem": "Redemption"
})

# Keep only positive amounts
tx = tx[tx["amount_inr"] > 0]

# Fix KYC values
tx["kyc_status"] = tx["kyc_status"].replace({
    "verified": "Verified",
    "pending": "Pending"
})

# Save cleaned file
tx.to_csv(f"{OUT}/08_investor_transactions_clean.csv", index=False)

print("Transactions cleaned:", len(tx))

#  Task 3: Clean Scheme Performance 

perf = pd.read_csv(f"{RAW}/1788499985420-bb134abf-07_scheme_performance.csv")

# Convert numeric columns
cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "sharpe_ratio",
    "expense_ratio_pct"
]

for c in cols:
    perf[c] = pd.to_numeric(perf[c], errors="coerce")

# Flag negative Sharpe ratios
perf["negative_sharpe"] = perf["sharpe_ratio"] < 0

# Flag expense ratios outside 0.1–2.5%
perf["expense_issue"] = ~perf["expense_ratio_pct"].between(0.1, 2.5)

# Save cleaned file
perf.to_csv(f"{OUT}/07_scheme_performance_clean.csv", index=False)

print("Performance cleaned:", len(perf))
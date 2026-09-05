import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

missing = set(fund["amfi_code"]) - set(nav["amfi_code"])

print("Fund Master Codes:", fund["amfi_code"].nunique())
print("NAV Codes:", nav["amfi_code"].nunique())
print("Missing Codes:", len(missing))

if missing:
    print(missing)
else:
    print("All AMFI codes validated successfully.")
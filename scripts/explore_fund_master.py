import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")

print("Unique Fund Houses:")
print(fund["fund_house"].unique())

print("\nCategories:")
print(fund["category"].unique())

print("\nSub Categories:")
print(fund["sub_category"].unique())

print("\nRisk Grades:")
print(fund["risk_category"].unique())

print("\nTotal Schemes:", len(fund))
import pandas as pd
import os

RAW = "data/raw"

for file in sorted(os.listdir(RAW)):
    if file.endswith(".csv"):
        print("=" * 60)
        print(file)

        df = pd.read_csv(os.path.join(RAW, file))

        print("Shape:", df.shape)
        print("\nData Types:")
        print(df.dtypes)
        print("\nFirst 5 Rows:")
        print(df.head())
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("\n")
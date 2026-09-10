"""
Live NAV Fetcher

Fetches current NAV data for selected mutual fund schemes
from the MFAPI service and saves the results to data/raw/live_nav/.
"""

from pathlib import Path

import pandas as pd
import requests


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LIVE_NAV_DIR = PROJECT_ROOT / "data" / "raw" / "live_nav"

# Selected mutual fund schemes
SCHEMES = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841,
}


def fetch_nav(scheme_name, scheme_code):
    """Fetch and save NAV data for one mutual fund scheme."""

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    if "data" not in data:
        raise ValueError(
            f"No NAV data returned for {scheme_name} ({scheme_code})"
        )

    df = pd.DataFrame(data["data"])

    output_path = LIVE_NAV_DIR / f"{scheme_name}_{scheme_code}.csv"
    df.to_csv(output_path, index=False)

    print(f"✓ {scheme_name}: saved {len(df):,} records")


def main():
    """Fetch NAV data for all selected schemes."""

    LIVE_NAV_DIR.mkdir(parents=True, exist_ok=True)

    print("\nStarting live NAV fetch...\n")

    for scheme_name, scheme_code in SCHEMES.items():
        try:
            fetch_nav(scheme_name, scheme_code)
        except (requests.RequestException, ValueError) as error:
            print(f"✗ {scheme_name}: {error}")

    print("\n✓ Live NAV fetch completed.")


if __name__ == "__main__":
    main()
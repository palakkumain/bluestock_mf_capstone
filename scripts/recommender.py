
import pandas as pd

# Load fund performance data
performance = pd.read_csv("07_scheme_performance.csv")

# Map detailed risk grades to requested risk appetites
def map_risk_appetite(risk_grade):
    if risk_grade == "Low":
        return "Low"
    elif risk_grade == "Moderate":
        return "Moderate"
    else:
        return "High"

performance["risk_appetite"] = performance["risk_grade"].apply(
    map_risk_appetite
)

# Fund recommender
def recommend_funds(risk_appetite):
    result = (
        performance[
            performance["risk_appetite"].str.lower()
            == risk_appetite.lower()
        ]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    return result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_1yr_pct",
            "return_3yr_pct",
            "max_drawdown_pct"
        ]
    ]

# Example
if __name__ == "__main__":
    risk = input("Enter risk appetite (Low / Moderate / High): ")
    print(recommend_funds(risk).to_string(index=False))

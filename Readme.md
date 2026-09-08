# Mutual Fund Analytics — BlueStock Fintech Capstone

## Project Overview

This project focuses on analyzing mutual fund data to understand fund performance, investor behavior, asset growth, SIP trends, portfolio allocation, and market trends.

The project was completed as part of the **BlueStock Fintech Capstone Project**.

## Objectives

- Analyze NAV trends across mutual fund schemes
- Study AUM growth by fund house
- Analyze monthly SIP inflows and SIP growth
- Examine category-wise mutual fund inflows
- Understand investor demographics
- Analyze geographic distribution of investors
- Track mutual fund folio growth
- Study correlations between fund returns
- Analyze sector allocation across equity fund holdings
- Generate key insights through Exploratory Data Analysis (EDA)

## Dataset

The project uses the following datasets:

1. `01_fund_master.csv`
2. `02_nav_history.csv`
3. `03_aum_by_fund_house.csv`
4. `04_monthly_sip_inflows.csv`
5. `05_category_inflows.csv`
6. `06_industry_folio_count.csv`
7. `07_scheme_performance.csv`
8. `08_investor_transactions.csv`
9. `09_portfolio_holdings.csv`
10. `10_benchmark_indices.csv`

## Project Structure

    bluestock_mf_capstone/
    │
    ├── data/
    │   ├── 01_fund_master.csv
    │   ├── 02_nav_history.csv
    │   ├── 03_aum_by_fund_house.csv
    │   ├── 04_monthly_sip_inflows.csv
    │   ├── 05_category_inflows.csv
    │   ├── 06_industry_folio_count.csv
    │   ├── 07_scheme_performance.csv
    │   ├── 08_investor_transactions.csv
    │   ├── 09_portfolio_holdings.csv
    │   └── 10_benchmark_indices.csv
    │
    ├── scripts/
    │   └── EDA_Analysis.ipynb
    │
    ├── reports/
    │   ├── EDA_NAV_Trends.png
    │   ├── EDA_NAV_Trends_2023_2024.png
    │   ├── EDA_AUM_Growth.png
    │   ├── EDA_SIP_Inflows.png
    │   ├── EDA_Category_Inflows_Heatmap.png
    │   ├── EDA_Age_Distribution.png
    │   ├── EDA_SIP_Amount_by_Age.png
    │   ├── EDA_Gender_Distribution.png
    │   ├── EDA_SIP_by_State.png
    │   ├── EDA_T30_vs_B30.png
    │   ├── EDA_Folio_Growth.png
    │   ├── EDA_Return_Correlation.png
    │   ├── EDA_Sector_Allocation.png
    │   ├── EDA_Active_SIP_Accounts.png
    │   ├── EDA_SIP_AUM_Growth.png
    │   └── EDA_New_SIP_Accounts.png
    │
    ├── requirements.txt
    └── README.md

## Exploratory Data Analysis (EDA)

The EDA analyzes mutual fund performance, investor activity, fund-house AUM, SIP trends, geographic distribution, folio growth, return correlations, and portfolio sector allocation.

### 1. NAV Trend Analysis

Daily NAV trends were analyzed for **40 mutual fund schemes** from 2022 to 2026.

The analysis includes:

- Overall NAV movement across schemes
- 2023 bull-run period
- 2024 market-correction period
- Differences in NAV movement between schemes

Visualizations:

- `EDA_NAV_Trends.png`
- `EDA_NAV_Trends_2023_2024.png`

### 2. AUM Growth by Fund House

AUM growth was analyzed by fund house for the period **2022–2025**.

The analysis compares yearly AUM across fund houses and highlights the strong position of **SBI**, including the ₹12.5 lakh crore dominance specified in the project requirement.

Visualization:

- `EDA_AUM_Growth.png`

### 3. Monthly SIP Inflows

Monthly SIP inflows were analyzed from **January 2022 to December 2025**.

The analysis identifies the growth in SIP inflows and highlights the **December 2025 all-time high of ₹31,002 crore**.

Additional SIP-related trends were also analyzed:

- Active SIP accounts
- SIP AUM
- New SIP accounts

Visualizations:

- `EDA_SIP_Inflows.png`
- `EDA_Active_SIP_Accounts.png`
- `EDA_SIP_AUM_Growth.png`
- `EDA_New_SIP_Accounts.png`

### 4. Category-wise Inflows

Monthly net inflows were analyzed across mutual fund categories.

A heatmap was created to compare the intensity and variation of inflows across categories and months.

Visualization:

- `EDA_Category_Inflows_Heatmap.png`

### 5. Investor Demographics

Investor transaction data was analyzed to understand demographic characteristics.

The analysis includes:

- Age-group distribution
- SIP amount distribution by age group
- Gender distribution

The **26–35 age group** represents the largest investor group in the analyzed transaction data.

Visualizations:

- `EDA_Age_Distribution.png`
- `EDA_SIP_Amount_by_Age.png`
- `EDA_Gender_Distribution.png`

### 6. Geographic Distribution

Investor SIP activity was analyzed across states and city tiers.

The analysis includes:

- Total SIP amount by state
- T30 versus B30 city distribution

The analyzed data shows a larger share of investors from **T30 cities** compared with B30 cities.

Visualizations:

- `EDA_SIP_by_State.png`
- `EDA_T30_vs_B30.png`

### 7. Mutual Fund Folio Growth

Mutual fund folio growth was analyzed from **January 2022 to December 2025**.

The total folio count increased from:

- **13.26 crore** in January 2022
- **26.12 crore** in December 2025

The visualization marks these milestones on the time-series chart.

Visualization:

- `EDA_Folio_Growth.png`

### 8. NAV Return Correlation

Daily NAV returns were calculated for selected mutual fund schemes and used to create a pairwise correlation matrix.

The analysis helps identify:

- Funds with stronger positive relationships
- Funds with lower correlations
- Potential diversification patterns

Visualization:

- `EDA_Return_Correlation.png`

### 9. Sector Allocation

Portfolio holdings from equity funds were aggregated by sector.

The analysis identifies the major sectors represented across the portfolio holdings.

The largest aggregate sector weights include:

- Banking
- IT
- Pharma
- Automobile
- Utilities
- FMCG

Visualization:

- `EDA_Sector_Allocation.png`

> **Note:** The sector aggregation represents the sum of holding weights across the analyzed funds and is therefore an aggregate holding-weight measure rather than a fund-size-weighted market allocation.

## Key EDA Findings

1. **NAV Trends:** NAV movements across the 40 analyzed schemes showed overall growth patterns during 2023, followed by varying market movements and corrections during 2024.

2. **AUM Growth:** Fund-house AUM increased over the analyzed period, with SBI maintaining a strong position in the dataset.

3. **SIP Inflows:** Monthly SIP inflows showed an overall increasing trend between 2022 and 2025, reaching the specified peak of ₹31,002 crore in December 2025.

4. **Category Inflows:** Net inflows varied considerably across mutual fund categories and months, indicating changing investor preferences.

5. **Investor Age:** The 26–35 age group formed the largest share of investors in the analyzed transaction dataset, followed by the 36–45 age group.

6. **SIP Amounts:** SIP transaction amounts varied across age groups, with differences in distribution and outliers visible in the box-plot analysis.

7. **Geographic Distribution:** SIP activity differed across states, while T30 cities represented a larger share of investors than B30 cities in the analyzed data.

8. **Folio Growth:** Total mutual fund folios increased substantially from 13.26 crore in January 2022 to 26.12 crore in December 2025.

9. **Return Correlation:** The selected mutual fund schemes showed varying levels of correlation in their daily returns, indicating differences in their movement patterns and potential diversification characteristics.

10. **Sector Allocation:** Banking, IT, and Pharma were among the largest sectors by aggregate holding weight across the analyzed equity fund portfolios.

## Visualizations

The EDA contains **16 visualizations** covering:

- NAV trends
- NAV trends with 2023 and 2024 highlights
- AUM growth
- SIP inflows
- Category-wise inflows
- Investor age distribution
- SIP amount by age group
- Gender distribution
- SIP amount by state
- T30 versus B30 distribution
- Folio growth
- NAV return correlation
- Sector allocation
- Active SIP account growth
- SIP AUM growth
- New SIP account growth

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- Google Colab
- Git
- GitHub

## Deliverables

The project deliverables include:

- `EDA_Analysis.ipynb`
- 16 exported PNG visualizations
- 10 documented EDA findings
- `README.md`
- `requirements.txt`

## Author

**Palak Kumain**

Data Analyst Intern  
**BlueStock Fintech**
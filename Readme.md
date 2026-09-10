# Mutual Fund Analytics — BlueStock Fintech Capstone

## Project Overview

This project is a comprehensive Mutual Fund Analytics solution developed as part of the **BlueStock Fintech Capstone Project**.

The project covers the complete analytics workflow, including:

- Data ingestion and ETL
- Data cleaning and preprocessing
- SQLite database creation and SQL analysis
- Exploratory Data Analysis (EDA)
- Mutual fund performance analytics
- Investor behavior analysis
- SIP and market trend analysis
- Risk analytics using VaR and CVaR
- Rolling Sharpe ratio analysis
- Investor cohort analysis
- SIP continuity analysis
- Fund recommendation system
- Portfolio concentration analysis using HHI
- Interactive Power BI dashboard

## Objectives

The main objectives of the project are to:

- Analyze NAV trends across mutual fund schemes
- Study AUM growth by fund house
- Analyze monthly SIP inflows and SIP growth
- Examine category-wise mutual fund inflows
- Understand investor demographics and transaction behavior
- Analyze geographic distribution of investors
- Track mutual fund folio growth
- Evaluate fund performance using return and risk metrics
- Calculate Sharpe ratio, Beta, Alpha and other performance measures
- Calculate Historical VaR and CVaR
- Analyze investor cohorts
- Evaluate SIP continuity
- Build a simple risk-based fund recommender
- Analyze portfolio concentration using HHI
- Build an interactive Power BI dashboard
- Generate actionable insights from mutual fund and investor data

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

The raw datasets are stored under:

`data/raw/`

Processed datasets and analytical outputs are stored under:

`data/processed/`

## Project Structure

    bluestock_mf_capstone/
    │
    ├── data/
    │   ├── raw/
    │   │   ├── 01_fund_master.csv
    │   │   ├── 02_nav_history.csv
    │   │   ├── 03_aum_by_fund_house.csv
    │   │   ├── 04_monthly_sip_inflows.csv
    │   │   ├── 05_category_inflows.csv
    │   │   ├── 06_industry_folio_count.csv
    │   │   ├── 07_scheme_performance.csv
    │   │   ├── 08_investor_transactions.csv
    │   │   ├── 09_portfolio_holdings.csv
    │   │   └── 10_benchmark_indices.csv
    │   │
    │   ├── processed/
    │   │   ├── alpha_beta.csv
    │   │   ├── fund_scorecard.csv
    │   │   ├── tracking_error.csv
    │   │   ├── var_cvar_report.csv
    │   │   ├── investor_cohort_analysis.csv
    │   │   ├── sip_continuity_analysis.csv
    │   │   └── sector_hhi_analysis.csv
    │   │
    │   └── db/
    │
    ├── notebooks/
    │   ├── EDA_Analysis.ipynb
    │   ├── Performance_Analytics.ipynb
    │   └── Advanced_Analytics.ipynb
    │
    ├── scripts/
    │   ├── clean_data.py
    │   ├── create_db.py
    │   ├── data_ingestion.py
    │   ├── explore_fund_master.py
    │   ├── live_nav_fetch.py
    │   ├── validate_amfi.py
    │   └── recommender.py
    │
    ├── sql/
    │   ├── schema.sql
    │   └── queries.sql
    │
    ├── dashboard/
    │   └── Mutual_Fund_Analytics_Bluestock.pbix
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
    │   ├── EDA_New_SIP_Accounts.png
    │   ├── rolling_sharpe_chart.png
    │   └── Mutual_Fund_Analytics_Bluestock.pdf
    │
    ├── requirements.txt
    ├── README.md
    └── .gitignore

The SQLite database file is intentionally excluded from Git tracking. The database schema and SQL queries are provided through `sql/schema.sql` and `sql/queries.sql`.

## 1. Data Ingestion and ETL

The project includes Python scripts for data ingestion, validation, cleaning and database preparation.

Key scripts include:

- `data_ingestion.py`
- `clean_data.py`
- `validate_amfi.py`
- `create_db.py`
- `live_nav_fetch.py`

The ETL workflow prepares raw datasets for analysis and database loading.

The project uses Python file-path handling to support reproducible execution without relying on machine-specific absolute paths.

## 2. SQLite Database and SQL Analysis

A SQLite database was created to support structured querying and relational analysis.

Database-related files include:

- `create_db.py`
- `schema.sql`
- `queries.sql`

The database schema supports relationships between:

- Fund master data
- NAV history
- Scheme performance
- Investor transactions
- Portfolio holdings

The SQLite database itself is excluded from GitHub through `.gitignore`.

## 3. Exploratory Data Analysis

The EDA analyzes mutual fund performance, investor activity, fund-house AUM, SIP trends, geographic distribution, folio growth, return correlations and portfolio sector allocation.

### NAV Trend Analysis

Daily NAV trends were analyzed across **40 mutual fund schemes** from 2022 onward.

The analysis includes:

- Overall NAV movement
- Period-based trend analysis
- Differences in NAV movement between schemes

Visualizations:

- `EDA_NAV_Trends.png`
- `EDA_NAV_Trends_2023_2024.png`

### AUM Growth by Fund House

AUM growth was analyzed by fund house across the available time period.

Visualization:

- `EDA_AUM_Growth.png`

### Monthly SIP Inflows

Monthly SIP inflows were analyzed to understand long-term growth and changes in investor participation.

The analysis also covers:

- Active SIP accounts
- SIP AUM
- New SIP accounts

Visualizations:

- `EDA_SIP_Inflows.png`
- `EDA_Active_SIP_Accounts.png`
- `EDA_SIP_AUM_Growth.png`
- `EDA_New_SIP_Accounts.png`

### Category-wise Inflows

Monthly net inflows were analyzed across mutual fund categories.

Visualization:

- `EDA_Category_Inflows_Heatmap.png`

### Investor Demographics

Investor transaction data was analyzed by:

- Age group
- Gender
- Transaction amount

Visualizations:

- `EDA_Age_Distribution.png`
- `EDA_SIP_Amount_by_Age.png`
- `EDA_Gender_Distribution.png`

### Geographic Distribution

Investor activity was analyzed across states and city tiers.

Visualizations:

- `EDA_SIP_by_State.png`
- `EDA_T30_vs_B30.png`

### Folio Growth

Mutual fund folio growth was analyzed over time.

Visualization:

- `EDA_Folio_Growth.png`

The analyzed data showed growth from approximately **13.26 crore folios in January 2022 to 26.12 crore in December 2025**.

### NAV Return Correlation

Daily NAV returns were used to analyze correlations between selected mutual fund schemes.

Visualization:

- `EDA_Return_Correlation.png`

The correlation analysis helps identify funds with similar movement patterns and potential diversification differences.

### Sector Allocation

Portfolio holdings were aggregated by sector to understand sector exposure across the analyzed equity fund holdings.

Visualization:

- `EDA_Sector_Allocation.png`

## 4. Performance Analytics

Performance analytics were performed using scheme performance and NAV datasets.

The analysis includes:

- 1-year returns
- 3-year returns
- 5-year returns
- Benchmark comparison
- Alpha
- Beta
- Sharpe ratio
- Sortino ratio
- Standard deviation
- Maximum drawdown
- Tracking error
- Fund scorecard

Supporting outputs include:

- `alpha_beta.csv`
- `fund_scorecard.csv`
- `tracking_error.csv`

The calculations are documented in:

`notebooks/Performance_Analytics.ipynb`

## 5. Interactive Power BI Dashboard

An interactive Power BI dashboard was developed to present the major findings.

The dashboard contains four primary analytical pages.

### Industry Overview

Includes:

- Total AUM
- SIP inflows
- Folios
- Number of schemes
- Industry AUM trend
- AUM by fund house

### Fund Performance

Includes:

- Return vs risk analysis
- Fund performance table
- NAV trends
- Fund house/category/plan filters

### Investor Analytics

Includes:

- Transaction amount by state
- Transaction type analysis
- Average transaction by age group
- Transaction volume trends
- Investor filters

### SIP & Market Trends

Includes:

- SIP inflow trends
- Benchmark market trends
- Category-wise inflow analysis
- Top categories
- Interactive filters

A NAV drill-through page is also included for scheme-level analysis.

Power BI file:

`dashboard/Mutual_Fund_Analytics_Bluestock.pbix`

## 6. Advanced Analytics

Advanced analytics were implemented to extend the project beyond descriptive analysis.

### Historical VaR and CVaR

Historical **95% Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)** were calculated for all **40 schemes** using historical daily NAV returns.

Output:

`data/processed/var_cvar_report.csv`

More negative values indicate greater historical downside risk.

### Rolling 90-Day Sharpe Ratio

A 90-day rolling Sharpe ratio was calculated for five key funds.

Visualization:

`reports/rolling_sharpe_chart.png`

### Investor Cohort Analysis

Investors were grouped according to their first transaction year.

The analysis compares:

- Investor count
- Total invested amount
- Average transaction amount
- Preferred fund

Output:

`data/processed/investor_cohort_analysis.csv`

### SIP Continuity Analysis

SIP transaction history was analyzed to identify investors with regular versus potentially at-risk SIP behavior.

The analysis considered transaction gaps for investors with sufficient SIP history.

Output:

`data/processed/sip_continuity_analysis.csv`

### Fund Recommender

A simple risk-based fund recommendation system was developed using fund risk classification and Sharpe ratio.

The recommender supports:

- Low-risk funds
- Moderate-risk funds
- High-risk funds

Script:

`scripts/recommender.py`

### Portfolio Concentration — HHI

The Herfindahl-Hirschman Index (HHI) was calculated to evaluate portfolio concentration across equity fund holdings.

Output:

`data/processed/sector_hhi_analysis.csv`

## 7. Key Findings

The analysis generated several important findings:

1. **NAV Trends:** The 40 analyzed schemes showed different NAV growth patterns and varying responses to market movements.

2. **AUM Growth:** Fund-house AUM increased over the analyzed period, with SBI representing one of the strongest fund-house positions in the dataset.

3. **SIP Growth:** Monthly SIP inflows demonstrated strong growth over the analyzed period, reaching approximately **₹31,002 crore in December 2025**.

4. **Folio Growth:** Total mutual fund folios increased substantially, from approximately **13.26 crore in January 2022 to 26.12 crore in December 2025**.

5. **Investor Demographics:** The **26–35 age group** represented the largest investor group in the analyzed transaction dataset.

6. **Fund Risk:** Historical VaR and CVaR showed meaningful differences in downside risk across the 40 analyzed schemes.

7. **Rolling Sharpe:** Rolling Sharpe analysis demonstrated that risk-adjusted performance varied across funds and over time.

8. **SIP Continuity:** Among investors meeting the minimum SIP-history criterion, the majority were classified as At-Risk based on their average transaction gap.

9. **Portfolio Concentration:** HHI analysis identified differences in portfolio concentration across funds, with some schemes showing substantially higher concentration than others.

10. **Fund Recommendation:** The risk-based recommender identified funds with comparatively stronger Sharpe ratios within each risk group.

## 8. Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLite
- SQL
- Power BI
- Jupyter Notebook
- Google Colab
- Git
- GitHub

## 9. Project Deliverables

### Data & ETL

- Raw mutual fund datasets
- Data cleaning scripts
- Data ingestion scripts
- Database creation scripts

### SQL

- Database schema
- SQL queries

### EDA

- EDA notebook
- 16 exported visualizations
- Analytical findings

### Performance Analytics

- Performance analytics notebook
- Alpha/Beta analysis
- Fund scorecard
- Tracking error analysis

### Dashboard

- Interactive Power BI dashboard
- Industry overview
- Fund performance
- Investor analytics
- SIP and market trends
- NAV drill-through

### Advanced Analytics

- Advanced analytics notebook
- VaR/CVaR report
- Rolling Sharpe analysis
- Investor cohort analysis
- SIP continuity analysis
- Fund recommender
- HHI analysis

### Reports

- Power BI PDF export
- Analytical visualizations

## 10. Future Enhancements

Potential future improvements include:

- Automated weekday NAV ingestion
- Streamlit web application
- Monte Carlo NAV simulation
- Markowitz efficient frontier
- Automated weekly performance email reports
- Additional portfolio optimization techniques
- Real-time market data integration

## Author

**Palak Kumain**

Data Analyst Intern  
**BlueStock Fintech**
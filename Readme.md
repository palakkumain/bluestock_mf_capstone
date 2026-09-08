# BlueStock Fintech – Mutual Fund Analytics

## Project Overview

This project is part of the BlueStock Fintech Mutual Fund Analytics Capstone. It covers the end-to-end analysis of mutual fund data, including data cleaning, database design, SQL analytics, fund performance evaluation, risk-adjusted performance analysis, and benchmark comparison.

The project combines Python, Pandas, NumPy, SQLite, SQLAlchemy, SciPy, and data visualization techniques to derive meaningful insights from mutual fund datasets.

## Objectives

- Clean and validate mutual fund datasets
- Standardize date, NAV, and transaction formats
- Handle missing values and duplicate records
- Design and build a SQLite database using a star schema
- Write analytical SQL queries for mutual fund and SIP analysis
- Calculate daily fund returns
- Calculate 1-year and 3-year CAGR
- Evaluate Sharpe and Sortino ratios
- Calculate Alpha and Beta against the NIFTY 100
- Calculate Maximum Drawdown and identify the worst drawdown period
- Develop a 0–100 mutual fund performance scorecard
- Compare top-performing funds against NIFTY 50 and NIFTY 100
- Calculate benchmark tracking error
- Generate analytical outputs and visualizations

## Tools & Technologies

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- SQLite
- SQLAlchemy
- Jupyter Notebook / Google Colab
- Git & GitHub

## Folder Structure

bluestock_mf_capstone/
├── dashboard/
├── data/
│   ├── raw/
│   │   ├── 01_fund_master.csv
│   │   ├── 02_nav_history.csv
│   │   └── 10_benchmark_indices.csv
│   └── processed/
│       ├── fund_scorecard.csv
│       ├── alpha_beta.csv
│       └── tracking_error.csv
├── reports/
│   └── benchmark_comparison.png
├── scripts/
│   └── Performance_Analytics.ipynb
├── sql/
├── bluestock_mf.db
├── README.md
└── requirements.txt

## Data Analysis

### 1. Data Cleaning & Validation

The datasets were inspected and prepared for analysis by:

- Standardizing date formats
- Checking missing values
- Checking duplicate records
- Validating data types
- Checking the number of mutual fund schemes
- Validating historical NAV observations

### 2. Daily Returns

Daily fund returns were calculated using:

Daily Return = (NAV_t / NAV_(t-1)) - 1

The distribution of daily returns was also analyzed to identify unusual observations and understand return behavior across the schemes.

### 3. CAGR Analysis

Compound Annual Growth Rate was calculated for:

- 1-year period
- 3-year period
- 5-year period where sufficient historical data was available

The available dataset contained at least three years of observations for all 40 schemes, but did not provide five years of historical data for the complete set of schemes. Therefore, 5-year CAGR was reported as unavailable rather than estimated.

Formula:

CAGR = (Ending NAV / Beginning NAV)^(1 / Number of Years) - 1

### 4. Sharpe Ratio

The Sharpe Ratio was calculated to evaluate risk-adjusted returns.

A 6.5% annual risk-free rate was used as the RBI repo-rate proxy.

Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Standard Deviation

The annualized ratio was used to rank the 40 schemes.

### 5. Sortino Ratio

The Sortino Ratio was calculated using downside deviation to focus specifically on negative/downside performance.

This provides a risk-adjusted performance measure that penalizes downside volatility rather than total volatility.

### 6. Alpha & Beta

Fund returns were regressed against NIFTY 100 benchmark returns using Ordinary Least Squares regression.

The analysis provides:

- Alpha
- Beta
- R-squared

Annualized Alpha was calculated from the regression intercept.

### 7. Maximum Drawdown

Maximum Drawdown was calculated using the running maximum NAV:

Drawdown = NAV / Running Maximum NAV - 1

The analysis identifies:

- Maximum drawdown
- Drawdown starting date
- Drawdown ending date

### 8. Fund Performance Scorecard

A 0–100 composite score was created to rank the 40 mutual fund schemes.

The scoring weights are:

| Metric | Weight |
|---|---:|
| 3-Year Return | 30% |
| Sharpe Ratio | 25% |
| Alpha | 20% |
| Expense Ratio | 15% |
| Maximum Drawdown | 10% |

Higher returns, Sharpe Ratio, and Alpha receive higher scores, while lower expense ratios and lower drawdown severity receive higher scores.

### 9. Benchmark Comparison

The top 5 funds from the performance scorecard were compared against:

- NIFTY 50
- NIFTY 100

The comparison covers the available three-year period and normalizes each series to a starting value of 100.

### 10. Tracking Error

Tracking Error was calculated to measure the volatility of the difference between fund returns and benchmark returns.

Tracking Error = Std(Fund Return - Benchmark Return) × √252

The Top 5 funds were evaluated against the NIFTY 100 benchmark.

## Key Deliverables

### Performance Analytics

- `Performance_Analytics.ipynb`
- `fund_scorecard.csv`
- `alpha_beta.csv`
- `tracking_error.csv`
- `benchmark_comparison.png`

### Database & SQL Analytics

- Cleaned mutual fund datasets
- SQLite database (`bluestock_mf.db`)
- Star schema definition
- Analytical SQL queries
- Data dictionary
- Python data-cleaning script

## Setup & Installation

### 1. Clone the Repository

    git clone https://github.com/palakkumain/bluestock_mf_capstone.git
    cd bluestock_mf_capstone

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Run the Performance Analytics

Open:

    scripts/Performance_Analytics.ipynb

The notebook can be executed using Jupyter Notebook or Google Colab.

### 4. Build the SQLite Database

    sqlite3 bluestock_mf.db < sql/schema.sql

### 5. Run Analytical SQL Queries

    sqlite3 bluestock_mf.db < sql/queries.sql

## Repository Outputs

The repository contains:

- Raw source datasets
- Processed analytical outputs
- Performance analytics notebook
- Benchmark visualization
- SQLite database
- SQL schema and analytical queries
- Supporting documentation

## Status

**Complete — ready for submission.**

## Author

**Palak Kumain**

BCA (AI & Data Science)  
Graphic Era Hill University
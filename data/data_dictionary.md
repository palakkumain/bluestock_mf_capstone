# BlueStock Mutual Fund Data Dictionary

## Source Files

| File | Description |
|------|-------------|
| 01_fund_master.csv | Master list of mutual funds |
| 02_nav_history.csv | Historical NAV data |
| 07_scheme_performance.csv | Fund performance metrics |
| 08_investor_transactions.csv | Investor transaction records |



## 02_nav_history

| Column | Type | Business Definition |
|--------|------|---------------------|
| amfi_code | TEXT | AMFI scheme identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |



## 08_investor_transactions

| Column | Type | Business Definition |
|--------|------|---------------------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| amfi_code | TEXT | Fund identifier |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| kyc_status | TEXT | KYC verification status |



## 07_scheme_performance

| Column | Type | Business Definition |
|--------|------|---------------------|
| return_1yr_pct | REAL | One-year return |
| return_3yr_pct | REAL | Three-year CAGR |
| return_5yr_pct | REAL | Five-year CAGR |
| sharpe_ratio | REAL | Risk-adjusted return |
| expense_ratio_pct | REAL | Annual expense ratio |
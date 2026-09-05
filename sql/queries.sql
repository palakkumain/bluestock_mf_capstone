-- 1. Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT substr(nav_date,1,7) AS month,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. SIP inflow YoY growth
SELECT substr(transaction_date,1,4) AS year,
       SUM(amount_inr) AS sip_total
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

-- 4. Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with expense ratio below 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Highest 5-year return
SELECT *
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Average transaction amount
SELECT AVG(amount_inr) AS avg_amount
FROM fact_transactions;

-- 8. Total redemption amount
SELECT SUM(amount_inr) AS redemption_total
FROM fact_transactions
WHERE transaction_type='Redemption';

-- 9. Monthly transaction count
SELECT substr(transaction_date,1,7) AS month,
       COUNT(*) AS total
FROM fact_transactions
GROUP BY month;

-- 10. Average Sharpe Ratio
SELECT AVG(sharpe_ratio) AS avg_sharpe
FROM fact_performance;
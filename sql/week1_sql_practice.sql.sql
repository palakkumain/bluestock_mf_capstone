-- ============================================================
-- SQL PRACTICE QUERIES: Customer Orders, Revenue & Product Performance
-- Domain: Mutual Fund Investor Transactions
-- Tables: fund_master (products), investor_transactions (orders)
-- ============================================================

-- 1. SELECT + WHERE
-- All SIP transactions above Rs. 5,000
SELECT investor_id, transaction_date, amount_inr, state
FROM investor_transactions
WHERE transaction_type = 'SIP' AND amount_inr > 5000
LIMIT 20;

-- 2. ORDER BY
-- Top 10 highest-value transactions of any type
SELECT investor_id, transaction_type, amount_inr, transaction_date
FROM investor_transactions
ORDER BY amount_inr DESC
LIMIT 10;

-- 3. GROUP BY + Aggregate Functions
-- Total revenue (inflow) and transaction count by transaction type
-- Note: "Revenue" here = SIP + Lumpsum inflows; Redemption is outflow
SELECT
    transaction_type,
    COUNT(*)          AS num_transactions,
    SUM(amount_inr)    AS total_amount,
    ROUND(AVG(amount_inr), 2) AS avg_amount
FROM investor_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;

-- 4. GROUP BY + HAVING
-- States contributing more than Rs. 25 crore in total transaction value
SELECT
    state,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
HAVING SUM(amount_inr) > 250000000
ORDER BY total_amount DESC;

-- 5. JOIN
-- Revenue (SIP + Lumpsum only) by fund house and scheme
SELECT
    fm.fund_house,
    fm.scheme_name,
    fm.category,
    SUM(it.amount_inr) AS total_inflow
FROM investor_transactions it
JOIN fund_master fm ON it.amfi_code = fm.amfi_code
WHERE it.transaction_type IN ('SIP', 'Lumpsum')
GROUP BY fm.amfi_code, fm.scheme_name
ORDER BY total_inflow DESC
LIMIT 15;

-- 6. Product Performance Ranking
-- Best performing schemes by net inflow (inflow - redemptions)
SELECT
    fm.scheme_name,
    fm.fund_house,
    fm.category,
    SUM(CASE WHEN it.transaction_type IN ('SIP','Lumpsum') THEN it.amount_inr ELSE 0 END) AS total_inflow,
    SUM(CASE WHEN it.transaction_type = 'Redemption' THEN it.amount_inr ELSE 0 END) AS total_redemption,
    SUM(CASE WHEN it.transaction_type IN ('SIP','Lumpsum') THEN it.amount_inr ELSE -it.amount_inr END) AS net_flow
FROM investor_transactions it
JOIN fund_master fm ON it.amfi_code = fm.amfi_code
GROUP BY fm.amfi_code, fm.scheme_name
ORDER BY net_flow DESC
LIMIT 15;

-- 7. Repeat vs One-Time Customers (investors)
-- Investors with more than 5 transactions = loyal/repeat investors
SELECT
    investor_id,
    COUNT(*) AS num_transactions,
    SUM(amount_inr) AS total_invested
FROM investor_transactions
WHERE transaction_type IN ('SIP', 'Lumpsum')
GROUP BY investor_id
HAVING COUNT(*) > 5
ORDER BY num_transactions DESC
LIMIT 20;

-- 8. Subquery
-- Investors whose total investment exceeds the average total investment per investor
SELECT investor_id, total_invested
FROM (
    SELECT investor_id, SUM(amount_inr) AS total_invested
    FROM investor_transactions
    WHERE transaction_type IN ('SIP', 'Lumpsum')
    GROUP BY investor_id
) sub
WHERE total_invested > (
    SELECT AVG(inv_total)
    FROM (
        SELECT SUM(amount_inr) AS inv_total
        FROM investor_transactions
        WHERE transaction_type IN ('SIP', 'Lumpsum')
        GROUP BY investor_id
    )
)
ORDER BY total_invested DESC
LIMIT 20;

-- 9. Category-wise Revenue Breakdown (Product Performance by Category)
SELECT
    fm.category,
    fm.sub_category,
    COUNT(DISTINCT fm.amfi_code) AS num_schemes,
    SUM(CASE WHEN it.transaction_type IN ('SIP','Lumpsum') THEN it.amount_inr ELSE 0 END) AS total_inflow
FROM investor_transactions it
JOIN fund_master fm ON it.amfi_code = fm.amfi_code
GROUP BY fm.category, fm.sub_category
ORDER BY total_inflow DESC;

-- 10. Window Function
-- Monthly inflow trend with running total (cumulative revenue over time)
SELECT
    strftime('%Y-%m', transaction_date) AS month,
    SUM(amount_inr) AS monthly_inflow,
    SUM(SUM(amount_inr)) OVER (ORDER BY strftime('%Y-%m', transaction_date)) AS running_total
FROM investor_transactions
WHERE transaction_type IN ('SIP', 'Lumpsum')
GROUP BY month
ORDER BY month;

-- 11. Window Function - Rank
-- Rank each fund house by total inflow, using RANK()
SELECT
    fund_house,
    total_inflow,
    RANK() OVER (ORDER BY total_inflow DESC) AS revenue_rank
FROM (
    SELECT fm.fund_house, SUM(it.amount_inr) AS total_inflow
    FROM investor_transactions it
    JOIN fund_master fm ON it.amfi_code = fm.amfi_code
    WHERE it.transaction_type IN ('SIP', 'Lumpsum')
    GROUP BY fm.fund_house
) t;

-- 12. City Tier Analysis (Business Reporting)
-- Compare T30 vs B30 city contribution to total transaction value
SELECT
    city_tier,
    COUNT(DISTINCT investor_id) AS num_investors,
    SUM(amount_inr) AS total_amount,
    ROUND(AVG(amount_inr), 2) AS avg_transaction
FROM investor_transactions
GROUP BY city_tier
ORDER BY total_amount DESC;

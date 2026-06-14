-- 1. Total Companies
SELECT COUNT(*) AS total_companies
FROM recycling_companies;

-- 2. Average Credit Score
SELECT ROUND(AVG(Credit_Score),2) AS avg_credit_score
FROM recycling_companies;

-- 3. Approved Credit Candidates
SELECT Company_Name,
       Credit_Score,
       Debt_to_Equity,
       Cash_Flow_USD
FROM recycling_companies
WHERE Credit_Score >= 80
  AND Debt_to_Equity < 1.5
  AND Cash_Flow_USD > 0;

-- 4. Average Revenue by State
SELECT State,
       ROUND(AVG(Annual_Revenue_USD),2) AS avg_revenue
FROM recycling_companies
GROUP BY State
ORDER BY avg_revenue DESC
LIMIT 10;

-- 5. Top Compliance Companies
SELECT Company_Name,
       Regulatory_Compliance_Score
FROM recycling_companies
ORDER BY Regulatory_Compliance_Score DESC
LIMIT 10;

-- 6. Highest Profit Margin Companies
SELECT Company_Name,
       Profit_Margin_Pct
FROM recycling_companies
ORDER BY Profit_Margin_Pct DESC
LIMIT 10;

-- 7. Highest Debt Risk Companies
SELECT Company_Name,
       Debt_to_Equity
FROM recycling_companies
ORDER BY Debt_to_Equity DESC
LIMIT 10;

-- 8. Sustainability Leaders
SELECT Company_Name,
       CO2_Saved_Tons
FROM recycling_companies
ORDER BY CO2_Saved_Tons DESC
LIMIT 10;

-- 9. Average Cash Flow
SELECT ROUND(AVG(Cash_Flow_USD),2) AS avg_cash_flow
FROM recycling_companies;

-- 10. Top Revenue Companies
SELECT Company_Name,
       Annual_Revenue_USD
FROM recycling_companies
ORDER BY Annual_Revenue_USD DESC
LIMIT 10;
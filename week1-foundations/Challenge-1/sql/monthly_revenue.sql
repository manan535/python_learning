-- Insight: Calculates total revenue for each month in 2009.

SELECT
    strftime('%Y-%m', InvoiceDate) AS Month,
    ROUND(SUM(Total), 2) AS MonthlyRevenue
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2009'
GROUP BY Month
ORDER BY Month;


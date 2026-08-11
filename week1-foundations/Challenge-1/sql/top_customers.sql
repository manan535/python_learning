-- Insight: Identifies the top 5 customers based on their total purchase spending.

SELECT
    c.CustomerId,
    c.FirstName,
    c.LastName,
    ROUND(SUM(il.UnitPrice * il.Quantity), 2) AS TotalSpent
FROM Customer c
JOIN Invoice i
    ON c.CustomerId = i.CustomerId
JOIN InvoiceLine il
    ON i.InvoiceId = il.InvoiceId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
LIMIT 5;

-- Insight: Identifies the 10 best-selling tracks based on total quantity sold.

SELECT
    t.TrackId,
    t.Name AS Track,
    SUM(il.Quantity) AS UnitsSold
FROM Track t
JOIN InvoiceLine il
    ON t.TrackId = il.TrackId
GROUP BY t.TrackId
ORDER BY UnitsSold DESC
LIMIT 10;


-- Insight: Identify the 10 most expensive tracks.

SELECT TrackId,
       Name,
       Composer,
       UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;

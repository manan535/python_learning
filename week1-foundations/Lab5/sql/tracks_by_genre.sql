-- Insight: Shows the number of tracks available in each music genre.

SELECT
    g.GenreId,
    g.Name AS Genre,
    COUNT(t.TrackId) AS TrackCount
FROM Genre g
JOIN Track t
    ON g.GenreId = t.GenreId
GROUP BY g.GenreId
ORDER BY TrackCount DESC;

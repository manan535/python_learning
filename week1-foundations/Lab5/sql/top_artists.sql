-- Insight: Identifies the top 5 artists based on the number of tracks in the database.

SELECT
    ar.ArtistId,
    ar.Name AS Artist,
    COUNT(t.TrackId) AS TrackCount
FROM Artist ar
JOIN Album al
    ON ar.ArtistId = al.ArtistId
JOIN Track t
    ON al.AlbumId = t.AlbumId
GROUP BY ar.ArtistId
ORDER BY TrackCount DESC
LIMIT 5;

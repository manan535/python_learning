# Lab 5 – SQL Fundamentals

## Objective

The objective of this lab is to practice SQL fundamentals using the **Chinook SQLite database**.

The lab covers:

- Filtering data using `WHERE`
- Sorting using `ORDER BY`
- Limiting results using `LIMIT`
- Aggregate functions such as `COUNT()` and `SUM()`
- Grouping using `GROUP BY`
- Joining related tables using `JOIN`
- Basic data analysis using SQL

---

## Database

This lab uses the **Chinook SQLite sample database**.

The database contains information about:

- Customers
- Invoices
- Invoice items
- Artists
- Albums
- Tracks
- Genres
- Playlists

Database file:

```text
Chinook_Sqlite.sqlite
```

---

# Queries

## 1. Customers by Country

### Objective

List all customers belonging to a specific country.

### Query

**File:** `sql/customers_by_country.sql`

```sql
-- Insight: Lists customers from a selected country for country-level customer analysis.

SELECT CustomerId,
       FirstName,
       LastName,
       Email,
       Country
FROM Customer
WHERE Country = 'India';
```

### Result

The query returns 2 customers from India:

| Customer ID | Name | Email | Country |
|-------------:|------|-------|---------|
| 58 | Manoj Pareek | manoj.pareek@rediff.com | India |
| 59 | Puja Srivastava | puja_srivastava@yahoo.in | India |

### SQL Concepts

- `SELECT`
- `WHERE`
- Filtering records

---

## 2. 10 Most Expensive Tracks

### Objective

Find the 10 tracks with the highest unit price.

### Query

**File:** `sql/expensive_tracks.sql`

```sql
-- Insight: Identify the 10 most expensive tracks.

SELECT TrackId,
       Name,
       Composer,
       UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;
```

### Result

The top 10 tracks returned by the database all have a unit price of **1.99**.

| Track ID | Track | Unit Price |
|---------:|-------|-----------:|
| 2819 | Battlestar Galactica: The Story So Far | 1.99 |
| 2820 | Occupation / Precipice | 1.99 |
| 2821 | Exodus, Pt. 1 | 1.99 |
| 2822 | Exodus, Pt. 2 | 1.99 |
| 2823 | Collaborators | 1.99 |
| 2824 | Torn | 1.99 |
| 2825 | A Measure of Salvation | 1.99 |
| 2826 | Hero | 1.99 |
| 2827 | Unfinished Business | 1.99 |
| 2828 | The Passage | 1.99 |

### SQL Concepts

- `ORDER BY`
- `DESC`
- `LIMIT`

---

## 3. Top 5 Customers by Total Spending

### Objective

Calculate the total amount spent by each customer and identify the top 5 customers.

### Query

**File:** `sql/top_customers.sql`

```sql
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
```

### Result

| Customer | Total Spent |
|----------|------------:|
| Helena Holý | 49.62 |
| Richard Cunningham | 47.62 |
| Luis Rojas | 46.62 |
| Hugh O'Reilly | 45.62 |
| Ladislav Kovács | 45.62 |

### SQL Concepts

- `JOIN`
- `SUM()`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`
- `ROUND()`

### Table Relationship

```text
Customer
   │
   │ CustomerId
   ▼
Invoice
   │
   │ InvoiceId
   ▼
InvoiceLine
```

The total spending is calculated using:

```text
UnitPrice × Quantity
```

# Lab 5 – SQL Fundamentals

## Objective

The objective of this lab is to practice SQL fundamentals using the **Chinook SQLite database**.

The lab covers:

- Filtering data using `WHERE`
- Sorting using `ORDER BY`
- Limiting results using `LIMIT`
- Aggregate functions such as `COUNT()` and `SUM()`
- Grouping using `GROUP BY`
- Joining related tables using `JOIN`
- Basic data analysis using SQL

---

## Database

This lab uses the **Chinook SQLite sample database**.

The database contains information about:

- Customers
- Invoices
- Invoice items
- Artists
- Albums
- Tracks
- Genres
- Playlists

Database file:

```text
Chinook_Sqlite.sqlite
```

---

# Queries

## 1. Customers by Country

### Objective

List all customers belonging to a specific country.

### Query

**File:** `sql/customers_by_country.sql`

```sql
-- Insight: Lists customers from a selected country for country-level customer analysis.

SELECT CustomerId,
       FirstName,
       LastName,
       Email,
       Country
FROM Customer
WHERE Country = 'India';
```

### Result

The query returns 2 customers from India:

| Customer ID | Name | Email | Country |
|-------------:|------|-------|---------|
| 58 | Manoj Pareek | manoj.pareek@rediff.com | India |
| 59 | Puja Srivastava | puja_srivastava@yahoo.in | India |

### SQL Concepts

- `SELECT`
- `WHERE`
- Filtering records

---

## 2. 10 Most Expensive Tracks

### Objective

Find the 10 tracks with the highest unit price.

### Query

**File:** `sql/expensive_tracks.sql`

```sql
-- Insight: Identify the 10 most expensive tracks.

SELECT TrackId,
       Name,
       Composer,
       UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;
```

### Result

The top 10 tracks returned by the database all have a unit price of **1.99**.

| Track ID | Track | Unit Price |
|---------:|-------|-----------:|
| 2819 | Battlestar Galactica: The Story So Far | 1.99 |
| 2820 | Occupation / Precipice | 1.99 |
| 2821 | Exodus, Pt. 1 | 1.99 |
| 2822 | Exodus, Pt. 2 | 1.99 |
| 2823 | Collaborators | 1.99 |
| 2824 | Torn | 1.99 |
| 2825 | A Measure of Salvation | 1.99 |
| 2826 | Hero | 1.99 |
| 2827 | Unfinished Business | 1.99 |
| 2828 | The Passage | 1.99 |

### SQL Concepts

- `ORDER BY`
- `DESC`
- `LIMIT`

---

## 3. Top 5 Customers by Total Spending

### Objective

Calculate the total amount spent by each customer and identify the top 5 customers.

### Query

**File:** `sql/top_customers.sql`

```sql
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
```

### Result

| Customer | Total Spent |
|----------|------------:|
| Helena Holý | 49.62 |
| Richard Cunningham | 47.62 |
| Luis Rojas | 46.62 |
| Hugh O'Reilly | 45.62 |
| Ladislav Kovács | 45.62 |

### SQL Concepts

- `JOIN`
- `SUM()`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`
- `ROUND()`

### Table Relationship

```text
Customer
   │
   │ CustomerId
   ▼
Invoice
   │
   │ InvoiceId
   ▼
InvoiceLine
```

The total spending is calculated using:

```text
UnitPrice × Quantity
```

for each invoice item.

---

## 4. Track Count by Genre

### Objective

Count how many tracks belong to each genre.

### Query

**File:** `sql/tracks_by_genre.sql`

```sql
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
```

### Result

The genres with the highest number of tracks are:

| Genre | Track Count |
|-------|------------:|
| Rock | 1297 |
| Latin | 579 |
| Metal | 374 |
| Alternative & Punk | 332 |
| Jazz | 130 |

### Key Insight

**Rock** is the largest genre in the database with **1,297 tracks**.

### SQL Concepts

- `JOIN`
- `COUNT()`
- `GROUP BY`
- `ORDER BY`
- Aggregate functions

---

## 5. Top 5 Artists by Track Count

### Objective

Find the five artists with the highest number of tracks.

### Query

**File:** `sql/top_artists.sql`

```sql
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
```

### Result

| Artist | Track Count |
|--------|------------:|
| Iron Maiden | 213 |
| U2 | 135 |
| Led Zeppelin | 114 |
| Metallica | 112 |
| Lost | 92 |

### Table Relationship

```text
Artist
   │
   │ ArtistId
   ▼
Album
   │
   │ AlbumId
   ▼
Track
```

### Key Insight

**Iron Maiden** has the highest number of tracks in the database with **213 tracks**.

### SQL Concepts

- Multiple `JOIN`s
- `COUNT()`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`

---

# SQL Concepts Practiced

| Concept | Usage |
|---------|-------|
| `SELECT` | Retrieve data |
| `WHERE` | Filter records |
| `ORDER BY` | Sort results |
| `LIMIT` | Restrict number of results |
| `COUNT()` | Count records |
| `SUM()` | Calculate totals |
| `ROUND()` | Format numeric results |
| `GROUP BY` | Group records |
| `JOIN` | Combine related tables |
| Aggregate Functions | Perform calculations on groups of records |

---

# How to Run the Queries

Make sure SQLite is installed:

```bash
sqlite3 --version
```

Open the database:

```bash
sqlite3 Chinook_Sqlite.sqlite
```

Alternatively, run a query file directly from the terminal:

```bash
sqlite3 Chinook_Sqlite.sqlite < sql/customers_by_country.sql
```

For formatted output:

```bash
sqlite3 -header -column Chinook_Sqlite.sqlite < sql/top_customers.sql
```

---

# Repository Structure

```text
Lab5/
├── README.md
├── Chinook_Sqlite.sqlite
└── sql/
    ├── customers_by_country.sql
    ├── expensive_tracks.sql
    ├── top_customers.sql
    ├── tracks_by_genre.sql
    └── top_artists.sql
```

---

# Conclusion

This lab provided practical experience with relational databases and SQL.

The queries demonstrated how SQL can be used to:

- Filter customer data
- Identify expensive products/tracks
- Analyze customer spending
- Categorize and count records
- Analyze relationships between artists, albums, and tracks

The lab also provided hands-on experience working with **SQLite from the Linux command line**.

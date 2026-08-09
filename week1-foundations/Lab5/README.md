# Lab 5 – SQL Fundamentals

## Objective

Practice SQL fundamentals using the Chinook SQLite database, including filtering, sorting, aggregation, grouping, and joins.

## Database

The lab uses the Chinook SQLite sample database.

## Queries

### 1. Customers by Country

Lists customers from India.

**File:** `sql/customers_by_country.sql`

**Insight:** Identifies customers from a selected country for country-level customer analysis.

---

### 2. 10 Most Expensive Tracks

Finds the 10 tracks with the highest unit price.

**File:** `sql/expensive_tracks.sql`

**Insight:** Identifies the 10 most expensive tracks based on their unit price.

---

### 3. Top 5 Customers by Total Spending

Calculates the total spending of customers and returns the top five.

**File:** `sql/top_customers.sql`

**Insight:** Identifies the top 5 customers based on their total purchase spending.

---

### 4. Track Count by Genre

Counts the number of tracks available in each genre.

**File:** `sql/tracks_by_genre.sql`

**Insight:** Shows the number of tracks available in each music genre.

---

### 5. Top 5 Artists by Track Count

Finds the five artists with the highest number of tracks.

**File:** `sql/top_artists.sql`

**Insight:** Identifies the top 5 artists based on the number of tracks in the database.

---

## SQL Concepts Practiced

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`
- `COUNT()`
- `SUM()`
- `ROUND()`
- `GROUP BY`
- `JOIN`
- Aggregate functions
- Table relationships

## Results

- India has 2 customers in the database.
- The 10 most expensive tracks have a unit price of 1.99.
- Helena Holý is the highest-spending customer with total spending of 49.62.
- Rock has the highest number of tracks with 1,297 tracks.
- Iron Maiden has the highest number of tracks with 213 tracks.

## Conclusion

This lab provided practical experience with SQL queries and relational database concepts using SQLite and the Chinook database.

# Challenge 1 – CSV Data Profiler & SQL Analysis

## Overview

This challenge combines Python command-line development and SQL data analysis.

The project consists of two parts:

1. **CSV Data Profiler** – A Python command-line tool called `csvstat.py` that analyzes CSV files and reports basic data quality and statistical information.
2. **SQL Analysis** – Four SQL queries using the Chinook SQLite database to answer common business questions.

The challenge also focuses on writing clean code, handling errors, testing functionality, and following a professional Git/GitHub workflow.

---

# Project Structure

```text
Challenge-1/
├── README.md
├── requirements.txt
├── .gitignore
├── csvstat.py
├── sql/
│   ├── top_customers.sql
│   ├── revenue_by_country.sql
│   ├── best_selling_tracks.sql
│   └── monthly_revenue.sql
└── samples/
    ├── example.csv
    └── sales.csv
```

---

# Part A – CSV Data Profiler

## Description

`csvstat.py` is a command-line CSV profiling tool built using Python's standard library.

It accepts a CSV file as input and reports useful information about the dataset.

## Features

The tool provides:

- Number of rows
- Number of columns
- Automatic column type inference
- Missing-value count
- Missing-value percentage
- Minimum value for numeric columns
- Mean value for numeric columns
- Maximum value for numeric columns
- Most frequent values for text columns
- Command-line support using `argparse`
- Friendly error messages for invalid input

---

## Supported Data Types

The profiler attempts to classify each column as:

### Numeric

Columns containing values that can be converted to numbers.

Example:

```text
25
30
35
```

### Date

Columns containing values matching supported date formats such as:

```text
2024-01-15
2024-03-10
```

### Text

Columns that do not consistently match numeric or date formats.

Example:

```text
Engineering
Sales
Marketing
```

---

# Usage

Run the profiler using:

```bash
python3 csvstat.py <file>
```

Example:

```bash
python3 csvstat.py samples/example.csv
```

---

## Top Frequent Values

The optional `--top` argument displays the most frequent values for text columns.

Example:

```bash
python3 csvstat.py samples/example.csv --top 3
```

Example output:

```text
Column: department
  Type: text
  Missing: 0 (0.0%)
  Top 3:
    Engineering: 3
    Sales: 3
    Marketing: 2
```

---

# Example Dataset

The project includes a small sample dataset:

```text
samples/example.csv
```

Example columns:

```text
name
age
salary
department
join_date
```

The dataset intentionally contains missing values so that missing-value detection can be tested.

---

# Sample Output

Running:

```bash
python3 csvstat.py samples/example.csv
```

produces output similar to:

```text
File: samples/example.csv
Rows: 8
Columns: 5

Column: name
  Type: text
  Missing: 0 (0.0%)

Column: age
  Type: numeric
  Missing: 1 (12.5%)
  Min: 25.00
  Mean: 29.14
  Max: 35.00

Column: salary
  Type: numeric
  Missing: 1 (12.5%)
  Min: 48000.00
  Mean: 60000.00
  Max: 72000.00

Column: department
  Type: text
  Missing: 0 (0.0%)

Column: join_date
  Type: date
  Missing: 1 (12.5%)
```

---

# Error Handling

The program handles common input errors without displaying a Python traceback.

## Missing File

```bash
python3 csvstat.py samples/not_found.csv
```

Output:

```text
Error: File not found: samples/not_found.csv
```

## Invalid `--top` Value

```bash
python3 csvstat.py samples/example.csv --top -3
```

Output:

```text
csvstat.py: error: --top must be a positive integer
```

The program also validates `--top 0` and rejects it because the value must be positive.

---

# Testing

The profiler was tested using two different CSV files:

```text
samples/example.csv
samples/sales.csv
```

Testing covered:

- Row and column counting
- Numeric type inference
- Text type inference
- Date type inference
- Missing-value detection
- Missing-value percentages
- Numeric minimum
- Numeric mean
- Numeric maximum
- Most frequent text values
- Missing input files
- Invalid `--top` values

---

# Part B – SQL Analysis

The SQL portion uses the **Chinook SQLite sample database**.

The database represents a digital music store and contains related tables such as:

```text
Artist
Album
Track
Genre
Customer
Invoice
InvoiceLine
```

The database used for local testing was the Chinook SQLite database from the previous lab.

The database itself is intentionally not included in this challenge repository because it is a data file rather than source code.

---

# SQL Query 1 – Top 5 Customers by Total Spend

### File

```text
sql/top_customers.sql
```

### Query

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

```text
6|Helena|Holý|49.62
26|Richard|Cunningham|47.62
57|Luis|Rojas|46.62
46|Hugh|O'Reilly|45.62
45|Ladislav|Kovács|45.62
```

### Insight

Helena Holý is the highest-spending customer with total spending of **49.62**.

---

# SQL Query 2 – Revenue by Country

### File

```text
sql/revenue_by_country.sql
```

### Query

```sql
-- Insight: Calculates total revenue generated by each customer country.

SELECT
    c.Country,
    ROUND(SUM(i.Total), 2) AS TotalRevenue
FROM Customer c
JOIN Invoice i
    ON c.CustomerId = i.CustomerId
GROUP BY c.Country
ORDER BY TotalRevenue DESC;
```

### Top Results

```text
USA|523.06
Canada|303.96
France|195.1
Brazil|190.1
Germany|156.48
United Kingdom|112.86
Czech Republic|90.24
Portugal|77.24
India|75.26
```

### Insight

The **USA generates the highest revenue**, with total revenue of **523.06**.

---

# SQL Query 3 – 10 Best-Selling Tracks

### File

```text
sql/best_selling_tracks.sql
```

### Query

```sql
-- Insight: Identifies the 10 best-selling tracks based on total quantity sold.

SELECT
    t.TrackId,
    t.Name AS Track,
    SUM(il.Quantity) AS UnitsSold
FROM Track t
JOIN InvoiceLine il
    ON t.TrackId = il.TrackId
GROUP BY t.TrackId
ORDER BY UnitsSold DESC, t.Name ASC
LIMIT 10;
```

### Result

The top tracks returned by the database include:

```text
2|Balls to the Wall|2
8|Inject The Venom|2
9|Snowballed|2
20|Overdose|2
32|Deuces Are Wild|2
48|Not The Doctor|2
66|Por Causa De Você|2
84|Welcome Home (Sanitarium)|2
161|Snowblind|2
162|Cornucopia|2
```

### Insight

The database contains several tracks tied at **2 units sold**, so the query uses track name as a secondary sort to make the result deterministic.

---

# SQL Query 4 – Monthly Revenue

### File

```text
sql/monthly_revenue.sql
```

### Query

```sql
-- Insight: Calculates total revenue for each month in 2009.

SELECT
    strftime('%Y-%m', InvoiceDate) AS Month,
    ROUND(SUM(Total), 2) AS MonthlyRevenue
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2009'
GROUP BY Month
ORDER BY Month;
```

### Result

```text
2009-01|35.64
2009-02|37.62
2009-03|37.62
2009-04|37.62
2009-05|37.62
2009-06|37.62
2009-07|37.62
2009-08|37.62
2009-09|37.62
2009-10|37.62
2009-11|37.62
2009-12|37.62
```

### Insight

The query groups invoices by month using SQLite's `strftime()` function and calculates the total revenue for each month of 2009.

---

# SQL Concepts Practiced

The SQL analysis demonstrates:

- `SELECT`
- `WHERE`
- `JOIN`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`
- `SUM()`
- `ROUND()`
- SQLite `strftime()`
- Aggregate functions
- Relational table relationships

---

# Python Concepts Practiced

The CSV profiler demonstrates:

- `argparse`
- CSV file handling
- `csv.DictReader`
- Functions
- List comprehensions
- Exception handling
- Type inference
- Numeric calculations
- `Counter`
- Date parsing
- Command-line arguments

---

# Technologies

- Python 3
- SQLite
- SQL
- Linux / WSL
- Git
- GitHub

The CSV profiler uses only Python's standard library and does not require third-party packages.

---

# How to Run

## CSV Profiler

```bash
python3 csvstat.py samples/example.csv
```

With top values:

```bash
python3 csvstat.py samples/example.csv --top 3
```

## SQL Queries

The SQL queries can be executed using SQLite:

```bash
sqlite3 <path-to-Chinook_Sqlite.sqlite> < sql/top_customers.sql
```

For example:

```bash
sqlite3 ../Lab5/Chinook_Sqlite.sqlite < sql/top_customers.sql
```

---

# Git Workflow

The challenge is developed using a feature-branch workflow.

The intended workflow is:

```text
main
  │
  └── feature/challenge-1
          │
          ├── Small commits
          ├── Testing
          ├── Pull Request
          ├── Peer Review
          └── Merge
```

Changes are reviewed through GitHub Pull Requests before being merged into `main`.

---

# Conclusion

This challenge combines Python scripting, command-line development, CSV data profiling, SQL analysis, relational databases, error handling, testing, and Git/GitHub collaboration.

The project demonstrates how Python can be used to build reusable command-line data tools while SQL can be used to answer business questions from structured relational data.

---

## Author

**Manan Gupta**

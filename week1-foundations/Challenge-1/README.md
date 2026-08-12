# Challenge 1 – CSV Data Profiler & SQL Analysis

## Overview

This challenge combines Python command-line development and SQL data analysis.

The project consists of two main parts:

1. **CSV Data Profiler** – A Python command-line tool called `csvstat.py` that analyzes CSV files and reports basic data quality and statistical information.
2. **SQL Analysis** – Four SQL queries using the Chinook SQLite database to answer common business questions.

The challenge also focuses on writing clean code, handling errors, testing functionality, validating data quality, documenting limitations, and following a professional Git/GitHub workflow.

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
    ├── sales.csv
    └── unsupported_dates.csv
```

---

# Part A – CSV Data Profiler

## Description

`csvstat.py` is a command-line CSV profiling tool built using Python's standard library.

It accepts a CSV file as input and reports useful information about the dataset.

The profiler provides basic statistical information while also attempting to identify potential data-quality issues.

---

## Features

The tool provides:

- Number of rows
- Number of columns
- Automatic column type inference
- Numeric statistics
- Missing-value count
- Missing-value percentage
- Minimum value for numeric columns
- Mean value for numeric columns
- Maximum value for numeric columns
- Most frequent values for text columns
- Date-format detection
- Unsupported date-format detection
- Warnings for potentially unrecognized date values
- Command-line support using `argparse`
- Input validation
- Friendly error messages for invalid input

---

# Supported Data Types

The profiler attempts to classify each column as:

- Numeric
- Date
- Text

---

## Numeric

A column is classified as numeric when all non-empty values can be converted to numbers.

Example:

```text
25
30
35
```

For numeric columns, the profiler calculates:

- Minimum
- Mean
- Maximum

Example:

```text
Column: age
  Type: numeric
  Missing: 1 (12.5%)
  Min: 25.00
  Mean: 29.14
  Max: 35.00
```

---

## Date

A column is classified as a date when all non-empty values match one of the explicitly supported date formats.

The currently supported date formats are:

```text
YYYY-MM-DD
YYYY-MM-DD HH:MM:SS
DD/MM/YYYY
MM/DD/YYYY
```

Examples:

```text
2024-01-15
2024-01-15 14:30:00
15/01/2024
01/15/2024
```

These formats are explicitly defined in the Python implementation.

They are also displayed in the command-line help:

```bash
python3 csvstat.py --help
```

---

## Text

A column is classified as text when its non-empty values do not consistently match the supported numeric or date formats.

Example:

```text
Engineering
Sales
Marketing
```

---

# Unsupported Date Formats

The profiler does not silently assume that an unrecognized date format is valid.

For example:

```text
15-Jan-2024
```

is not one of the currently supported date formats.

If a value appears to contain date information but uses an unsupported format, the profiler:

1. Classifies the column as `text`.
2. Generates a warning.
3. Alerts the user that the values may require additional date-format support.

Example:

```text
Column: birth_date
  Type: text
  Warning: Some values appear to be dates but use an unsupported date format.
  Missing: 0 (0.0%)
```

This behavior helps prevent potentially important data from being silently misclassified.

---

# Missing Values

Empty values are treated as missing.

The profiler reports:

- Number of missing values
- Percentage of missing values

Example:

```text
Missing: 1 (12.5%)
```

Missing values are excluded when calculating numeric statistics.

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

# Top Frequent Values

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

The `--top` argument must be a positive integer.

For example:

```bash
python3 csvstat.py samples/example.csv --top -3
```

produces:

```text
csvstat.py: error: --top must be a positive integer
```

The same validation applies to:

```bash
python3 csvstat.py samples/example.csv --top 0
```

---

# Command-Line Help

The tool provides command-line help using `argparse`.

Run:

```bash
python3 csvstat.py --help
```

The help output includes the supported date formats:

```text
Profile a CSV file and display basic statistics. Supported date formats:
YYYY-MM-DD, YYYY-MM-DD HH:MM:SS, DD/MM/YYYY, MM/DD/YYYY.
```

This makes the supported input formats visible to users instead of requiring them to inspect the source code.

---

# Example Dataset

The project includes three sample CSV datasets.

## `samples/example.csv`

This is the primary sample dataset.

It contains:

```text
name
age
salary
department
join_date
```

The dataset contains:

- Text values
- Numeric values
- Date values
- Missing values

Example:

```csv
name,age,salary,department,join_date
Alice,25,50000,Engineering,2024-01-15
Bob,30,65000,Sales,2023-06-20
Charlie,28,55000,Engineering,2024-03-10
David,,70000,Marketing,2022-11-05
Eva,35,,Sales,2021-08-12
Frank,26,48000,Engineering,2024-05-18
Grace,31,72000,Marketing,2023-09-25
Henry,29,60000,Sales,
```

---

## `samples/sales.csv`

This dataset provides a second dataset for testing.

It contains:

```text
product
quantity
price
category
sale_date
```

It includes:

- Numeric values
- Text values
- Date values
- Missing values
- Repeated categorical values

Example usage:

```bash
python3 csvstat.py samples/sales.csv --top 3
```

---

## `samples/unsupported_dates.csv`

This dataset is specifically used to test unsupported date-format detection.

Example:

```csv
name,birth_date,department
Alice,15-Jan-2024,Engineering
Bob,20-Feb-2024,Sales
Charlie,25-Mar-2024,Engineering
```

The `birth_date` values are date-like but use a format that is not currently supported.

Running:

```bash
python3 csvstat.py samples/unsupported_dates.csv
```

produces a warning:

```text
Column: birth_date
  Type: text
  Warning: Some values appear to be dates but use an unsupported date format.
  Missing: 0 (0.0%)
```

---

# Sample Output

Running:

```bash
python3 csvstat.py samples/example.csv
```

produces:

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

Command:

```bash
python3 csvstat.py samples/not_found.csv
```

Output:

```text
Error: File not found: samples/not_found.csv
```

---

## Invalid `--top` Value

Command:

```bash
python3 csvstat.py samples/example.csv --top -3
```

Output:

```text
csvstat.py: error: --top must be a positive integer
```

The same validation is applied to:

```bash
python3 csvstat.py samples/example.csv --top 0
```

---

## Invalid CSV

The program checks whether the CSV contains a header row.

If a valid CSV header cannot be detected, the program displays an error instead of producing a Python traceback.

---

## Unsupported Date Format

When date-like values use an unsupported format, the profiler does not silently ignore the values.

Instead, it displays a warning:

```text
Warning: Some values appear to be dates but use an unsupported date format.
```

This makes potential data-quality problems visible to the user.

---

# Testing

The CSV profiler was tested using three CSV files:

```text
samples/example.csv
samples/sales.csv
samples/unsupported_dates.csv
```

Testing covered:

- Row counting
- Column counting
- Numeric type inference
- Text type inference
- Date type inference
- Supported date formats
- Missing-value detection
- Missing-value percentages
- Numeric minimum
- Numeric mean
- Numeric maximum
- Most frequent text values
- Missing input files
- Invalid `--top` values
- Unsupported date-format detection
- Warning generation for unsupported date-like values
- Command-line help

The profiler was also tested to ensure that normal text values such as:

```text
Marketing
```

do not incorrectly trigger an unsupported-date warning.

---

# Part B – SQL Analysis

The SQL portion uses the **Chinook SQLite sample database**.

The Chinook database represents a digital music store and contains related tables such as:

```text
Artist
Album
Track
Genre
Customer
Invoice
InvoiceLine
Playlist
PlaylistTrack
Employee
MediaType
```

The database used for local testing was the Chinook SQLite database from the previous lab.

The database itself is intentionally not included in this challenge repository because it is a data file rather than source code.

---

# SQL Query 1 – Top 5 Customers by Total Spend

## File

```text
sql/top_customers.sql
```

## Purpose

Identifies the five customers with the highest total purchase spending.

## Query

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

## Result

```text
6|Helena|Holý|49.62
26|Richard|Cunningham|47.62
57|Luis|Rojas|46.62
46|Hugh|O'Reilly|45.62
45|Ladislav|Kovács|45.62
```

## Insight

Helena Holý is the highest-spending customer in the result, with total spending of **49.62**.

---

# SQL Query 2 – Revenue by Country

## File

```text
sql/revenue_by_country.sql
```

## Purpose

Calculates the total revenue generated by customers from each country.

## Query

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

## Top Results

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

## Insight

The **USA generates the highest revenue**, with total revenue of **523.06**.

India generates **75.26** in revenue in the dataset.

---

# SQL Query 3 – 10 Best-Selling Tracks

## File

```text
sql/best_selling_tracks.sql
```

## Purpose

Identifies the ten tracks with the highest total quantity sold.

## Query

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

## Result

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

## Insight

Several tracks are tied at **2 units sold**.

A secondary alphabetical sort by track name is used to make the output deterministic when multiple tracks have the same number of sales.

---

# SQL Query 4 – Monthly Revenue

## File

```text
sql/monthly_revenue.sql
```

## Purpose

Calculates total revenue for each month in 2009.

## Query

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

## Result

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

## Insight

The query uses SQLite's `strftime()` function to group invoices by month and calculate the total revenue for each month of 2009.

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
- Deterministic ordering
- Data aggregation

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
- Regular expressions
- Numeric calculations
- `Counter`
- Date parsing
- Command-line arguments
- Input validation
- Data-quality warnings

---

# Data Quality Considerations

A key design consideration in this project is avoiding silent misclassification of input data.

The profiler has a limited set of explicitly supported date formats:

```text
YYYY-MM-DD
YYYY-MM-DD HH:MM:SS
DD/MM/YYYY
MM/DD/YYYY
```

A value using a different date representation should not be silently assumed to be ordinary text without notifying the user.

For example:

```text
15-Jan-2024
```

is not currently supported.

The profiler therefore:

1. Detects that the value appears to be date-like.
2. Classifies the column as text.
3. Generates a warning.
4. Alerts the user that the format is unsupported.

This approach makes the limitation visible and reduces the risk of silently producing incorrect analysis.

It also makes it easier to extend the profiler later when new date formats need to be supported.

---

# Technologies

- Python 3
- SQLite
- SQL
- Linux / WSL
- Git
- GitHub

The CSV profiler uses only the Python standard library and does not require third-party packages.

---

# Dependencies

No external Python packages are required.

The project uses Python standard-library modules including:

```text
argparse
csv
collections
datetime
re
```

The `requirements.txt` file documents that there are no external dependencies.

---

# How to Run

## CSV Profiler

Run the profiler on the main sample:

```bash
python3 csvstat.py samples/example.csv
```

Run it with the top three frequent text values:

```bash
python3 csvstat.py samples/example.csv --top 3
```

Run it on the second dataset:

```bash
python3 csvstat.py samples/sales.csv --top 3
```

Test unsupported date formats:

```bash
python3 csvstat.py samples/unsupported_dates.csv
```

View command-line help:

```bash
python3 csvstat.py --help
```

---

## SQL Queries

The SQL queries can be executed using SQLite and the Chinook database.

The database used during development is located in the previous Lab 5 directory:

```text
../Lab5/Chinook_Sqlite.sqlite
```

Run the top customers query:

```bash
sqlite3 ../Lab5/Chinook_Sqlite.sqlite < sql/top_customers.sql
```

Run the revenue by country query:

```bash
sqlite3 ../Lab5/Chinook_Sqlite.sqlite < sql/revenue_by_country.sql
```

Run the best-selling tracks query:

```bash
sqlite3 ../Lab5/Chinook_Sqlite.sqlite < sql/best_selling_tracks.sql
```

Run the monthly revenue query:

```bash
sqlite3 ../Lab5/Chinook_Sqlite.sqlite < sql/monthly_revenue.sql
```

---

# Git Workflow

The challenge is developed using a feature-branch workflow.

```text
main
  │
  └── feature/challenge-1
          │
          ├── Development
          ├── Small commits
          ├── Testing
          ├── Pull Request
          ├── Peer Review
          ├── Manager Review
          ├── Address Feedback
          └── Merge
```

The workflow used for this challenge includes:

- Creating a feature branch
- Making focused commits
- Testing changes locally
- Pushing the feature branch to GitHub
- Creating a Pull Request
- Receiving peer/manager review
- Addressing review feedback
- Updating the Pull Request
- Merging the approved Pull Request into `main`

---

# Engineering Considerations

This challenge goes beyond simply producing the expected output.

The implementation considers:

### Input Validation

Command-line arguments are validated before processing.

For example, `--top` must be a positive integer.

### Error Handling

Missing files and invalid input are handled with clear messages rather than exposing Python tracebacks.

### Data Quality

Unsupported date-like values generate warnings instead of being silently ignored.

### Explicit Limitations

The supported date formats are documented both in the README and in the command-line help.

### Deterministic SQL Results

Queries with possible ties use secondary sorting where appropriate so that results are reproducible.

---

# Conclusion

This challenge combines Python scripting, command-line development, CSV data profiling, SQL analysis, relational databases, error handling, data-quality validation, testing, and Git/GitHub collaboration.

The project demonstrates how Python can be used to build reusable command-line data tools while SQL can be used to answer business questions from structured relational data.

The implementation also considers how a data-processing tool should behave when it encounters input formats that it does not explicitly support, making potential data-quality issues visible instead of silently ignoring them.

---

## Author

**Manan Gupta**

# Python Learning Labs

This repository contains my weekly Python lab assignments completed as part of my internship/training.

The labs focus on building a strong foundation in Python programming, Linux development, SQL, Git, GitHub collaboration, Bash scripting, virtual environments, and software engineering best practices.

---

## Repository Structure

```text
python_learning/
├── README.md
├── week1/
│   └── week1-foundations/
│       ├── Lab1/
│       │   ├── hello.py
│       │   ├── README.md
│       │   ├── requirements.txt
│       │   └── screenshots/
│       │
│       ├── Lab2/
│       │   ├── main.py
│       │   ├── numbers.txt
│       │   ├── README.md
│       │   └── screenshots/
│       │
│       ├── Lab3/
│       │   ├── README.md
│       │   └── screenshots/
│       │
│       ├── Lab4/
│       │   ├── README.md
│       │   ├── top_words.sh
│       │   ├── 1342-0.txt
│       │   ├── 11-0.txt
│       │   └── screenshots/
│       │
│       └── Lab5/
│           ├── README.md
│           ├── Chinook_Sqlite.sqlite
│           └── sql/
│               ├── customers_by_country.sql
│               ├── expensive_tracks.sql
│               ├── top_customers.sql
│               ├── tracks_by_genre.sql
│               └── top_artists.sql
│
├── week2/
├── week3/
└── ...
```

---

## Weekly Progress

| Week | Lab | Topics Covered |
|------|-----|----------------|
| Week 1 | Lab 1 | Project setup, virtual environments, Linux (WSL), Git, GitHub |
| Week 1 | Lab 2 | File handling, dictionaries, word frequency analysis, exception handling |
| Week 1 | Lab 3 | Git branching, feature branches, pull requests, peer review, merge workflow |
| Week 1 | Lab 4 | Linux command-line tools, `curl`, `wc`, text processing, Bash scripting, file permissions |
| Week 1 | Lab 5 | SQL fundamentals, SQLite, filtering, sorting, aggregation, grouping, joins |

---

## Technologies Used

- Python
- SQL
- SQLite
- Linux (WSL)
- Git
- GitHub
- Bash
- Virtual Environments (`venv`)
- Visual Studio Code

---

## Skills Learned

- Setting up Python development environments
- Working with Linux and WSL
- Using Git and GitHub
- Creating and managing Git branches
- Opening and reviewing Pull Requests
- Collaborating using GitHub workflows
- Reading and writing files in Python
- Using dictionaries for data processing
- Using Linux command-line utilities
- Writing Bash scripts
- Managing file permissions with `chmod`
- Writing SQL queries
- Working with SQLite databases
- Using `JOIN`, `GROUP BY`, `COUNT()`, and `SUM()`
- Performing basic data analysis using SQL
- Writing clean and maintainable code

---

# Labs

## Lab 1 – Python & Environment Setup

### Topics Covered

- Python project setup
- Python virtual environments
- Linux and WSL
- Git fundamentals
- GitHub repository setup
- Basic project structure

### Key Skills

- Creating and activating a Python virtual environment
- Installing dependencies
- Running Python programs from the terminal
- Initializing and using Git repositories
- Connecting a local repository to GitHub

---

## Lab 2 – Python File Processing

### Topics Covered

- File handling
- Reading data from files
- Dictionaries
- Word frequency analysis
- Exception handling
- Python program structure

### Key Skills

- Reading and processing text files
- Counting word frequencies
- Using dictionaries for data processing
- Handling errors and exceptions
- Writing reusable Python code

---

## Lab 3 – Git & GitHub Collaboration

### Topics Covered

- Git branching
- Feature branches
- Multiple commits
- Pull Requests
- Peer code reviews
- Merge workflow

### Workflow Practiced

```text
main
 │
 └── feature/word-count
          │
          ├── Commit changes
          ├── Push branch
          ├── Create Pull Request
          ├── Peer review
          ├── Address feedback
          └── Merge into main
```

### Key Skills

- Creating feature branches
- Making small, meaningful commits
- Opening Pull Requests
- Reviewing peer code
- Addressing review feedback
- Merging Pull Requests
- Cleaning up feature branches

---

## Lab 4 – Linux & Bash

### Topics Covered

- Linux command-line tools
- `curl`
- `wc`
- `tr`
- `sort`
- `uniq`
- `head`
- Bash scripting
- File permissions
- Command-line arguments
- Text processing pipelines

### Main Script

```bash
./top_words.sh <filename> [count]
```

### Example

```bash
./top_words.sh 1342-0.txt
```

### Key Skills

- Downloading files using `curl`
- Counting lines, words, and characters
- Processing text using Linux pipelines
- Finding word frequencies
- Creating Bash scripts
- Using command-line arguments
- Making scripts executable with `chmod`
- Combining multiple Linux utilities

---

## Lab 5 – SQL Fundamentals

### Database

The lab uses the **Chinook SQLite database** to practice SQL and relational database concepts.

### Topics Covered

- SQL fundamentals
- SQLite
- Filtering data
- Sorting results
- Aggregate functions
- Grouping
- Table joins
- Relational database concepts

### SQL Queries

Five SQL queries were implemented:

#### 1. Customers by Country

Lists customers from India.

```sql
SELECT CustomerId,
       FirstName,
       LastName,
       Email,
       Country
FROM Customer
WHERE Country = 'India';
```

**Result:** 2 customers from India.

---

#### 2. 10 Most Expensive Tracks

Finds the 10 tracks with the highest unit price.

```sql
SELECT TrackId,
       Name,
       Composer,
       UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;
```

**Result:** The 10 returned tracks have a unit price of `1.99`.

---

#### 3. Top 5 Customers by Total Spending

Calculates customer spending using invoices and invoice items.

```sql
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

**Top customer:** Helena Holý — `49.62`

---

#### 4. Track Count by Genre

Counts the number of tracks in each genre.

```sql
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

**Top genre:** Rock — `1,297` tracks.

---

#### 5. Top 5 Artists by Track Count

Finds the five artists with the highest number of tracks.

```sql
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

**Top artist:** Iron Maiden — `213` tracks.

### SQL Concepts Practiced

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

---

## Overall Skills Developed

Through these labs, I have practiced:

### Python

- Python programming fundamentals
- File handling
- Dictionaries
- Exception handling
- Data processing

### Linux

- Working with the Linux terminal
- File and directory management
- Command-line utilities
- Bash scripting
- File permissions
- Text processing pipelines

### Git & GitHub

- Git repositories
- Commits
- Branches
- Feature development
- Pull Requests
- Peer reviews
- Merge workflows
- Collaborative development

### SQL

- Relational databases
- SQLite
- Data filtering
- Sorting
- Aggregation
- Grouping
- Joining tables
- Basic data analysis

---

## Goal

To document my progress throughout the internship by completing weekly labs while following software engineering best practices, maintaining clean code, and using professional Python, Linux, SQL, Git, and GitHub workflows.

---

## Author

**Manan Gupta**

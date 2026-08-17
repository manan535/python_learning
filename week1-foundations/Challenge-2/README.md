# csvstat

A command-line CSV data profiler built with Python.

`csvstat` analyzes CSV files and displays useful information about their structure and contents, including column types, missing values, numeric statistics, frequent values, and date formats.

The project is implemented as a Python package, unit tested using `pytest`, built into distributable packages, and published on PyPI.

## Features

- Count CSV rows and columns
- Automatically detect column types:
  - Numeric
  - Date
  - Text
- Detect missing values
- Calculate missing-value percentages
- Calculate numeric statistics:
  - Minimum
  - Mean
  - Maximum
- Display the most frequent values in text columns
- Detect supported date formats
- Warn about unsupported date-like formats
- Command-line interface using `argparse`
- Validate command-line arguments
- Handle common file and CSV errors
- Unit tested using `pytest`
- Installable using `pip`
- Published on PyPI

## Installation

Install `csvstat` directly from PyPI:

```bash
pip install csvstat-manan
```

After installation, verify that the command is available:

```bash
csvstat --help
```

## Usage

### Basic Usage

Run `csvstat` with the path to a CSV file:

```bash
csvstat example.csv
```

Example output:

```text
File: example.csv
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

### Show Frequent Values

Use the `--top` option to display the most frequent values in text columns:

```bash
csvstat example.csv --top 3
```

Example:

```text
Column: department
  Type: text
  Missing: 0 (0.0%)
  Top 3:
    Engineering: 3
    Sales: 3
    Marketing: 2
```

The `--top` value must be a positive integer.

### Display Help

```bash
csvstat --help
```

## Supported Data Types

### Numeric

A column is classified as numeric when all non-empty values can be converted to numbers.

For numeric columns, `csvstat` calculates:

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

### Date

A column is classified as a date when its non-empty values match one of the supported date formats.

Supported formats:

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

### Text

Values that are neither numeric nor supported dates are classified as text.

For text columns, the `--top` option can be used to display the most frequent values.

## Missing Values

Empty values are detected for every column.

For example:

```text
Missing: 1 (12.5%)
```

The first number represents the number of missing values.

The percentage represents the proportion of missing values relative to the total number of rows.

Missing values are ignored when determining the column type and when calculating numeric statistics.

## Unsupported Date Formats

`csvstat` detects some date-like values that do not match the supported date formats.

For example:

```text
15-Jan-2024
20-Feb-2024
25-Mar-2024
```

These values are classified as text and a warning is displayed:

```text
Warning: Some values appear to be dates but use an unsupported date format.
```

## Example CSV

A simple CSV file can look like this:

```csv
name,age,department
Alice,25,Engineering
Bob,30,Sales
Charlie,35,Engineering
David,28,Sales
```

Run:

```bash
csvstat example.csv
```

The output identifies:

- `name` as text
- `age` as numeric
- `department` as text

and calculates numeric statistics for the `age` column.

## Project Structure

```text
Challenge-2/
│
├── src/
│   └── csvstat/
│       ├── __init__.py
│       ├── cli.py
│       └── core.py
│
├── tests/
│   ├── test_cli.py
│   └── test_core.py
│
├── samples/
│   ├── example.csv
│   ├── sales.csv
│   └── unsupported_dates.csv
│
├── pyproject.toml
├── README.md
└── .gitignore
```

## Project Modules

### `core.py`

Contains the main CSV profiling functions:

- `infer_type()` — detects the type of a column
- `numeric_stats()` — calculates minimum, mean, and maximum
- `top_values()` — finds the most frequent non-empty values

### `cli.py`

Contains the command-line interface.

It handles:

- Command-line arguments
- CSV file reading
- Column processing
- Output formatting
- Error handling

### `__init__.py`

The package initialization file.

It is intentionally empty because the package does not require package-level initialization logic.

### `tests/`

Contains automated tests for the core functionality and command-line interface.

## Testing

The project uses `pytest` for unit testing.

Install pytest:

```bash
pip install pytest
```

Run the complete test suite:

```bash
python -m pytest
```

Current test result:

```text
26 passed
```

The tests cover:

- Numeric type detection
- Text type detection
- Date detection
- Unsupported date detection
- Empty values
- Missing values
- Numeric statistics
- Top frequent values
- CLI output
- Missing files
- Invalid `--top` values
- Error handling

## Development Setup

Clone the repository:

```bash
git clone https://github.com/manan535/python_learning.git
```

Move into the project directory:

```bash
cd Challenge-2
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install the package in editable mode:

```bash
python -m pip install -e .
```

Run the tests:

```bash
python -m pytest
```

Run the application:

```bash
csvstat samples/example.csv
```

## Package Configuration

The project uses `pyproject.toml` for Python packaging.

The package uses a `src` layout:

```text
src/
└── csvstat/
```

The command-line entry point is configured as:

```toml
[project.scripts]
csvstat = "csvstat.cli:main"
```

This allows users to run:

```bash
csvstat example.csv
```

instead of:

```bash
python csvstat.py example.csv
```

## Building the Package

Install the packaging tools:

```bash
python -m pip install build twine
```

Build the package:

```bash
python -m build
```

This generates a wheel and a source distribution:

```text
dist/
├── csvstat_manan-0.1.0-py3-none-any.whl
└── csvstat_manan-0.1.0.tar.gz
```

## Validating the Package

Validate the generated distributions using Twine:

```bash
python -m twine check dist/*
```

Expected result:

```text
Checking csvstat_manan-0.1.0-py3-none-any.whl: PASSED
Checking csvstat_manan-0.1.0.tar.gz: PASSED
```

## Testing the Built Wheel

The wheel can be installed in a clean virtual environment:

```bash
python -m venv testenv
```

Activate the environment and install the wheel:

```bash
python -m pip install dist/csvstat_manan-0.1.0-py3-none-any.whl
```

Then verify:

```bash
csvstat --help
```

Run it against a sample CSV:

```bash
csvstat samples/example.csv
```

## PyPI

The package is published on the Python Package Index (PyPI).

**Package:** `csvstat-manan`

**Version:** `0.1.0`

Install directly from PyPI:

```bash
pip install csvstat-manan
```

PyPI project page:

https://pypi.org/project/csvstat-manan/

## Runtime Dependencies

`csvstat` has no external runtime dependencies.

It uses Python standard-library modules including:

- `argparse`
- `csv`
- `re`
- `collections`
- `datetime`

Development and packaging tools:

- `pytest`
- `setuptools`
- `build`
- `twine`

## Error Handling

The application handles common errors such as:

- File not found
- Invalid CSV files
- Unsupported file encoding
- Operating system file errors
- Invalid `--top` values

Example:

```bash
csvstat missing.csv
```

Output:

```text
Error: File not found: missing.csv
```

## License

MIT License

Copyright (c) 2026 Manan Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

## Author

**Manan Gupta**

GitHub: https://github.com/manan535

PyPI: https://pypi.org/project/csvstat-manan/

## Project Status

The project currently provides:

- A working CSV profiling CLI
- 26 automated tests
- Python package configuration
- Wheel and source distribution builds
- Successful package validation
- Installation from a built wheel
- Publication to PyPI
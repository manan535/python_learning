import argparse
import csv
import re
from collections import Counter
from datetime import datetime


SUPPORTED_DATE_FORMATS = [
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M:%S",
    "%d/%m/%Y",
    "%m/%d/%Y",
]


def infer_type(values):
    """Infer column type and detect unsupported date-like values."""

    non_empty = [
        value.strip()
        for value in values
        if value.strip()
    ]

    if not non_empty:
        return "text", None

    # Check numeric
    try:
        for value in non_empty:
            float(value)
        return "numeric", None
    except ValueError:
        pass

    # Check whether all values match a supported date format
    date_matches = []

    for value in non_empty:
        matched = False

        for date_format in SUPPORTED_DATE_FORMATS:
            try:
                datetime.strptime(value, date_format)
                matched = True
                break
            except ValueError:
                continue

        date_matches.append(matched)

    if all(date_matches):
        return "date", None

    # Detect common date-like formats that are not supported
    unsupported_date_patterns = [
        r"^\d{1,2}-[A-Za-z]{3,9}-\d{4}$",
        r"^\d{1,2}/[A-Za-z]{3,9}/\d{4}$",
        r"^[A-Za-z]{3,9}\s+\d{1,2},\s+\d{4}$",
        r"^\d{4}\.\d{1,2}\.\d{1,2}$",
    ]

    unsupported_dates = []

    for value in non_empty:
        for pattern in unsupported_date_patterns:
            if re.match(pattern, value):
                unsupported_dates.append(value)
                break

    if unsupported_dates:
        return (
            "text",
            "Some values appear to be dates but use "
            "an unsupported date format.",
        )

    return "text", None


def numeric_stats(values):
    """Calculate minimum, mean, and maximum for numeric values."""

    numbers = []

    for value in values:
        value = value.strip()

        if value:
            numbers.append(float(value))

    if not numbers:
        return None

    return {
        "min": min(numbers),
        "mean": sum(numbers) / len(numbers),
        "max": max(numbers),
    }


def top_values(values, count):
    """Return the most frequent non-empty values."""

    non_empty = [
        value.strip()
        for value in values
        if value.strip()
    ]

    return Counter(non_empty).most_common(count)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Profile a CSV file and display basic statistics. "
            "Supported date formats: YYYY-MM-DD, "
            "YYYY-MM-DD HH:MM:SS, DD/MM/YYYY, MM/DD/YYYY."
        )
    )

    parser.add_argument(
        "file",
        help="Path to the CSV file",
    )

    parser.add_argument(
        "--top",
        type=int,
        help="Show the N most frequent values for text columns",
    )

    args = parser.parse_args()

    # Validate --top
    if args.top is not None and args.top <= 0:
        parser.error("--top must be a positive integer")

    try:
        with open(
            args.file,
            "r",
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print(
                    "Error: The file is not a valid CSV "
                    "with a header row."
                )
                return

            rows = list(reader)

            print(f"File: {args.file}")
            print(f"Rows: {len(rows)}")
            print(f"Columns: {len(reader.fieldnames)}")
            print()

            for column in reader.fieldnames:
                values = [
                    row[column]
                    for row in rows
                ]

                missing = sum(
                    1
                    for value in values
                    if not value.strip()
                )

                missing_percentage = (
                    missing / len(rows) * 100
                    if rows
                    else 0
                )

                column_type, warning = infer_type(values)

                print(f"Column: {column}")
                print(f"  Type: {column_type}")

                if warning:
                    print(f"  Warning: {warning}")

                print(
                    f"  Missing: {missing} "
                    f"({missing_percentage:.1f}%)"
                )

                # Numeric statistics
                if column_type == "numeric":
                    stats = numeric_stats(values)

                    if stats:
                        print(
                            f"  Min: {stats['min']:.2f}"
                        )
                        print(
                            f"  Mean: {stats['mean']:.2f}"
                        )
                        print(
                            f"  Max: {stats['max']:.2f}"
                        )

                # Top values for text columns
                if column_type == "text" and args.top:
                    counts = top_values(
                        values,
                        args.top,
                    )

                    print(f"  Top {args.top}:")

                    for value, count in counts:
                        print(
                            f"    {value}: {count}"
                        )

                print()

    except FileNotFoundError:
        print(
            f"Error: File not found: {args.file}"
        )

    except csv.Error:
        print(
            f"Error: Invalid CSV file: {args.file}"
        )

    except UnicodeDecodeError:
        print(
            f"Error: Could not decode file: {args.file}"
        )

    except OSError as error:
        print(
            f"Error: Could not read file: {error}"
        )


if __name__ == "__main__":
    main()

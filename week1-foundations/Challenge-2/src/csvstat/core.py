import re
from collections import Counter
from datetime import datetime


SUPPORTED_DATE_FORMATS = [
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M:%S",
    "%d/%m/%Y",
    "%m/%d/%Y",
]


UNSUPPORTED_DATE_PATTERNS = [
    r"^\d{1,2}-[A-Za-z]{3,9}-\d{4}$",
    r"^\d{1,2}/[A-Za-z]{3,9}/\d{4}$",
    r"^[A-Za-z]{3,9}\s+\d{1,2},\s+\d{4}$",
    r"^\d{4}\.\d{1,2}\.\d{1,2}$",
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

    # Check supported date formats
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

    # Detect unsupported date-like formats
    unsupported_dates = []

    for value in non_empty:
        for pattern in UNSUPPORTED_DATE_PATTERNS:
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
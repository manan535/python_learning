import pytest

from csvstat.core import infer_type, numeric_stats, top_values


# ---------------------------------------------------------
# infer_type() tests
# ---------------------------------------------------------

def test_infer_numeric():
    values = ["25", "30", "35"]

    result = infer_type(values)

    assert result == ("numeric", None)


def test_infer_decimal_numeric():
    values = ["25.5", "30.2", "35.75"]

    result = infer_type(values)

    assert result == ("numeric", None)


def test_infer_text():
    values = ["Engineering", "Sales", "Marketing"]

    result = infer_type(values)

    assert result == ("text", None)


def test_infer_empty_values():
    values = ["", "", ""]

    result = infer_type(values)

    assert result == ("text", None)


def test_infer_supported_date_yyyy_mm_dd():
    values = [
        "2024-01-15",
        "2024-02-20",
        "2024-03-10",
    ]

    result = infer_type(values)

    assert result == ("date", None)


def test_infer_supported_date_with_time():
    values = [
        "2024-01-15 14:30:00",
        "2024-02-20 10:15:00",
        "2024-03-10 18:45:00",
    ]

    result = infer_type(values)

    assert result == ("date", None)


def test_infer_supported_date_dd_mm_yyyy():
    values = [
        "15/01/2024",
        "20/02/2024",
        "10/03/2024",
    ]

    result = infer_type(values)

    assert result == ("date", None)


def test_infer_supported_date_mm_dd_yyyy():
    values = [
        "01/15/2024",
        "02/20/2024",
        "03/10/2024",
    ]

    result = infer_type(values)

    assert result == ("date", None)


def test_infer_unsupported_date():
    values = [
        "15-Jan-2024",
        "20-Feb-2024",
        "25-Mar-2024",
    ]

    result = infer_type(values)

    assert result[0] == "text"
    assert result[1] == (
        "Some values appear to be dates but use "
        "an unsupported date format."
    )


def test_normal_text_does_not_trigger_date_warning():
    values = [
        "Engineering",
        "Sales",
        "Marketing",
    ]

    result = infer_type(values)

    assert result == ("text", None)


def test_mixed_values_are_text():
    values = [
        "25",
        "30",
        "Engineering",
    ]

    result = infer_type(values)

    assert result == ("text", None)


def test_missing_values_are_ignored_for_type_detection():
    values = [
        "25",
        "",
        "30",
        "35",
    ]

    result = infer_type(values)

    assert result == ("numeric", None)


# ---------------------------------------------------------
# numeric_stats() tests
# ---------------------------------------------------------

def test_numeric_stats():
    values = [
        "10",
        "20",
        "30",
    ]

    result = numeric_stats(values)

    assert result["min"] == 10
    assert result["mean"] == 20
    assert result["max"] == 30


def test_numeric_stats_with_decimal_values():
    values = [
        "10.5",
        "20.5",
        "30.5",
    ]

    result = numeric_stats(values)

    assert result["min"] == 10.5
    assert result["mean"] == 20.5
    assert result["max"] == 30.5


def test_numeric_stats_ignores_missing_values():
    values = [
        "10",
        "",
        "20",
        "",
        "30",
    ]

    result = numeric_stats(values)

    assert result["min"] == 10
    assert result["mean"] == 20
    assert result["max"] == 30


def test_numeric_stats_empty_values():
    values = [
        "",
        "",
        "",
    ]

    result = numeric_stats(values)

    assert result is None


# ---------------------------------------------------------
# top_values() tests
# ---------------------------------------------------------

def test_top_values():
    values = [
        "Engineering",
        "Sales",
        "Engineering",
        "Marketing",
        "Engineering",
        "Sales",
    ]

    result = top_values(values, 2)

    assert result == [
        ("Engineering", 3),
        ("Sales", 2),
    ]


def test_top_values_ignores_empty_values():
    values = [
        "Engineering",
        "",
        "Engineering",
        "",
        "Sales",
    ]

    result = top_values(values, 2)

    assert result == [
        ("Engineering", 2),
        ("Sales", 1),
    ]


def test_top_values_returns_requested_count():
    values = [
        "A",
        "B",
        "C",
        "A",
        "B",
        "A",
    ]

    result = top_values(values, 1)

    assert result == [
        ("A", 3),
    ]


def test_top_values_when_count_exceeds_unique_values():
    values = [
        "A",
        "B",
        "A",
    ]

    result = top_values(values, 10)

    assert result == [
        ("A", 2),
        ("B", 1),
    ]
import sys

from csvstat.cli import main


def test_cli_basic_csv(tmp_path, capsys, monkeypatch):
    csv_file = tmp_path / "example.csv"

    csv_file.write_text(
        "name,age\n"
        "Alice,25\n"
        "Bob,30\n"
        "Charlie,35\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["csvstat", str(csv_file)],
    )

    main()

    output = capsys.readouterr().out

    assert f"File: {csv_file}" in output
    assert "Rows: 3" in output
    assert "Columns: 2" in output

    assert "Column: name" in output
    assert "Type: text" in output

    assert "Column: age" in output
    assert "Type: numeric" in output

    assert "Min: 25.00" in output
    assert "Mean: 30.00" in output
    assert "Max: 35.00" in output


def test_cli_missing_values(tmp_path, capsys, monkeypatch):
    csv_file = tmp_path / "missing.csv"

    csv_file.write_text(
        "name,age\n"
        "Alice,25\n"
        "Bob,\n"
        "Charlie,35\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["csvstat", str(csv_file)],
    )

    main()

    output = capsys.readouterr().out

    assert "Column: age" in output
    assert "Missing: 1 (33.3%)" in output


def test_cli_top_values(tmp_path, capsys, monkeypatch):
    csv_file = tmp_path / "departments.csv"

    csv_file.write_text(
        "name,department\n"
        "Alice,Engineering\n"
        "Bob,Sales\n"
        "Charlie,Engineering\n"
        "David,Engineering\n"
        "Eva,Sales\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            str(csv_file),
            "--top",
            "2",
        ],
    )

    main()

    output = capsys.readouterr().out

    assert "Top 2:" in output
    assert "Engineering: 3" in output
    assert "Sales: 2" in output


def test_cli_unsupported_date_warning(
    tmp_path,
    capsys,
    monkeypatch,
):
    csv_file = tmp_path / "dates.csv"

    csv_file.write_text(
        "name,birth_date\n"
        "Alice,15-Jan-2024\n"
        "Bob,20-Feb-2024\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["csvstat", str(csv_file)],
    )

    main()

    output = capsys.readouterr().out

    assert "Column: birth_date" in output
    assert "Type: text" in output

    assert (
        "Some values appear to be dates but use "
        "an unsupported date format."
    ) in output


def test_cli_missing_file(tmp_path, capsys, monkeypatch):
    missing_file = tmp_path / "does_not_exist.csv"

    monkeypatch.setattr(
        sys,
        "argv",
        ["csvstat", str(missing_file)],
    )

    main()

    output = capsys.readouterr().out

    assert f"Error: File not found: {missing_file}" in output


def test_cli_invalid_top_value(
    tmp_path,
    monkeypatch,
):
    csv_file = tmp_path / "example.csv"

    csv_file.write_text(
        "name\n"
        "Alice\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "csvstat",
            str(csv_file),
            "--top",
            "0",
        ],
    )

    # argparse.error() raises SystemExit
    try:
        main()
    except SystemExit as error:
        assert error.code == 2
    else:
        raise AssertionError(
            "Expected SystemExit for invalid --top"
        )
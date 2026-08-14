import argparse
import boto3
import csv
import io
import re
from collections import Counter
from contextlib import redirect_stdout
from datetime import datetime
from pathlib import Path


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

    try:
        for value in non_empty:
            float(value)
        return "numeric", None
    except ValueError:
        pass

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


def profile_csv(file_path, top):
    """Profile a CSV file and return the results as text."""

    output = io.StringIO()

    with redirect_stdout(output):
        try:
            with open(
                file_path,
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
                    return output.getvalue()

                rows = list(reader)

                print(f"File: {file_path}")
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

                    if column_type == "text" and top:
                        counts = top_values(
                            values,
                            top,
                        )

                        print(f"  Top {top}:")

                        for value, count in counts:
                            print(
                                f"    {value}: {count}"
                            )

                    print()

        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")

        except csv.Error:
            print(f"Error: Invalid CSV file: {file_path}")

        except UnicodeDecodeError:
            print(f"Error: Could not decode file: {file_path}")

    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Profile CSV files from an S3 input folder "
            "and save results to an S3 output folder."
        )
    )

    parser.add_argument(
        "--bucket",
        required=True,
        help="S3 bucket name",
    )

    parser.add_argument(
        "--top",
        type=int,
        help="Show the N most frequent values for text columns",
    )

    args = parser.parse_args()

    if args.top is not None and args.top <= 0:
        parser.error("--top must be a positive integer")

    s3 = boto3.client("s3")

    input_prefix = "input/"
    run_id = datetime.now().strftime("run-%Y%m%d-%H%M%S")
    output_prefix = f"output/{run_id}/"

    temp_dir = Path("/tmp/csvstat")
    temp_dir.mkdir(parents=True, exist_ok=True)

    response = s3.list_objects_v2(
        Bucket=args.bucket,
        Prefix=input_prefix,
    )

    objects = response.get("Contents", [])

    csv_objects = [
        obj
        for obj in objects
        if obj["Key"].lower().endswith(".csv")
    ]

    if not csv_objects:
        print(f"No CSV files found in s3://{args.bucket}/{input_prefix}")
        return

    print(f"Processing {len(csv_objects)} CSV file(s)...")
    print(f"Output location: s3://{args.bucket}/{output_prefix}")
    print()

    for obj in csv_objects:
        s3_key = obj["Key"]
        filename = Path(s3_key).name
        local_path = temp_dir / filename

        print(f"Processing: {s3_key}")

        s3.download_file(
            args.bucket,
            s3_key,
            str(local_path),
        )

        result = profile_csv(
            local_path,
            args.top,
        )

        output_filename = f"{Path(filename).stem}.txt"
        output_key = f"{output_prefix}{output_filename}"

        s3.upload_file(
            str(local_path),
            args.bucket,
            f"{output_prefix}input-{filename}",
        )

        result_bytes = result.encode("utf-8")

        s3.put_object(
            Bucket=args.bucket,
            Key=output_key,
            Body=result_bytes,
            ContentType="text/plain",
        )

        print(f"Saved: s3://{args.bucket}/{output_key}")
        print()

        local_path.unlink(missing_ok=True)

    print("Run completed successfully.")


if __name__ == "__main__":
    main()

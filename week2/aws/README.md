# CSVStat — AWS S3 + EC2

## Overview

This project extends the CSVStat utility to run on an AWS EC2 instance and process CSV files stored in Amazon S3.

The application:

1. Reads CSV files from an S3 `input/` prefix.
2. Processes each CSV using the existing CSVStat analysis logic.
3. Creates a unique output directory for every execution.
4. Stores the generated analysis results in the S3 `output/` prefix.
5. Uses an EC2 IAM instance profile for AWS authentication instead of hard-coded credentials.

---

## Architecture

```text
                         GitHub Repository
                                |
                                | git clone / git pull
                                v
                    +------------------------+
                    |      EC2 Instance      |
                    |    Amazon Linux 2023   |
                    |                        |
                    |      csvstat.py        |
                    +-----------+------------+
                                |
                         IAM Instance Profile
                                |
                         Role: S3-access
                                |
                                v
                    +------------------------+
                    |       Amazon S3         |
                    |                        |
                    |  manan-csvstat-2026    |
                    |                        |
                    |  input/                |
                    |    *.csv               |
                    |                        |
                    |  output/               |
                    |    run-YYYYMMDD-HHMMSS/|
                    |       *.txt             |
                    +------------------------+
```

---

## AWS Resources

| Resource         | Configuration        |
| ---------------- | -------------------- |
| AWS Region       | `ap-south-1`         |
| EC2 OS           | Amazon Linux 2023    |
| IAM Role         | `S3-access`          |
| S3 Bucket        | `manan-csvstat-2026` |
| S3 Input Prefix  | `input/`             |
| S3 Output Prefix | `output/`            |

---

## Project Structure

```text
week2/aws/
├── .gitignore
├── README.md
├── csvstat.py
└── requirements.txt
```

---

## Requirements

### AWS

* AWS account
* Amazon EC2 instance
* Amazon S3 bucket
* IAM role attached to the EC2 instance
* S3 permissions for the IAM role

### EC2

* Amazon Linux 2023
* Python 3
* pip
* Git

### Python

The application uses:

* Python standard library
* `boto3`

Dependencies are listed in `requirements.txt`.

---

## IAM Instance Profile

The EC2 instance uses the IAM role:

```text
S3-access
```

The role is attached to the EC2 instance through an IAM instance profile.

The role provides the permissions required for the application to:

* List objects in the S3 bucket
* Read CSV files from `input/`
* Write analysis results to `output/`

No AWS access keys are stored in:

* `csvstat.py`
* `README.md`
* GitHub
* the project configuration

The AWS SDK obtains temporary credentials from the EC2 instance metadata service through the attached IAM role.

### Verify the IAM role

On the EC2 instance:

```bash
aws sts get-caller-identity
```

The returned ARN should show the `S3-access` assumed role.

You can also check:

```bash
aws configure list
```

The credential type should show:

```text
iam-role
```

---

# Setup

## 1. Clone the Repository

On the EC2 instance:

```bash
git clone https://github.com/manan535/python_learning.git
```

Enter the AWS project:

```bash
cd python_learning/week2/aws
```

---

## 2. Create a Python Virtual Environment

Create the environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

The terminal should show:

```text
(.venv)
```

---

## 3. Install Dependencies

Install the required Python package:

```bash
pip install -r requirements.txt
```

Verify that `boto3` is installed:

```bash
python -c "import boto3; print(boto3.__version__)"
```

---

# S3 Configuration

## 1. Create the S3 Bucket

Create the bucket in the Mumbai region:

```bash
aws s3 mb s3://manan-csvstat-2026 --region ap-south-1
```

Verify:

```bash
aws s3 ls
```

---

## 2. Create Input and Output Prefixes

Create the `input/` prefix:

```bash
aws s3api put-object \
    --bucket manan-csvstat-2026 \
    --key input/
```

Create the `output/` prefix:

```bash
aws s3api put-object \
    --bucket manan-csvstat-2026 \
    --key output/
```

Verify:

```bash
aws s3 ls s3://manan-csvstat-2026/
```

Expected:

```text
PRE input/
PRE output/
```

---

# Upload CSV Input Files

The CSV files used for this project are:

```text
example.csv
sales.csv
unsupported_dates.csv
```

Upload them to the S3 `input/` prefix:

```bash
aws s3 cp ./samples/ s3://manan-csvstat-2026/input/ \
    --recursive \
    --exclude "*" \
    --include "*.csv"
```

Verify:

```bash
aws s3 ls s3://manan-csvstat-2026/input/
```

Expected files:

```text
example.csv
sales.csv
unsupported_dates.csv
```

---

# Running CSVStat

The application automatically discovers CSV files under the S3 `input/` prefix.

Run:

```bash
python csvstat.py --bucket manan-csvstat-2026
```

The optional `--top` argument can be used to display the most frequent values for text columns.

For example:

```bash
python csvstat.py --bucket manan-csvstat-2026 --top 5
```

---

# Processing Flow

For every execution:

```text
S3 input/
    |
    | Download CSV
    v
csvstat.py
    |
    | Profile CSV
    |
    | Infer column types
    | Calculate missing values
    | Calculate numeric statistics
    | Detect unsupported date formats
    | Calculate top values when requested
    v
S3 output/run-TIMESTAMP/
```

The application creates a unique output directory using the current date and time.

Example:

```text
output/run-20260814-090425/
```

---

# Output Structure

After a successful run:

```text
s3://manan-csvstat-2026/
├── input/
│   ├── example.csv
│   ├── sales.csv
│   └── unsupported_dates.csv
│
└── output/
    ├── run-20260814-075215/
    │   ├── example.txt
    │   ├── sales.txt
    │   └── unsupported_dates.txt
    │
    └── run-20260814-090425/
        ├── example.txt
        ├── sales.txt
        └── unsupported_dates.txt
```

Each execution creates a new `run-*` directory, so previous results are preserved.

---

# Example Execution

Command:

```bash
python csvstat.py --bucket manan-csvstat-2026
```

Example output:

```text
Processing 3 CSV file(s)...
Output location: s3://manan-csvstat-2026/output/run-20260814-090425/

Processing: input/example.csv
Saved: s3://manan-csvstat-2026/output/run-20260814-090425/example.txt

Processing: input/sales.csv
Saved: s3://manan-csvstat-2026/output/run-20260814-090425/sales.txt

Processing: input/unsupported_dates.csv
Saved: s3://manan-csvstat-2026/output/run-20260814-090425/unsupported_dates.txt

Run completed successfully.
```

---

# Verifying Results

List all generated results:

```bash
aws s3 ls s3://manan-csvstat-2026/output/ --recursive
```

A successful run contains:

```text
example.txt
sales.txt
unsupported_dates.txt
```

To inspect a generated result locally, download it:

```bash
aws s3 cp \
    s3://manan-csvstat-2026/output/run-20260814-090425/sales.txt \
    .
```

Then:

```bash
cat sales.txt
```

---

# CSV Analysis Features

The CSVStat program performs the following analysis:

### Column Type Inference

Columns are classified as:

* `numeric`
* `date`
* `text`

### Missing Values

For each column, the program reports:

* Number of missing values
* Percentage of missing values

### Numeric Statistics

For numeric columns:

* Minimum
* Mean
* Maximum

### Date Detection

Supported date formats include:

```text
YYYY-MM-DD
YYYY-MM-DD HH:MM:SS
DD/MM/YYYY
MM/DD/YYYY
```

The program also detects common date-like values that use unsupported formats and reports a warning.

### Top Values

For text columns, the optional `--top` argument displays the most frequent values.

Example:

```bash
python csvstat.py --bucket manan-csvstat-2026 --top 5
```

---

# Security

The application does not store AWS credentials in source code.

Authentication is handled through the EC2 IAM instance profile:

```text
EC2
 |
 +-- IAM Instance Profile
       |
       +-- S3-access Role
```

This allows AWS SDK operations to use temporary credentials automatically.

The project also excludes local Python environments and cache files through `.gitignore`.

---

# Troubleshooting

## `AccessDenied`

Check the IAM role attached to the EC2 instance:

```bash
aws sts get-caller-identity
```

Then verify that the role has the required S3 permissions.

---

## No CSV files found

Check the S3 input prefix:

```bash
aws s3 ls s3://manan-csvstat-2026/input/
```

Make sure CSV files are present.

---

## `ModuleNotFoundError: No module named 'boto3'`

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

## Python syntax check

Run:

```bash
python3 -m py_compile csvstat.py
```

No output indicates that the syntax check passed.

---

# Git Workflow

After modifying the project:

```bash
git status
```

Stage only the AWS project:

```bash
git add week2/aws/
```

Commit:

```bash
git commit -m "Update AWS CSV processing"
```

Push:

```bash
git push origin main
```

On the EC2 instance, update the clone:

```bash
git pull origin main
```

---

# Cleanup

To remove all objects from the bucket:

```bash
aws s3 rm s3://manan-csvstat-2026/ --recursive
```

Then delete the bucket:

```bash
aws s3 rb s3://manan-csvstat-2026
```

The EC2 instance and IAM role can also be removed from the AWS Console when they are no longer required.

---

# Verification Summary

The implementation was tested successfully on an EC2 Amazon Linux 2023 instance.

The final test processed:

```text
3 CSV files
```

and generated:

```text
example.txt
sales.txt
unsupported_dates.txt
```

under a unique S3 output directory.

The EC2 instance accessed S3 using the:

```text
S3-access
```

IAM instance profile without storing long-term AWS credentials in the application.

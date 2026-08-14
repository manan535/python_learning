# CSVStat - AWS S3 Processing

## Overview

This project runs the CSVStat profiler on an AWS EC2 instance.

CSV files are stored in an Amazon S3 bucket under the `input/` prefix. The
script downloads and processes the CSV files and stores each run's results
under the `output/` prefix.

## Architecture

EC2 Instance
    |
    | IAM Instance Profile
    v
Amazon S3
    |
    +-- input/
    |     +-- example.csv
    |     +-- sales.csv
    |     +-- unsupported_dates.csv
    |
    +-- output/
          +-- run-YYYYMMDD-HHMMSS/

## Requirements

- AWS account
- Amazon EC2 instance
- Amazon Linux 2023
- Python 3
- Git
- Amazon S3 bucket
- IAM instance profile attached to the EC2 instance
- S3 permissions for the instance profile

## Setup

Clone the repository on the EC2 instance:

    git clone https://github.com/manan535/python_learning.git

Enter the AWS project:

    cd python_learning/week2/aws

Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

## S3 Setup

Create the bucket:

    aws s3 mb s3://BUCKET_NAME --region ap-south-1

Create the input and output prefixes:

    aws s3api put-object --bucket BUCKET_NAME --key input/
    aws s3api put-object --bucket BUCKET_NAME --key output/

Upload CSV files:

    aws s3 cp ./samples/ s3://BUCKET_NAME/input/ --recursive --exclude "*" --include "*.csv"

Verify the files:

    aws s3 ls s3://BUCKET_NAME/input/

## IAM Instance Profile

The EC2 instance uses an IAM instance profile to access S3.

No AWS access keys are stored in the source code or on the EC2 instance.

The attached IAM role must have permission to list, read, and write to the
required S3 bucket.

## Running the Program

Run:

    python csvstat.py --bucket BUCKET_NAME

To display the top N values for text columns:

    python csvstat.py --bucket BUCKET_NAME --top 5

The program reads CSV files from:

    s3://BUCKET_NAME/input/

Each execution creates a unique output directory:

    s3://BUCKET_NAME/output/run-YYYYMMDD-HHMMSS/

The results are stored as `.txt` files inside that directory.

## Verify Output

List the generated results:

    aws s3 ls s3://BUCKET_NAME/output/ --recursive

Download an output file if required:

    aws s3 cp s3://BUCKET_NAME/output/RUN_ID/sales.txt .

## Security

AWS credentials are not hard-coded in the application.

The EC2 IAM instance profile is used to obtain temporary AWS credentials.

The `.venv/` directory and Python cache files are excluded from Git.

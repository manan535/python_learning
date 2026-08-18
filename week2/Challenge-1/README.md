# Challenge 1 — Titanic EDA

## Overview

This project performs an exploratory data analysis of the Titanic passenger dataset.

The goal is to determine:

- What is in the dataset?
- What can be trusted?
- What are the three most important findings?
- What data-quality or modeling risks should be considered?

## Dataset

The analysis uses the Titanic `train.csv` dataset containing 891 passenger records and 12 columns.

The dataset includes passenger information such as:

- Passenger class
- Sex
- Age
- Family relationships
- Ticket
- Fare
- Cabin
- Embarkation port
- Survival outcome

The dataset is stored locally in the `data/` directory and is intentionally excluded from Git using `.gitignore`.

Source: Kaggle Titanic dataset.

## Analysis

The notebook covers:

1. Raw data profiling
2. Missing-value analysis
3. Data-type inspection
4. Duplicate detection
5. Missing-value handling
6. Categorical type conversion
7. IQR-based outlier detection
8. Exploratory visualizations
9. Survival analysis by passenger class
10. Survival analysis by sex
11. Age and fare comparisons
12. Sex and passenger-class interaction
13. Family-size analysis
14. Key insights
15. Data-quality and modeling risks
16. Final validation

## Cleaning Decisions

- Missing `Age` values were replaced with the median because age is numerical and the median is less affected by extreme values.
- Missing `Embarked` values were replaced with the mode because it is categorical.
- Missing `Cabin` values were replaced with `"Unknown"` because missing cabin information represents an unknown value rather than a measurable numerical value.
- Duplicate rows were checked and none were found.
- Potential outliers were identified using the IQR method but retained because extreme fares, ages, and family sizes can represent legitimate observations.

## Key Findings

1. Sex and passenger class interact strongly with survival. Female passengers had substantially higher survival rates, while survival also decreased across passenger classes.
2. Small-to-medium family groups showed higher observed survival than solo passengers and very large groups.
3. Survivors paid substantially higher average fares than non-survivors, although fare is related to passenger class and should not be interpreted as a causal factor.

## Modeling Risk

The `Cabin` column contains substantial missingness. Treating missing values as `"Unknown"` preserves records, but the missingness pattern itself may contain information.

`Pclass`, `Fare`, and `Cabin` also contain related information. A model may therefore learn overlapping signals representing passenger circumstances.

These relationships should be interpreted as associations rather than causal effects.

## Files

```text
Challenge-1/
├── data/
│   └── train.csv
├── eda.ipynb
├── summary.md
├── README.md
├── requirements.txt
└── .gitignore
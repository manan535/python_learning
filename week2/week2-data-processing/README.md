# Week 2 – Data Processing & Exploratory Data Analysis

## Overview

This week focuses on data processing and exploratory data analysis using Python.

The project uses the Wine Quality dataset to explore data cleaning, statistical analysis, distributions, outliers, and visualization techniques.

The work is divided into six Jupyter notebooks, progressing from basic dataset exploration to more advanced statistical visualization.

---

## Project Structure

```text
week2-data-processing/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── WineQT.csv
└── notebooks/
    ├── 01_eda.ipynb
    ├── 02_numpy_pandas.ipynb
    ├── 03_distribution.ipynb
    ├── 04_iqr_outliers.ipynb
    ├── 05_kde.ipynb
    └── 06_contour_plots.ipynb
```

---

# Dataset

The project uses the **Wine Quality dataset**.

The dataset contains physicochemical measurements of wine along with a quality score.

Important features include:

- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality

The dataset also contains an `Id` column.

---

# Notebook 1 – Exploratory Data Analysis

### File

```text
notebooks/01_eda.ipynb
```

Topics covered:

- Loading the dataset
- Dataset dimensions
- Column names
- Data types
- Statistical summary
- Missing values
- Duplicate records
- Unique values
- Quality distribution
- Histograms
- Box plots
- Correlation matrix
- Scatter plots
- Feature relationships

The dataset was checked for missing values and duplicate rows.

---

# Notebook 2 – NumPy & Pandas

### File

```text
notebooks/02_numpy_pandas.ipynb
```

### NumPy

Topics covered:

- NumPy arrays
- Array dimensions
- Shape
- Indexing
- Slicing
- Arithmetic operations
- Mean
- Median
- Standard deviation
- Minimum and maximum
- Two-dimensional arrays

### Pandas

Topics covered:

- Series
- DataFrames
- Column selection
- `loc`
- `iloc`
- Filtering
- Sorting
- `value_counts()`
- `groupby()`
- Aggregation
- Missing values
- Duplicate detection
- Creating new columns

---

# Notebook 3 – Distribution Analysis

### File

```text
notebooks/03_distribution.ipynb
```

Topics covered:

- Mean
- Median
- Mode
- Variance
- Standard deviation
- Range
- Skewness
- Kurtosis
- Histograms
- KDE
- Normal distribution
- Empirical rule
- Z-scores

The notebook compares the distribution of the wine features with a normal distribution and examines how mean, median, and standard deviation describe the data.

---

# Notebook 4 – IQR & Outliers

### File

```text
notebooks/04_iqr_outliers.ipynb
```

Topics covered:

- Quartiles
- Q1
- Median
- Q3
- Interquartile Range (IQR)
- Lower and upper outlier boundaries
- Outlier detection
- Outlier counts
- Box plots
- Removing IQR-based outliers
- Comparing data before and after outlier removal

The IQR is calculated using:

```text
IQR = Q3 - Q1
```

Outlier boundaries are calculated using:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

---

# Notebook 5 – Kernel Density Estimation

### File

```text
notebooks/05_kde.ipynb
```

Topics covered:

- Kernel Density Estimation (KDE)
- Histogram vs KDE
- Density estimation
- Bandwidth
- `bw_adjust`
- KDE for multiple features
- KDE by wine quality
- Two-dimensional KDE

Different bandwidth values are compared to understand how bandwidth affects the smoothness and detail of a KDE curve.

---

# Notebook 6 – Contour Plots

### File

```text
notebooks/06_contour_plots.ipynb
```

Topics covered:

- Two-dimensional density
- Contour plots
- Filled contour plots
- KDE-based contours
- Feature-pair comparisons
- Contour plots by wine quality

Contour plots are used to visualize where observations are concentrated across two variables.

---

# Data Quality Checks

The project includes several data-quality checks:

- Missing-value detection
- Duplicate detection
- Data-type inspection
- Unique-value analysis
- Outlier detection

For the dataset used in the notebooks:

```text
Duplicate rows: 0
```

No missing values were found in the dataset columns.

---

# Statistical Concepts

The project covers:

- Mean
- Median
- Mode
- Variance
- Standard deviation
- Range
- Quartiles
- IQR
- Skewness
- Kurtosis
- Normal distribution
- Z-score
- Probability density
- KDE
- Outlier detection

---

# Visualization Techniques

The notebooks use:

- Histograms
- Box plots
- Count plots
- Scatter plots
- Heatmaps
- KDE plots
- 2D KDE
- Contour plots
- Filled contour plots

---

# Technologies

- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- Jupyter Notebook

---

# Installation

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

# Running the Notebooks

Open the project in VS Code or Jupyter.

Run the notebooks in the following order:

```text
01_eda.ipynb
02_numpy_pandas.ipynb
03_distribution.ipynb
04_iqr_outliers.ipynb
05_kde.ipynb
06_contour_plots.ipynb
```

The notebooks use the dataset located at:

```text
data/WineQT.csv
```

---

# Learning Outcomes

By completing this project, the following skills were practiced:

- Loading and inspecting datasets
- Working with NumPy arrays
- Working with Pandas DataFrames
- Cleaning and validating data
- Calculating descriptive statistics
- Understanding distributions
- Identifying skewness
- Detecting outliers using IQR
- Understanding z-scores
- Visualizing distributions
- Understanding KDE and bandwidth
- Creating two-dimensional density visualizations
- Interpreting statistical plots
- Using Python libraries for data analysis

---

# Conclusion

This project provides a practical introduction to data processing and exploratory data analysis.

The notebooks progress from basic dataset inspection and Pandas operations to statistical distributions, outlier detection, KDE, and contour-based visualization.

---

## Author

**Manan Gupta**
import pandas as pd

df = pd.read_csv("week2/Lab3/data.csv")

print(df.isnull().sum())
print(df.isnull().mean() * 100)

df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

df = df.drop_duplicates()

df = df[df["age"].between(18, 100)]

df["join_date"] = df["join_date"].fillna(df["join_date"].mode()[0])

print(df.isnull().sum())
print(df.dtypes)
print(df.describe())
print(df.shape)
print("age: median imputation preserves the typical age without removing rows.")
print("salary: median imputation reduces the effect of extreme salaries.")
print("join_date: mode imputation replaces the invalid date with the most common valid date.")
print("duplicates: duplicate rows were removed to avoid counting the same record twice.")
print("age outlier: age 200 was removed because it is outside a sensible human age range.")
import pandas as pd

df = pd.read_csv("week2/week2-data-processing/data/WineQT.csv")

print(df.head())
df.info()
print(df.describe())
print(df.shape)

print(df[["alcohol", "pH", "quality"]].head())

print(df.loc[0:4, ["alcohol", "quality"]])
print(df.iloc[0:5, 0:3])

print(df[df["quality"] >= 7])

print(df[(df["quality"] >= 7) & (df["alcohol"] > 10)])

df["alcohol_high"] = df["alcohol"] > 10

print(df.groupby("quality")["alcohol"].agg(["mean", "count"]))

print(df.isnull().sum())
print(df.duplicated().sum())
df1 = df[["Id", "quality"]]
df2 = df[["Id", "alcohol"]]

merged = pd.merge(df1, df2, on="Id")

print(merged.head())
print(merged.shape)
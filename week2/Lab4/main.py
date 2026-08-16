import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

df = pd.read_csv("week2/week2-data-processing/data/WineQT.csv")

alcohol = df["alcohol"]

print(alcohol.mean())
print(alcohol.median())
print(alcohol.std())
print(alcohol.quantile([0.25, 0.5, 0.75]))

print(alcohol.skew())

q1 = alcohol.quantile(0.25)
q3 = alcohol.quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[(alcohol < lower) | (alcohol > upper)]

print(lower)
print(upper)
print(outliers.shape[0])

plt.hist(alcohol, bins=20)
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.title("Alcohol Distribution")
plt.show()

correlation = df.corr(numeric_only=True)
corr = correlation.abs().where(correlation.abs() < 1)
strongest = corr.stack().idxmax()

print(strongest)
print(correlation.loc[strongest])

group1 = df[df["quality"] <= 5]["alcohol"]
group2 = df[df["quality"] >= 6]["alcohol"]

t_stat, p_value = ttest_ind(group1, group2, equal_var=False)

print(t_stat)
print(p_value)

print("Higher-quality wines have higher mean alcohol content.")
print("The p-value measures evidence against equal group means.")
print("A small p-value does not prove that alcohol causes higher quality.")
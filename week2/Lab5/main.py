import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("week2/week2-data-processing/data/WineQT.csv")

plt.hist(df["alcohol"], bins=20)
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.title("Alcohol Distribution")
plt.show()

quality_counts = df["quality"].value_counts().sort_index()

plt.bar(quality_counts.index, quality_counts.values)
plt.xlabel("Quality")
plt.ylabel("Count")
plt.title("Wine Quality Distribution")
plt.show()

plt.scatter(df["alcohol"], df["quality"])
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.title("Alcohol vs Quality")
plt.show()

plt.boxplot(df["alcohol"])
plt.ylabel("Alcohol")
plt.title("Alcohol Box Plot")
plt.show()

print(df.groupby("quality")["alcohol"].mean())
print(df.groupby("quality")["alcohol"].median())
print(df.groupby("quality")["alcohol"].count())
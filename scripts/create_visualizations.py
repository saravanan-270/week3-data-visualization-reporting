import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/gapminder_cleaned.csv")

# Bar chart
d2007 = df[df["year"] == 2007].groupby("continent")["lifeexp"].mean().sort_values(ascending=False)
plt.figure(figsize=(10,6))
plt.bar(d2007.index, d2007.values)
plt.title("Average Life Expectancy by Continent — 2007")
plt.xlabel("Continent"); plt.ylabel("Average Life Expectancy (years)")
plt.tight_layout(); plt.show()

# Line chart
trend = df.groupby("year")["lifeexp"].mean()
plt.figure(figsize=(10,6))
plt.plot(trend.index, trend.values, marker="o")
plt.title("Global Average Life Expectancy Over Time")
plt.xlabel("Year"); plt.ylabel("Average Life Expectancy (years)")
plt.grid(alpha=.25); plt.tight_layout(); plt.show()

# Scatter plot
s = df[df["year"] == 2007]
plt.figure(figsize=(10,6))
for continent, g in s.groupby("continent"):
    plt.scatter(g["gdp_per_capita"], g["lifeexp"], label=continent, alpha=.7)
plt.xscale("log")
plt.title("GDP per Capita vs Life Expectancy — 2007")
plt.xlabel("GDP per Capita (log scale)")
plt.ylabel("Life Expectancy (years)")
plt.legend(title="Continent")
plt.tight_layout(); plt.show()

# Heatmap
pivot = df.pivot_table(index="continent", columns="year", values="lifeexp", aggfunc="mean")
plt.figure(figsize=(12,5))
plt.imshow(pivot.values, aspect="auto")
plt.colorbar(label="Average Life Expectancy")
plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=45)
plt.yticks(range(len(pivot.index)), pivot.index)
plt.title("Average Life Expectancy by Continent and Year")
plt.tight_layout(); plt.show()

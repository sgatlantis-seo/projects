import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
flights_year = flights.groupby("year", as_index=False)['passengers'].sum()
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

sns.barplot(x="year", y="passengers", data=flights_year)
plt.savefig("flights_year_barplot.png")

sns.heatmap(flights_pivot, cmap="YlGnBu", annot=True, fmt="d")
plt.savefig("flights_pivot_heatmap.png")

print(flights_year.corr())

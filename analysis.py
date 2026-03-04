import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("pokemon_data.csv")

print(data.head())

print("Total Rows:", len(data))

type_count = data["Type 1"].value_counts()

print(type_count)

type_count.plot(kind="bar")

plt.title("Pokemon Types Distribution")

plt.xticks()   # x-axis values
plt.yticks()   # y-axis values

plt.show()

legendary = data[data["Legendary"] == True]

print("Legendary Pokemon Count:", len(legendary))

# avg ATTACK by pokemon 

print("\nAverage Attack by Pokemon Type:")
avg_attack = data.groupby("Type 1")["Attack"].mean()

print(avg_attack)

# top 10 strongest pokemon

print("\n Top 10 Strongest Pokemon: ")

top_attack = data.sort_values("Attack", ascending = False)

print(top_attack[["Name","Attack"]].head(10))

# Top 5 Fastest Pokémon

print("\nTop 5 Fastest Pokemon:")

fastest = data.sort_values("Speed", ascending=False)

print(fastest[["Name","Speed"]].head(5))

## ATTACK DISTRIBUTION GRAPH 

data["Attack"].hist(bins=20)

plt.title("Attack Distribution")

plt.xlabel("Attack")

plt.ylabel("Count")

plt.xticks()   # x-axis values
plt.yticks()   # y-axis values

plt.show()
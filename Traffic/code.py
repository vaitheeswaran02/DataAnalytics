import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("traffic.csv")

# Replace missing values with 0
df["Vehicle_Count"].fillna(0, inplace=True)

# Calculate total and average
total = df["Vehicle_Count"].sum()
average = df["Vehicle_Count"].mean()

print("Total Traffic:", total)
print("Average Traffic:", average)

# Find date with highest traffic
max_date = df.loc[df["Vehicle_Count"].idxmax(), "Date"]
print("Highest Traffic Date:", max_date)

# Plot line graph
plt.plot(df["Date"], df["Vehicle_Count"], marker='o')
plt.xticks(rotation=45)
plt.title("Daily Traffic Volume")
plt.xlabel("Date")
plt.ylabel("Vehicle Count")
plt.show()

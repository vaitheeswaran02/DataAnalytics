import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("temperature.csv")

# Fill missing values with column average
df["Min_Temp"].fillna(df["Min_Temp"].mean(), inplace=True)
df["Max_Temp"].fillna(df["Max_Temp"].mean(), inplace=True)

# Add Average_Temp column
df["Average_Temp"] = (df["Min_Temp"] + df["Max_Temp"]) / 2

# Find date with highest average temperature
max_date = df.loc[df["Average_Temp"].idxmax(), "Date"]
print("Hottest Date:", max_date)

# Plot line chart
plt.plot(df["Date"], df["Average_Temp"], marker='o')
plt.xticks(rotation=45)
plt.title("Average Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()

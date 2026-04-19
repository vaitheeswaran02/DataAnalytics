import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (from CSV)
df = pd.read_csv("sales.csv")

# Fill missing Price with average price of same product
df["Price"] = df.groupby("Product")["Price"].transform(lambda x: x.fillna(x.mean()))

# Create Total_Sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Find product with highest sales
total_sales = df.groupby("Product")["Total_Sales"].sum()
print("Top Product:", total_sales.idxmax())

# Plot bar chart
total_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.show()

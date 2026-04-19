import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ratings.csv")

# Remove rows with missing ratings
df = df.dropna()

# Average rating
avg_rating = df["Customer_Rating"].mean()
print("Average Rating:", avg_rating)

# Top 3 highest-rated products
top3 = df.sort_values(by="Customer_Rating", ascending=False).head(3)
print("Top 3 Products:\n", top3)

# Top 5 for visualization
top5 = df.sort_values(by="Customer_Rating", ascending=False).head(5)

# Bar chart
plt.bar(top5["Product_Name"], top5["Customer_Rating"])
plt.title("Top 5 Product Ratings")
plt.xlabel("Product")
plt.ylabel("Rating")
plt.show()

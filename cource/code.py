import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Fill missing values with "No"
df["Completion_Status"].fillna("No", inplace=True)

# Count completed and not completed
count = df["Completion_Status"].value_counts()
print(count)

# Pie chart
plt.pie(count, labels=count.index, autopct='%1.1f%%')
plt.title("Course Completion Status")
plt.show()

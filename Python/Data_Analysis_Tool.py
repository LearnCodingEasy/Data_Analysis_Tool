
# 📌 Step 1: Import the required libraries
# pandas: for working with data
# matplotlib: for visualizing data

import pandas as pd
import matplotlib.pyplot as plt

# 📌 Step 2: Define our sample data
# We're creating a simple dataset that contains:
# - User names
# - Their ages
# - Their sales numbers

data = {
    'User_Name': ['Ahmed', 'Mahmoud', 'Fatima', 'Sara', 'Hossam'],
    'User_Age': [23, 25, 22, 30, 33],
    'User_Sales': [1200, 1500, 800, 1800, 2500]
}

# 📌 Step 3: Convert the data into a DataFrame
# Think of a DataFrame as a table like you’d see in Excel or Google Sheets

df = pd.DataFrame(data)

# 📌 Step 4: Analyze the data
# Let's calculate the average (mean) sales value
average_sales = df['User_Sales'].mean()

# 📌 Step 5: Visualize the sales data using a bar chart
# Each bar represents a user and their total sales

plt.figure(figsize=(10, 6))  # Set the size of the chart
plt.bar(df['User_Name'], df['User_Sales'], color='skyblue')  # Create the bars

# Add chart title and labels
plt.title('User Sales Overview', fontsize=16)
plt.xlabel('User Name', fontsize=12)
plt.ylabel('Sales', fontsize=12)

# Show the chart
plt.tight_layout()  # Better spacing
plt.show()

# 📌 Step 6: Display the average sales in the terminal
print("="*40)
print(f"Average Sales: {average_sales}")
print("="*40)

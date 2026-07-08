import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print("First 5 Rows")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

# ==========================
# DATA CLEANING
# ==========================

df.drop_duplicates(inplace=True)

# ==========================
# DATA STORYTELLING
# ==========================

# Sales by Category
sales_category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
sales_category.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Profit by Category
profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit_category.plot(kind="bar")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7,7))
plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%"
)
plt.title("Sales Distribution by Region")
plt.show()

# Top 10 States by Sales
top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_states.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.show()

# ==========================
# HYPOTHESIS TESTING
# ==========================

print("\n===== HYPOTHESIS TESTING =====")

discount_profit = df[df["Discount"] > 0]["Profit"]
no_discount_profit = df[df["Discount"] == 0]["Profit"]

t_stat, p_value = ttest_ind(
    discount_profit,
    no_discount_profit,
    equal_var=False
)

print("T Statistic =", t_stat)
print("P Value =", p_value)

if p_value < 0.05:
    print("\nReject Null Hypothesis")
    print("Discount significantly affects profit.")
else:
    print("\nFail to Reject Null Hypothesis")
    print("Discount does not significantly affect profit.")

# ==========================
# BUSINESS INSIGHTS
# ==========================

print("\n===== BUSINESS INSIGHTS =====")

print(
    "Highest Sales Category:",
    df.groupby("Category")["Sales"].sum().idxmax()
)

print(
    "Highest Profit Category:",
    df.groupby("Category")["Profit"].sum().idxmax()
)

print(
    "Best Performing Region:",
    df.groupby("Region")["Sales"].sum().idxmax()
)

print("\nConclusion:")
print("1. Technology category generates the highest sales.")
print("2. Focus on high-profit categories for growth.")
print("3. Strong-performing regions should receive more investment.")
print("4. Discounts should be optimized to maximize profitability.")

print("Task-4 COMPLETED SUCCESSFULLY")
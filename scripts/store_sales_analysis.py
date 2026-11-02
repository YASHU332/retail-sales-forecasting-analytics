
import pandas as pd
import matplotlib.pyplot as plt

# Load the retail sales dataset
df = pd.read_csv("data/retail_sales_data.csv")

# Calculate total sales for each store
store_sales = df.groupby("Store")["Sales"].sum().sort_values(ascending=False)

print("Total sales by store:")
print(store_sales)

# Create the chart
plt.figure(figsize=(10, 6))

bars = plt.bar(
    store_sales.index,
    store_sales.values
)

# Add sales values above each bar
for bar in bars:
    value = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:,.0f}",
        ha="center",
        va="bottom"
    )

plt.title("Total Retail Sales by Store (2015–2024)")
plt.xlabel("Store")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

# Save the chart
plt.savefig("reports/store_sales_comparison.png", dpi=300)

plt.show()

print("\nChart saved successfully!")

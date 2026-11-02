
import pandas as pd
import matplotlib.pyplot as plt

# Load the retail sales dataset
df = pd.read_csv("data/retail_sales_data.csv")

# Calculate total sales for each category
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Display category sales
print("Total sales by category:")
print(category_sales)

# Create category sales chart
plt.figure(figsize=(10, 6))

bars = plt.bar(category_sales.index, category_sales.values)

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

plt.title("Total Sales by Product Category (2015–2024)")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

# Save chart
plt.savefig("reports/category_sales_comparison.png", dpi=300)

print("\nCategory sales chart saved successfully!")
plt.show()

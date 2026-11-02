
import pandas as pd
import matplotlib.pyplot as plt

# Load the retail sales dataset
df = pd.read_csv("data/retail_sales_data.csv")

# Convert Date column into date format
df["Date"] = pd.to_datetime(df["Date"])

# Group sales by month
monthly_sales = (
    df.set_index("Date")["Sales"]
    .resample("MS")
    .sum()
)

# Display monthly sales
print("First 12 months of sales:")
print(monthly_sales.head(12))

# Create monthly sales chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Retail Sales Trend (2015–2024)")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()

# Save chart inside reports folder
plt.savefig("reports/monthly_sales_trend.png", dpi=300)

print("\nMonthly sales chart saved successfully!")
plt.show()

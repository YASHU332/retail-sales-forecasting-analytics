
import pandas as pd
import matplotlib.pyplot as plt

# Load the retail sales dataset
df = pd.read_csv("data/retail_sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total sales for each year
yearly_sales = df.groupby(df["Date"].dt.year)["Sales"].sum()

# Display yearly sales
print("Total sales by year:")
print(yearly_sales)

# Create yearly sales chart
plt.figure(figsize=(11, 6))

bars = plt.bar(yearly_sales.index.astype(str), yearly_sales.values)

# Add sales values above each bar
for bar in bars:
    value = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:,.0f}",
        ha="center",
        va="bottom",
        fontsize=8
    )

plt.title("Yearly Retail Sales (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

# Save chart
plt.savefig("reports/yearly_sales_trend.png", dpi=300)

print("\nYearly sales chart saved successfully!")
plt.show()


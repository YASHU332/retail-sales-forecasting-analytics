
# Retail Sales Forecasting with Prophet
# ---------------------------------------------------------------
# Usage:
#   pip install prophet matplotlib pandas scikit-learn
#   python forecast_with_prophet.py
# Outputs:
#   - performance.csv : Backtest metrics on the last 6 months
#   - forecast.csv : Prophet forecast for next 12 months
#   - forecast_plot.png : Plot of history + forecast
# ---------------------------------------------------------------

import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_percentage_error
import matplotlib.pyplot as plt

# Load data
monthly_total = pd.read_csv("data/monthly_total_for_prophet.csv", parse_dates=["ds"])

# Train/Test split: last 6 months as test
cutoff = monthly_total["ds"].max() - pd.offsets.MonthBegin(5)
train = monthly_total[monthly_total["ds"] < cutoff].copy()
test = monthly_total[monthly_total["ds"] >= cutoff].copy()

# Fit Prophet
m = Prophet(seasonality_mode="additive", yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
m.fit(train)

# In-sample forecast to evaluate on test period
future = pd.DataFrame({"ds": pd.date_range(train["ds"].min(), test["ds"].max(), freq="MS")})
fcst = m.predict(future)

# Evaluate accuracy on test
eval_df = fcst.merge(test, on="ds", how="inner")
mape = mean_absolute_percentage_error(eval_df["y"], eval_df["yhat"]) * 100
accuracy = 100 - mape

# Save backtest metrics
perf = pd.DataFrame({
    "metric": ["MAPE", "Accuracy(100-MAPE)"],
    "value": [mape, accuracy],
})
perf.to_csv("performance.csv", index=False)

# Forecast next 12 months
future_12 = m.make_future_dataframe(periods=12, freq="MS")
fcst_12 = m.predict(future_12)
fcst_12.to_csv("forecast.csv", index=False)

# Plot
fig = plt.figure()
plt.plot(monthly_total["ds"], monthly_total["y"], label="History")
plt.plot(fcst_12["ds"], fcst_12["yhat"], label="Forecast")
plt.fill_between(fcst_12["ds"], fcst_12["yhat_lower"], fcst_12["yhat_upper"], alpha=0.2)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Retail Monthly Sales Forecast (Prophet)")
plt.legend()
plt.tight_layout()
fig.savefig("forecast_plot.png", dpi=150)

print("Saved: performance.csv, forecast.csv, forecast_plot.png")
print(f"Accuracy on last 6 months: {accuracy:.2f}%")

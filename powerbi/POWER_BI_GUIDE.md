
# Power BI Dashboard – Retail Sales KPIs

## Data Sources (CSV)
- `monthly_sales_by_store.csv` – Month, Store, SalesAmount
- `monthly_sales_by_category.csv` – Month, Category, SalesAmount
- `forecast.csv` (after running Prophet script) – ds, yhat, yhat_lower, yhat_upper

## Recommended Model
- Create a Date table (Month granularity) using Power BI:
  ```DAX
  Dates = CALENDAR(MIN('Sales'[Month]), MAX('Sales'[Month]))
  ```

- Relationships:
  - `Sales[Month]` -> `Dates[Date]` (Many-to-One)
  - `Forecast[ds]` -> `Dates[Date]` (Many-to-One)

## Suggested KPIs
1. **Total Sales (MTD/QTD/YTD)**
   ```DAX
   Total Sales := SUM(Sales[SalesAmount])
   Sales YTD := TOTALYTD([Total Sales], 'Dates'[Date])
   ```

2. **Forecast vs Actual**
   ```DAX
   Forecast := SUM(Forecast[yhat])
   Variance := [Total Sales] - [Forecast]
   Variance % := DIVIDE([Variance], [Forecast])
   ```

3. **Revenue Target Attainment**
   - Create a Target table with monthly targets.
   ```DAX
   Target := SUM(Targets[TargetAmount])
   Target Attainment % := DIVIDE([Total Sales], [Target])
   ```

4. **Seasonality: Peak Months**
   - Line chart with `Dates[Date]` on axis and `[Total Sales]` + `[Forecast]` as values.

5. **Inventory Optimization Indicator**
   - Proxy metric: When forecast exceeds target by a margin (e.g., 10%+), flag potential overstock or understock risks.
   ```DAX
   Overstock Risk Flag := IF([Variance %] > 0.10, 1, 0)
   Understock Risk Flag := IF([Variance %] < -0.10, 1, 0)
   ```

## Visuals Layout
- Card: Total Sales (YTD), Forecast Accuracy (from `performance.csv`)
- Line chart: Actual vs Forecast with confidence band
- Bar charts: Sales by Store, Sales by Category
- Slicers: Store, Category, Month

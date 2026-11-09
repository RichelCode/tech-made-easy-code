"""Time Series Forecasting, Explained Simply: the code.

Builds 36 months of pretend ice cream sales from trend + season + noise,
holds back the last 9 months, and compares three forecasts from simplest to smartest.
Then it shows what goes wrong if you shuffle the data before splitting.

Run:  python forecast.py
"""
import json

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# ---------- 1. Make the data: trend + season + noise ----------
rng = np.random.default_rng(42)
months = pd.date_range("2023-01-01", periods=36, freq="MS")
t = np.arange(36)

trend = 100 + 1.5 * t                                      # slowly climbing
season = 12 * np.sin(2 * np.pi * (months.month - 4) / 12)  # peaks in summer
noise = rng.normal(0, 4, size=36)                          # random wiggles

df = pd.DataFrame({"month": months, "sales": (trend + season + noise).round(1)})
df["t"] = t
df["month_of_year"] = df["month"].dt.month

# ---------- 2. Split by time: train on the past, test on the future ----------
TEST_MONTHS = 9
train = df.iloc[:-TEST_MONTHS]
test = df.iloc[-TEST_MONTHS:]
print(f"Train: {train.month.min():%b %Y} to {train.month.max():%b %Y} ({len(train)} months)")
print(f"Test:  {test.month.min():%b %Y} to {test.month.max():%b %Y} ({len(test)} months)\n")

# ---------- 3. Three forecasts, simplest first ----------
# Model 1, naive: every future month = the last month we saw.
naive = np.full(TEST_MONTHS, train.sales.iloc[-1])

# Model 2, seasonal naive: every future month = the same month last year.
seasonal_naive = df.sales.shift(12).iloc[-TEST_MONTHS:].to_numpy()


# Model 3, trend + season: a straight line plus a bump for each month of the year.
def features(frame):
    X = pd.get_dummies(frame.month_of_year, prefix="m").reindex(
        columns=[f"m_{m}" for m in range(1, 13)], fill_value=0)
    X.insert(0, "t", frame.t)
    return X.astype(float)


model = LinearRegression().fit(features(train), train.sales)
trend_season = model.predict(features(test))

# ---------- 4. Check the error ----------
scores = {
    "Naive (last month)": mean_absolute_error(test.sales, naive),
    "Seasonal naive (same month last year)": mean_absolute_error(test.sales, seasonal_naive),
    "Trend + season": mean_absolute_error(test.sales, trend_season),
}
print("Mean absolute error on the 9 test months (units off, on average):")
for name, mae in scores.items():
    print(f"  {name:<40} {mae:5.1f}")

# ---------- 5. The common mistake: shuffle, then split ----------
# A random forest is a popular, flexible model. Watch how the split changes its score.
X_all = df[["t", "month_of_year"]]

# Wrong way: train_test_split shuffles rows by default, so the model trains on
# months on both sides of each test month and just copies its neighbours.
X_tr, X_te, y_tr, y_te = train_test_split(X_all, df.sales, test_size=TEST_MONTHS, random_state=0)
forest = RandomForestRegressor(random_state=0).fit(X_tr, y_tr)
shuffled_mae = mean_absolute_error(y_te, forest.predict(X_te))

# Right way: train on the past, test on the future.
forest = RandomForestRegressor(random_state=0).fit(X_all.iloc[:-TEST_MONTHS], train.sales)
time_mae = mean_absolute_error(test.sales, forest.predict(X_all.iloc[-TEST_MONTHS:]))

print(f"\nRandom forest, shuffled split: {shuffled_mae:5.1f}   <- looks amazing")
print(f"Random forest, time split:     {time_mae:5.1f}   <- what really happens")

# Save numbers for the article's chart
json.dump({
    "month_index": [int(i) + 1 for i in t],
    "actual": df.sales.tolist(),
    "forecast_months": [int(i) + 1 for i in test.t],
    "forecast": [round(float(v), 1) for v in trend_season],
    "split_at": len(train) + 0.5,
    "mae": {k: round(v, 1) for k, v in scores.items()},
    "forest_shuffled_mae": round(shuffled_mae, 1),
    "forest_time_mae": round(time_mae, 1),
}, open("results.json", "w"), indent=2)
print("\nSaved results.json")

"""Build Your First Demand Forecast in Python, Step by Step: the code.

Builds two years of pretend daily coffee sales for a small shop (weekly pattern,
yearly season, gentle trend, a few promotion days, noise), holds back the last
8 weeks, beats two baselines with a model, then forecasts the next 14 days.
It also shows how one tiny leak in a feature makes a model look better than it is.

Run:  python forecast.py
"""
import json

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# ---------- 1. Make the data: two years of daily cups sold ----------
rng = np.random.default_rng(7)
dates = pd.date_range("2024-11-01", "2026-10-31", freq="D")
n = len(dates)
t = np.arange(n)

trend = 120 + 0.03 * t                                           # gentle growth
weekly = np.array([-10, -8, -6, -4, 6, 18, 14])[dates.day_of_week]  # Mon..Sun, busy weekends
yearly = 12 * np.cos(2 * np.pi * (dates.day_of_year - 15) / 365.25)  # busiest in winter
promo = np.zeros(n, dtype=int)
promo[rng.choice(n, size=20, replace=False)] = 1                 # 20 promotion days
noise = rng.normal(0, 6, size=n)

df = pd.DataFrame({"date": dates, "promo": promo})
df["cups"] = (trend + weekly + yearly + 35 * promo + noise).round().astype(int)
print(df.head(3).to_string(index=False), "\n")

# ---------- 2. Split by time: the last 8 weeks are the test ----------
TEST_DAYS = 56
split_date = df.date.iloc[-TEST_DAYS]
is_test = df.date >= split_date
print(f"Train: {df.date.min():%d %b %Y} to {df.date[~is_test].max():%d %b %Y} ({(~is_test).sum()} days)")
print(f"Test:  {split_date:%d %b %Y} to {df.date.max():%d %b %Y} ({is_test.sum()} days)\n")


# ---------- 3. Features: clues the model may use, all from the PAST ----------
def add_features(frame):
    f = frame.copy()
    f["day_of_week"] = f.date.dt.day_of_week
    f["month"] = f.date.dt.month
    f["lag_7"] = f.cups.shift(7)                             # same weekday last week
    f["rolling_7"] = f.cups.shift(1).rolling(7).mean()       # average of the 7 days BEFORE today
    return f


def to_X(f):
    X = pd.get_dummies(f[["day_of_week", "month"]].astype("category"))
    X = X.reindex(columns=[f"day_of_week_{d}" for d in range(7)] + [f"month_{m}" for m in range(1, 13)],
                  fill_value=0)
    return pd.concat([X, f[["lag_7", "rolling_7", "promo"]]], axis=1).astype(float)


feat = add_features(df)
train = feat[~is_test].dropna()       # the first week has no lag yet, so drop it
test = feat[is_test]

# ---------- 4. Baselines and a model, each forecasting one day ahead ----------
# Each morning in the test period, we forecast today using only what we knew up to yesterday.
naive = df.cups.shift(1)[is_test]             # today = yesterday
seasonal_naive = df.cups.shift(7)[is_test]    # today = same weekday last week

model = LinearRegression().fit(to_X(train), train.cups)
model_pred = model.predict(to_X(test))

scores = {
    "Naive (yesterday)": mean_absolute_error(test.cups, naive),
    "Seasonal naive (same day last week)": mean_absolute_error(test.cups, seasonal_naive),
    "Model with features": mean_absolute_error(test.cups, model_pred),
}
print("Mean absolute error on the 56 test days (cups off, on average):")
for name, mae in scores.items():
    print(f"  {name:<38} {mae:5.1f}")

# ---------- 5. The sneaky mistake: a feature that peeks at today ----------
leaky = feat.copy()
leaky["rolling_7"] = leaky.cups.rolling(7).mean()   # forgot shift(1): includes TODAY's sales
leaky_model = LinearRegression().fit(to_X(leaky[~is_test].dropna()), leaky[~is_test].dropna().cups)
leaky_mae = mean_absolute_error(test.cups, leaky_model.predict(to_X(leaky[is_test])))
print(f"\nLeaky rolling mean (includes today): {leaky_mae:5.1f}   <- looks amazing, can't exist in real life")
print(f"Safe rolling mean (past days only):  {scores['Model with features']:5.1f}   <- the honest score")

# ---------- 6. Forecast the next 14 days ----------
# Retrain on ALL the history, then step forward one day at a time.
# Each prediction becomes "history" for the days after it.
full = feat.dropna()
model = LinearRegression().fit(to_X(full), full.cups)

future_dates = pd.date_range(df.date.max() + pd.Timedelta(days=1), periods=14, freq="D")
planned_promos = {pd.Timestamp("2026-11-07")}         # promotions are planned ahead, so we know them
history = df[["date", "cups", "promo"]].copy()
for day in future_dates:
    row = pd.DataFrame({"date": [day], "cups": [np.nan], "promo": [int(day in planned_promos)]})
    history = pd.concat([history, row], ignore_index=True)
    x = to_X(add_features(history).tail(1))
    history.loc[history.index[-1], "cups"] = round(float(model.predict(x)[0]))

future = history.tail(14)
print("\nNext 14 days:")
for _, r in future.iterrows():
    print(f"  {r.date:%a %d %b}  {int(r.cups):4d} cups{'   (promo)' if r.promo else ''}")
print(f"  Total: {int(future.cups.sum())} cups")

# Save numbers for the article's charts
last = 98  # last 14 weeks of history, so the chart stays readable
show = df.tail(last)
day0 = show.date.iloc[0]
json.dump({
    "n_days": n,
    "train_days": int((~is_test).sum()),
    "test_days": TEST_DAYS,
    "chart_day": [int((d - day0).days) + 1 for d in show.date] + [last + i + 1 for i in range(14)],
    "chart_start": f"{day0:%d %b %Y}",
    "actual_day": [int((d - day0).days) + 1 for d in show.date],
    "actual": show.cups.tolist(),
    "test_day": [int((d - day0).days) + 1 for d in test.date],
    "test_pred": [round(float(v), 1) for v in model_pred],
    "future_day": [last + i + 1 for i in range(14)],
    "future": [int(v) for v in future.cups],
    "future_dates": [f"{d:%a %d %b}" for d in future.date],
    "future_total": int(future.cups.sum()),
    "split_at": int((split_date - day0).days) + 0.5,
    "future_at": last + 0.5,
    "mae": {k: round(v, 1) for k, v in scores.items()},
    "leaky_mae": round(leaky_mae, 1),
}, open("results.json", "w"), indent=2)
print("\nSaved results.json")

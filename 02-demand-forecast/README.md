# ☕ Build Your First Demand Forecast in Python, Step by Step

**Two years of coffee sales, two baselines, one model and the next 14 days.**

This is the code for my Medium story *Build Your First Demand Forecast in Python, Step by Step*.

📖 **Read the story:** [link coming soon]

## What this code does
The script builds two years of pretend daily coffee sales for a small shop: a weekly pattern, a yearly season, a gentle trend, a few promotion days and some noise. It holds back the last 8 weeks as a test set, compares two simple baselines with a linear regression that uses calendar, lag and promo features, then forecasts the next 14 days. It also shows a sneaky leak: a rolling average that accidentally includes today's sales.

## What you'll learn
- **Features are clues.** Calendar, memory and known plans turn a list of numbers into something a model can learn from.
- **Every clue must come from the past.** Shift your lags and rolling averages, or the model peeks at the answer.
- **Beat your baselines, then look ahead.** Our model beat "yesterday" and "same day last week", then forecast 14 new days one step at a time.

## What's in this folder
- `forecast.py`: the full code. It runs top to bottom, and numbered comments mark each step from the story.
- `requirements.txt`: the Python packages the code needs.
- `results.json`: created when you run the script. It holds the numbers it printed.

## What you need
- Python 3.9 or newer
- About two minutes
- New to Python or the terminal? Follow the [Getting Started guide](../GETTING_STARTED.md) first. It walks you through every step.

## How to run it
Open a terminal inside this folder, then run these four lines one at a time:
```bash
python3 -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python forecast.py
```

## What you should see
```
Train: 01 Nov 2024 to 05 Sep 2026 (674 days)
Test:  06 Sep 2026 to 31 Oct 2026 (56 days)

Mean absolute error on the 56 test days (cups off, on average):
  Naive (yesterday)                        9.2
  Seasonal naive (same day last week)      8.2
  Model with features                      6.4

Leaky rolling mean (includes today):   5.3   <- looks amazing, can't exist in real life
Safe rolling mean (past days only):    6.4   <- the honest score
```
After that it prints a forecast for each of the next 14 days (2,110 cups in total). Your numbers should match these (or land very close, if you have newer package versions). The script also saves them to `results.json`, which is what the story's chart is drawn from.

**A note on the random seed:** the data uses seed 7, the first one I tried. I also ran seeds 0 to 11. The order never changed: the model always beat both baselines (its error ranged from about 4.7 to 6.7 cups), and the leaky feature always looked better than the honest one. Seed 7 actually gives the model one of its smaller wins.

---

⬅️ [Back to all projects](../README.md)

Part of my **Tech Made Easy** series. Richel makes tech easy 💕

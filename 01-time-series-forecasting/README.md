# 📈 Time Series Forecasting, Explained Simply

**How models learn from the past to predict tomorrow, with no heavy math.**

This is the code for my Medium story *Time Series Forecasting, Explained Simply*.

📖 **Read the story:** [link coming soon]

## What this code does
The script builds 36 months of pretend ice cream sales from three parts: a trend, a season and some noise. It holds back the last 9 months as a test set and compares three forecasts, from simplest to smartest. Then it shows the most common forecasting mistake: shuffling your data before you split it.

## What you'll learn
- **Every time series is trend + season + noise.** Model the first two, and let the noise go.
- **Always split by time.** Train on the past, test on the future, never shuffle.
- **Beat a simple baseline first.** If your model can't beat "same as last month", it isn't ready.

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
Train: Jan 2023 to Mar 2025 (27 months)
Test:  Apr 2025 to Dec 2025 (9 months)

Mean absolute error on the 9 test months (units off, on average):
  Naive (last month)                        16.1
  Seasonal naive (same month last year)     19.7
  Trend + season                             2.9

Random forest, shuffled split:   3.4   <- looks amazing
Random forest, time split:      20.0   <- what really happens
```
Your numbers should match these (or land very close, if you have newer package versions). The script also saves them to `results.json`, which is what the story's chart is drawn from.

**A note on the shuffled score:** it depends on which months the shuffle happens to pick. With other random seeds it lands between about 3 and 7. That's still far better than the honest 20.0, which is the point.

---

⬅️ [Back to all projects](../README.md)

Part of my **Tech Made Easy** series. Richel makes tech easy 💕

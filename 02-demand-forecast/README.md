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


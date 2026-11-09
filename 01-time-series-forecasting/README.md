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


# ☕ Build Your First Demand Forecast in Python, Step by Step

**Two years of coffee sales, two baselines, one model and the next 14 days.**

This is the code for my Medium story *Build Your First Demand Forecast in Python, Step by Step*.

📖 **Read the story:** [link coming soon]

## What this code does
The script builds two years of pretend daily coffee sales for a small shop: a weekly pattern, a yearly season, a gentle trend, a few promotion days and some noise. It holds back the last 8 weeks as a test set, compares two simple baselines with a linear regression that uses calendar, lag and promo features, then forecasts the next 14 days. It also shows a sneaky leak: a rolling average that accidentally includes today's sales.


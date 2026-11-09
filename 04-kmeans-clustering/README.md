# 🔵 K-Means Clustering, Explained Simply

**How machines find groups on their own, with no heavy math.**

This is the code for my Medium story *K-Means Clustering, Explained Simply*.

📖 **Read the story:** [link coming soon]

## What this code does
The script builds 300 pretend shop customers, each described by two numbers: how much they spend in a year and how many times they visit per month. Hidden inside are three types of customer, but K-Means never gets told about them. It scales the data, tries k = 1 to 8, uses the elbow and the silhouette score to pick the number of groups, and describes what it found. Then it shows the most common K-Means mistake: forgetting to scale.

## What you'll learn
- **K-Means finds groups without labels.** Place centres, assign each point to the nearest one, move the centres, repeat.
- **Always scale first.** K-Means runs on distance, so a column with big numbers will drown out the rest.
- **Don't guess k.** Use the elbow and the silhouette score, then describe each group in plain words to check it makes sense.

## What's in this folder
- `kmeans.py`: the full code. It runs top to bottom, and numbered comments mark each step from the story.
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
python kmeans.py
```


# 🍷 PCA, Explained Simply

**How to shrink your data without losing the story, with no heavy math.**

This is the code for my Medium story *PCA, Explained Simply*.

📖 **Read the story:** [link coming soon]

## What this code does
The script loads the wine dataset that ships with scikit-learn: 178 wines, 13 chemical measurements each, from 3 grape types. It shows why you must scale your data before PCA, runs PCA, reports how much information each component keeps, and squeezes all 13 columns down to just 2. Then it checks how much accuracy a simple classifier loses when it only gets those 2 columns.

## What you'll learn
- **PCA finds the directions where your data spreads the most** and turns them into a few new columns, called components.
- **Always scale first.** Otherwise the column with the biggest numbers wins, just because of its units.
- **Check what you kept with a real test.** Here, 2 components held 55.4% of the variance but still reached 95.5% accuracy, against 98.3% with all 13 columns.

## What's in this folder
- `pca_explained.py`: the full code. It runs top to bottom, and numbered comments mark each step from the story.
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
python pca_explained.py
```


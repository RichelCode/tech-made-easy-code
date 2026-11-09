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

## What you should see
```
178 wines, 13 measurements each, 3 grape types

Without scaling, component 1 'explains' 99.8% of the variance,
and it is almost entirely one column: proline

Variance explained after scaling:
  PC1   36.2%   running total  36.2%
  PC2   19.2%   running total  55.4%
  ...
  PC13   0.8%   running total 100.0%

Accuracy, 5-fold cross-validation:
  All 13 columns (scaled)           98.3%   (folds: 97% to 100%)
  2 PCA components (scaled)         95.5%   (folds: 92% to 97%)
  2 PCA components (NOT scaled)     69.7%   (folds: 61% to 80%)
```
Your numbers should match these (or land very close, if you have newer package versions). The script also saves them to `results.json`, which is what the story's charts are drawn from.

**A note on the accuracy numbers:** they are averages over 5 train/test splits (5-fold cross-validation), so no lucky random seed is involved. The scaler and PCA sit inside a pipeline, so they only ever learn from the training slice of each split.

---

⬅️ [Back to all projects](../README.md)

Part of my **Tech Made Easy** series. Richel makes tech easy 💕

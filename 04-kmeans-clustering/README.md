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

## What you should see
```
k   inertia   silhouette
1     600.0     -
2     280.8   0.56
3      47.4   0.77
4      37.3   0.65
5      28.5   0.54
6      25.5   0.51
7      22.2   0.50
8      19.5   0.35

Best silhouette score: k = 3

What K-Means found:
         customers  avg_spend  avg_visits
cluster
0              100      608.8        10.0
1              100     1972.2         3.0
2              100      447.8         2.0

Scaled:   100% of customers grouped with their real type
Unscaled: 67% of customers grouped with their real type

What K-Means found WITHOUT scaling:
   customers  avg_spend  avg_visits
0        200      528.3         6.0
1         67     2111.1         3.2
2         33     1690.3         2.6
```
Your numbers should match these (or land very close, if you have newer package versions). The script also saves them to `results.json`, which is what the story's charts are drawn from.

**A note on the random seed:** the data uses seed 42. I also tried seeds 0 to 19. Every one picked k = 3, the scaled version matched 99% to 100% of customers to their real type, and the unscaled version matched between 66% and 83%. So the lesson holds, whatever the seed.

---

⬅️ [Back to all projects](../README.md)

Part of my **Tech Made Easy** series. Richel makes tech easy 💕

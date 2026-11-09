# 🌳 XGBoost, Explained Simply

**How small trees that fix each other's mistakes became a go-to tool for table data.**

This is the code for my Medium story *XGBoost, Explained Simply*.

📖 **Read the story:** [link coming soon]

## What this code does
The script uses the breast cancer dataset that ships inside scikit-learn (569 tumours, 30 measurements each, no download needed). It compares one decision tree, a random forest and XGBoost on the same unseen test set, then repeats the comparison on 10 different splits so one lucky split can't fool you. It also watches XGBoost's error fall as trees are added, uses early stopping to decide when to stop, tries a bigger learning rate, and shows which measurements mattered most.

## What you'll learn
- **Boosting adds small trees one at a time**, each one fixing the mistakes of the trees before it. A random forest grows its trees independently and lets them vote.
- **Learning rate and early stopping work as a pair.** Take small steps, watch a validation set, and stop when it stops improving.
- **XGBoost is strong, not magic.** In our test it tied a random forest. Compare it fairly, on more than one split, before you crown a winner.

## What's in this folder
- `boosting.py`: the full code. It runs top to bottom, and numbered comments mark each step from the story.
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
python boosting.py
```

**Mac users:** if `import xgboost` fails with a message about `libomp`, install it with `brew install libomp` and try again.

## What you should see
```
Test accuracy on 114 unseen tumours (split seed 42):
  Single decision tree         94.7%  (6 wrong)
  Random forest (300 trees)    94.7%  (6 wrong)
  XGBoost                      94.7%  (6 wrong)

Average test accuracy over 10 different splits (seeds 0 to 9):
  Single decision tree         93.7%  (range 90.4% to 96.5%)
  Random forest (300 trees)    96.8%  (range 93.9% to 98.2%)
  XGBoost                      96.8%  (range 94.7% to 98.2%)

XGBoost built 257 trees before early stopping kicked in.
Best validation error at tree 207: 0.138
With learning_rate=0.3: best at tree 33, validation error 0.143, test accuracy 93.9%
```
Your numbers should match these (or land very close, if you have newer package versions). The script also saves them to `results.json`, which is what the story's charts are drawn from.

**A note on the scores:** on any single split, the three models can land very close together (on seed 42 they tie). That's why the script repeats everything on 10 splits. Averaged, both tree ensembles beat a single tree, and on this small, clean dataset XGBoost and the random forest tie.

---

⬅️ [Back to all projects](../README.md)

Part of my **Tech Made Easy** series. Richel makes tech easy 💕

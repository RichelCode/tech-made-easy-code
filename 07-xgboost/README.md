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


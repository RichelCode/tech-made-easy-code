# 🌳 XGBoost, Explained Simply

**How small trees that fix each other's mistakes became a go-to tool for table data.**

This is the code for my Medium story *XGBoost, Explained Simply*.

📖 **Read the story:** [link coming soon]

## What this code does
The script uses the breast cancer dataset that ships inside scikit-learn (569 tumours, 30 measurements each, no download needed). It compares one decision tree, a random forest and XGBoost on the same unseen test set, then repeats the comparison on 10 different splits so one lucky split can't fool you. It also watches XGBoost's error fall as trees are added, uses early stopping to decide when to stop, tries a bigger learning rate, and shows which measurements mattered most.


"""XGBoost Explained Simply: the code.

Uses the breast cancer dataset that ships inside scikit-learn (no download).
Compares one decision tree, a random forest and XGBoost on the same test set,
watches the error fall as XGBoost adds trees, and uses early stopping to pick
how many trees to keep.

Run:  python boosting.py
"""
import json

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

SEED = 42

# ---------- 1. Load the data ----------
data = load_breast_cancer()
X, y = data.data, data.target  # 569 tumours, 30 measurements each, 0 = malignant, 1 = benign
print(f"{X.shape[0]} rows, {X.shape[1]} features")

# ---------- 2. Split: train, validation (for early stopping), test (final score) ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, stratify=y_train, random_state=SEED)
print(f"Train: {len(X_tr)}  Validation: {len(X_val)}  Test: {len(X_test)}\n")

# ---------- 3. Three models, same training data ----------
def make_models(seed, learning_rate=0.05):
    return {
        # One decision tree: a single flowchart of yes/no questions.
        "Single decision tree": DecisionTreeClassifier(random_state=seed),
        # Random forest: 300 trees grown independently, then they vote.
        "Random forest (300 trees)": RandomForestClassifier(n_estimators=300, random_state=seed),
        # XGBoost: small trees added one at a time, each fixing the last ones' mistakes.
        "XGBoost": XGBClassifier(
            n_estimators=1000,         # the most trees we allow
            max_depth=3,               # each tree is small
            learning_rate=learning_rate,  # each tree only nudges the answer a little
            early_stopping_rounds=50,  # stop if validation error hasn't improved for 50 trees
            eval_metric="logloss",
            random_state=seed,
        ),
    }


def fit_all(models, X_tr, y_tr, X_val, y_val):
    for name, model in models.items():
        if name == "XGBoost":  # XGBoost watches the validation set while it trains
            model.fit(X_tr, y_tr, eval_set=[(X_tr, y_tr), (X_val, y_val)], verbose=False)
        else:
            model.fit(X_tr, y_tr)
    return models


models = fit_all(make_models(SEED), X_tr, y_tr, X_val, y_val)
xgb = models["XGBoost"]

# ---------- 4. Score them all on the same unseen test set ----------
scores = {name: accuracy_score(y_test, m.predict(X_test)) for name, m in models.items()}
print(f"Test accuracy on {len(y_test)} unseen tumours (split seed {SEED}):")
for name, acc in scores.items():
    wrong = round((1 - acc) * len(y_test))
    print(f"  {name:<28} {acc:.1%}  ({wrong} wrong)")

# One split can be lucky or unlucky, so repeat the whole thing on 10 different splits.
runs = {name: [] for name in scores}
for seed in range(10):
    Xa, Xt, ya, yt = train_test_split(X, y, test_size=0.2, stratify=y, random_state=seed)
    Xr, Xv, yr, yv = train_test_split(Xa, ya, test_size=0.2, stratify=ya, random_state=seed)
    for name, m in fit_all(make_models(seed), Xr, yr, Xv, yv).items():
        runs[name].append(accuracy_score(yt, m.predict(Xt)))
avg = {name: float(np.mean(v)) for name, v in runs.items()}
print("\nAverage test accuracy over 10 different splits (seeds 0 to 9):")
for name, v in runs.items():
    print(f"  {name:<28} {np.mean(v):.1%}  (range {min(v):.1%} to {max(v):.1%})")

# ---------- 5. Watch the error fall as trees are added ----------
log = xgb.evals_result()
train_loss = log["validation_0"]["logloss"]
val_loss = log["validation_1"]["logloss"]
best = xgb.best_iteration
print(f"\nXGBoost built {len(val_loss)} trees before early stopping kicked in.")
print(f"Best validation error at tree {best + 1}: {val_loss[best]:.3f}")
for n in (1, 10, 50, 100, best + 1):
    print(f"  after {n:>3} trees: train {train_loss[n - 1]:.3f}  validation {val_loss[n - 1]:.3f}")

# Same thing with a bigger learning rate: each tree takes a bigger step.
fast = make_models(SEED, learning_rate=0.3)["XGBoost"]
fast.fit(X_tr, y_tr, eval_set=[(X_val, y_val)], verbose=False)
fast_loss = fast.evals_result()["validation_0"]["logloss"]
print(f"With learning_rate=0.3: best at tree {fast.best_iteration + 1}, "
      f"validation error {fast_loss[fast.best_iteration]:.3f}, test accuracy "
      f"{accuracy_score(y_test, fast.predict(X_test)):.1%}")

# ---------- 6. Which measurements mattered most? ----------
importance = xgb.feature_importances_
top = np.argsort(importance)[::-1][:6]
print("\nTop 6 features (share of XGBoost importance):")
for i in top:
    print(f"  {data.feature_names[i]:<22} {importance[i]:.1%}")

# Save numbers for the article's charts
json.dump({
    "n_rows": int(X.shape[0]), "n_features": int(X.shape[1]),
    "n_train": len(X_tr), "n_val": len(X_val), "n_test": len(X_test),
    "accuracy": {k: round(float(v), 3) for k, v in scores.items()},
    "avg_accuracy_10_splits": {k: round(v, 3) for k, v in avg.items()},
    "range_10_splits": {k: [round(min(v), 3), round(max(v), 3)] for k, v in runs.items()},
    "wrong": {k: round((1 - float(v)) * len(y_test)) for k, v in scores.items()},
    "trees_built": len(val_loss),
    "best_trees": int(best + 1),
    "fast_lr_best_trees": int(fast.best_iteration + 1),
    "fast_lr_best_val_logloss": round(fast_loss[fast.best_iteration], 4),
    "fast_lr_test_accuracy": round(float(accuracy_score(y_test, fast.predict(X_test))), 3),
    "train_logloss": [round(v, 4) for v in train_loss],
    "val_logloss": [round(v, 4) for v in val_loss],
    "top_features": [str(data.feature_names[i]) for i in top],
    "top_importance": [round(float(importance[i]) * 100, 1) for i in top],
}, open("results.json", "w"), indent=2)
print("\nSaved results.json")

"""PCA Explained Simply: the code.

Loads the wine dataset that ships with scikit-learn (178 wines, 13 chemical
measurements, 3 grape types). Shows why you must scale before PCA, runs PCA,
reports how much information each component keeps, squeezes 13 columns down
to 2, and checks how much accuracy a simple classifier loses.

Run:  python pca_explained.py
"""
import json

import numpy as np
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# ---------- 1. Load the data ----------
wine = load_wine(as_frame=True)
X, y = wine.data, wine.target
print(f"{X.shape[0]} wines, {X.shape[1]} measurements each, {y.nunique()} grape types\n")

# ---------- 2. Why scaling matters ----------
# The columns live on wildly different scales.
spread = X.std().sort_values()
print("How much each column varies (standard deviation):")
print(f"  smallest: {spread.index[0]:<22} {spread.iloc[0]:8.2f}")
print(f"  largest:  {spread.index[-1]:<22} {spread.iloc[-1]:8.2f}\n")

# PCA on the raw numbers: the biggest column wins, just because its numbers are big.
raw_pca = PCA().fit(X)
raw_pc1 = raw_pca.explained_variance_ratio_[0]
top_feature = X.columns[np.argmax(np.abs(raw_pca.components_[0]))]
print(f"Without scaling, component 1 'explains' {raw_pc1:.1%} of the variance,")
print(f"and it is almost entirely one column: {top_feature}\n")

# ---------- 3. Scale, then run PCA ----------
X_scaled = StandardScaler().fit_transform(X)  # every column: mean 0, spread 1
pca = PCA().fit(X_scaled)
ratios = pca.explained_variance_ratio_
cumulative = np.cumsum(ratios)

print("Variance explained after scaling:")
for i, (r, c) in enumerate(zip(ratios, cumulative), start=1):
    print(f"  PC{i:<2} {r:6.1%}   running total {c:6.1%}")
print()

# ---------- 4. Squeeze 13 columns down to 2 ----------
X_2d = PCA(n_components=2).fit_transform(X_scaled)
print(f"Shape before: {X_scaled.shape}   Shape after: {X_2d.shape}\n")

# ---------- 5. Does a model still work on just 2 columns? ----------
# 5-fold cross-validation: train on 4/5 of the wines, test on the other 1/5,
# five times, then average. The scaler and PCA are inside the pipeline, so they
# only ever learn from the training slice.
cv = StratifiedKFold(n_splits=5)
models = {
    "All 13 columns (scaled)": make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000)),
    "2 PCA components (scaled)": make_pipeline(StandardScaler(), PCA(n_components=2),
                                               LogisticRegression(max_iter=5000)),
    "2 PCA components (NOT scaled)": make_pipeline(PCA(n_components=2), LogisticRegression(max_iter=5000)),
}
accuracy = {}
print("Accuracy, 5-fold cross-validation:")
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=cv)
    accuracy[name] = scores.mean()
    print(f"  {name:<32} {scores.mean():6.1%}   (folds: {scores.min():.0%} to {scores.max():.0%})")

# Save numbers for the article's charts
json.dump({
    "n_rows": int(X.shape[0]),
    "n_features": int(X.shape[1]),
    "smallest_spread": {"feature": spread.index[0], "std": round(float(spread.iloc[0]), 2)},
    "largest_spread": {"feature": spread.index[-1], "std": round(float(spread.iloc[-1]), 2)},
    "unscaled_pc1_pct": round(float(raw_pc1) * 100, 1),
    "unscaled_pc1_top_feature": top_feature,
    "variance_pct": [round(float(r) * 100, 1) for r in ratios],
    "cumulative_pct": [round(float(c) * 100, 1) for c in cumulative],
    "pc_scatter": {
        f"Type {k + 1}": {"pc1": [round(float(v), 3) for v in X_2d[y == k, 0]],
                          "pc2": [round(float(v), 3) for v in X_2d[y == k, 1]]}
        for k in sorted(y.unique())
    },
    "accuracy_pct": {k: round(float(v) * 100, 1) for k, v in accuracy.items()},
}, open("results.json", "w"), indent=2)
print("\nSaved results.json")

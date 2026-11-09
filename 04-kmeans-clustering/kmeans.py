"""K-Means Explained Simply: the code.

Builds 300 pretend shop customers (yearly spend and visits per month),
scales the two columns, and lets K-Means find the groups on its own.
It uses the elbow and the silhouette score to choose k, describes each group,
and then shows what goes wrong if you forget to scale.

Run:  python kmeans.py
"""
import json

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# ---------- 1. Make the data: 300 customers, 3 hidden types ----------
# We know the real types, but K-Means never sees them. We only use them at the end to check.
rng = np.random.default_rng(42)
hidden_types = {
    #  name                 spend mean, spend sd, visits mean, visits sd
    "window shoppers":    (450, 150, 2, 0.8),
    "loyal regulars":     (600, 150, 10, 1.5),
    "big-ticket buyers":  (2000, 250, 3, 1.0),
}
rows = []
for name, (spend_mu, spend_sd, visit_mu, visit_sd) in hidden_types.items():
    for _ in range(100):
        rows.append({
            "annual_spend": max(50, rng.normal(spend_mu, spend_sd)),
            "visits_per_month": max(0.5, rng.normal(visit_mu, visit_sd)),
            "true_type": name,
        })
df = pd.DataFrame(rows).round({"annual_spend": 0, "visits_per_month": 1})
X = df[["annual_spend", "visits_per_month"]]
print(f"{len(df)} customers. First three rows:\n{X.head(3)}\n")

# ---------- 2. Scale: put both columns on the same footing ----------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------- 3. Try k = 1 to 8: the elbow and the silhouette score ----------
ks = range(1, 9)
inertias, silhouettes = [], {}
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X_scaled)
    inertias.append(km.inertia_)
    if k >= 2:  # silhouette needs at least 2 groups
        silhouettes[k] = silhouette_score(X_scaled, km.labels_)

print("k   inertia   silhouette")
for k, inertia in zip(ks, inertias):
    sil = f"{silhouettes[k]:.2f}" if k in silhouettes else "  -"
    print(f"{k}   {inertia:7.1f}   {sil}")
best_k = max(silhouettes, key=silhouettes.get)
print(f"\nBest silhouette score: k = {best_k}\n")

# ---------- 4. Fit the final model and describe each group ----------
kmeans = KMeans(n_clusters=best_k, n_init=10, random_state=0)
df["cluster"] = kmeans.fit_predict(X_scaled)

# Turn the centres back into dollars and visits so we can read them
centres = scaler.inverse_transform(kmeans.cluster_centers_)
summary = df.groupby("cluster").agg(customers=("annual_spend", "size"),
                                    avg_spend=("annual_spend", "mean"),
                                    avg_visits=("visits_per_month", "mean"))
print("What K-Means found:")
print(summary.round(1), "\n")


# ---------- 5. How well did it match the hidden types? ----------
def match_rate(labels):
    """Share of customers whose cluster's most common true type is their own type."""
    majority = df.groupby(labels)["true_type"].agg(lambda s: s.value_counts().index[0])
    return float((df["true_type"] == pd.Series(labels).map(majority)).mean())


scaled_match = match_rate(df["cluster"].to_numpy())
print(f"Scaled:   {scaled_match:.0%} of customers grouped with their real type")

# ---------- 6. The common mistake: forget to scale ----------
raw_labels = KMeans(n_clusters=best_k, n_init=10, random_state=0).fit_predict(X)
raw_match = match_rate(raw_labels)
print(f"Unscaled: {raw_match:.0%} of customers grouped with their real type")
raw_summary = df.groupby(raw_labels).agg(customers=("annual_spend", "size"),
                                         avg_spend=("annual_spend", "mean"),
                                         avg_visits=("visits_per_month", "mean"))
print("\nWhat K-Means found WITHOUT scaling:")
print(raw_summary.round(1))

# Save numbers for the article's charts
order = summary.sort_values("avg_spend").index  # clusters from lowest to highest spend
json.dump({
    "k": list(ks),
    "inertia": [round(float(v), 1) for v in inertias],
    "silhouette": {str(k): round(float(v), 2) for k, v in silhouettes.items()},
    "best_k": int(best_k),
    "clusters": [{
        "spend": df.loc[df.cluster == c, "annual_spend"].tolist(),
        "visits": df.loc[df.cluster == c, "visits_per_month"].tolist(),
        "customers": int(summary.loc[c, "customers"]),
        "avg_spend": round(float(summary.loc[c, "avg_spend"])),
        "avg_visits": round(float(summary.loc[c, "avg_visits"]), 1),
        "centre_spend": round(float(centres[c][0])),
        "centre_visits": round(float(centres[c][1]), 1),
    } for c in order],
    "scaled_match": round(scaled_match, 3),
    "unscaled_match": round(raw_match, 3),
    "unscaled_groups": [{
        "customers": int(r.customers), "avg_spend": round(float(r.avg_spend)),
        "avg_visits": round(float(r.avg_visits), 1)} for r in raw_summary.sort_values("avg_spend").itertuples()],
}, open("results.json", "w"), indent=2)
print("\nSaved results.json")

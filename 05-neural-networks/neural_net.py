"""Neural Networks Explained Simply: the code.

Makes a "two circles" dataset (a ring of points around a smaller blob of points),
then compares one single neuron with a small neural network that has one hidden layer.
Finally it grows the hidden layer (1, 2, 4, 8, 16 neurons) to see how much each size helps.

Run:  python neural_net.py
"""
import json
import warnings

import numpy as np
from sklearn.datasets import make_circles
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# ---------- 1. Make the data: an inner circle (class 1) inside an outer ring (class 0) ----------
X, y = make_circles(n_samples=1000, noise=0.1, factor=0.5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print(f"Training points: {len(X_train)}   Test points: {len(X_test)}\n")

# ---------- 2. One neuron: inputs x weights + bias, then an activation ----------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))         # squashes any number into the range 0 to 1


# A neuron with weights we pick ourselves, so you can follow the math.
x1, x2 = 0.5, 0.2                       # two inputs
w1, w2, b = 2.0, -1.0, 0.1              # two weights and a bias
total = x1 * w1 + x2 * w2 + b           # step 1: weighted sum plus bias
print(f"Hand-made neuron: sum = {total:.2f}, after sigmoid = {sigmoid(total):.2f}")

# Logistic regression is exactly one neuron with a sigmoid activation.
# Here it learns its own weights from the training points.
neuron = LogisticRegression().fit(X_train, y_train)
w1, w2 = neuron.coef_[0]
b = neuron.intercept_[0]
print(f"Trained neuron:   weights = {w1:.2f}, {w2:.2f}   bias = {b:.2f}")
print(f"Its guess for every test point is close to 50/50: "
      f"{neuron.predict_proba(X_test)[:, 1].min():.2f} to {neuron.predict_proba(X_test)[:, 1].max():.2f}\n")

neuron_acc = neuron.score(X_test, y_test)

# ---------- 3. A small network: one hidden layer of 8 neurons ----------
net = MLPClassifier(hidden_layer_sizes=(8,), activation="relu",
                    learning_rate_init=0.01, max_iter=3000, random_state=0).fit(X_train, y_train)
net_acc = net.score(X_test, y_test)

print("Test accuracy (share of unseen points classified correctly):")
print(f"  One neuron                     {neuron_acc:.1%}")
print(f"  Network, 8 hidden neurons      {net_acc:.1%}")

# How learning went: the error shrinks as the network nudges its weights.
loss = net.loss_curve_
print(f"\nNetwork error at step 1: {loss[0]:.2f}   at the end (step {len(loss)}): {loss[-1]:.2f}\n")

# ---------- 4. Grow the hidden layer ----------
sizes = [1, 2, 4, 8, 16]
accs = {}
print("Hidden neurons -> test accuracy (seed 0), and the range over seeds 0 to 4:")
for n in sizes:
    scores = []
    for seed in range(5):
        m = MLPClassifier(hidden_layer_sizes=(n,), activation="relu",
                          learning_rate_init=0.01, max_iter=3000, random_state=seed).fit(X_train, y_train)
        scores.append(m.score(X_test, y_test))
    accs[n] = scores
    print(f"  {n:>2}  {scores[0]:.1%}   (seeds 0 to 4: {min(scores):.1%} to {max(scores):.1%})")

# Save numbers for the article's chart
json.dump({
    "n_train": len(X_train),
    "n_test": len(X_test),
    "neuron_weights": [round(float(w1), 2), round(float(w2), 2)],
    "neuron_bias": round(float(b), 2),
    "neuron_acc": round(neuron_acc * 100, 1),
    "net8_acc": round(net_acc * 100, 1),
    "loss_start": round(loss[0], 2),
    "loss_end": round(loss[-1], 2),
    "loss_steps": len(loss),
    "hidden_sizes": sizes,
    "hidden_acc_seed0": [round(accs[n][0] * 100, 1) for n in sizes],
    "hidden_acc_min": [round(min(accs[n]) * 100, 1) for n in sizes],
    "hidden_acc_max": [round(max(accs[n]) * 100, 1) for n in sizes],
}, open("results.json", "w"), indent=2)
print("\nSaved results.json")

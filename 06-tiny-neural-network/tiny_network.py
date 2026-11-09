"""Build a Tiny Neural Network From Scratch in NumPy: the code.

Builds a 2-layer neural network with nothing but NumPy and teaches it to
separate two interleaving half moons. You'll see the forward pass, the loss,
backpropagation ("blame flows backwards") and gradient descent, all in a
training loop you can read line by line. Then it tries three learning rates.

scikit-learn is only used to make the data and split it.

Run:  python tiny_network.py
"""
import json

import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

# ---------- 1. Make the data: two interleaving half moons ----------
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
y = y.reshape(-1, 1)  # a column of 0s and 1s
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {len(X_train)} points   Test: {len(X_test)} points (held out)\n")


# ---------- 2. The network: 2 inputs -> 8 hidden neurons -> 1 output ----------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))  # squashes any number into 0 to 1


def init_params(n_hidden=8, seed=0):
    rng = np.random.default_rng(seed)
    return {
        "W1": rng.normal(0, 1, size=(2, n_hidden)),  # input -> hidden weights
        "b1": np.zeros((1, n_hidden)),
        "W2": rng.normal(0, 1, size=(n_hidden, 1)),  # hidden -> output weights
        "b2": np.zeros((1, 1)),
    }


def forward(X, p):
    h = np.tanh(X @ p["W1"] + p["b1"])      # hidden layer: weigh, add, squash
    out = sigmoid(h @ p["W2"] + p["b2"])    # output: a probability of class 1
    return h, out


def loss_fn(out, y):
    out = np.clip(out, 1e-9, 1 - 1e-9)      # avoid log(0)
    return float(-np.mean(y * np.log(out) + (1 - y) * np.log(1 - out)))


def backward(X, y, h, out, p):
    n = len(X)
    d_out = (out - y) / n                    # how wrong each prediction was
    dW2 = h.T @ d_out                        # blame for the output weights
    db2 = d_out.sum(axis=0, keepdims=True)
    d_h = (d_out @ p["W2"].T) * (1 - h**2)   # pass the blame back through tanh
    dW1 = X.T @ d_h                          # blame for the hidden weights
    db1 = d_h.sum(axis=0, keepdims=True)
    return {"W1": dW1, "b1": db1, "W2": dW2, "b2": db2}


def accuracy(X, y, p):
    _, out = forward(X, p)
    return float(np.mean((out > 0.5) == y))


# ---------- 3. The training loop ----------
def train(lr, epochs=2000, log_every=50):
    p = init_params()
    log = []
    for epoch in range(epochs + 1):
        h, out = forward(X_train, p)         # 1. guess
        loss = loss_fn(out, y_train)         # 2. measure how wrong
        grads = backward(X_train, y_train, h, out, p)  # 3. share out the blame
        for k in p:                          # 4. nudge every weight downhill
            p[k] -= lr * grads[k]
        if epoch % log_every == 0:
            log.append((epoch, loss))
    return p, log


LR = 1.0
params, log = train(LR)
print(f"Learning rate {LR}: loss over epochs")
for epoch, loss in log:
    if epoch in (0, 100, 250, 500, 1000, 1500, 2000):
        print(f"  epoch {epoch:>4}   loss {loss:.3f}")

train_acc = accuracy(X_train, y_train, params)
test_acc = accuracy(X_test, y_test, params)
print(f"\nTrain accuracy: {train_acc:.1%}")
print(f"Test accuracy:  {test_acc:.1%}   <- points it never saw")

# A guess of 0.5 for everyone scores this loss. Anything lower means learning.
coin_flip = loss_fn(np.full_like(y_train, 0.5, dtype=float), y_train)
print(f"Loss of a coin-flip guess: {coin_flip:.3f}")

# ---------- 4. Learning rate: too low, just right, too high ----------
print("\nSame network, same 2,000 epochs, three learning rates:")
lr_results = {}
for lr in (0.01, 1.0, 50.0):
    p, lg = train(lr)
    lr_results[lr] = {"log": lg, "test_acc": accuracy(X_test, y_test, p)}
    losses = [l for _, l in lg]
    last = losses[-10:]                      # the last 500 epochs
    print(f"  lr {lr:>5}: final loss {losses[-1]:.3f}   test accuracy {lr_results[lr]['test_acc']:.1%}"
          f"   (last 500 epochs: loss {min(last):.2f} to {max(last):.2f})")

# Save numbers for the article's charts
json.dump({
    "lr": LR,
    "epochs": [e for e, _ in log],
    "loss": [round(l, 4) for _, l in log],
    "train_acc": round(train_acc, 3),
    "test_acc": round(test_acc, 3),
    "coin_flip_loss": round(coin_flip, 3),
    "n_train": len(X_train),
    "n_test": len(X_test),
    "lr_compare": {
        str(lr): {
            "epochs": [e for e, _ in r["log"]],
            "loss": [round(l, 4) for _, l in r["log"]],
            "final_loss": round(r["log"][-1][1], 3),
            "test_acc": round(r["test_acc"], 3),
            "last500_min": round(min(l for _, l in r["log"][-10:]), 2),
            "last500_max": round(max(l for _, l in r["log"][-10:]), 2),
        } for lr, r in lr_results.items()
    },
}, open("results.json", "w"), indent=2)
print("\nSaved results.json")

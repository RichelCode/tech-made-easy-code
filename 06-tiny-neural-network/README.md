# 🛠️ Build a Tiny Neural Network From Scratch in NumPy

**Forward pass, loss, backprop and a training loop, one plain line at a time.**

This is the code for my Medium story *Build a Tiny Neural Network From Scratch in NumPy*.

📖 **Read the story:** [link coming soon]

## What this code does
The script builds a 2-layer neural network with nothing but NumPy: 2 inputs, 8 hidden neurons and 1 output. It teaches the network to separate two interleaving half moons (scikit-learn's `make_moons`), using a forward pass, a loss, backpropagation and gradient descent in a training loop you can read line by line. Then it trains the same network with three learning rates to show what "too low" and "too high" really look like.

scikit-learn is only used to make the data and split it. The network itself is pure NumPy.

## What you'll learn
- **A network learns in one loop:** forward pass, measure the loss, pass the blame backwards, nudge the weights, repeat.
- **Backpropagation is just shared blame.** Start at the error and work backwards, so every weight knows its share.
- **Watch your learning rate.** Too low crawls, too high bounces. A loss that zigzags usually means "make the steps smaller".

## What's in this folder
- `tiny_network.py`: the full code. It runs top to bottom, and numbered comments mark each step from the story.
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
python tiny_network.py
```

## What you should see
```
Train: 800 points   Test: 200 points (held out)

Learning rate 1.0: loss over epochs
  epoch    0   loss 0.722
  epoch  100   loss 0.244
  epoch  250   loss 0.145
  epoch  500   loss 0.089
  epoch 1000   loss 0.071
  epoch 1500   loss 0.066
  epoch 2000   loss 0.064

Train accuracy: 97.8%
Test accuracy:  99.0%   <- points it never saw
Loss of a coin-flip guess: 0.693

Same network, same 2,000 epochs, three learning rates:
  lr  0.01: final loss 0.290   test accuracy 86.5%   (last 500 epochs: loss 0.29 to 0.29)
  lr   1.0: final loss 0.064   test accuracy 99.0%   (last 500 epochs: loss 0.06 to 0.07)
  lr  50.0: final loss 2.917   test accuracy 87.0%   (last 500 epochs: loss 1.17 to 2.92)
```
Your numbers should match these (or land very close, if you have newer package versions). The script also saves them to `results.json`, which is what the story's charts are drawn from.

**A note on randomness:** the starting weights come from a random seed (0 here). With seeds 0 to 9, the final loss landed between 0.060 and 0.074 and test accuracy between 98% and 99%. On this data, learning rates from about 0.5 to 10 all train smoothly; at 20 and above the loss starts to bounce.

---

⬅️ [Back to all projects](../README.md)

Part of my **Tech Made Easy** series. Richel makes tech easy 💕

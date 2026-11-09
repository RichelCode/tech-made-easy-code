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


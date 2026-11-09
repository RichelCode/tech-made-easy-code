# 🛠️ Build a Tiny Neural Network From Scratch in NumPy

**Forward pass, loss, backprop and a training loop, one plain line at a time.**

This is the code for my Medium story *Build a Tiny Neural Network From Scratch in NumPy*.

📖 **Read the story:** [link coming soon]

## What this code does
The script builds a 2-layer neural network with nothing but NumPy: 2 inputs, 8 hidden neurons and 1 output. It teaches the network to separate two interleaving half moons (scikit-learn's `make_moons`), using a forward pass, a loss, backpropagation and gradient descent in a training loop you can read line by line. Then it trains the same network with three learning rates to show what "too low" and "too high" really look like.

scikit-learn is only used to make the data and split it. The network itself is pure NumPy.


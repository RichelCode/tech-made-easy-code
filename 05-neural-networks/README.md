# 🧠 Neural Networks, Explained Simply

**From one neuron to deep learning, with real Python and no heavy math.**

This is the code for my Medium story *Neural Networks, Explained Simply*.

📖 **Read the story:** [link coming soon]

## What this code does
The script makes a "bullseye" dataset with scikit-learn's `make_circles`: an inner circle of dots inside an outer ring. It works through one neuron by hand, then shows that a single trained neuron (logistic regression) can only draw a straight line, so it scores no better than a coin flip. A small neural network with one hidden layer of 8 neurons solves it. Finally it grows the hidden layer from 1 to 16 neurons to see how many you really need.

## What you'll learn
- **A neuron is a tiny calculator.** Multiply inputs by weights, add a bias, squash it with an activation.
- **One neuron can only draw a straight line.** On our bullseye data it scored 48.8%, a coin flip. A hidden layer of 8 neurons scored 99.2%.
- **Networks learn by nudging.** Start with random weights, measure the error, nudge every weight to shrink it, repeat. Deep learning is the same idea with more layers.

## What's in this folder
- `neural_net.py`: the full code. It runs top to bottom, and numbered comments mark each step from the story.
- `requirements.txt`: the Python packages the code needs.
- `results.json`: created when you run the script. It holds the numbers it printed.

## What you need
- Python 3.9 or newer
- About two minutes
- New to Python or the terminal? Follow the [Getting Started guide](../GETTING_STARTED.md) first. It walks you through every step.


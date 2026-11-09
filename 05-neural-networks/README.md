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

## How to run it
Open a terminal inside this folder, then run these four lines one at a time:
```bash
python3 -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python neural_net.py
```

## What you should see
```
Training points: 750   Test points: 250

Hand-made neuron: sum = 0.90, after sigmoid = 0.71
Trained neuron:   weights = 0.01, -0.01   bias = 0.00
Its guess for every test point is close to 50/50: 0.50 to 0.50

Test accuracy (share of unseen points classified correctly):
  One neuron                     48.8%
  Network, 8 hidden neurons      99.2%

Network error at step 1: 0.71   at the end (step 452): 0.02

Hidden neurons -> test accuracy (seed 0), and the range over seeds 0 to 4:
   1  48.0%   (seeds 0 to 4: 48.0% to 64.8%)
   2  62.4%   (seeds 0 to 4: 48.0% to 80.4%)
   4  97.2%   (seeds 0 to 4: 71.6% to 98.0%)
   8  99.2%   (seeds 0 to 4: 98.0% to 99.2%)
  16  98.8%   (seeds 0 to 4: 98.4% to 98.8%)
```
Your numbers should match these (or land very close, if you have newer package versions). The script also saves them to `results.json`, which is what the story's chart is drawn from.

**A note on seeds:** a neural network starts from random weights, and `random_state` picks them. The story's main numbers use seed 0. The script also tries seeds 0 to 4 for each hidden layer size and prints the range, so you can see that small networks (4 neurons or fewer) sometimes get stuck, while 8 or more score at least 98.0% with every seed tried.

---

⬅️ [Back to all projects](../README.md)

Part of my **Tech Made Easy** series. Richel makes tech easy 💕

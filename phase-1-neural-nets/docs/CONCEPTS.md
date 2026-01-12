# Phase 1: Neural Network Concepts

**Learn the fundamentals before you code them.**

---

## What is a Neural Network?

A neural network is a **function approximator**. It learns to map inputs to outputs by adjusting internal parameters (weights and biases).

**Simple analogy**: Like a recipe that adjusts ingredient amounts until it tastes right.

---

## The Basic Building Blocks

### 1. **Neuron (Node)**

A neuron does three things:
1. Takes multiple inputs
2. Computes a weighted sum: `sum = (input1 * weight1) + (input2 * weight2) + ... + bias`
3. Applies an activation function: `output = activation(sum)`

**Code representation**:
```python
output = activation(np.dot(weights, inputs) + bias)
```

**Why it matters**: Neurons are the atoms. Everything else is made of these.

---

### 2. **Weights**

Numbers that determine **how much each input matters**.

- Large positive weight → input strongly increases output
- Large negative weight → input strongly decreases output  
- Zero weight → input is ignored

**During training**: Weights get adjusted to make better predictions.

---

### 3. **Bias**

A constant that **shifts** the neuron's output up or down.

**Analogy**: Like a thermostat offset. Even with no input, output can be non-zero.

**Why it matters**: Without bias, the line/plane always goes through the origin. Bias adds flexibility.

---

### 4. **Activation Functions**

Non-linear functions that introduce complexity.

#### **ReLU (Rectified Linear Unit)** — Most common
```
ReLU(x) = max(0, x)
```
- Negative → 0
- Positive → unchanged

**Why**: Fast to compute, doesn't saturate, works well in practice.

#### **Sigmoid** — For probabilities
```
Sigmoid(x) = 1 / (1 + e^(-x))
```
- Outputs between 0 and 1
- Good for binary classification

#### **Tanh** — Zero-centered
```
Tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
```
- Outputs between -1 and 1
- Sometimes better than sigmoid

**Why activation functions matter**: Without them, stacking layers is pointless—it's just linear transformations. Activation adds non-linearity, allowing networks to learn complex patterns.

---

### 5. **Layers**

Stack neurons together:
- **Input layer**: Raw data goes in
- **Hidden layers**: Intermediate transformations
- **Output layer**: Final prediction

**Why layers**: Each layer extracts higher-level features. First layer might detect edges, second layer shapes, third layer objects.

---

## How Neural Networks Learn

### **Forward Propagation**

Data flows forward through layers:
```
Input → Layer 1 → Layer 2 → ... → Output → Prediction
```

### **Loss Function**

Measures "how wrong" the prediction is:
- **MSE (Mean Squared Error)**: For regression  
  `loss = (prediction - actual)^2`
- **Cross-Entropy**: For classification  
  `loss = -actual * log(prediction)`

**Goal**: Minimize this loss.

### **Backpropagation**

The magic algorithm that figures out:
1. How much each weight contributed to the error
2. How to adjust weights to reduce error

**Uses chain rule from calculus** to compute gradients.

**Process**:
1. Compute loss (how wrong we are)
2. Compute gradient (direction to improve)
3. Update weights: `weight = weight - learning_rate * gradient`

### **Gradient Descent**

The optimization algorithm:
```
for each epoch:
    for each batch:
        1. Forward pass (make predictions)
        2. Compute loss
        3. Backward pass (compute gradients)
        4. Update weights
```

---

## Key Hyperparameters

### **Learning Rate**
How big the weight updates are.
- Too large → overshoots, diverges
- Too small → learns slowly, gets stuck

**Typical values**: 0.001 to 0.1

### **Batch Size**
How many examples to process before updating weights.
- Larger batch → stable gradients, slower iterations
- Smaller batch → noisy gradients, faster iterations

**Typical values**: 32, 64, 128

### **Epochs**
How many times to go through entire dataset.

**Typical values**: 10 to 1000 (depends on problem)

---

## Common Problems & Solutions

### **Problem: Not Learning (Loss Stuck)**
- Learning rate too small
- Weights initialized poorly
- Dead ReLU neurons (outputs always 0)

**Solution**: Increase learning rate, reinitialize weights, check activations.

### **Problem: Loss Exploding**
- Learning rate too large
- Gradients exploding

**Solution**: Decrease learning rate, gradient clipping.

### **Problem: Overfitting**
- Model memorizes training data, fails on new data

**Solution**: More data, dropout, regularization, simpler model.

### **Problem: Vanishing Gradients**
- Deep networks: gradients become tiny, early layers don't learn

**Solution**: Better initialization, ReLU activation, batch normalization.

---

## Mental Models

### **Neural Network = Function Approximator**
You have data: `(x, y)` pairs. Neural network learns: `y = f(x)`

### **Training = Search Process**
Start with random weights. Search for weights that minimize loss. Backpropagation guides the search.

### **Layers = Feature Extractors**
Each layer transforms data into more useful representations.

---

## What You'll Build in Phase 1

1. **Single neuron**: Understand the atomic unit
2. **Backpropagation**: Implement gradient computation manually
3. **Multi-layer network**: Stack layers together
4. **Training loop**: Put it all together
5. **Real data (MNIST)**: Train on actual images
6. **Optimizers**: Implement SGD, Momentum, Adam

**By the end**: You'll understand neural networks deeply because you built one from scratch.

---

## Resources (Read AFTER Coding)

- [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — Best visual explanation
- [Michael Nielsen: Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) — Free online book
- [CS231n Lecture Notes](https://cs231n.github.io/) — Stanford course notes

**Remember**: Code first, theory second. Understanding comes from building.

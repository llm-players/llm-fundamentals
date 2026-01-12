# 01_single_neuron.py - Documentation

**Companion doc for:** [../01_single_neuron.py](../01_single_neuron.py)  
**Teaches:** CONCEPTS_FOR_ENGINEERS.md - Part 1 (Neurons as Smooth If-Statements)

---

## What You'll Learn

This code file teaches you how to build a **single neuron from scratch**. You'll understand:
- What a neuron actually is (spoiler: it's just weighted addition + activation)
- How weights and bias control decision-making
- Why ReLU is like a smooth if-statement
- Real-world application: coffee buying decisions

---

## Core Concept

A neuron is a **configurable decision-maker**. Think of it like a function:

```
output = max(0, weights·inputs + bias)
```

- **Inputs**: The data you feed in (money, tiredness, etc.)
- **Weights**: How important each input is (0.3 for money, 0.7 for tiredness)
- **Bias**: Your baseline preference (-2.0 means "generally avoid coffee")
- **Activation (ReLU)**: Converts weighted sum to final output (negative → 0, positive → kept)

---

## Code Walkthrough

### 1. The Neuron Class

```python
class Neuron:
    def __init__(self, n_inputs):
        self.weights = np.random.randn(n_inputs) * 0.01
        self.bias = 0.0
```

**What's happening:**
- `weights`: One weight per input, initialized randomly (small values help learning)
- `bias`: Shifts the decision threshold up/down (starts at 0)

**Engineering analogy:**
```python
# Like a config object for a decision function
config = {
    'feature_importance': [0.01, -0.02, 0.03],  # weights
    'baseline_threshold': 0.0                    # bias
}
```

### 2. The Forward Pass

```python
def forward(self, inputs):
    weighted_sum = np.dot(self.weights, inputs) + self.bias
    output = max(0, weighted_sum)
    return output
```

**What's happening:**
1. `weighted_sum`: Multiply each input by its weight, sum them up, add bias
2. `output`: Apply ReLU activation (kills negatives, keeps positives)

**Engineering analogy:**
```python
# Step 1: Weighted scoring
score = sum(weight * feature for weight, feature in zip(weights, inputs)) + bias

# Step 2: Apply threshold decision
result = score if score > 0 else 0  # ReLU in one line
```

---

## Demo Breakdowns

### Demo 1: Coffee Decision (Real-World)

**The Setup:**
```python
neuron = Neuron(n_inputs=2)
neuron.weights = np.array([0.3, 0.7])  # [money_weight, tiredness_weight]
neuron.bias = -2.0
```

**What this means:**
- **Inputs**: [money, tiredness]
- **Weight 0.3**: Money is somewhat important
- **Weight 0.7**: Tiredness is MORE important
- **Bias -2.0**: You're generally reluctant to buy coffee

**Test Case:**
```python
inputs = [10.0, 9.0]  # Rich and exhausted
output = neuron.forward(inputs)
# weighted_sum = 0.3*10 + 0.7*9 + (-2.0) = 3.0 + 6.3 - 2.0 = 7.3
# output = max(0, 7.3) = 7.3
# Decision: BUY COFFEE! (output > 3.0)
```

**Key insight:** The neuron learned that tiredness matters more than money for this decision.

### Demo 2: Generic Neuron (Abstract)

Tests the neuron with 3 different input vectors to show:
- Positive weighted sums → positive outputs
- Negative weighted sums → zero outputs (ReLU kills them)

**Why this matters:**
- Shows ReLU's "smooth if-statement" behavior
- Demonstrates how negative inputs/weights affect output

### Demo 3: Visualization

Creates a 1D neuron (`output = max(0, 2.0 * input - 1.0)`) and plots:
- X-axis: Input values
- Y-axis: Neuron output
- **The kink at x=0.5**: This is where ReLU activates!

**What you'll see:**
- Before x=0.5: Output = 0 (ReLU kills negative weighted sums)
- After x=0.5: Output = 2x - 1 (linear growth)
- **This is the "smooth if-statement"**

---

## Key Formulas

### Weighted Sum
```
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
z = weights·inputs + bias  (vectorized)
```

### ReLU Activation
```
output = max(0, z)
```

**In code:**
```python
output = z if z > 0 else 0  # Python version
output = max(0, z)           # numpy version
```

---

## How to Run

```bash
# Activate your environment
venv\Scripts\activate

# Run the code
python phase-1-neural-nets/01_single_neuron.py
```

**Expected output:**
1. Coffee decision scenarios (4 cases)
2. Generic neuron predictions (3 cases)
3. Visualization saved to `outputs/01_neuron_behavior.png`

---

## Common Questions

### Q: Why random weights?
**A:** Neurons start with random weights, then **learn** the right values through training (you'll see this in `02_backpropagation.py`). Random initialization prevents all neurons from learning the same thing.

### Q: Why multiply weights by 0.01?
**A:** Small initial weights help training converge faster. Large weights can cause exploding gradients (bad for learning).

### Q: Why ReLU instead of sigmoid/tanh?
**A:** ReLU is:
- Faster to compute (just `max(0, x)`)
- Doesn't suffer from vanishing gradients
- Still non-linear (the kink at 0 is crucial)

### Q: What's the point of bias?
**A:** Bias shifts the activation threshold. Without it:
- Neuron can only activate when weighted sum > 0
- With bias, you control when it activates (e.g., bias=-2 means you need weighted sum > 2 to activate)

### Q: Can one neuron learn complex patterns?
**A:** **No!** One neuron can only learn linear decisions (with a kink). For complex patterns, you need **multiple neurons in layers** (coming in `03_multi_layer_network.py`).

---

## Experiments to Try

1. **Change the coffee weights:**
   ```python
   neuron.weights = np.array([0.9, 0.1])  # Now money matters more
   ```
   Run again. What changes?

2. **Adjust the bias:**
   ```python
   neuron.bias = 0.0  # No baseline reluctance
   ```
   Do you buy coffee more often?

3. **Add a third input (hunger):**
   ```python
   neuron = Neuron(n_inputs=3)
   neuron.weights = np.array([0.2, 0.5, 0.3])  # [money, tiredness, hunger]
   ```

4. **Use sigmoid instead of ReLU:**
   ```python
   output = 1 / (1 + np.exp(-weighted_sum))  # Sigmoid activation
   ```
   How does the behavior change?

---

## Connection to Real LLMs

In GPT-4 or LLaMA:
- **Billions of neurons** like this one
- Organized in **layers** (you'll build this in Step 3)
- Weights learned from **massive datasets** (you'll implement training in Step 4)
- Same core formula: `weights·inputs + bias`

**You just built the atomic unit of modern AI!** 🎉

---

## Next Steps

Continue to [02_backpropagation.py](02_backpropagation.py) to learn:
- How neurons **learn** the right weights
- Gradient descent (the "blame game")
- Training loops

---

## Further Reading

- **CONCEPTS_FOR_ENGINEERS.md Part 1**: High-level explanation of neurons
- **CONCEPTS.md Part 1**: Mathematical perspective on neurons
- [3Blue1Brown - Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk): Visual explanation

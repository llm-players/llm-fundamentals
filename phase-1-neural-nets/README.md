# Phase 1: Neural Networks from Scratch

**Goal**: Understand how neural networks actually learn by building everything yourself.

---

## Setup (First Time Only)

If you haven't set up the environment yet:

```powershell
# 1. Make sure you're in the project root
cd LLM-Fundamentals

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate.bat  # Windows
# source venv/bin/activate  # Mac/Linux

# 4. Install dependencies
python -m pip install -r requirements.txt
```

**Verify setup**:
```powershell
python -c "import numpy; import matplotlib; print('Ready!')"
```

---

## What You'll Build

1. **Linear layers** (matrix multiplication)
2. **Activation functions** (ReLU, Sigmoid, Tanh)
3. **Loss functions** (MSE, Cross-Entropy)
4. **Backpropagation** (the magic of learning)
5. **Optimizers** (SGD, Adam)
6. **Complete neural network** (putting it all together)

**No PyTorch magic. Just NumPy and math.**

---

## Why This Matters

You can't understand transformers or LLMs without understanding:
- How gradients flow backward through layers
- Why learning rates matter
- What happens during training
- Why neural networks sometimes don't learn

**Build the foundation first.**

---

## The Learning Path

### **Step 1: Single Neuron** (Day 1-2)
Build one neuron. Understand weights, bias, activation.

**Files**: `01_single_neuron.py`

**You'll learn**:
- What a neuron does (weighted sum + activation)
- Forward propagation
- How to make predictions

---

### **Step 2: Backpropagation** (Day 3-5)
Implement gradient descent manually.

**Files**: `02_backpropagation.py`

**You'll learn**:
- How gradients are computed
- Chain rule in action
- Why learning happens

**This is the most important step.** Take your time.

---

### **Step 3: Multi-Layer Network** (Day 6-8)
Stack multiple layers together.

**Files**: `03_multilayer_network.py`

**You'll learn**:
- How layers connect
- Why deep networks are powerful
- Vanishing/exploding gradients

---

### **Step 4: Training Loop** (Day 9-10)
Build the complete training pipeline.

**Files**: `04_training_loop.py`

**You'll learn**:
- Batch processing
- Epochs and iterations
- Monitoring loss and accuracy

---

### **Step 5: Real Data** (Day 11-14)
Train on MNIST (handwritten digits).

**Files**: `05_mnist_classifier.py`

**You'll learn**:
- Data loading and preprocessing
- Evaluation metrics
- Debugging training issues

---

### **Step 6: Optimizers** (Day 15-16)
Implement SGD, Momentum, Adam.

**Files**: `06_optimizers.py`

**You'll learn**:
- Why Adam works better than SGD
- Momentum and adaptive learning rates
- When to use which optimizer

---

## Success Criteria

You're ready for Phase 2 when you can:

✅ Explain forward and backward propagation without looking at notes  
✅ Build a neural network from scratch (no libraries)  
✅ Train it on real data and achieve >90% accuracy on MNIST  
✅ Debug training issues (slow learning, overfitting, etc.)  
✅ Explain why neural networks learn

---

## Getting Started

### **Step 0: Learn the Concepts** (Optional but Recommended)

**New to ML?** Start here:
- [docs/CONCEPTS_FOR_ENGINEERS.md](docs/CONCEPTS_FOR_ENGINEERS.md) — **For software engineers with no ML background**
  - Uses programming analogies you already know
  - No jargon, no assumptions
  - Concrete examples and code

**Want more depth?**
- [docs/CONCEPTS.md](docs/CONCEPTS.md) — Traditional ML explanations
  - Neurons, layers, activations
  - Backpropagation details
  - Common problems and solutions

**Or**: Jump straight into coding and refer back when needed!

### **Step 1: Start Coding**
Open [01_single_neuron.py](01_single_neuron.py) and run it:
```powershell
python phase-1-neural-nets/01_single_neuron.py
```

**Remember**: 
- Type the code yourself (no copy-paste)
- Run it frequently
- Break it intentionally
- Document what you learn in `docs/LEARNING_LOG.md`

**Let's build!**

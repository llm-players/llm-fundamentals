# LLM Fundamentals: The Complete Stack

**Learn Large Language Models from the ground up through hands-on coding.**

A collaborative learning project for building LLMs from scratch.

---

## 🚀 Quick Start (For Collaborators)

### 1. Clone the Repository
```bash
git clone https://github.com/LLM-Players/LLM-Fundamentals.git
cd LLM-Fundamentals
```

### 2. Set Up Environment
```powershell
# Create virtual environment (Python 3.11 or 3.12)
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt
```

### 3. Verify Setup
```powershell
python -c "import numpy; import matplotlib; print('Setup successful!')"
```

### 4. Run Your First Code
```powershell
python phase-1-neural-nets/01_single_neuron.py
```

### 5. Start Learning
Read [docs/START_HERE.md](docs/START_HERE.md) for the complete learning path.

---

## 🎯 Philosophy

**Build → Break → Understand → Scale**

No hand-waving. No black boxes. We build everything from scratch, measure it, break it, and understand why it works (or doesn't).

---

## 🗺️ Learning Path

### **Phase 1: Neural Networks Basics** (2-3 weeks)
Build neural networks from scratch. Understand backpropagation, gradients, and optimization.

**You'll build:**
- Linear layers, activation functions
- Forward/backward propagation
- SGD, Adam optimizers
- Simple feedforward networks
- Train on real data (MNIST, text classification)

**Goal**: Understand how neural networks actually learn.

---

### **Phase 2: Transformers Architecture** (3-4 weeks)
Build the transformer architecture piece by piece.

**You'll build:**
- Embeddings and positional encoding
- Self-attention mechanism
- Multi-head attention
- Feed-forward networks
- Layer normalization
- Complete transformer block
- Encoder and decoder

**Goal**: Understand why transformers work and where they fail.

---

### **Phase 3: Language Models** (2-3 weeks)
Build actual language models and watch them learn.

**You'll build:**
- Tokenization (BPE, WordPiece)
- Causal language modeling
- Small GPT-style model
- Train on text corpus
- Generate text

**Goal**: See how models learn language patterns.

---

### **Phase 4: Training at Scale** (3-4 weeks)
Understand what happens when you scale up.

**You'll learn:**
- Distributed training (DDP, FSDP)
- Mixed precision training
- Gradient accumulation
- Checkpointing strategies
- Memory optimization
- Multi-GPU coordination

**Goal**: Understand why training large models is hard.

---

### **Phase 5: Inference Engineering** (2-3 weeks)
Make trained models actually usable in production.

**You'll learn:**
- KV cache management
- Quantization (INT8, INT4)
- Batching strategies
- Latency vs throughput
- Memory profiling
- GPU optimization

**Goal**: Understand production inference challenges.

---

### **Phase 6: Production Systems** (3-4 weeks)
Build real-world LLM serving infrastructure.

**You'll build:**
- Request queuing
- Dynamic batching
- Load balancing
- Monitoring and metrics
- Cost optimization
- Scaling strategies

**Goal**: Build production-ready LLM systems.

---

## 🛠️ Project Structure

```
/phase-1-neural-nets       # Build NNs from scratch
/phase-2-transformers      # Build transformer architecture
/phase-3-language-models   # Build and train LMs
/phase-4-training          # Distributed training
/phase-5-inference         # Inference optimization
/phase-6-production        # Production systems

/docs
  - START_HERE.md          # Begin here (absolute beginner guide)
  - LEARNING_LOG.md        # Document your journey
  - CONCEPTS.md            # Core concepts reference
  
/shared                    # Shared utilities across phases
```

---

## 🚀 Getting Started

1. **Read**: [docs/START_HERE.md](docs/START_HERE.md) — Complete beginner's guide
2. **Setup**: Follow setup instructions for your environment
3. **Start**: Begin Phase 1 — Neural Networks Basics
4. **Document**: Log your learnings in LEARNING_LOG.md

---

## 💻 Hardware Requirements

**Minimum:**
- Any modern CPU
- 8GB RAM
- Phases 1-3 run on CPU

**Recommended:**
- NVIDIA GPU with 8GB+ VRAM
- 16GB+ RAM
- Required for Phases 4-6

---

## 🎓 Who This Is For

- Software engineers wanting to understand LLMs deeply
- ML engineers transitioning to LLM work
- Anyone preparing for AI infrastructure roles (NVIDIA, OpenAI, Anthropic, etc.)
- Engineers who want to build, not just use

**Not for:**
- Those wanting to just call APIs
- Those looking for quick tutorials
- Those unwilling to code and debug

---

## 🤝 Collaboration

This is a collaborative learning project. As you progress:
- **Document**: Add your learnings to `docs/LEARNING_LOG.md`
- **Share**: Push your code and insights to the repo
- **Help**: Debug each other's code, review implementations
- **Discuss**: Use GitHub Issues/Discussions for questions

### Git Workflow
```bash
# Pull latest changes before starting work
git pull origin main

# Create a branch for your work (optional)
git checkout -b phase-1-yourname

# After completing work, commit and push
git add .
git commit -m "Completed Phase 1, Step 2: Backpropagation"
git push origin main
```

**Note**: `venv/` and Python cache files are gitignored. Only code and documentation get committed.

---

## 📚 What You'll Know By The End

- How transformers actually work (not just "attention is all you need")
- Why GPU memory is the bottleneck in inference
- Why distributed training is hard
- How to profile and optimize LLM systems
- What breaks first when you scale
- How to speak credibly in technical interviews

1. **Setup**: Follow Quick Start above to install dependencies
2. **Read**: [docs/START_HERE.md](docs/START_HERE.md) for complete guide
3. **Code**: Start with [phase-1-neural-nets/01_single_neuron.py](phase-1-neural-nets/01_single_neuron.py)
4. **Document**: Log your progress in [docs/LEARNING_LOG.md](docs/LEARNING_LOG.md)
5. **Collaborate**: Share your insights with the team!

---

## 📞 Getting Help

- **Questions**: Open a GitHub Issue
- **Stuck**: Document the problem in LEARNING_LOG.md
- **Bugs**: Submit a PR with the fix
- **Ideas**: Share in GitHub Discussions*

---

## ⚙️ Tech Stack

- **Python** (3.11 or 3.12)
- **PyTorch** (core deep learning)
- **NumPy** (numerical computing)
- **Matplotlib** (visualization)
- **CUDA** (GPU programming, later phases)

---

## 🎯 Next Steps

**Go to**: [docs/START_HERE.md](docs/START_HERE.md) to begin your journey.

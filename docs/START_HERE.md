# Start Here: Your LLM Learning Journey

**For absolute beginners. No ML background needed.**

---

## What Are We Actually Doing?

You're going to **build Large Language Models from scratch**. Not use them. Not fine-tune them. **Build them.**

By the end, you'll understand:
- How neural networks actually learn
- How transformers work (the architecture behind ChatGPT, Claude, etc.)
- How to train models on real data
- How to make them run efficiently in production
- What breaks when you scale

**This isn't a course. It's a building project.**

---

## The Journey (Plain English)

### **Phase 1: Neural Networks** (Start Here)
**What**: Build a neural network from scratch. No PyTorch magic, just math and code.

**Why**: You can't understand transformers without understanding basic neural networks. We build the foundation first.

**What you'll build**: A neural network that learns to classify images. You'll code forward/backward propagation by hand, understand gradients, and see how learning actually happens.

**Analogy**: Building LEGO bricks before building the castle.

---

### **Phase 2: Transformers**
**What**: Build the transformer architecture piece by piece.

**Why**: Transformers are the foundation of all modern LLMs (GPT, BERT, LLaMA, etc.).

**What you'll build**: Self-attention, multi-head attention, positional encoding. Each piece separately, then together.

**Analogy**: Understanding how an engine works by building each part.

---

### **Phase 3: Language Models**
**What**: Build a small GPT-like model and train it to generate text.

**Why**: This is where you see how models learn language patterns.

**What you'll build**: A language model that learns to predict the next word. Train it on text data and watch it learn to write.

**Analogy**: Teaching a parrot to speak by showing it examples.

---

### **Phase 4: Training at Scale**
**What**: Learn how to train bigger models across multiple GPUs.

**Why**: Small models are educational, but real-world models need distributed training.

**What you'll learn**: How to split training across GPUs, manage memory, and not run out of resources.

**Analogy**: Learning to coordinate a team instead of working alone.

---

### **Phase 5: Inference Engineering**
**What**: Make trained models fast and efficient.

**Why**: A slow model is useless in production. Users want instant responses.

**What you'll learn**: Quantization, batching, memory optimization, GPU profiling.

**Analogy**: Making a race car out of a regular car.

---

### **Phase 6: Production Systems**
**What**: Build real serving infrastructure.

**Why**: Running one inference is easy. Serving thousands of users simultaneously is hard.

**What you'll build**: Request queuing, load balancing, monitoring, scaling.

**Analogy**: Running a restaurant (kitchen + waiters + management).

---

## What You Need to Know Right Now

### Prerequisites
✅ **Programming**: Comfortable with Python  
✅ **Math**: High school algebra (we'll teach the rest)  
✅ **Mindset**: Willing to debug, break things, and learn from errors

❌ **Don't need**: ML experience, deep learning knowledge, PhD in math

### Time Commitment
- **Minimum**: 5-10 hours/week
- **Duration**: 3-6 months for full stack
- **Pace**: Your own (no deadlines)

### Hardware
- **Phase 1-3**: Any laptop (CPU is fine)
- **Phase 4-6**: GPU recommended (but we'll show workarounds)

---

## How This Works

### 1. **Read the Phase Guide**
Each phase has a guide explaining what you'll build and why.

### 2. **Code It**
No copy-paste. Type it out. Break it. Fix it.

### 3. **Run It**
See it work (or fail). Debug. Measure. Understand.

### 4. **Document It**
Write what you learned in `LEARNING_LOG.md`. This becomes your reference.

### 5. **Move Forward**
Once you understand one phase, move to the next.

---

## The Learning Philosophy

**Traditional ML courses:**
1. Watch lectures
2. Do assignments
3. Forget everything in 2 weeks

**Our approach:**
1. Build it from scratch
2. Break it intentionally
3. Measure and understand
4. Document insights
5. Remember forever (because you built it)

**Why this works**: You can't forget what you built with your own hands.

---

## Common Questions

**Q: I'm not a math person. Can I still do this?**  
A: Yes. We explain math **after** you see it in code. Math makes sense when you see what it does.

**Q: How is this different from online courses?**  
A: You **build** everything. No black boxes. No "just trust this works."

**Q: What if I get stuck?**  
A: That's the point. Debugging is learning. Document the problem, and we'll work through it.

**Q: Can I skip phases?**  
A: No. Each phase builds on previous ones. Skipping = you'll be lost later.

**Q: Will this help me get a job at NVIDIA/OpenAI/Anthropic?**  
A: If you complete this, you'll understand LLM systems deeply. You'll speak from experience, not buzzwords. That's what matters in interviews.

---

## What Makes This Effective

When you finish, you can say things like:

> "I built a transformer from scratch, trained it on a text corpus, and optimized inference. On my RTX 2000 with 8GB, I hit OOM at 4K context length due to KV cache growth. I solved it with INT8 quantization, reducing memory by 50% with minimal accuracy loss."

**That's not memorized. That's experienced.**

---

## Ready to Start?

**Next step**: [Phase 1 - Neural Networks Basics](../phase-1-neural-nets/README.md)

You'll build your first neural network from scratch and watch it learn.

No frameworks. No magic. Just code and math.

**Let's build.**

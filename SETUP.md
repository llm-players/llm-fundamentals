# Setup Instructions

## Prerequisites
- Python 3.11 or 3.12
- pip (comes with Python)

## Installation

### 1. Create Virtual Environment

```powershell
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows PowerShell:**
```powershell
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## Verify Setup

```powershell
python -c "import numpy; import matplotlib; print('Setup successful!')"
```

## Start Learning

Once setup is complete:

1. Read [docs/START_HERE.md](docs/START_HERE.md)
2. Go to Phase 1: [phase-1-neural-nets/README.md](phase-1-neural-nets/README.md)
3. Run your first code: `python phase-1-neural-nets/01_single_neuron.py`

## GPU Setup (For Later Phases)

Phase 1-2 run on CPU. Phase 3+ benefit from GPU.

If you have NVIDIA GPU, install PyTorch with CUDA:
```powershell
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Troubleshooting

**Import errors**: Reinstall dependencies  
**Slow performance**: Normal for Phase 1-2 (CPU-based)  
**Questions**: Document in LEARNING_LOG.md and discuss with team

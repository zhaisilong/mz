# MZ

## Setup

```bash
cd mz
mamba create python=3.9 -nmz
mamba activate mz
mamba install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
mamba install seaborn pandas scikit-learn ipykernel

pip install -e .
```

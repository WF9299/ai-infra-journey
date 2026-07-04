# Environment Record

## Project

- Project Name: AI Infra Journey
- Final Target: Heterogeneous AI Inference Platform on GPU and RK3588 Edge Device
- Current Stage: Stage 0 - Environment Setup

## Host

- Host OS: Windows + WSL2
- WSL Distribution: Ubuntu 22.04.5 LTS
- WSL Kernel: 6.6.87.2-microsoft-standard-WSL2
- Linux User: tong
- Project Path: /home/tong/projects/ai-infra-journey

## GPU

- GPU: NVIDIA GeForce RTX 5060 Ti
- VRAM: 16GB
- NVIDIA Driver: 595.97
- CUDA Version shown by nvidia-smi: 13.2

## Python Environment

- Python: Python 3.10.12
- Pip: pip 26.1.2 from /home/tong/projects/ai-infra-journey/.venv/lib/python3.10/site-packages/pip (python 3.10)
- Virtual Environment: .venv

## PyTorch

- Torch: 2.12.1+cu132
- TorchVision: 0.27.1+cu132
- CUDA Available: True
- Torch CUDA Version: 13.2
- GPU Name in PyTorch: NVIDIA GeForce RTX 5060 Ti

## Network Notes

- WSL proxy: http://127.0.0.1:6789
- PyTorch wheel source: Aliyun PyTorch wheels mirror
- Ubuntu apt source: mirror source adjusted for faster download

## Verification

CUDA tensor test passed.

## Created At

Sat Jul  4 17:02:02 CST 2026

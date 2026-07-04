# Stage 0 Summary: Environment Setup

## Project

AI Infra Journey

Final target:

Heterogeneous AI Inference Platform on GPU and RK3588 Edge Device

## Stage 0 Goal

Set up the basic development environment and engineering foundation for the AI Infra project.

## Completed Items

- Created WSL2 Ubuntu development environment
- Verified NVIDIA GPU access inside WSL2
- Created Python virtual environment
- Installed PyTorch CUDA version
- Verified CUDA tensor computation
- Created project directory structure
- Created root README.md
- Created docs/env.md
- Created Stage 0 CUDA check script
- Saved Stage 0 Python dependency snapshot
- Initialized Git repository
- Completed Stage 0 environment verification commit

## Verified Environment

- Host: Windows + WSL2
- WSL: Ubuntu 22.04.5 LTS
- GPU: NVIDIA GeForce RTX 5060 Ti 16GB
- NVIDIA Driver: 595.97
- CUDA shown by nvidia-smi: 13.2
- Python: 3.10
- PyTorch: 2.12.1+cu132
- TorchVision: 0.27.1+cu132
- CUDA available in PyTorch: True

## Important Files

- README.md
- docs/env.md
- stage0_env_setup/scripts/check_torch_cuda.py
- stage0_env_setup/requirements_stage0.txt
- stage0_env_setup/cuda_check_result.txt

## Next Stage

Stage 1: PyTorch Training Performance Lab

Initial Stage 1 tasks:

1. Create stage1_training_lab project skeleton
2. Implement baseline training script
3. Use ResNet18 and FakeData/CIFAR10-style data
4. Record metrics.csv
5. Track step_time, data_time, compute_time, samples/sec, GPU memory
6. Prepare for DataLoader sweep, AMP, batch size sweep, and torch.compile experiments

# Stage 0 Handoff: Environment Setup Completed

## Project Name

AI Infra Journey

## Final Project Target

Heterogeneous AI Inference Platform on GPU and RK3588 Edge Device

The final project will integrate:

- GPU-based LLM inference service
- RK3588 edge AI inference service
- Heterogeneous task scheduler
- Benchmark and profiling system
- Health check, retry, fallback, and observability modules

## Completed Stage

Stage 0: Environment Setup

## Stage 0 Completed Items

- Installed and verified WSL2 Ubuntu environment
- Verified NVIDIA GPU access inside WSL2
- Created Python virtual environment
- Installed PyTorch CUDA version
- Verified CUDA tensor computation
- Created project directory structure
- Created root README.md
- Created docs/env.md
- Created Stage 0 CUDA verification script
- Saved Stage 0 dependency snapshot
- Initialized Git repository
- Configured Git user information
- Configured GitHub SSH key
- Pushed repository to GitHub main branch

## Verified Environment

- Host OS: Windows + WSL2
- WSL Distribution: Ubuntu 22.04.5 LTS
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
- docs/stage0_handoff.md
- stage0_env_setup/scripts/check_torch_cuda.py
- stage0_env_setup/requirements_stage0.txt
- stage0_env_setup/cuda_check_result.txt

## GitHub Repository

https://github.com/WF9299/ai-infra-journey

## Next Stage

Stage 1: PyTorch Training Performance Lab

## Stage 1 Initial Goal

Build a single-GPU PyTorch training benchmark and profiling lab.

The first task in Stage 1 should be:

1. Create the `stage1_training_lab` project skeleton
2. Implement a baseline training script
3. Use ResNet18 + FakeData or CIFAR10-style data
4. Save training metrics to `metrics.csv`
5. Record:
   - step_time
   - data_time
   - compute_time
   - samples/sec
   - GPU memory
6. Prepare for later experiments:
   - DataLoader sweep
   - Batch size sweep
   - AMP
   - torch.compile
   - profiling trace

## Notes for Next Conversation

The next GPT conversation should start from Stage 1.

Do not restart environment setup unless there is an error. The environment has already passed the PyTorch CUDA verification test.

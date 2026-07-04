# AI Infra Journey

This repository documents my AI Infrastructure learning and project-building journey.

The final goal is to build a heterogeneous AI inference infrastructure system that integrates GPU-based LLM inference, RK3588 edge AI inference, heterogeneous task scheduling, benchmark/profiling, health check, fallback, and observability.

## Final Project Target

Heterogeneous AI Inference Platform on GPU and RK3588 Edge Device

The final system will include:

- GPU-based LLM inference service
- RK3588 edge AI inference service
- Heterogeneous task scheduler
- Benchmark and profiling system
- Health check, retry, fallback, and observability modules

## Project Roadmap

Repository structure:

    ai-infra-journey/
    ├── docs/
    ├── stage0_env_setup/
    ├── stage1_training_lab/
    ├── stage2_llm_serving/
    ├── stage3_rk3588_edge_ai/
    └── stage4_heterogeneous_scheduler/

## Stages

### Stage 0: Environment Setup

Set up the basic AI Infra development environment:

- Windows + WSL2 Ubuntu
- NVIDIA GPU access inside WSL2
- Python virtual environment
- PyTorch CUDA verification
- Git repository initialization
- Environment documentation

Current verified environment:

- GPU: NVIDIA GeForce RTX 5060 Ti 16GB
- WSL: Ubuntu 22.04.5 LTS
- Python: 3.10
- PyTorch: 2.12.1+cu132
- CUDA in PyTorch: 13.2

### Stage 1: PyTorch Training Performance Lab

Build a single-GPU training benchmark and profiling lab.

Main goals:

- Implement a reproducible PyTorch training pipeline
- Measure step time, data loading time, compute time, samples/sec, GPU memory, and GPU utilization
- Compare baseline, DataLoader tuning, batch size sweep, AMP, and torch.compile
- Generate benchmark reports and profiling traces

This stage builds the performance analysis foundation for the whole project.

### Stage 2: Local LLM Serving Lab

Build a local LLM inference service on RTX 5060 Ti.

Main goals:

- Implement a FastAPI-based LLM serving system
- Support non-streaming and streaming responses
- Measure TTFT, TPOT, P50/P95/P99 latency, tokens/s, error rate, and GPU memory
- Compare HuggingFace baseline, quantized inference, batching, and optional vLLM backend

This stage becomes the GPU LLM Worker in the final system.

### Stage 3: RK3588 Edge AI Inference

Deploy vision models on RK3588 edge device.

Main goals:

- Convert vision models from ONNX to RKNN
- Apply INT8 quantization
- Deploy models on RK3588 NPU
- Build an edge inference API service
- Measure FPS, latency, memory usage, CPU/NPU load, and long-running stability

This stage becomes the RK3588 Edge Worker in the final system.

### Stage 4: Heterogeneous AI Scheduler

Integrate the GPU LLM Worker and RK3588 Edge Worker into a unified heterogeneous AI inference system.

Main goals:

- Build a unified API gateway
- Implement task routing based on task type, device health, queue length, latency target, and worker status
- Add health check, timeout retry, fallback, and fault injection
- Build benchmark tools for mixed workloads
- Compare fixed routing, load-aware routing, and fallback strategies

This stage is the core system design part of the final project.

## Final System Architecture

System flow:

    User Request
         |
    API Gateway
         |
    Scheduler
      /      \
     /        \
GPU LLM Worker    RK3588 Edge Worker
RTX 5060 Ti       RK3588 8GB
LLM Serving       YOLO / MobileNet / RKNN
HF / vLLM         NPU / ARM / INT8
     \        /
      \      /
Benchmark / Profiling System

## Current Status

- [x] WSL2 Ubuntu environment created
- [x] NVIDIA GPU visible inside WSL2
- [x] Python virtual environment created
- [x] PyTorch CUDA installed
- [x] CUDA tensor test passed
- [ ] Environment documentation completed
- [ ] Git repository initialized
- [ ] Stage 1 project skeleton created

## Repository Principles

This repository focuses on engineering reproducibility and measurable system performance.

Each stage should include:

- Clear README
- Reproducible setup commands
- Benchmark scripts
- Metrics logs
- Experiment reports
- Failure cases and troubleshooting notes
- Resume-ready technical summaries

## Notes

This project is not a collection of isolated AI demos.

The final goal is to build and document a complete AI infrastructure project that can demonstrate:

- Model serving
- GPU inference
- Edge AI deployment
- Heterogeneous scheduling
- Performance profiling
- System reliability
- Engineering reproducibility

# Remote Access Plan

## Goal

Use the Windows desktop as a remote GPU development server and access its WSL2 Ubuntu environment from a laptop.

## Final Architecture

Laptop
-> Tailscale
-> Windows desktop Tailscale IP:2222
-> Windows portproxy
-> WSL2 Ubuntu NAT IP:22
-> OpenSSH server in WSL
-> AI Infra project environment

## Current Stable Design

The stable design uses WSL2 NAT mode instead of mirrored networking.

- WSL distro: Ubuntu-22.04
- WSL network mode: NAT
- WSL SSH port: 22
- Windows exposed port: 2222
- Windows portproxy: 0.0.0.0:2222 -> current WSL NAT IP:22
- Laptop SSH alias: ai-infra-wsl
- Project path: /home/tong/projects/ai-infra-journey
- Python environment: /home/tong/projects/ai-infra-journey/.venv
- GPU: NVIDIA GeForce RTX 5060 Ti

## Laptop SSH Config

On the laptop:

    Host ai-infra-wsl
        HostName 100.100.173.91
        User tong
        Port 2222
        ServerAliveInterval 30
        ServerAliveCountMax 6
        TCPKeepAlive yes

Connect with:

    ssh ai-infra-wsl

## Windows Startup Automation

A Windows Scheduled Task named:

    AI Infra Start WSL SSH

runs after Windows user login.

It performs the following actions:

1. Starts WSL Ubuntu-22.04.
2. Creates /run/sshd inside WSL.
3. Starts sshd in foreground mode to keep WSL alive.
4. Gets the current WSL NAT IP.
5. Rebuilds portproxy from Windows port 2222 to WSL port 22.
6. Ensures the Windows firewall allows inbound TCP 2222.

This is required because WSL may be stopped after Windows restart, and WSL NAT IP may change.

## Verification Commands

On the Windows desktop:

    wsl -l -v
    netsh interface portproxy show all
    ssh -p 2222 tong@localhost
    ssh -p 2222 tong@100.100.173.91

On the laptop:

    ssh ai-infra-wsl

Inside WSL:

    cd ~/projects/ai-infra-journey
    source .venv/bin/activate
    python stage0_env_setup/scripts/check_torch_cuda.py

Expected result:

    cuda available: True
    device name: NVIDIA GeForce RTX 5060 Ti
    cuda tensor test: success

## Operational Notes

- The Windows desktop must not enter sleep or hibernation.
- The display may turn off.
- Win + L lock screen is allowed after Windows login.
- Do not run wsl --shutdown when remote access is needed.
- Use tmux for long-running training, benchmark, profiling, and serving tasks.
- VS Code Remote SSH can be used as the main development interface from the laptop.

## AI Infra Meaning

This setup turns the Windows desktop plus WSL2 environment into a single-node remote GPU worker.

The key infrastructure components are:

- Tailscale for private network access.
- Windows portproxy for ingress forwarding.
- WSL sshd for remote shell access.
- tmux for long-running task survival.
- Python .venv for reproducible project dependencies.
- RTX 5060 Ti for GPU training and inference workloads.

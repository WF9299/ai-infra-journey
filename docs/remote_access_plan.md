# Remote Access Plan

## Goal

Use the desktop machine as a remote GPU development server and access its WSL2 Ubuntu environment from a laptop.

## Architecture

Laptop
-> Tailscale private network
-> Windows desktop Tailscale IP:2222
-> Windows portproxy
-> WSL2 Ubuntu SSH:22
-> AI Infra project environment

## Desktop

- Windows + WSL2 Ubuntu
- GPU: NVIDIA GeForce RTX 5060 Ti
- WSL user: tong
- Project path: /home/tong/projects/ai-infra-journey
- SSH in WSL listens on port 22
- Windows forwards port 2222 to WSL SSH
- Tailscale is used to bypass LAN isolation

## Laptop

Connect through Tailscale:

    ssh -p 2222 tong@<desktop-tailscale-ip>

Recommended SSH config on laptop:

    Host ai-infra-wsl
        HostName <desktop-tailscale-ip>
        User tong
        Port 2222

Then connect with:

    ssh ai-infra-wsl

## Verification

After SSH login:

    cd ~/projects/ai-infra-journey
    source .venv/bin/activate
    python stage0_env_setup/scripts/check_torch_cuda.py

Expected result:

    cuda available: True
    device name: NVIDIA GeForce RTX 5060 Ti
    cuda tensor test: success

## Recommended Workflow

- Use GitHub for code synchronization.
- Use VS Code Remote SSH for development from the laptop.
- Use tmux for long-running training, benchmark, and serving experiments.
- Do not expose SSH directly to the public Internet.

import torch
import torchvision

print("torch version:", torch.__version__)
print("torchvision version:", torchvision.__version__)
print("cuda available:", torch.cuda.is_available())
print("torch cuda version:", torch.version.cuda)
print("device count:", torch.cuda.device_count())

if torch.cuda.is_available():
    print("device name:", torch.cuda.get_device_name(0))
    x = torch.randn(4096, 4096, device="cuda")
    y = x @ x
    torch.cuda.synchronize()
    print("cuda tensor test: success")
else:
    print("cuda tensor test: failed")

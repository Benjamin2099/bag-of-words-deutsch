import torch

def get_device():
    """
    Gibt das verfügbare Gerät zurück: CUDA falls verfügbar, sonst CPU.
    """
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

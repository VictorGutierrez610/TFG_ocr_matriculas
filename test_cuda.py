import torch
print(torch.cuda.is_available())  # Devuelve True si CUDA está disponible
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))  # Nombre de la GPU
else:
    print("CUDA no está disponible.")
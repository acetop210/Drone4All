import random
import torch

a = torch.randn(4, 4)
print(a)
b = a.view(16)
print(b)
c = b.view(4, -1)
print(c)
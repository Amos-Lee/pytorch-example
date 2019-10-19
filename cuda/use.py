import torch

a = torch.tensor([[1., 2.],
                  [3., 4.]]).cuda()
b = torch.tensor([[1., 2.],
                  [3., 4.]]).cuda()
c = a + b

print(c)

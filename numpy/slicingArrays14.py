import numpy as np

a = np.array([10, 20, 30, 40])
b = a[1:3] # slicing create view not copy

b[0] = 999
print(a)

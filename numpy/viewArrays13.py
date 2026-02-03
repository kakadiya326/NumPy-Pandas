import numpy as np

a = np.array([1, 2, 3, 4])
b = a

b[0] = 100
print(a)

c = a.copy()
c[0] = 999
print(a)

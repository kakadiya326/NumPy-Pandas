import numpy as np

a = np.arange(1, 7)

b = np.split(a, 3)
print(b)

# Vertical / Horizontal Split
dm = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = np.vsplit(dm, 3)
d = np.hsplit(dm, 3)

print(c)
print(d)
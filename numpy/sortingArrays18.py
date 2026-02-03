import numpy as np

a = np.array([5, 2, 9, 1, 7])

b = np.sort(a)
print(b)

a = np.array([[3, 2, 1],
              [6, 5, 4]])

c = np.sort(a, axis=0)   # column-wise
d = np.sort(a, axis=1)   # row-wise

print(c)
print(d)
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.sum())
print(a.mean())
print(a.max())
print(a.min())
print(a.sum(axis=0))  # column-wise → [5 7 9]
print(a.sum(axis=1))  # row-wise → [6 15]
print(np.median(a))
print(np.std(a))
print(np.var(a))
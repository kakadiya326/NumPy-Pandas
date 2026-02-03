import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[1:4])      # [20 30 40]
print(a[:3])       # [10 20 30]
print(a[::2])      # [10 30 50]

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(a[:2, :2])
# [[1 2]
#  [4 5]]

print(a[:, 1])
# [2 5 8]

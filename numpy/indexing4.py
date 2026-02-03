import numpy as np

a = np.array([10, 20, 30, 40])

print(a[0])     # 10
print(a[-1])    # 40

a = np.array([[10, 20, 30],
              [40, 50, 60]])

print(a[0, 1])   # 20
print(a[1, 2])   # 60

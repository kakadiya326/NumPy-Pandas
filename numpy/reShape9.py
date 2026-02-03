import numpy as np

a = np.arange(1, 13)  # [1 2 3 4 5 6 7 8 9 10 11 12]

b=a.reshape(3, 4)
print(b)

# Auto Dimension
c=a.reshape(2, -1)  # NumPy automatically calculates missing size.


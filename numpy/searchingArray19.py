import numpy as np

a = np.array([10, 20, 30, 40])

b = np.where(a > 20)
print(b) # return index

c = np.argmax(a)
d = np.argmin(a)
print(c)
print(d)
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

#Vertcal Stacking
c = np.vstack((a, b))
print(c)

#Horizonal Stacking
d = np.hstack((a,b))
print(d)

# Column Stack
e = np.column_stack((a,b))
print(e)
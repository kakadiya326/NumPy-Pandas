import numpy as np

a = np.array([10, 25, 30, 15, 40])
mask = a>20
print(mask)
print(a[mask])

val=np.array([True,False,False,False,False])
print(a[val])

# Direct condition
print(a[a % 2 == 0])

# where()

res = np.where(a > 20, "High", "Low")
print(res)
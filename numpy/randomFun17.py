import numpy as np

a = np.random.rand(3, 3)     # values 0–1
b = np.random.randn(3, 3)   # normal distribution

c = np.random.randint(1, 10, size=5)

print(a)
print(b)
print(c)

# Random Seed
d = np.random.seed(42)
e = np.random.rand(3)

print(d)
print(e)
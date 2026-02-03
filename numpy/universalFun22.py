import numpy as np 

a = np.array([[10,20,30],[40,50,60]])

# Functions that operate element-wise at C speed.
print(np.add(a,10))
print(np.divide(a,2))
print(np.subtract(a,10))
print(np.multiply(a,10))

# Comparison ufuncs ---> return booleans in numpy array
print(np.greater(a,40))
print(np.greater_equal(a,40))
print(np.less(a,40))
print(np.less_equal(a,40))
print(np.equal(a,40))
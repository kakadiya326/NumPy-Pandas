import numpy as np

a = np.array([11,22,33,44,55,66])

# Index list
print(a[[1,3,5]])


# Index array
idx = np.array([1,2,5])
print(a[idx])


#2D indexing
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])

# [0,2] is row
# [1,2] is column
print(arr[[0,2],[1,2]])
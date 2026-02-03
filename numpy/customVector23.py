import numpy as np

def grade(x):
    if x >= 80:
        return "A"
    elif x >= 60:
        return "B"
    else:
        return "C"

vgrade = np.vectorize(grade)

marks = np.array([45, 67, 82, 91])


print(vgrade(marks),end="")
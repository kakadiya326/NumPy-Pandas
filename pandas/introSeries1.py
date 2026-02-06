import pandas as pd
a=pd.Series([1,2,3,4,5])
print(a)


# Custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

# Series from Dictionary
data = {'Math': 80, 'Science': 90, 'English': 85}
d = pd.Series(data)
print(d)

# Access Series Values
print(d['Math'])
# print(d[0])

# Series Properties
print(d.index)
print(d.values)
print(d.dtype)
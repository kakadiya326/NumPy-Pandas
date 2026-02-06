import pandas as pd
data = [
    {'Id': 1, 'Name': 'Ram', 'Age': 21},
    {'Id': 2, 'Name': 'Shyam', 'Age': 23}
]

df = pd.DataFrame(data)
      
print(df.shape) # (rows, columns)
print(df.columns) # column names
print(df.index) # row index
print(df.dtypes) # data types
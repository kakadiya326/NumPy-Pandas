import pandas as pd

data = {
    'Id': [1, 2, 3],
    'Name': ['Ram', 'Shyam', 'Mohan'],
    'Age': [21, 23, 22]
}

df = pd.DataFrame(data)

# Sort by Column
print(df.sort_values('Name',ascending=False))

# Sort by Index
print(df.sort_index())

# Reset & Set Index
print(df.set_index('Name',inplace=True))
print(df.reset_index(inplace=True))

# Select Single Value (Fastest)
print(df.at[0,'Name'])
print(df.iat[0,1])
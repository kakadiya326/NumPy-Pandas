# Indexing vie .loc() and iloc()
import pandas as pd


data = {
    'Id': [1, 2, 3],
    'Name': ['Ram', 'Shyam', 'Mohan'],
    'Age': [21, 23, 22]
}

df = pd.DataFrame(data)

print(df.loc[0])
print(df.loc[0,'Name'])
print(df.loc[0:1])

print('--------------------------')

print(df.iloc[0])
print(df.iloc[0,1])
print(df.iloc[0,:2])


# Selecting Rows + Columns Together
print(df.loc[0:2, ['Name', 'Age']])
print(df.iloc[0:3, 1:3])

# Boolean Filtering :

# Single Condition
print(df[df['Age']>22])

# Multiple Condition
print('Multi condi.',df[(df['Age'] > 22) & (df['Name'] == 'Shyam')])

# query() (Clean & Readable)
print(df.query("Age > 22 and Name == 'Shyam'"))

# isin() (SQL IN)
print(df[df['Name'].isin(['Ram', 'Mohan'])])


# String Filtering
print(df[df['Name'].str.startswith('R')])
print(df[df['Name'].str.contains('ha')])
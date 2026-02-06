import pandas as pd

# From Dictionary (Most common)
data = {
    'Id': [1, 2, 3],
    'Name': ['Ram', 'Shyam', 'Mohan'],
    'Age': [21, 23, 22]
}

df = pd.DataFrame(data)
print(df)


# From List of Lists
data = [
    [1, 'Ram', 21],
    [2, 'Shyam', 23],
    [3, 'Mohan', 22]
]

df = pd.DataFrame(data, columns=['Id', 'Name', 'Age'])

# List of dictionary
data = [
    {'Id': 1, 'Name': 'Ram', 'Age': 21},
    {'Id': 2, 'Name': 'Shyam', 'Age': 23}
]

df = pd.DataFrame(data)
import pandas as pd

df=pd.read_excel('students.xlsx')
print(df)

# Writing Excel File :

df.to_excel('output.xlsx', index=False)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())


# Rename Columns (Very Common) :

df.columns = ['Id', 'FullName', 'Age', 'Marks']
# ( or )
df.rename(columns={'FullName': 'Name'}, inplace=True)

# Change Data Types :
df['Age'] = df['Age'].astype(int)
df['Marks'] = df['Marks'].astype(float)


# Drop Rows / Columns :
df.dropna()              # drop rows with missing values
df.dropna(axis=1)        # drop columns

# Fill Missing Values
df.fillna(0)
df['Marks'].fillna(df['Marks'].mean(), inplace=True)

# Duplicate Handling
df.duplicated()
df.drop_duplicates()
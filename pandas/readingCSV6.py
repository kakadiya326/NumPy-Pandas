import pandas as pd

df=pd.read_csv('student.csv',usecols=['Age'])
print(df)

# Important read_csv() Parameters :

# pd.read_csv(
#     'students.csv',
#     sep=',',        # delimiter
#     header=0,       # header row
#     index_col=None, # index column
#     usecols=['Name', 'Marks'],
#     nrows=5
# )


# Handling Missing Values While Reading :

df = pd.read_csv('students.csv', na_values=['NA', 'null', '--','--'])
print(df)


# Writing CSV File :
df.to_csv('output.csv',index=False)
import pandas as pd

try:
    df=pd.read_csv("D:\\vector\\DataSet\\marksheet.csv")
    # print('--> Show first 5 rows :\n')
    # print(df.head())

    # print('--> Find missing value :\n')
    # print(df.isnull().any())

    # print('--> drop row if missing value :\n')
    # print(df.dropna())

    # print('--> drop column if missing value :\n')
    # print(df.dropna(axis=1))

    # print('--> fill missing value :\n')
    # print(df.fillna(0))

    # print('--> fill column wise value :\n')
    # print(df.fillna({'Science':df['Science'].mean()},inplace=True))
    # print(df.fillna({'Age':df['Age'].median()},inplace=True))

    # print('--> Fill forward / backward :\n')
    # print(df.ffill())
    # print(df.bfill())

    # Replace Values (Not Missing)
    # print(df.replace({'Male':'M','Female':'F'}))

    # Change Data Types (VERY COMMON)
    # df['Science']=df['Science'].astype(float)
    # print(df.head())

    # Rename Columns (Clean Names)
    # print(df.columns.str.lower())
    # print(df.columns.str.upper())
    # print(df.columns.str.replace(' ','_'))

    # Remove Duplicates
    # print(df.duplicated())
    # print(df.drop_duplicates())
    # print(df.drop_duplicates(subset=['id']))

    df['Name'] = df['Name'].str.strip()
    df['Name'] = df['Name'].str.lower()
    df['Name'] = df['Name'].str.title()
    print(df['Name'])
    


except Exception as e:
    print('Error ',e)

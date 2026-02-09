import pandas as pd

# Average marks per city
# Highest marks per gender
# Number of students in each city
# City-wise min, max, avg marks
# Add a column showing city average marks

try:
    df=pd.read_csv("student.csv")
    # print(df.groupby('City')['Marks'].mean().reset_index())
    # print(df.groupby('City')['Marks'].nlargest(1).reset_index())
    # print(df.groupby('City')['Id'].size())
    # print(df.groupby('City')['Marks'].agg(['min','max','mean']))
    # df['city_avg']=df.groupby('City')['Marks'].transform('mean')
    # print(df)

    print(df.groupby('City')['Id'].size().reset_index(name='student_count'))
    print(df)
except Exception as e:
    print(e)
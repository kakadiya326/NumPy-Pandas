# Students with marks ≥ 80
# Students from Delhi OR Mumbai
# Names starting with “R”
# Top 3 students by marks
# Students aged between 20 and 22
import pandas as pd

try:
    df=pd.read_csv('students_messy.csv',na_values=['NaN','Na',' ','','  ','-','_'])
    df.columns=df.columns.str.lower()
    print(df[df['marks']>=80])
    print(df[df['city'].isin(['Delhi','Mumbai'])])
    print(df[df['name'].str.startswith('R')])
    print(df.sort_values('marks',ascending=False).head(3))
    df['age']=pd.to_numeric(df['age'],errors='coerce')
    print(df[df['age'].between(20,22)])
except Exception as e:
    print("Error : ",e)
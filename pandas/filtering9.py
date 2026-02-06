import pandas as pd

data = {
    'name': ['Ram', 'Shyam', 'Mohan', 'Sita', 'Geeta'],
    'age': [21, 23, 22, 20, 24],
    'marks': [78, 85, 67, 92, 55],
    'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)

# print(df[df['marks']>70])
# print(df[df['city']=='Delhi'])
# print(df[(df['marks']>70)&(df['city']=='Delhi')])
# print(df.query("marks>70 and city=='Delhi'"))
# print(df.loc[df['marks']>70,['name','city']])
# print(df[df['city'].isin(['Pune','Mumbai'])])
# print(df[df['marks'].between(70,100)])
# print(df[df['name'].str.startswith('S')])
# print(df[df['name'].str.contains('t')])
# print(df[df['name'].str.contains('s',case=False)])
# print(df.sort_values('marks'))
# print(df.sort_values('marks', ascending=False))
# print(df.sort_values(['city','marks'],ascending=[False,True]))
# print(df.sort_index())
# print(df.nlargest(3, 'marks'))
# print(df.nsmallest(2, 'age'))

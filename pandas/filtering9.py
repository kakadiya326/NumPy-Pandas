import pandas as pd

data = {
    'name': ['Ram', 'Shyam', 'Mohan', 'Sita', 'Geeta'],
    'age': [21, 23, 22, 20, 24],
    'marks': [78, 85, 67, 92, 55],
    'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)
 # BASIC FILTERING (MOST COMMON)

 # Students with marks > 70 :
print(df[df['marks']>70])

# Students from Delhi :
print(df[df['city']=='Delhi'])

# MULTIPLE CONDITIONS (IMPORTANT ⚠️) :

# AND condition:
print(df[(df['marks']>70)&(df['city']=='Delhi')])

# OR condition :
print(df[(df['marks']>70)&(df['city']=='Delhi')])

# direct query :
print(df.query("marks>70 and city=='Delhi'"))

# FILTER + SELECT COLUMNS :
print(df.loc[df['marks']>70,['name','city']])

# isin() → SQL IN :
print(df[df['city'].isin(['Pune','Mumbai'])])

# BETWEEN (Clean way) :
print(df[df['marks'].between(70,100)])

# STRING FILTERING (VERY COMMON) :

# Starts with :
print(df[df['name'].str.startswith('S')])

# Contains : 
print(df[df['name'].str.contains('t')])

# Case insensitive :
print(df[df['name'].str.contains('s',case=False)])

# SORTING DATA :

# Sort by one column :
print(df.sort_values('marks'))

# Descending:
print(df.sort_values('marks', ascending=False))

# Sort by multiple columns :
print(df.sort_values(['city','marks'],ascending=[False,True]))

# SORT BY INDEX :
print(df.sort_index())

# TOP / BOTTOM RECORDS :
print(df.nlargest(3, 'marks'))
print(df.nsmallest(2, 'age'))

# RESET INDEX (AFTER FILTERING) :
print(df = df.reset_index(drop=True))
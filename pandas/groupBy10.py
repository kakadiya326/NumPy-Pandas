import pandas as pd

data = {
    'name': ['Ram', 'Shyam', 'Mohan', 'Sita', 'Geeta', 'Anita'],
    'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Mumbai', 'Delhi'],
    'marks': [78, 85, 67, 92, 55, 88],
    'gender': ['Male', 'Male', 'Male', 'Female', 'Female', 'Female']
}

df = pd.DataFrame(data)
# BASIC GROUPBY

# Average marks per city :
print(df.groupby('city')['marks'].mean())

# Max marks per city :
print(df.groupby('city')['marks'].max())

# Count students per city :
print(df.groupby('city')['name'].count())

# GROUPBY MULTIPLE COLUMNS :

# Average marks by city + gender :
print(df.groupby(['city','gender'])['marks'].mean())

# MULTIPLE AGGREGATIONS (VERY COMMON) :
print(df.groupby('city')['marks'].agg(['min','max','mean','sum','count']))

# Rename output :
print(df.groupby('city')['marks'].agg(min_marks='min',max_marks='max',avg_marks='mean'))

# GROUPBY WITH FILTER :

# Only students with marks > 70 :
print(df[df['marks']>70].groupby('city')['marks'].mean())

# GROUPBY + SORT :
print(df.groupby('city')['marks'].mean().sort_values(ascending=False))

# RESET INDEX (IMPORTANT) :
result = df.groupby('city')['marks'].mean().reset_index()
print(result)

# GROUPBY ON NON-NUMERIC (COUNT) :
print(df.groupby('gender').size())
print(df.groupby('gender')['name'].count())

# GROUPBY WITH CUSTOM LOGIC :
print(df.groupby('city').apply(lambda x: x[x['marks'] > 80]))

# TRANSFORM (ADVANCED BUT IMPORTANT) :
df['city_avg'] = df.groupby('city')['marks'].transform('mean')
print(df)
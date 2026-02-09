import pandas as pd
# Merge students & city tables
# Use left join and find missing cities
# Merge on multiple columns
# Concatenate two monthly datasets
# Explain merge vs join
students = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Ram', 'Shyam', 'Mohan', 'Sita'],
    'city_id': [101, 102, 101, 103]
})

cities = pd.DataFrame({
    'city_id': [101, 102, 103],
    'city': ['Delhi', 'Mumbai', 'Pune']
})

print(pd.merge(students,cities))
print(pd.merge(students,cities,how="left",on="city_id"))
print(pd.merge(students,cities,on=['city_id','d_id']))
print(pd.concat([students,cities],axis=1))
import pandas as pd

students = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Ram', 'Shyam', 'Mohan', 'Sita'],
    'city_id': [101, 102, 101, 103]
})

cities = pd.DataFrame({
    'city_id': [101, 102, 103],
    'city': ['Delhi', 'Mumbai', 'Pune']
})

# inner join
print(pd.merge(students, cities, on='city_id'))

print(pd.merge(students,cities,how="inner",on="city_id"))
print(pd.merge(students,cities,how="left",on="city_id"))
print(pd.merge(students,cities,how="right",on="city_id"))
print(pd.merge(students,cities,how="outer",on="city_id"))
print(pd.merge(students,cities,how="cross",on="city_id"))  # ERROR

# MERGE ON DIFFERENT COLUMN NAMES
print(pd.merge(students,cities,left_on='city_id',right_on="city_id"))

# MERGE MULTIPLE KEYS
print(pd.merge(students,cities,on=['city', 'gender']))

# JOIN USING INDEX
print(students.join(cities.set_index('city_id'), on='city_id'))

# CONCAT
print(pd.concat([students,cities]))
print(pd.concat([students,cities],axis=1))


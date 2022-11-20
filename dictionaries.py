

students = {'name': 'Hrmn', 'age': 25, 'courses': ['Math', 'CompSci']}

#students['phone'] = '555555-5555'
#students['name'] = 'Singh'

# print(students.get('name', 'Not found'))  # to get the value none


# To update the dictionary
#students.update({'name': 'Annural', 'age': 23, 'courses': ['Sing', 'Artist']})

# To delete any key
#del students['age']

# pop method
#age = students.pop('age')

# print(students.values())
# print(students.keys())

# print(students.items())


# loop
for key, value in students.items():
    print(key, value)

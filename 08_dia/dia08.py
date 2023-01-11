################ DICTIONARY ###############

# Create an empty dictionary called dog
dog = dict()  # Empty dictionary also dog = {}

# Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Piano'
dog['color'] = 'Black'
dog['breed'] = 'WOW'
dog['legs'] = 4
dog['age'] = 30
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name': 'Victor',
    'last_name': 'Gonzalez',
    'gender': 'Male',
    'age': 45,
    'marital_status': 'Married',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'country': 'Chile',
        'city': 'Santiago'
    }
}

print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('Linux')
student['skills'].append('Windows')
print(student['skills'])
# Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)
# Get the dictionary values as a list
student_values = student.values()
print(student_values)
# Change the dictionary to a list of tuples using items() method

print(student.items())
# Delete one of the items in the dictionary
student.pop('age')
print(student)
# Delete one of the dictionaries
del student

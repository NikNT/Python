# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a dictionary

person = {
    'first_name' : 'John', 
    'last_name' : 'Doe', 
    'age' : 30
}

# Using a constructor 

person2 = dict(first_name='Sarah', last_name='Williams')

# print(person2, type(person2))
# print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'
print(person)
# Get keys
print(person.keys())

# Get items
print(person.items())

# Copy dict 
person2 = person.copy() #similar to spread operator
person2['city'] = 'Boston'
print(person2)

# Delete item
del(person['age'])
print(person)

person.pop('last_name')
print(person)

# List of Dictionaries -> Array of Objects 

people = [
    {'first_name' : 'John', 'age': 30},
        {'first_name' : 'Doe', 'age': 23},
            {'first_name' : 'Sarah', 'age': 33},
                {'first_name' : 'Williams', 'age': 29},
]

print(people)
print(people[0]['first_name'])
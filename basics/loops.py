# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# for person in people:
#     print(f'Current person {person}')
    
# Break out of loop
# for person in people:
#     if person == 'Sara':
#         break
#     print(f'Current person {person}')
    
# Continue loop - Skips the element
for person in people:
    if person == 'Sara':
        continue
    print(f'Current person {person}')
    
# Range
for i in range(len(people)):
    print(f'{people[i]} is at {i+1} location')

#(included, excluded)
for i in range(0, 11):
    print(f'Number {i}')

# While loops execute a set of statements as long as a condition is true.
count = 0
while count < 10:
    print(f'Count: {count}')
    count += 1

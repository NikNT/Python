# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple 
fruits = ('apples', 'oranges', 'grapes')
# fruit = tuple(('apples', 'oranges', 'grapes'))

# A tuple with just one value will be considered as a string. To avoid, always use a trailing comma. 
fruit2 = ('apple', )

# Get value 
# print(fruits[1])

# Can't change value in Tuples 
# fruits[1] = 'blueberries' 

# Delete tuple
del fruit2

# print(fruit2)




# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set 
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set 

print('Apples' in fruits_set)

# Add to set 

fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear entire set
fruits_set.clear()

# Del
del fruits_set

print(fruits_set)
# A List is a collection which is ordered and changeable. Allows duplicate members.

#common way
# numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#use a constructor
# numbers2 = list((1,2,3,4,5))

#Get a value
print(fruits[1])

#Get length
print(len(fruits))

#Append to list
fruits.append('Mangoes')
print(fruits)

#Remove from list 
fruits.remove('Grapes')
print(fruits)

#Insert into position 
fruits.insert(2, 'Strawberry')
print(fruits)

#Remove with pop
fruits.pop(2)
print(fruits)

#Reverse List 
fruits.reverse()
print(fruits)

#Sort list 
fruits.sort()
print(fruits)

#Reverse Sort 
fruits.sort(reverse=True)
print(fruits)

#Change value 
fruits[0] = 'Blueberries'
print(fruits)


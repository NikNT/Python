# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Nikhil'
age = 26

#Concat 

# print('Hello, my name is ', name)
print('Hello my name is', name, 'and my age is', age)

# String Formatting

#Arguments by position 
print('My name is {name} and I am {age}!'.format(name=name, age=age))

#F-Strings() >3.6
print(f'Hello my name is {name}')


# String Methods
s = 'hello world'
print(s.capitalize())
print(s.swapcase())
print(len(s))
print(s.replace('world', 'everyone'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())

# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function 

def say_name(name='Sam'):
    print(f'Hey {name}')
    
# say_name('John')
say_name()

# Return Values 
def getSum(num1, num2):
    total = num1 + num2
    print(f'Sum of {num1} and {num2} is {total}')
    
getSum(1,2)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(4, 7))
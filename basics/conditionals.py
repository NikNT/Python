# If/ Else conditions are used to decide to do something based on something being true or false

x = 51
y = 50

if x > y:
    print(f'{x} is gt {y}')
elif x == y:
    print(f'{x} is eq to {y}')
else:
    print(f'{y} is gt {x}')
    
    
# Nested If
if(x > 10):
    if y > 10:
        print('x and y are gt 10')


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values



# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and y < 10:
    print(f'{x} is gt 2 and {y} is lt 10')

if x > 2 or y < 10:
    print(f'{x} is gt 2 and {y} is lt 10')
    
if not x == y:
    print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

mylist = [1,2,3,4,5]

if x in mylist:
    print(x in mylist)
    
if x not in mylist:
    print(x not in mylist)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

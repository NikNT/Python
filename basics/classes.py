# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class 

class User:
    # Constructor 
    def __init__(self, name, email, age):
        self.name = name #similar to this.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return (f'My name is {self.name} and my email is {self.email} and my age is {self.age}')
    
    def has_Birthday(self):
        self.age += 1
    
#Init user object 
nik = User('Nikhil Tanwar', 'nik@tan.com', 26)
print(nik.name, nik.email, nik.age, type(nik))
print(nik.greeting())
print(nik.has_Birthday())
print(nik.greeting())

# Extend Class 
class Customer(User):
    #Constructor 
        def __init__(self, name, email, age):
            self.name = name 
            self.email = email
            self.age = age
            self.balance = 0
        
        def set_balance(self, balance):
            self.balance = balance
            
        def greeting(self):
            return (f'My name is {self.name} and my email is {self.email} and my age is {self.age} and my balance is {self.balance}')
 
# Init customer      

sarah = Customer('Sarah', 'sarah@sarah.com', 25)
sarah.set_balance(1000)
print(sarah.greeting())
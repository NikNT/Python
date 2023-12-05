# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

userJSON = '{ "firstname": "John", "lastname": "Doe", "age": 30 }'

#Parse to dict

user = json.loads(userJSON)
print(user['firstname'])

car = {
    'make' : 'Ford', 
    'model' : 'Mustang',
    'year' : 1970
}

carJSON = json.dumps(car)
print(carJSON)
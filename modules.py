# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core Modules
# import datetime 
# from datetime import date
# import time
# from camelcase import CamelCase

# today = datetime.date.today()
# today = date.today()
# timestamp = time.time()
# print(today)
# print(timestamp)

#pip modules
# camel = CamelCase()
# my_string = "hello world"
# camel_cased_string = camel.hump(my_string)

# print(camel_cased_string)

# Import Custom Module

import validator
from validator import validate_email

if validate_email('nikhil#gmail.com'):
    print('Valid Email')
else: 
    print('Wrong Email')
    
from sum import sum

print(sum(1,2))
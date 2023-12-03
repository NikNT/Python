# Python has functions for creating, reading, updating, and deleting files.

# Open a file 

myFile = open('myfile.txt', 'w')
# myFile = open('myfile.py', 'w')

# Get info 
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

myFile.write('I like Python')
myFile.write('I know JavaScript')
myFile.close()


# Append to file
myFile = open('myfile.txt', 'a') # if we keep 'w' -> that will override the compelte content 
myFile.write('I also like Svelte')
myFile.close()


# Read from file 
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
myFile.close()


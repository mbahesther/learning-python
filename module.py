#create a file called mymodule 
import mymodule

mymodule.greeting("esther")

# When using a function from a module, use the syntax: module_name.function_name.


a = mymodule.person1["age"]
print(a)


#Re-naming a Module
#You can create an alias when you import a module, by using the as keyword:

#Create an alias for mymodule called mx
import mymodule as mx

a = mx.person1["first name"]
print(a)

#built-in Modules
#There are several built-in modules in Python, which you can import whenever you like.

#Import and use the platform module:

import platform

x = platform.system()
print(x)

#Using the dir() Function
#There is a built-in function to list all the function names 
# (or variable names) in a module. The dir() function:

#List all the defined names belonging to the platform module:

import platform
x = dir(platform)
print(x)

#Note: The dir() function can be used on all modules, also the ones you create yourself


#Import From Module
#You can choose to import only parts from a module, by using the from keyword.

from mymodule2 import person2
print(person2['last name'])

#Note: When importing using the from keyword, do not use the module name when referring 
# to elements in the module. Example: person1["age"], not mymodule.person1["age"]

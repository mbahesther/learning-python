#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of 
#the try- and except blocks.

#Exception Handling
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

#these exceptions can be handled using the try statement:

#The try block will generate an exception, because x is not defined:



try:
    print(x)
except:
    print("an expection occured")

#    Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error: 

#This statement will raise an error, because x is not defined:
#print(x)

#Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
   print("variable x is not defined")
except:
    print("something else went occur")

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

# In this example, the try block does not generate any error:

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")   

#  Finally
# The finally block, if specified, will be executed regardless if 
# he try block raises an error or not.   

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")


# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

x = -1

if x < 0:
    raise Exception("sorry, no munbers below zero")


#Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
    raise TypeError("only integers are allowed")

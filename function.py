#A function is a block of code which only runs when it is called.
#you can pass data, known as parameters, into a function.

#calling a function
def myfunction():
    print("hello here is my first function")
myfunction()

#arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.
def naming(fname):
    print(fname + " Rufus")

naming("emily")
naming("nicole")
naming("chole")  

#This function expects 2 arguments, and gets 2 arguments:
def name(fname, lname):
    print(fname + " " + lname)
name("angel", "johnson")

def kidname(*kids):
    print("The youngest child is " + kids[2])

kidname("emily","jane", "ivan")

#Keyword Arguments
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def child(child3, child2, child1):
    print("the youngest child is " + child3)
child(child1 = "emily", child2 = "james", child3 = "linus")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition

def last(**kid):
    print("his last name is " + kid["lname"])
last(fname = "linus", lname = "james")
#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.


#Default Parameter Value
#The following example shows how to use a default parameter value.
#if we call the function without argument, it uses the default value:
def nation(country = "norway"):
    print("i am from " + country)

nation("sweden")
nation("nigeria")
nation()
nation("germany")

#Passing a List as an Argument
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food):
    for x in food:
        print(x)
fruits = ["cherry", "apple", "mango"] 

my_function(fruits)

#To let a function return a value, use the return statement:
def value_return(y):
    return print (5 * y)
value_return(4)   
value_return(8) 
value_return(3)

#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
  pass


#Recursion Example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

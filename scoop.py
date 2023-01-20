#A variable is only available from inside the region it is created. This is called scope.

#Local Scope
#A variable created inside a function belongs to the local scope of that function, 
#and can only be used inside that function.

def myfunc():
    x = 490
    print(x)

myfunc()  

#The local variable can be accessed from a function within the function:

def myfunc():
    x = 500
    def myinnerF():
        print(x)
    myinnerF()
myfunc()    

#lobal variables are available from within any scope, global and local.
#A variable created outside of a function is global and can be used by anyone:

x = 21
def myfun():
    print(x)
myfun()

print(x)


#If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables,

x = 37
def myfunc():
    x = 66
    print(x)
myfunc()

print(x)

#The global keyword makes the variable global.
#If you use the global keyword, the variable belongs to the global scope:

def myfunt():
    global y 
    y = 19
    
myfunt()

print(y)

#to change the value of a global variable inside a function,
# refer to the variable by using the global keyword:

z = 89

def myf():
    global z
    z = 76
    print(z)
myf()    
print (z)
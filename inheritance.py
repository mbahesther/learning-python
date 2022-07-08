#Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#create a parent class

#Create a class named Person, with firstname and lastname properties, and a printname method:

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

#this is a method
    def printname(selfff):
        print(selfff.fname, selfff.lname)

#Use the Person class to create an object, and then execute the printname method:   

         # the x is the object
x = person("john", "chole")
x.printname()  
    
#Create a child class
#To create a class that inherits the functionality from another class, 
#send the parent class as a parameter when creating the child class:

#  Create a class named Student, which will inherit the properties 
# and methods from the Person class:

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(selfff):
        print(selfff.fname, selfff.lname)
   

x = person("john", "james")
x.printname()  

class student(person):
   pass

y = student("mike", "oslen")
y.printname()
#y for the child class method

#We want to add the __init__() function to the child class (instead of the pass keyword).

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(selfff):
        print(selfff.fname, selfff.lname)

#adding the __init__ to the class
class student(person):
    def __init__(addself, fname, lname):
        person.__init__(addself, fname, lname)

#To keep the inheritance of the parent's __init__() function,
#  add a call to the parent's __init__() function:

x = student("sweetie", "pie")
x.printname()

#Using the super function()

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(selfff):
        print(selfff.fname, selfff.lname)

#adding the __init__ to the class
class student(person):
    def __init__(addself, fname, lname):
        super().__init__(fname, lname)

x = student("honey", "pie")
x.printname()

# add a property

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(selfff):
        print(selfff.fname, selfff.lname)

#adding the __init__ to the class
class student(person):
    def __init__(addself, fname, lname):
        super().__init__(fname, lname)
        addself.graduationyear = 2009

x = student("maria", "johnson")
print(x.graduationyear)


#add a method
#Add a method called welcome to the Student class

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(selfff):
        print(selfff.fname, selfff.lname)

#creating the child class and adding the __init__ to the class
class student(person):
    def __init__(addself, fname, lname, year):
        super().__init__(fname, lname)
        addself.graduationyear = year
    
    #the method created
    def welcome(oneness):
        print("welcome", oneness.fname, oneness.lname, "to the class of", oneness.graduationyear)


x = student("maria", "johnson", 2011)
x.welcome()
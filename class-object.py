#A Class is like an object constructor, or a "blueprint" for creating objects.
#To create a class, use the keyword class:

class myclass:
    x = 5
print(myclass)

#create a object
#Create an object named p1, and print the value of x:

p1 = myclass()
print(p1.x)

#The __init+__()function
#All classes have a function called __init__(), which is always executed
#  when the class is being initiated.

#Create a class named Person, use the __init__() function to assign values for name and age:

class person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = person("john", 29)

print(p1.name)
print(p1.age)

#Note: The __init__() function is called automatically 
#every time the class is being used to create a new object.

#object methods
#Let us create a method in the Person class:

#Insert a function that prints a greeting, and execute it on the p1 object:

class person:

    def __init__(self, name, age):
       self.name = name
       self.age = age

    def myfunc(self):

       print("hello my name is " + self.name)

p1 = person("john", 29)
p1.myfunc()  

#The self Parameter
#The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.

#It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

#Use the words mysillyobject and abc instead of self:

class person:

    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("hello my name is " + abc.name)

p1 = person("sam", 22)
p1.myfunc()


#You can modify properties on objects like this:
#Set the age of p1 to 40:


class person:

    def __init__(self, name, age):
       self.name = name
       self.age = age

    def myfunc(self):

       print("hello my name is " + self.name)

p1 = person("john", 29)
p1.age = 49
print(p1.age)

#Delete Object Properties


class person:

    def __init__(self, name, age):
       self.name = name
       self.age = age

    def myfunc(self):

       print("hello my name is " + self.name)

p1 = person("john", 29)
del p1.age
#print(p1.age)

#Delete Objects
#You can delete objects by using the del keyword:
class person:

    def __init__(self, name, age):
       self.name = name
       self.age = age

    def myfunc(self):

       print("hello my name is " + self.name)

p1 = person("john", 29)
del p1
#print(p1.age)

#the pass statement
class person:
    pass
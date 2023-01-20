#An iterator is an object that contains a countable number of values.
#Technically, in Python, an iterator is an object which implements the iterator protocol, 
# which consist of the methods __iter__() and __next__().

#Lists, tuples, dictionaries, and sets are all iterable objects. 
# They are iterable containers which you can get an iterator from.

#Return an iterator from a tuple, and print each value:
mytuple = ("maggi", "sugar", "salt", "honey")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping Through an Iterator
#We can also use a for loop to iterate through an iterable object:
mytuple = ("cherry", "mango", "pineapple")
for x in mytuple:

    print(x)


#Create an Iterator
#To create an object/class as an iterator you have
 #to implement the methods __iter__() and __next__() to your object.4


 #Create an iterator that returns numbers, starting with 1, 
 # and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))     
print(next(myiter))     
print(next(myiter))  
print(next(myiter))     
print(next(myiter))        


#StopIteration
#The example above would continue forever if you had enough next() statements, 
#or if it was used in a for loop.

class mynumbers:
    def __iter__(selff):
        selff.a = 1
        return selff

    def __next__(self):
        if self .a <=20:
            x = self.a
            self.a += 1
        
            return x
        else:
         raise StopIteration

myclass = mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
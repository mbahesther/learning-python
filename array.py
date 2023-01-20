#An array is a special variable, which can hold more than one value at a time.
#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

#This page shows you how to use LISTS as ARRAYS, however, to work with arrays
#  in Python you will have to import a library, like the NumPy library.

#Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Access the Elements of an Array
#You refer to an array element by referring to the index number.
cars = ["ford", "toyota", "volvo"]
x = cars[1]
print(x)

#Modify the value of the first array item:
cars = ["ford", "toyota", "volvo"]
cars[0] = "BMW"
print(cars)

#Use the len() method to return the length of an array (the number of elements in an array).
cars = ["ford", "toyota", "volvo"]
print(len(cars))

#loop through in an array
cars = ["ford", "toyota", "volvo"]
for x in cars:
    print(x)

#add to an array using append()method
cars = ["ford", "toyota", "volvo"]
cars.append("wagon")
print(cars)

#removing an array with pop()method
cars = ["ford", "toyota", "volvo"]
cars.pop(1)
print(cars)

#removing an array with remove 
cars = ["ford", "toyota", "volvo"]
cars.remove("volvo")
print(cars)
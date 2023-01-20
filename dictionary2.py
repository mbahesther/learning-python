
#Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
x = car.values()
print(x)
car["color"] = "white"
print(x)

#The items() method will return each item in a dictionary, as tuples in a list.
car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
x = car.items()
print(x)

#Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
x = car.items()
print(x)
car["year"] = 1908
print(x)

car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
x = car.items()
print(x)
car["country-use"] = "USA"
print(x)

#To determine if a specified key is present in a dictionary use the in keyword:
car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
if "model" in car:
    print("yes, 'model' is one of keys in car dictionary ")

#You can change the value of a specific item by referring to its key name:
thiscar = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
thiscar["year"] = 2023
print(thiscar)

#Update the "year" of the car by using the update() method:
thiscar = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
thiscar.update({"year":2042})
thiscar.update({"brand":"Mercedes Benz"})
print(thiscar)

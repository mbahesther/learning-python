#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#dirtionary are wriiten in a curly bracket and have keys and values

thisdict = {
    "brand": "ford",
    "model": "musta",
    "year":"1989"
}
print(thisdict)

#Dictionary items are presented in key:value pairs, 
#and can be referred to by using the key name.
#print the brand value of the dictionary
thisdict = {
    "brand": "ford",
    "model": "musta",
    "year":"1989"
}
print(thisdict["brand"])

#duplicate- Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values
thisdict = {
    "brand": "ford",
    "model": "musta",
    "year": "1989",
    "year": "2021"
}
print(thisdict)

#To determine how many items a dictionary has, use the len() function:
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1989"
}
print(len(thisdict))

#You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1989"
}
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1989"
}
x = thisdict.get("model")
print(x)

#The keys() method will return a list of all the keys in the dictionary.
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1989"
}
x = thisdict.keys()
print(x)

#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
x = car.keys()
print(x)
car["color"] = "blue"
print(x)

#The values() method will return a list of all the values in the dictionary.
car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
x = car.values()
print(x)
# or use this to print print(car.values())

#Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "toyota",
    "model": "camry",
    "year" : "2010"
}
x = car.values()
print(x)
car["year"] = 2021
print(x)
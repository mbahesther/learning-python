import json
#JSON is a syntax for storing and exchanging data.
#Convert from JSON to Python
#If you have a JSON string, you can parse it by using the json.loads() method.

#some json
x = '{"name":"chidi", "age":30, "country":"new york"}'

#parse x
y = json.loads(x)

print(y["country"])

#Convert from Python to JSON
#If you have a Python object, you can convert it into a JSON string 
# by using the json.dumps() method.

# a python object dict
x = {
    "name": "john",
    "age": "21",
    "country": "trindad and tabgo"
}
#convert to json

y = json.dumps(x)
print(y)

#convert the python objects into json strings
print(json.dumps({"name": "oma", "age": "16" ,"school": "queens college"}))
print(json.dumps(["apple", "cherry"]))
print(json.dumps(("mango", "orange")))
print(json.dumps(43))
print(json.dumps(32.33))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



#Convert a Python object containing all the legal data types:
x = {
    "name" : "sakani",
    "age" : "35",
    "married": "True",
    "Divorced": "False",
    "children": ("anna", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW230", "mpg": 29.2},
        {"model": "Toyota Rav4", "mpg": 23.7}
    ]
}
print(json.dumps(x))


#Format the Result
#The example above prints a JSON string, but it is not very easy to read, 
# with no indentations and line breaks.

#The json.dumps() method has parameters to make it easier to read the result:


#Use the indent parameter to define the numbers of indents:
x = {
    "name" : "sakani",
    "age" : "35",
    "married": "True",
    "Divorced": "False",
    "children": ("anna", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW230", "mpg": 29.2},
        {"model": "Toyota Rav4", "mpg": 23.7}
    ]
}

print(json.dumps(x, indent = 4, separators = (" . ", " = ") ))

# use . and a space to separate objects, and a space, 
# a = and a space to separate keys from their values:

print("\n")
x = {
    "name" : "sakani",
    "age" : "35",
    "married": "True",
    "divorced": "False",
    "children": ("anna", "Billy"),
    "pets": "None",
    "cars": [
        {"model": "BMW230", "mpg": 29.2},
        {"model": "Toyota Rav4", "mpg": 23.7}
    ]
}

print(json.dumps(x, indent = 4, sort_keys =True))
#Order the Result

#Use the sort_keys parameter to specify if the result should be sorted or not:
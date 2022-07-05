#You can also use the values() method to return values of a dictionary:
thisdic = {
  "food" : "Rice",
  "benefit" : "strong bone",
  "work" : "energy"
}
for x in thisdic.values():
    print(x)

#You can use the keys() method to return the keys of a dictionary:
thisdic = {
  "food" : "Rice",
  "benefit" : "strong bone",
  "work" : "energy"
}
for x in thisdic.keys():
    print(x)

#Loop through both keys and values, by using the items() method:
thisdic = {
  "food" : "Rice",
  "class" : "carbondhydrate",
  "work" : "energy"
}
for x,y in thisdic.items():
    print(x,y)
#copy dictionary
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdic = {
  "food" : "beans",
  "benefit" : "build the body",
  "class": "protein"
}
mydict = thisdic.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function:
thisdic = {
  "food" : "beans",
  "benefit" : "build the body",
  "class": "protein"
}
mydict = dict(thisdic)
print(mydict)


#nested dictionary
#Create a dictionary that contain three dictionaries:
schoolRegister = {
    "student1" :{
     "name": "tobias",
     "age": "9",
    },

     "student2" :{
     "name": "sam",
     "age": "10",
    },

     "student3" :{
     "name": "tolu",
     "age": "8",
    },
}
print(schoolRegister)
#Create three dictionaries, then create one dictionary 
# that will contain the other three dictionaries:
child1 = {
    "name" : "joy",
    "year" : "2001"
}

child2 = {
    "name" : "tobi",
    "year" : "2005"
}
child3 = {
    "name": "sakani",
    "year" : "2011"
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#Adding an item to the dictionary is done by using a new index key
#  and assigning a value to it:

thisdic = {
  "food" : "Rice",
  "class" : "carbonhydrate",
  "work" : "energy"
}
thisdic["color"] = "lightbrown"
print(thisdic)

#The update() method will update the dictionary with the items from a given argument.
# If the item does not exist, the item will be added.
thisdic = {
  "food" : "Rice",
  "class" : "carbonhydrate",
  "work" : "energy"
}
thisdic.update({"benefit": "strong bone"})
print(thisdic)

#The pop() method removes the item with the specified key name:
thisdic = {
  "food" : "Rice",
  "class" : "carbonhydrate",
  "work" : "energy"
}
thisdic.pop("class")
print(thisdic)

#The popitem() method removes the last inserted item 
#(in versions before 3.7, a random item is removed instead):
thisdic = {
  "food" : "Rice",
  "class" : "carbonhydrate",
  "work" : "energy"
}
thisdic.popitem()
print(thisdic)

#The del keyword removes the item with the specified key name:
thisdic = {
  "food" : "Rice",
  "class" : "carbonhydrate",
  "work" : "energy"
}
del thisdic["class"]
print(thisdic)

#The del keyword can also delete the dictionary completely:
thisdic = {
  "food" : "Rice",
  "class" : "carbonhydrate",
  "work" : "energy"
}
del thisdic
#print(thisdic)

#The clear() method empties the dictionary:
thisdic = {
  "food" : "Rice",
  "class" : "carbonhydrate",
  "work" : "energy"
}
thisdic.clear()
print(thisdic)

#When looping through a dictionary, the return value are the keys of the dictionary, 
# but there are methods to return the values as well.
thisdic = {
  "food" : "Rice",
  "benefit": "strong bone",
  "work" : "energy"
}
for x in thisdic:
    print(x)

#Print all values in the dictionary, one by one:
thisdic = {
  "food" : "Rice",
  "benefit" : "strong bone",
  "work" : "energy"
}
for x in thisdic:
    print(thisdic[x])
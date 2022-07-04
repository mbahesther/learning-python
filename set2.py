#To add one item to a set use the add() method.
myown = {"monkey","fish","maggi"}

myown.add("orange")
print(myown)

#To add items from another set into the current set, use the update() method.
thisset = {"onions", "cashew", "ice cube"}
tropical = {"monkey", "plate", "moi moi", "rice"}
thisset.update(tropical)
print(thisset)

#The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"head", "nose", "eye", "leg"}
thislist = ["orange", "grape"]
thisset.update(thislist)
print(thisset)

#remove an item using remove() or dicard method 
thisset = {"head", "nose", "eye", "leg"}
thisset.remove("nose")
print(thisset)

#clear empties the set
thisset = {"head", "nose", "eye", "leg"}
thisset.clear()
print(thisset)

#del keyword will delete completely

# looping the set with for loop
thisset = {"head", "nose", "eye", "leg"}
for x in thisset:
    print(x)
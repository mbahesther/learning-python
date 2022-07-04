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
    #print(x)
 
 #join two set using union
 set1 = {"mango", "apple", "melon"} 
set2 = {"bag", "shoe", "weavon"}
sett = set1.union(set2)
print(sett)

#update
set1 = {"mango", "apple", "melon"}
set2 = {"bag"}
set1.update(set2)
print(set1)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"microsoft", "google", "speedpay"}
y = {"ice", "microsoft", "speedpay"}
x.intersection_update(y)
print(x)


 #The symmetric_difference_update() method will keep only the elements 
 # that are NOT present in both sets.
a = {"telephone", "spar", "amazon", "apple"}
b = {"adobe", "apple", "catfish"}

a.symmetric_difference_update(b)
print(a)

#Return a set that contains all items from both sets, except items that are present in both:
a = {"sweet", "biscuit", "yoghurt"}
b = {"grape", "pineaple", "sweet", "yoghurt"}
c = a.symmetric_difference(b)
print(c)
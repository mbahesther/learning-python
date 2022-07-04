#set are written in a curly bracket {}
# set are unordered you can't be sure which order the item will appear, 
# can't be changed and don't allow duplicate
thisset = {"pot", "cup", "monkey"}
print(thisset)

#duplicate
thisset = {"pot", "cup", "monkey", "pot", "cup"}
print(thisset)

#get the length
thisset = {"pot", "cup", "monkey"}
print(len(thisset))

#set constructor
thisset = set(("pot",  "monkey", "chair"))
print(thisset)

#You cannot access items in a set by referring to an index or a key but can loop

thisset = {"pot", "cup", "stone"}
for x in (thisset):
    print(x)

 # to check if a item is present
    myset= {"pot", "cup", "ice"}
   print("ice" in myset)
#tuple are written in round bracket
import this


thistuple = ("bag", "shoe", "sandal")
print(thistuple)

#tuple allows duplicate a
thistuple =("bag", "shoe", "sandal", "shoe", "bag")
print(thistuple)
#and to determine how many length tuple has use 
# the len()function
thistuple =("bag", "shoe", "sandal", "shoe", "bag")
print(len(thistuple))

#one item tuple add a comma to recognize is a tuple
thistuple = ("maggi",)
print(thistuple)

#the tuple() constructor can also be use to create tuple
thistuple =tuple(("bag", "shoe", "sandal",))
print(thistuple)

#access tuple items by referring to the index
thistuple = ("bag", "clothe", "sandal")
print(thistuple[1])

#negative index means start from the end with -1
thistuple = ("bag", "shoe", "sandal")
print(thistuple[-1])

#range of indexs the search will start at index2 and index5 excluded
thistuple = ("bag", "shoe","sandal","salt","fridge","milk","melon")
print(thistuple[2:5])

#from the beginning not including the 4th
thistuple = ("bag", "shoe","sandal","salt","fridge","milk","melon")
print(thistuple[:4])

#By leaving out the end value, the range will go on
# to the end of the list:
thistuple = ("bag", "shoe","sandal","salt","fridge","milk","melon")
print(thistuple[1:])

#To determine if a specified item is present in a tuple use the in keyword
thistuple = ("bag", "shoe","sandal","salt","fridge","milk","melon")
if "salt" in thistuple:
    print("yes 'salt' is in the cate")

#tuple cannot be changed as stated, tuples are unchangeable
#but there is a workaround, You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.
x = ("yoghurt", "biscit","apple")
y = list(x)
y[1] = "sweet"
x = tuple(y)
print(x)

# to add to tuple you convert to list, add the items then convert back to a tuple
thistuple = ("yoghurt", "biscit","apple")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#add tuple to a tuple
thistuple = ("yoghurt", "biscit","apple")
y = ("sweet",)
total = thistuple +  y
print(total)
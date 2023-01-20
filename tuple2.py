#to remove from a tuple
# Convert the tuple into a list, remove "biscuit", and convert it back into a tuple:
from xml.dom import HierarchyRequestErr


thistuple = ("yoghurt", "biscuit","apple")
x = list(thistuple)
x.remove("biscuit")
thistuple = tuple(x)
print(thistuple)

# or delete completely
thistuple = ("yoghurt", "biscuit","apple")
del thistuple
#print(thistuple)

#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#But, in Python, we are also allowed to extract the values back into variables. 
# This is called "unpacking"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#If the number of variables is less than the number of values, you can add an * to the 
# variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign
#  values to the variable until the number of values left matches the number of variables left.
ruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#loop with for
thistuple = ("apple", "carton", "ice cube")
for x in thistuple:
    print(x)

    thistuplee = ("card", "house", "resturant", "bell")
    i = 0
    while i < len(thistuplee):
        print(thistuplee[i])
        i = i + 1

#join tuple
hey1 = ("apple", "phone", "rain")
hey2 = (1, 2, 10009)
hey3 = hey1 + hey2
print(hey3)
#OR hey3 = print(hey1 + hey2)

#If you want to multiply the content of a tuple a given number of times,
# you can use the * operator:
hey = ("apple", "phone", "rain")
mytuple = hey * 2
print(mytuple)
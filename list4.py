#copy a list using the copy() method
thislist =  ['dog', 'truck', 'ship', 'apple']
mylist = thislist.copy()
print(mylist)

#another way is to use the list() method to copy
thislist =  ['dog', 'truck', 'ship', ]
mylist = list(thislist)
print(mylist)

#joining two list with + operator
list1 = ['house', 'mouse', 'fish',]
list2 = ['pet', 'bag', 'chief', 'lappy']
list3 = list1 + list2
print(list3)

#another way is to use the extend()method
list1 = ['ice', 'body', 'food']
list2 = [1, 2, 4]
list1.extend(list2)
print(list1)
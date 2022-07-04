#using the pop() to remove alist it removes a specified index
thislist = ['mango', 'orange', 'apple']
thislist.pop(1)
print(thislist)

#del() can also remove the entire list
thislist = ['mango', 'orange', 'apple']
del thislist
#print(thislist) thiswill cause an error

#loop through a list usin the for
thislist = ['mango', 'orange', 'apple']
for x in thislist:
    print(x)

    #while loop
    #thislist = ['mango', 'orange', 'apple']
    #i = 0
    #while i < len(thislist):
        #print(thislist[i])
        #i = i + 1
#sorting alphanumerically by ascending default with sort()method
thislist = ['mango', 'orange', 'apple']
thislist.sort()
print(thislist)

#sort the list numerically
num = [12, 100, 39, 10, 47]
num.sort()
print(num)

#sorting in desecending order
thislist = ['mango', 'orange', 'apple']
thislist.sort(reverse = True)
print(thislist)

num = [12, 100, 39, 10, 47]
num.sort(reverse = True)
print(num)

#sorting is case sensitive soring the capital letters
#before lower letters

#performing case insensitive
thislist = ['mango', 'Orange', 'Apple']
thislist.sort(key = str.lower)
print(thislist)

#reverse order
thislist = ['mango', 'orange', 'apple', 'melon', 'cherry']
thislist.reverse()
print(thislist)
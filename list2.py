dinner = ['vera', 'nick', 'stella', 'hon']
print(dinner)
message = f"\n{dinner[0].upper()} you are invited to my 30th party"
print(message)

message = f"\n{dinner[1].upper()} you are welcome to my 30 party "
print(message)

message = f"\n{dinner[2].upper()} you are welcome to my 30 party "
print(message)
message = f"\n{dinner[3].upper()} you are welcome to my 30 party "
print(message)

dinner = ['vera', 'nick', 'stella']
dinner.append('bianca')
print(dinner)
noway = f"\n{dinner[2]} can't make it to my diner"
print(noway)

message = f"\n{dinner[0].upper()} you are welcome to my 30 party "
print(message)

message = f"\n{dinner[1].upper()} you are welcome to my 30 party "
print(message)

message = f"\n{dinner[3].upper()} you are welcome to my 30 party "
print(message)

#insert
dinner = ['vera', 'nick', 'stella']
dinner.insert(0, 'badgirl')
print(dinner)
dinner.insert(2, 'mila')
print(dinner)
dinner.append('nila')
print(dinner)

#getting a list length
thislist = ['mango', 'orange', 'apple', 'cashew']
print(len(thislist))

#extend list means to join two list or tuple together
thislist = ['mango', 'orange', 'apple']
tropical = ['pinneaple', 'watermelon']
thislist.extend(tropical) 
print(thislist)

#remove item using the remove()method
thislist = ['mango', 'orange', 'apple']
thislist.remove("mango")
print(thislist)


import random
print(random.randrange(1, 10))
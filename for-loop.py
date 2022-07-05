#looping through list,tuple, set
fruits = ["apple", "mango","cashew","banana"]
for fruit in fruits:
    print(fruit)

    #looping through a string
    #Even strings are iterable objects, they contain a sequence of characters:
for x in "i love you":
    print(x)

#With the break statement we can stop the loop before it has looped through all the items:
#Exit the loop when x is "cashew":
fruits = ["apple", "mango","cashew","banana"]
for x in fruits:
    print(x)
    if x == "cashew":
        break

#Exit the loop when x is "cashew", but this time the break comes before the print:
    fruits = ["apple", "mango","cashew","banana"]
    for y in fruits:       
     if y == "cashew":
        break 
        print(y)

#With the continue statement we can stop the current iteration of the loop,
#  and continue with the next:

#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)

#The range() function defaults to 0 as a starting value, however it is possible to specify the 
# starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)

#The range() function defaults to increment the sequence by 1, however it is possible 
# to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)

#the else keyword in a for loop specifies a block of code to be executed
#when the loop is finished:

#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#The else block will NOT be executed if the loop is stopped by a break statement.
#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#A nested loop is a loop inside a loop.

#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass

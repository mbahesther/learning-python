#storing data
# Let’s write a short program that stores a set of numbers and another program that 
# reads these numbers back into memory. The first program will use json.dump() to store 
# the set of numbers, and the second program will use json.load()


import json

numbers  = [2,3,5,7,9,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


# Let’s look at an example where we prompt the user for their name the
#  first time they run a program and then remember their name when they
#  run the program again.
# Let’s start by storing the user’s name:

username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
 json.dump(username, f)
print(f"We'll remember you when you come back, {username}!")



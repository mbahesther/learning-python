#Now we’ll write a program that uses json.load() to read the list back into
#memory:

import json

filename = 'numbers.json'
with open(filename) as f:
     numbers = json.load(f)
print(numbers)


#Now let’s write a new program that greets a user whose name has already been stored:
filename = 'username.json'
with open(filename) as f:
  username = json.load(f)
print(f"Welcome back, {username}!")
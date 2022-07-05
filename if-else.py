from re import A


a = 200
b = 4509
if b > a:
    print("b is greater than a")

    #The elif keyword is pythons way of saying "if the previous conditions were not true, 
    # then try this condition".
    c = 33
    d = 33
    if d > c:
        print("d is greater than c")
    elif d == c:
        print("c and d are equal")

#The else keyword catches anything which isn't caught by the preceding conditions.
a = 234
b = 12
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
    print("a is greater")

#You can also have an else without the elif:
a = 200
b = 13
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#short hand of if...
a = 200
b = 33

if a > b: print("a is greater than b")

#short hand for if and else
a = 2
b = 330

print("A") if a > b else print("B")

#You can also have multiple else statements on the same line:
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

#AND The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR The or keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

  #Nested if 
  # You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass
#Python has a set of built-in math functions, including an extensive math module,
# that allows you to perform mathematical tasks on numbers.

#built-in maths functions
#The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(90, 36, 70, 17)
y = max(38, 13, 62, 90)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)

print(x)

#The pow(x, y) function returns the value of x to the power of y (xy).

y = pow(7, 3)
print(y)


#The math module
import math
z = math.sqrt(64)
print(z)

#The math.ceil() method rounds a number upwards to its nearest integer, and the 
#math.floor() method rounds a number downwards to its nearest integer, and returns the result:
x = math.ceil(1.6)
y = math.floor(1.6)

print(x)
print(y)

#The math.pi constant, returns the value of PI (3.14...):
x = math.pi
print(x)

print(math.acos(0.233))
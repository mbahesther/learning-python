#Python Lambda
#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

#The expression is executed and the result is returned:

#Add 10 to argument a, and return the result:
def func(a, b, c=4, *args, **kwargs):
    return a + b + c


x = func(1, 4)

print(x)

x = lambda a, b: a + b


print(x(40, 89))
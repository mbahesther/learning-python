#Import the datetime module and display the current date:

import datetime


x = datetime.datetime.now()
print(x)

#Return the year and name of weekday:
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#Creating Date Objects
#The datetime() class requires three parameters to create a date: year, month, day.

import datetime

x = datetime.datetime(2012, 5, 15)
print(x)

#The strftime() Method
#The datetime object has a method for formatting date objects into readable strings.
#The method is called strftime(), and takes one parameter, format, 
# to specify the format of the returned string:

#Display the name of the month:
import datetime

#month of the year fullversion
x = datetime.datetime(2018, 4, 23)
print(x.strftime("%B"))

#week of the year
x = datetime.datetime.now()
print(x.strftime("%U"))

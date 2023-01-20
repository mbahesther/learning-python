#multiple line string you used three double 
# quote or three single quote

print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''')

#get the poistion of a string
a = "hello, world! "
print(a[1])
print(a[5])

#loop in a string
#for x in "banana":
    #print(x)

#to get the length of a string you use the len()function
b = "hello, my dear people"
print(len(b))

#check if a character or phrase is present in a string
txt = "i want to go home and be free !"
print("free" in txt)

#using if statement
txt = "i want to go home and be free !"
if "free" in txt:
 print("yes, 'free' is present")

#check if a certain character is not present
txt = "i want to go home and be free !"
print("expensive" not in txt )

#using if to check
txt = "i want to go home and be free !"
if "expensive" not in txt:
    print("no, 'expensive' not there")

    #sliding
    c = "hello, sugar!"
    print(c[2:6])

   #slide from the start 
c = "hello, sugar!"
print(c[:6])

#slide to the end
c = "hello, sugar!"
print(c[2:])

#replace string
c = "hello, sugar!"
print(c.replace('h', 'K'))

#split
c = "hello, sugar world of mine"
print(c.split())

#concentate
age = 34
print('my name is oma i am ' + str(age))

#or this format
print('my name is i am ' + format(age))

#the format take unlimited number of  argument
quantity = 8
itemno = 23344
price = 23.33

myorder = "i odered {} pizza at {} and the receipt is {}."
print(myorder.format(quantity, price, itemno))

#you can use the index 0 to be sure argument 
# are placed in the correct order

myorder = "i odered {0} pizza with receipt {1} at price {2}."
print(myorder.format(quantity, itemno, price))




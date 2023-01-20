# Open a File on the Server
# Assume we have the following file, located in the same folder as Python:


f = open("demo.txt", "r")
print(f.read())

# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method 
# for reading the content of the file:


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify
#  how many characters you want to return:

#Return the 5 first characters of the file:
f = open("demo.txt")
print(f.read(6))

# Read Lines
# You can return one line by using the readline() method:
f = open("demo.txt")
print(f.readline())

#By calling readline() two times, you can read the two first lines
f = open("demo.txt")
print(f.readline())
print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demo.txt")
for x in f:
    print(x)


#Close Files
#It is a good practice to always close the file when you are done with it.
f = open("demo.txt")
print(f.readline())
f.close()
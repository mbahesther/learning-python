# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("demo2.txt", "a")
f.write("Now it is created to add more content")
f.close()

#open and read the  file after appending
f = open("demo2.txt", "r")
print(f.read())


#Open the file "demofile3.txt" and overwrite the content:
#Note: the "w" method will overwrite the entire file.

f = open("demo3.txt", "w")
f.write("whoops! i have deleted the content")
f.close()

f = open("demo3.txt", "r")
print(f.read())


#Create a new file

# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

f = open("myfile.txt", "x")    #create a new file 

#f = open("file.txt", "w")
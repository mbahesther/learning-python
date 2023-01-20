# Exceptions
# Python uses special objects called exceptions to manage 
# errors that arise during a program’s execution

# Exceptions are handled with try-except blocks. A try-except block asks
# Python to do something, but it also tells Python what to do if an exception is raised

#print(5/0)

 #using try-except blocks

    #using exception to handle crashes
    #Let’s create a simple calculator that does only division:
#


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    firstNumber = input("\nFirst number: ")
    if firstNumber == 'q':
        break
    secondNumber = input("second number: ")
    if secondNumber == 'q':
        break
    try:
       answer = int(firstNumber) / int(secondNumber)
    except ZeroDivisionError:
        print("you cant divide by zero")
    else:
     print(answer)

#Handling the FileNotFoundError Exception
filename = 'alice.txt'
try:
  with open(filename, encoding='utf-8') as f:
    contents = f.read()
except FileNotFoundError:
    print(f"sorry the file {filename} doesn't exit")



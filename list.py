#list are written in square bracket[]
bicycles = ['trek', 'motor', 'redline', 'ship' ]
print(bicycles)

# to call individual in a list use the index
print(bicycles[1])

names = ['ella', 'chi', 'cythnia', 'ifeoma', 'chioma']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

message = f"welcome on board {names[0].upper() }"
print(message)

message = f"welcome on board {names[4].upper() }"
print(message)

#modifying a list
motor = ['honda', 'mercede', 'camry']
print(motor)
motor[0] = 'durati'
print(motor)

#appending a list meaning adding to a list
motor = ['honda', 'mercede', 'camry']
print(motor)
motor.append('toyota')
print(motor)

#inserting element using the insert() method
motor = ['honda', 'mercede', 'camry']
motor.insert(1, 'jeep')
print(motor)

#to delete in a list
motor = ['honda', 'mercede', 'camry']
print(motor)
del motor[1]
print(motor)

#using pop
motor = ['honda', 'mercede', 'camry']
print(motor)
popped_motor = motor.pop()
print(popped_motor)
print(motor)

#using pop to remove item from any position
motor = ['honda', 'mercede', 'camry']
print(motor)
first_use = motor.pop(0)
print(f" the first car i used is {first_use}.")
 
 
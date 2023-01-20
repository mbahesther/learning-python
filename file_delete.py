# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

#remove the file remove.txt
import os
os.remove("remove.txt")

# Check if File exist:
# To avoid getting an error, you might want to check
#  if the file exists before you try to delete it:
import os
if os.path.exists("removeee.txt"):
    os.remove("removeee.txt")
else:
    print("The file doesnt exit")


#     Delete Folder
# To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("removee")
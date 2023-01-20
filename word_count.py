#ananlyzing text
filename = 'alicee.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()

except FileNotFoundError:        
    print(f"sorry file {filename} doesn't ")

else:
    # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words")      


#working with multiple files
#Let’s add more books to analyze. But before we do, let’s move the bulk of
#this program to a function called count_words().

# def count_words(filename):
#     """Count the approximate number of words in a file."""
    
# filenames = ['conciseAccount.txt', 'alicee.txt', 'optimist.txt']
# for filename in filenames:
#    count_words(filename)

# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()

# except FileNotFoundError:        
#     print(f"sorry file {filename} doesn't ")

# else:
#     # Count the approximate number of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print(f"the file {filename} has about {num_words} words")    

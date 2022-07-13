#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

#Python has a built-in package called re, which can be used to work with Regular Expressions.
#Python has a built-in package called re, which can be used to work with Regular Expressions.

#Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in spain is falling"
x = re.search("^The.*falling$", txt)    #^ means-starts with, .means- any character, * means-zero or more occurrence, $ means-ends with 
print(x)

if x:
    print("yes! we have a match")
else:
    print("no match")

#meta characters
#[]	A set of characters	"[a-m]"	
#\	Signals a special sequence (can also be used to escape special characters)	"\d"	
#.	Any character (except newline character)	"he..o"	
#^	Starts with     e.t.c

#Special Sequences
#A special sequence is a \ followed by one of the characters

#\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
#\b	Returns a match where the specified characters are at the beginning or at the end of a word
#the "r" in the beginning is making sure that the string is being treated as a "raw string")
#\d	Returns a match where the string contains digits (numbers from 0-9)
#\s	Returns a match where the string contains a white space character


#Sets
#A set is a set of characters inside a pair of square brackets [] with a special meaning:

#[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
#[a-n]	Returns a match for any lower case character, alphabetically between a and n	
#[^arn]	Returns a match for any character EXCEPT a, r, and n	
#[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present


#The findall() Function
#The findall() function returns a list containing all matches.

#Print a list of all matches:
import re
txt = "the rain in spain and it is painful"
x = re.findall("ai", txt)
print(x)

#Return an empty list if no match was found:
txt = "the rain in spain and it is painful"
x = re.findall("portugal", txt)
print(x)

#The search() Function
#The search() function searches the string for a match, and returns a Match object if there is a match.

#If there is more than one match, only the first occurrence of the match will be returned:

txt = "the rain in spain"
x = re.search("\s", txt)
print("the first white space is located in position:", x.start())

#If no matches are found, the value None is returned:
txt = "the rain in spain"
x = re.search("port", txt)
print(x)

#The split() Function
#The split() function returns a list where the string has been split at each match:
#Split at each white-space character:
 
txt = "the rain in spain is heavy"
x = re.split("\s", txt)
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter:
#Split the string only at the first occurrence:

txt = "the rain in spain is heavy"
x = re.split("\s", txt, 1)
print(x)


#The sub() Function
#The sub() function replaces the matches with the text of your choice:

#Replace every white-space character with the number 9:
txt = "The rain in spain is heavy"
x = re.sub("\s","9", txt)
print(x)

#You can control the number of replacements by specifying the count parameter:
txt = "The rain in spain is heavy"
x = re.sub("\s","9", txt, 2)
print(x)

#Match Object
#A Match Object is an object containing information about the search and the result.
#Do a search that will return a Match Object:
txt = "the rain in spain"
x = re.search("ai", txt)
print(x)

#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S":

txt = "the rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x)

#Print the string passed into the function:
txt = "the rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S":
txt = "the rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
str="hello"
print(type(str))

# type() function is used to check the type of the variable

#ord() function is used to get the unicode value of the character

print(ord("h"))

#chr() function is used to get the character of the unicode value

print(chr(128522))

# indexing 

print(str[0]) #h
print(str[1]) #e
print(str[2]) #l
print(str[3]) #l
print(str[4]) #o
# negative indexing means reverse counting -1 will be last char and so on.
print(str[-1]) #o
print(str[-2]) #l
print(str[-3]) #l
print(str[-4]) #e
print(str[-5]) #h

#slicing is used to get the substring
print(str[0:3]) #hel
print(str[1:4]) #ell
print(str[2:5]) #llo
print(str[0:5]) #hello
print(str[1:3:1]) #el

# slicing with negative indexing means we are slicing it in respect of reverse counting.

print(str[-1:-4:-1]) #oll
print(str[-5:-1:-1]) #  intresting this one
print(str[-1:-5:-1]) #olleh

# built in string functions
str1="hello guys, nice to meet you!!"

# len() - is used to get the length of the string.
print(len(str1)) #30

# replace() - is used to replace a substring with another substring.
print(str1.replace("guys", "friends")) #hello friends, nice to meet you!!

# strip() - is used to remove leading and trailing whitespaces.
print(str1.strip()) #hello guys, nice to meet you!!

# split() - is used to split the string into a list.
print(str1.split(" ")) #['hello', 'guys,', 'nice', 'to', 'meet', 'you!!']

# count() - is used to count the number of occurrences of a substring.
print(str1.count("o")) #3

# lower() - is used to convert the string to lowercase.
print(str1.lower()) #hello guys, nice to meet you!!

# upper() - is used to convert the string to uppercase.
print(str1.upper()) #HELLO GUYS, NICE TO MEET YOU!!

# title() - is used to convert the string to title case.
print(str1.title()) #Hello Guys, Nice To Meet You!!

# capitalize() - is used to capitalize the first letter of the string.
print(str1.capitalize()) #Hello guys, nice to meet you!!

# find() - is used to find the index of a substring.
print(str1.find("guys")) #6

# startswith() - is used to check if the string starts with a substring.
print(str1.startswith("hello")) #True

# endswith() - is used to check if the string ends with a substring.
print(str1.endswith("you!!")) #True

# isalpha() - is used to check if the string is alphabetic.
print(str1.isalpha()) #False

# isdigit() - is used to check if the string is numeric.
print(str1.isdigit()) #False

# isalnum() - is used to check if the string is alphanumeric.
print(str1.isalnum()) #False

# islower() - is used to check if the string is lowercase.
print(str1.islower()) #False

# isupper() - is used to check if the string is uppercase.
print(str1.isupper()) #False

# istitle() - is used to check if the string is title case.
print(str1.istitle()) #False

# iscapitalize() - is used to check if the string is capitalized.
print(str1.istitle()) #False



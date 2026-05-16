
# Type conversions are used to convert one data type to another.

# type conversion can be done in two ways: 
# 1. Implicit type conversion

a=12
b=a+10.3
print("b = ", b)

#here automatically int is converted to float

# 2. Explicit type conversion

# int() - is used to convert a string to an integer.
print(int("123")) #123

# float() - is used to convert a string to a float.
print(float("123")) #123.0

# str() - is used to convert a number to a string.
print(str(123)) #123

# bool() - is used to convert a number to a boolean.
print(bool(123)) #True

# list() - is used to convert a string to a list.
print(list("hello")) #['h', 'e', 'l', 'l', 'o']

# tuple() - is used to convert a string to a tuple.
print(tuple("hello")) #('h', 'e', 'l', 'l', 'o')

# set() - is used to convert a string to a set.
print(set("hello")) #{'h', 'e', 'l', 'o'}

# dict() - is used to convert a string to a dictionary.
print(dict("hello")) #{'h': 0, 'e': 1, 'l': 2, 'o': 4}
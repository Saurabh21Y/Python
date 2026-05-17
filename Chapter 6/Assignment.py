# there are eight types of assignment operators.

a = 10
b = 20.5
c = "Hello"
d = [1, 2]

# Assignment = : this is use to assign the right side value to left side variable.
print("assignment =")
x = 10
print(x)  # 10 Int
y = "Hello"
print(y)  # Hello String

# Add and Assign += : this is use to add right side value to left side variable and assign the result to left side variable.
# It works on datatypes like Int, float, string, list.
print("\nadd and assign +=")
x1 = a
x1 += 5
print(x1)  # 15 Int
x2 = b
x2 += 2.5
print(x2)  # 23.0 float
x3 = c
x3 += " World"
print(x3)  # Hello World String
x4 = d.copy()
x4 += [3, 4]
print(x4)  # [1, 2, 3, 4] List

# Subtract and Assign -= : this is use to subtract right side value from left side variable and assign the result to left side variable.
# It works on datatypes like Int, float.
print("\nsubtract and assign -=")
x1 = a
x1 -= 3
print(x1)  # 7 Int
x2 = b
x2 -= 0.5
print(x2)  # 20.0 float

# Multiply and Assign *= : this is use to multiply right side value with left side variable and assign the result to left side variable.
# It works on datatypes like Int, float, string, list.
print("\nmultiply and assign *=")
x1 = a
x1 *= 2
print(x1)  # 20 Int
x2 = b
x2 *= 2
print(x2)  # 41.0 float
x3 = c
x3 *= 2
print(x3)  # HelloHello String
x4 = d.copy()
x4 *= 2
print(x4)  # [1, 2, 1, 2] List

# Divide and Assign /= : this is use to divide left side variable by right side value and assign the result to left side variable.
# It works on datatypes like Int, float.
print("\ndivide and assign /=")
x1 = a
x1 /= 2
print(x1)  # 5.0 float
x2 = b
x2 /= 2
print(x2)  # 10.25 float

# Floor Divide and Assign //= : this is use to floor divide left side variable by right side value and assign the result to left side variable.
# It works on datatypes like Int, float.
print("\nfloor divide and assign //=")
x1 = a
x1 //= 3
print(x1)  # 3 Int
x2 = b
x2 //= 2
print(x2)  # 10.0 float

# Modulus and Assign %= : this is use to find the remainder and assign the result to left side variable.
# It works on datatypes like Int, float.
print("\nmodulus and assign %=")
x1 = a
x1 %= 3
print(x1)  # 1 Int
x2 = b
x2 %= 3
print(x2)  # 2.5 float

# Exponentiation and Assign **= : this is use to find the power and assign the result to left side variable.
# It works on datatypes like Int, float.
print("\nexponentiation and assign **=")
x1 = a
x1 **= 2
print(x1)  # 100 Int
x2 = b
x2 **= 2
print(x2)  # 420.25 float

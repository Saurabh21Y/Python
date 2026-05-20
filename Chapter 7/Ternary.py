# Ternary operator is a concise way to write if-else statements

# syntax
# value_if_true if condition else value_if_false

# EXAMPLE

age = int(input("Enter your age: "))
result = "Eligible" if age >= 18 else "Not Eligible"
print(result)

# EXAMPLE 2

num = int(input("Enter a number: "))
result = "Positive" if num > 0 else "Not Positive"
print(result)


# question: greatest of two number.

num1= Int(input("Enter a number 1: "))
num2= Int(input("Enter a number 2: "))

max = num1 if num1 > num2 else num2
print("The greater number is: ", max)


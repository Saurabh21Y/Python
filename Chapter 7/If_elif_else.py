# if elif else statement

# syntax

# if (condition):
#     statement1
#     statement2
# elif (condition):
#     statement3
#     statement4
# else:
#     statement5
#     statement6

# EXAMPLE

age = int(input("Enter your age: "))
if (age <= 18):
    print("You are a minor")
elif (age >= 18 and age <= 60):
    print("You are an adult")
else:
    print("You are a senior citizen")

# EXAMPLE 2

num = int(input("Enter a number: "))
if (num > 0):
    print("The number is positive")
elif (num < 0):
    print("The number is negative")
else:
    print("The number is zero")

"""
Question:

take the input of temperature in celsius
Below 0°C → "Freezing Cold"
0°C to 10°C → "Very Cold"
10°C to 20°C → "Cold"
20°C to 30°C → "Pleasant"
30°C to 40°C → "Hot"
Above 40°C → "Very Hot"
"""

temp = int(input("Enter the temperature in Celsius: "))
if (temp < 0):
    print("Freezing Cold")
elif (temp >= 0 and temp <= 10):
    print("Very Cold")
elif (temp >= 10 and temp <= 20):
    print("Cold")
elif (temp >= 20 and temp <= 30):
    print("Pleasant")
elif (temp >= 30 and temp <= 40):
    print("Hot")
else:
    print("Very Hot")

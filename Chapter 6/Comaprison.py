# there are six types of comparison operators.

a = 10
b = 20
c = 10.0
d = "Hello"
e = "World"

# Equal to == : this is use to check if left side value is equal to right side value.
# It returns a boolean result (True or False) and works on datatypes like Int, float, string, list.
print("equal to ==")
print(a == b)  # False bool
print(d == e)  # False bool

# Not Equal to != : this is use to check if left side value is not equal to right side value.
# It returns a boolean result (True or False) and works on datatypes like Int, float, string, list.
print("\nnot equal to !=")
print(a != b)  # True bool
print(d != e)  # True bool

# Greater than > : this is use to check if left side value is greater than right side value.
# It returns a boolean result (True or False) and works on datatypes like Int, float, string (ASCII comparison).
print("\ngreater than >")
print(a > b)  # False bool
print(b > a)  # True bool
print(d > e)  # False bool

# Less than < : this is use to check if left side value is less than right side value.
# It returns a boolean result (True or False) and works on datatypes like Int, float, string (ASCII comparison).
print("\nless than <")
print(a < b)  # True bool
print(b < a)  # False bool
print(d < e)  # True bool

# Greater than or equal to >= : this is use to check if left side value is greater than or equal to right side value.
# It returns a boolean result (True or False) and works on datatypes like Int, float, string (ASCII comparison).
print("\ngreater than or equal to >=")
print(a >= b)  # False bool
print(b >= a)  # True bool

# Less than or equal to <= : this is use to check if left side value is less than or equal to right side value.
# It returns a boolean result (True or False) and works on datatypes like Int, float, string (ASCII comparison).
print("\nless than or equal to <=")
print(a <= b)  # True bool
print(b <= a)  # False bool

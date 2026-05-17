# there are three types of logical operators in python.

# Let's set up some variables for our examples
condition_true = True
condition_false = False

x = 10
y = 5
z = 20

# Logical AND (and) : this is use to check if multiple conditions are True at the same time.
# RULE: It returns True ONLY IF BOTH the conditions are True. Otherwise, it returns False.
print("logical AND (and)")
print(condition_true and condition_true)    # True bool (Both are True)
print(condition_true and condition_false)   # False bool (One is False)

# Practical example with numbers
# Here (10 > 5) is True AND (20 > 10) is True, so final result is True
print((x > y) and (z > x))                  # True bool 
# Here (10 > 5) is True BUT (20 < 10) is False, so final result is False
print((x > y) and (z < x))                  # False bool 


# Logical OR (or) : this is use to check if at least one condition is True.
# RULE: It returns True IF AT LEAST ONE of the conditions is True. It only returns False if BOTH are False.
print("\nlogical OR (or)")
print(condition_true or condition_false)    # True bool (At least one is True)
print(condition_false or condition_false)   # False bool (Both are False)

# Practical example with numbers
# Here (10 > 5) is True, so it doesn't matter that (20 < 10) is False. Final result is True
print((x > y) or (z < x))                   # True bool 
# Here (10 < 5) is False AND (20 < 10) is False. Both are False, so final result is False
print((x < y) or (z < x))                   # False bool 


# Logical NOT (not) : this is use to reverse the boolean result of a condition.
# RULE: It returns True if the condition is False, and returns False if the condition is True.
print("\nlogical NOT (not)")
print(not condition_true)                   # False bool (Reverses True to False)
print(not condition_false)                  # True bool (Reverses False to True)

# Practical example with numbers
# (x > y) is True, but applying 'not' reverses it to False
print(not (x > y))                          # False bool
# (x < y) is False, but applying 'not' reverses it to True
print(not (x < y))                          # True bool

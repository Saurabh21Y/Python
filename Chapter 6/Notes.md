# Chapter 6: Python Operators

## What are Operators?
**Operators** are symbols that perform operations on variables and values. Python has several types of operators for different tasks like arithmetic, comparison, logical operations, and more. 

Let's explore each operator type one by one.

---

## 1. Arithmetic Operators
Arithmetic operators perform mathematical operations like addition, subtraction, multiplication, division, etc. There are **7 types** of arithmetic operators in Python:

| Operator | Name | Symbol |
| :--- | :--- | :---: |
| **Addition** | Adds two values | `+` |
| **Subtraction** | Subtracts one value from another | `-` |
| **Multiplication** | Multiplies two values | `*` |
| **Division** | Divides and returns a float | `/` |
| **Floor Division** | Divides and rounds down to the nearest integer | `//` |
| **Modulus** | Returns the remainder of a division | `%` |
| **Exponentiation**| Raises a number to the power of another | `**` |

### Example:
```python
a = 12 
b = 8

print(a + b)
# Output: 20
```
> 💡 **Note:** See the *Sheryians Coding School* video for a proper explanation of how `/` and `*` behave differently.

---

## 2. Assignment Operators
Assignment operators are used to assign values to variables. The most basic assignment operator is the simple `=`.

### Compound Assignment Operators
Python also provides **compound assignment operators** that combine arithmetic operations with assignment. Using compound assignment operators makes reassigning variables cleaner and more efficient.

*(Before using these, it is important to understand how variable reassignment works in Python. Watch the video carefully for this concept.)*

| Operator | Description | Equivalent To |
| :---: | :--- | :--- |
| `+=` | Add and assign | `x = x + 3` |
| `-=` | Subtract and assign | `x = x - 3` |
| `*=` | Multiply and assign | `x = x * 3` |
| `/=` | Divide and assign | `x = x / 3` |
| `//=` | Floor divide and assign | `x = x // 3` |
| `%=` | Modulus and assign | `x = x % 3` |
| `**=` | Exponentiation and assign | `x = x ** 3` |

> 💡 **Note:** See the *Sheryians Coding School* video for a proper explanation.

---

## 3. Comparison Operators
Comparison operators, also called **relational operators**, are used to compare two values. 
They will **always** provide a Boolean result, which is either `True` or `False`.

| Operator | Description |
| :---: | :--- |
| `==` | Equal to |
| `!=` | Not Equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

**Important Note on Strings:**
Comparison operators work perfectly with numbers, but you can use them with strings as well! When comparing strings, Python compares the **ASCII values** of the characters.

---

## 4. Logical Operators
Logical operators in Python are used to combine multiple conditions and return a Boolean result (`True` or `False`). There are **3 types** of logical operators:

*   **`and`** : Returns `True` if **both** conditions are True.
*   **`or`** : Returns `True` if **at least one** condition is True.
*   **`not`** : Reverses the boolean value (e.g., `not True` becomes `False`).

> ⚠️ **Important:** Watch the full video from *Sheryians Coding School* for a better understanding of logical operators.

---

## 📝 Trivial Questions (Exercise)
Predict the output of the following statements (`True` or `False`):

```python
# Question 1
print(126 > 130)

# Question 2
print((456 == 456) != (235 == 236))

# Question 3
print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)

# Question 4
print(True and bool(0))
```
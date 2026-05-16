# Chapter 3: Python Data Types 🐍

Data types are the classifications of data items. They represent the kind of value that determines what operations can be performed on that specific data. In Python, every value has a data type.

---

## 1. Numbers 🔢
Python supports integers, floating-point numbers, and complex numbers.

### A. Integers (`int`)
Whole numbers without a decimal point. They can be positive or negative.
- **Example:** `5`, `-10`, `1000`
```python
x = 10
print(type(x)) # <class 'int'>
```

### B. Floating Point (`float`)
Numbers that contain decimal points or fractions.
- **Example:** `3.14`, `-0.001`, `2.0`
```python
y = 10.5
print(type(y)) # <class 'float'>
```

### C. Complex Numbers (`complex`)
Numbers with a real and an imaginary part, written with a `j` as the imaginary part.
- **Example:** `3 + 5j`
```python
z = 2 + 3j
print(type(z)) # <class 'complex'>
```

---

## 2. Strings (`str`) 🧵
A string is a sequence of characters. In Python, anything typed inside quotes (single or double) is considered a string.
- Strings can store letters, numbers, symbols, and even spaces.
- **Quotes:** You can use single quotes (`'...'`) or double quotes (`"..."`).

```python
name = "Saurabh"
message = 'Hello Python!'
numbers_in_str = "12345"

print(type(name)) # <class 'str'>
```

---

## 3. Boolean (`bool`) ✅❌
The Boolean data type has only two possible values: `True` or `False`. It is often used to represent the truth value of an expression.
- **Note:** `T` and `F` must be capitalized.

```python
is_python_fun = True
is_raining = False

print(type(is_python_fun)) # <class 'bool'>
```

---

## 4. Sequence Types (Brief Overview) 📚
While we will cover these in detail later, Python also has:
- **Lists:** Ordered and changeable collection. `[1, 2, "three"]`
- **Tuples:** Ordered and unchangeable collection. `(1, 2, 3)`
- **Dictionaries:** Unordered, changeable, and indexed collection of key-value pairs. `{"name": "Saurabh", "age": 20}`

---
*Keep learning and keep coding!* 🚀
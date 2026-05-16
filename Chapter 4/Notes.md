# 🐍 Python String Data Type

## 1. Introduction & Definition

### What is a String?
A **String** is a sequence of characters used to represent text data. In Python, strings are **immutable**, meaning once a string is created, its individual characters cannot be changed.

### How Strings Work (Unicode)
Strings in Python are stored as **Unicode code points**. This allows Python to represent characters from almost every language in the world, as well as emojis.
- **Memory Consumption**: Strings generally take more memory than types like `int` or `float` because every character is stored with its own unique Unicode value.
- **`ord()`**: Returns the Unicode code point of a character.
- **`chr()`**: Returns the character representing a specific Unicode code point.

### Examples
```python
# Creating strings
name = "Antigravity"  # Double quotes
message = 'Hello World'  # Single quotes
multiline = """This is a
multiline string."""  # Triple quotes

# Unicode examples
print(ord("A"))       # Output: 65
print(chr(128522))    # Output: 😊
```

---

## 2. String Indexing & Slicing

### Indexing
Access individual characters using their position.
- **Positive Indexing**: Starts from `0` (left to right).
- **Negative Indexing**: Starts from `-1` (right to left).

```python
s = "Python"
print(s[0])   # 'P'
print(s[-1])  # 'n' (last character)
```

### Slicing
Extract a portion of a string using the syntax `[start : stop : step]`.
- `start`: Inclusive index.
- `stop`: Exclusive index (slices up to `stop - 1`).
- `step`: The increment (default is 1).

```python
text = "Hello World"
print(text[0:5])    # 'Hello'
print(text[6:])     # 'World' (to the end)
print(text[::-1])    # 'dlroW olleH' (reverses the string)
```

---

## 3. String Type Conversion

### Implicit Conversion
Python automatically converts one data type to another when possible (e.g., during division).
```python
a = 12
print(a / 2) # Output: 6.0 (int converted to float)
```

### Explicit Conversion (Casting)
Using built-in functions to manually convert a value to a string.
- **`str()`**: Converts any data type to a string.

```python
num = 100
num_str = str(num)
print(type(num_str)) # <class 'str'>
```

---

## 4. String Functions

Below are the common built-in string methods. Each includes a documentation summary followed by an example.

### `len()`
> **Description:** Returns the total number of characters in the string.
```python
s = "Hello"
print(len(s))  # Output: 5
```

### `upper()` & `lower()`
> **Description:** Converts all characters in the string to uppercase or lowercase respectively.
```python
s = "Python"
print(s.upper()) # "PYTHON"
print(s.lower()) # "python"
```

### `strip()`
> **Description:** Removes any leading and trailing whitespace (or specific characters).
```python
s = "   clean me   "
print(s.strip()) # "clean me"
```

### `split()`
> **Description:** Splits the string into a list based on a separator (default is whitespace).
```python
s = "apple,banana,cherry"
print(s.split(",")) # ["apple", "banana", "cherry"]
```

### `join()`
> **Description:** Takes all items in an iterable and joins them into one string using a separator.
```python
words = ["Python", "is", "fun"]
print(" ".join(words)) # "Python is fun"
```

### `replace()`
> **Description:** Replaces a specified phrase with another specified phrase.
```python
s = "I like apples"
print(s.replace("apples", "oranges")) # "I like oranges"
```

### `find()`
> **Description:** Searches the string for a specified value and returns the position of where it was found (-1 if not found).
```python
s = "Hello"
print(s.find("e")) # 1
```

### `count()`
> **Description:** Returns the number of times a specified value occurs in a string.
```python
s = "banana"
print(s.count("a")) # 3
```

---

## 5. Basic DSA Question Types

In Data Structures and Algorithms (DSA), string problems are very common. Here are the most frequent types:

### I. String Reversal
**Problem:** Reverse a given string without using built-in reverse functions.
*   **Key Concept:** Slicing `[::-1]` or two-pointer approach.

### II. Palindrome Check
**Problem:** Check if a string reads the same forwards and backwards.
*   **Key Concept:** `s == s[::-1]`.

### III. Anagram Detection
**Problem:** Check if two strings contain the same characters in different orders (e.g., "listen" and "silent").
*   **Key Concept:** Sorting both strings and comparing or using a frequency hash map.

### IV. Character Frequency
**Problem:** Count the occurrence of each character in a string.
*   **Key Concept:** Using a dictionary or `collections.Counter`.

### V. Validating Substrings
**Problem:** Find if a pattern exists within a string.
*   **Key Concept:** Sliding window or KMP algorithm (for advanced).

### VI. String Compression
**Problem:** Compress "aaabbcc" to "a3b2c2".
*   **Key Concept:** Iterating through the string and counting consecutive characters.

---

## 6. Truthy & Falsy Values in Strings
In Python, any non-empty string is considered **True** in a boolean context.
- **Falsy String**: `""` (Empty string)
- **Truthy String**: `" "`, `"0"`, `"False"` (Any character makes it True)

```python
if "":
    print("This won't print")
if " ":
    print("Whitespace is Truthy!")
```
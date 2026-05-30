# Chapter 10.2: Tuples in Python

> **Topic Index:** 10.2 | **Prerequisites:** Introduction to Data Structures & Chapter 10.1 (Lists)  
> **Original Concept Attribution:** Sheryians Coding School (Enhanced for DSA & Professional Development)

---

## 📌 Introduction to Tuples

A **Tuple** is another key built-in data structure in Python. Much like a list, it is an ordered collection of elements. However, the defining difference is that **tuples are immutable**. Once a tuple is created, its contents cannot be modified, added to, or removed.

Think of a tuple as a "read-only list."

---

## ⚡ The "Powers" (Characteristics) of a Tuple

To understand tuples, we must learn their four core characteristics:

1. **Immutable (Unchangeable):** Once created, you cannot change the values, append new items, or delete elements. This is similar to Python strings.
2. **Ordered Sequence:** Tuples maintain the exact insertion order of their elements. Each element can be accessed using zero-based indexing (or negative indexing).
3. **Allows Duplicates:** There are no restrictions on duplicate elements. A tuple can store the same value multiple times.
4. **Heterogeneous Nature:** A tuple can store different types of data structures and data types simultaneously (e.g., integers, floats, strings, booleans, lists, or even other tuples).

### 💻 Code Demonstration of Tuple Characteristics
```python
# 1. Creation and Heterogeneous nature
demo_tuple = (10, "Python", 3.14, True, 10)  # Contains duplicate '10'

# 2. Ordered access
print("First Element:", demo_tuple[0])   # Output: 10
print("Last Element:", demo_tuple[-1])    # Output: 10

# 3. Immutability check
try:
    demo_tuple[1] = "DSA"  # Trying to modify elements
except TypeError as e:
    print(f"Error: {e}")   # Output: Error: 'tuple' object does not support item assignment
```

---

## 📝 Tuple Basics: Creation, Indexing & Slicing

### 1️⃣ Creating a Tuple
Tuples are defined by placing elements inside parentheses `()` separated by commas. Parentheses are optional but highly recommended for readability.

```python
# Empty tuple
empty_tuple = ()

# Tuple with multiple elements
fruits = ("Apple", "Banana", "Cherry")

# Parentheses are optional (Tuple Packing)
colors = "Red", "Green", "Blue" 
print(type(colors))  # <class 'tuple'>
```

> [!WARNING]  
> **The Single-Element Tuple Gotcha**  
> Defining a tuple with only one element requires a trailing comma. Without the comma, Python treats it as a standard data type wrapped in parentheses.
> ```python
> not_a_tuple = (42)   # Evaluates to the integer 42
> print(type(not_a_tuple))  # <class 'int'>
> 
> is_a_tuple = (42,)   # A valid tuple with 1 element
> print(type(is_a_tuple))   # <class 'tuple'>
> ```

### 2️⃣ Indexing & Slicing
Tuple indexing and slicing work exactly like strings and lists:
* **Positive Indexing:** Starts from `0` (left to right).
* **Negative Indexing:** Starts from `-1` (right to left).

```python
numbers = (10, 20, 30, 40, 50)

# Slicing syntax: tuple[start:stop:step]
print(numbers[1:4])   # Output: (20, 30, 40)
print(numbers[::-1])  # Output: (50, 40, 30, 20, 10) (Reverses the tuple)
```

---

## 🔄 Tuple Traversing

Traversing a tuple means visiting each element one by one. The traversal patterns are identical to lists.

### 1. Direct Iteration (By Value)
```python
names = ("Alice", "Bob", "Charlie")
for name in names:
    print(name)
```

### 2. Index-Based Iteration
```python
for idx in range(len(names)):
    print(f"Index {idx}: {names[idx]}")
```

### 💡 Pro-Tip: Using `enumerate()`
Best practice to access both index and value at the same time:
```python
for idx, name in enumerate(names):
    print(f"Index {idx} holds value '{name}'")
```

---

## 🛠️ Tuple Methods

Because tuples are immutable, they do not have methods like `.append()`, `.extend()`, `.pop()`, or `.sort()`. 

There are **only two** built-in methods available for tuples:

1. **`.count(value)`**: Returns the number of times a specified value occurs in the tuple.
2. **`.index(value)`**: Searches the tuple for a specified value and returns the index of its first occurrence. Raises a `ValueError` if the value is not found.

### 💻 Code Demonstration of Tuple Methods
```python
data = (10, 20, 30, 20, 40, 20)

# 1. count()
print("Count of 20:", data.count(20))  # Output: 3
print("Count of 50:", data.count(50))  # Output: 0

# 2. index()
print("Index of 30:", data.index(30))  # Output: 2
# print(data.index(50))  # Raises ValueError: tuple.index(x): x not in tuple
```

---

## 🧠 Why Use Tuples Instead of Lists?

If lists can do everything tuples do and are mutable, why does Python have tuples?

1. **Performance & Speed:** Tuples are stored in a single memory block, making them faster to instantiate and iterate over than lists.
2. **Data Integrity (Write-Protection):** If you have data that should never be modified (e.g., months of the year, days of the week, GPS coordinates), using a tuple protects it from accidental changes.
3. **Dictionary Keys:** Because tuples are immutable (and therefore hashable, provided they contain hashable elements), they can be used as keys in a dictionary. Lists cannot be used as dictionary keys.
4. **Tuple Unpacking:** Tuples allow elegant multiple assignment syntaxes:
   ```python
   # Unpacking coordinates
   point = (4, 5)
   x, y = point  # x = 4, y = 5
   
   # Variable Swapping
   a = 10
   b = 20
   a, b = b, a   # Behind the scenes, Python creates a temporary tuple (b, a) and unpacks it
   ```

---

## 📝 Practice Labs & Solutions

Here are standard problems involving tuples implemented with professional type hinting, clean structure, and documentation.

### Q1. Swap Two Variables Using Tuples
*Write a function that swaps two variables without using an explicit temporary third variable, explaining how tuples facilitate this.*

```python
from typing import Any

def swap_values(a: Any, b: Any) -> tuple[Any, Any]:
    """
    Swaps two values using tuple unpacking.
    
    Behind the scenes, (b, a) creates a tuple. 
    Then, the values are unpacked back into variables a and b.
    """
    a, b = b, a
    return a, b

# Test Run
x, y = "Hello", "World"
x, y = swap_values(x, y)
print(f"x: {x}, y: {y}")  # Output: x: World, y: Hello
```

---

### Q2. Sum of Numeric Elements in a Heterogeneous Tuple
*Write a function to sum all numbers (integers and floats) in a heterogeneous tuple, ignoring other data types.*

```python
def sum_numeric_elements(tpl: tuple) -> float:
    """
    Traverses a heterogeneous tuple and sums only the numeric values.
    """
    total = 0.0
    for item in tpl:
        if isinstance(item, (int, float)) and not isinstance(item, bool):  # bool is a subclass of int in Python!
            total += item
    return total

# Test Run
mix_tuple = (10, "Python", 3.5, True, 20, [1, 2], (5, 6))
print("Sum of numbers:", sum_numeric_elements(mix_tuple))  # Output: 33.5 (10 + 3.5 + 20)
```

---

### Q3. Find Duplicate Elements in a Tuple
*Write a function that returns a set of elements that appear more than once in a given tuple.*

```python
from typing import Any

def find_duplicates(tpl: tuple[Any, ...]) -> set[Any]:
    """
    Finds and returns duplicate elements in a tuple.
    """
    seen = set()
    duplicates = set()
    for item in tpl:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

# Test Run
numbers_tuple = (1, 2, 3, 2, 4, 5, 1, 6, 1)
print("Duplicates:", find_duplicates(numbers_tuple))  # Output: {1, 2}
```

---

### Q4. Unpack a Nested Tuple
*Write a function to access the element "Python" inside the nested structure `data = (10, 20, ("Inner", "Python", 30), 40)` using indexing, and print it.*

```python
def extract_nested_element(nested_tpl: tuple) -> str:
    """
    Extracts the element "Python" from the nested tuple structure.
    """
    # Structure:
    # Index 0: 10
    # Index 1: 20
    # Index 2: ("Inner", "Python", 30) -> Index 1 inside this is "Python"
    # Index 3: 40
    return nested_tpl[2][1]

# Test Run
data = (10, 20, ("Inner", "Python", 30), 40)
print("Extracted Element:", extract_nested_element(data))  # Output: Python
```
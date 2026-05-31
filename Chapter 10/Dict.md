# Chapter 10.4: Dictionaries in Python

> **Topic Index:** 10.4 | **Prerequisites:** Introduction to Data Structures & Chapter 10.1 (Lists)  
> **Original Concept Attribution:** Sheryians Coding School (Enhanced for DSA & Professional Development)

---

## 📌 Introduction to Dictionaries

A **Dictionary** (often called a `dict` in Python) is one of the most powerful and flexible built-in data structures. Unlike lists and tuples, which are ordered sequences indexed by a range of numbers, dictionaries are indexed by **keys**, which must be unique and hashable (immutable). 

Think of a dictionary as an associative container or a hash map. It stores data in **key-value pairs**, allowing you to look up, add, update, or remove data with extreme speed using custom labels instead of numerical positions.

---

## ⚡ The "Powers" (Characteristics) of a Dictionary

To master dictionaries, you need to understand their four core characteristics:

1. **Mutable (Changeable):** The dictionary container is mutable. You can add new key-value pairs, update existing values, or delete keys. However, the **keys themselves must be immutable (hashable)**.
2. **Key Uniqueness & Value Duplication:** 
   - **Keys must be unique:** A dictionary cannot contain duplicate keys. If you assign a value to an existing key, the new value will overwrite the old one.
   - **Values can be duplicates:** Multiple keys can point to the same value without any issue.
3. **Insertion Ordered (Python 3.7+):** Dictionaries preserve the order in which key-value pairs are inserted. If you iterate through a dictionary, the elements will appear in the order you added them.
4. **Heterogeneous Nature:**
   - **Keys:** Can be of any hashable (immutable) type (e.g., `str`, `int`, `float`, `bool`, `tuple` containing only hashable elements).
   - **Values:** Can be of **any** data type, mutable or immutable, including lists, other dictionaries, sets, custom objects, or functions.

### 💻 Code Demonstration of Dictionary Characteristics
```python
# 1. Creation and Heterogeneous Keys/Values
student_records = {
    "name": "Arjun",
    "age": 21,
    "skills": ["Python", "SQL"],  # List as value (mutable is fine)
    (1, 2): "Coordinate Point",   # Tuple as key (immutable is fine)
}
print("Dictionary:", student_records)

# 2. Key Uniqueness (Overwriting old values)
grades = {"Physics": 85, "Math": 90, "Physics": 95}
print("Unique keys check:", grades)  # Output: {'Physics': 95, 'Math': 90}

# 3. Invalid mutable key check
try:
    invalid_dict = {["list_key"]: "value"}  # Attempting to use a list as a key
except TypeError as e:
    print(f"Error: {e}")  # Output: unhashable type: 'list'
```

---

## 🧠 Behind the Scenes: Hash Maps in Python

Under the hood, Python dictionaries are implemented using highly optimized **Hash Tables**:

* **O(1) Operations:** Lookup, insertion, and deletion operations run in **constant average time ($O(1)$)**, making dictionaries incredibly fast for large datasets.
* **Hashability Requirement for Keys:** To locate a key-value pair instantly, Python computes a hash of the key. Since mutable objects (like lists or dicts) can change their values, their hash would change, which would lose their location in the hash table. Thus, only immutable types are hashable and allowed as keys.

---

## 📝 Dictionary Syntax & CRUD Operations

The keys in a dictionary behave like custom indexes. We can perform all standard CRUD (Create, Read, Update, Delete) operations. Note that we can modify the **values**, but we cannot mutate the **keys** themselves once created (you must delete the key and insert the new key-value pair).

### 1️⃣ Create (Initialization)
```python
# Empty dictionary
empty_dict = {}         # Recommended
empty_dict_alt = dict()  # Using constructor

# Pre-populated dictionary
user = {
    "id": 101,
    "username": "coder_xyz",
    "is_active": True
}
```

### 2️⃣ Read (Accessing Values)
```python
# Method A: Bracket Notation (Raises KeyError if key not found)
try:
    print(user["username"])
    print(user["email"])  # Key does not exist
except KeyError as e:
    print(f"KeyError: Key {e} not found")

# Method B: .get() Method (Recommended - returns None or default value if key not found)
print(user.get("username"))
print(user.get("email"))           # Output: None (No error raised!)
print(user.get("email", "N/A"))    # Output: N/A (Custom default value)
```

### 3️⃣ Update & Create (Modifying/Adding Pairs)
```python
# Modifying an existing key-value pair
user["is_active"] = False

# Adding a new key-value pair
user["email"] = "coder@example.com"

print(user)
```

### 4️⃣ Delete (Removing Pairs)
```python
# Method A: del statement (Raises KeyError if key not found)
del user["is_active"]

# Method B: .pop() Method (Removes key and returns its value; accepts default fallback)
email = user.pop("email", "Not Found")
print(f"Popped Email: {email}")

# Method C: .popitem() (Removes and returns the last inserted key-value pair as a tuple)
last_pair = user.popitem()
print(f"Popped Last Pair: {last_pair}")

# Method D: .clear() (Empties the dictionary completely)
user.clear()
print("After clear:", user)  # Output: {}
```

---

## 🔄 Dictionary Traversing (Iteration)

You can iterate through a dictionary in several ways. By default, iterating directly over a dictionary yields its **keys**.

```python
inventory = {"Apples": 50, "Bananas": 30, "Cherries": 75}

# 1. Default Loop: Iterates over keys
print("Keys (default loop):")
for item in inventory:
    print(f"Key: {item} | Value: {inventory[item]}")

# 2. Explicit Key Iteration (.keys())
print("\nExplicit Keys:")
for key in inventory.keys():
    print(key)

# 3. Explicit Value Iteration (.values())
print("\nExplicit Values:")
for value in inventory.values():
    print(value)

# 4. Key-Value Pair Iteration (.items() - Recommended)
print("\nKey-Value Pairs:")
for key, value in inventory.items():
    print(f"{key} -> {value}")
```

---

## 🛠️ Essential Dictionary Methods

Python provides a set of built-in methods to perform operations efficiently. 

> [!TIP]
> You can run `help(dict)` in the Python interactive shell to view a comprehensive list of all dictionary methods and documentation.

| Method | Description | Example |
| :--- | :--- | :--- |
| `.get(key, default)` | Returns the value of key. If key doesn't exist, returns `default` (or `None`). | `d.get("name", "Guest")` |
| `.keys()` | Returns a dynamic view object of all dictionary keys. | `d.keys()` |
| `.values()` | Returns a dynamic view object of all dictionary values. | `d.values()` |
| `.items()` | Returns a dynamic view object of all key-value tuples. | `d.items()` |
| `.update(other_dict)` | Updates the dictionary with key-value pairs from another dictionary or iterable. | `d.update({"age": 22})` |
| `.setdefault(key, default)`| Returns the value if key is present; otherwise inserts key with `default` and returns it. | `d.setdefault("country", "India")` |
| `.fromkeys(seq, value)` | Class method that creates a new dictionary with keys from sequence and values set to `value`. | `dict.fromkeys(["a", "b"], 0)` |
| `.pop(key, default)` | Removes and returns the value of the specified key, or `default` if key doesn't exist. | `d.pop("age", None)` |
| `.popitem()` | Removes and returns the last inserted `(key, value)` pair. | `d.popitem()` |
| `.clear()` | Removes all elements from the dictionary. | `d.clear()` |

---

## 📝 Practice Labs & Solutions

Here are standard interview and practical programming problems involving dictionaries, implemented with professional type hinting, docstrings, and clean explanations.

### Q1. Merge Two Python Dictionaries
*Write a function that merges two dictionaries. If there are overlapping keys, the values of the second dictionary should overwrite those of the first. Provide both the classic method and the modern Python 3.9+ method.*

```python
from typing import Any

def merge_dictionaries_classic(dict1: dict[Any, Any], dict2: dict[Any, Any]) -> dict[Any, Any]:
    """
    Merges two dictionaries using the .update() method.
    Returns a new dictionary without mutating the inputs.
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def merge_dictionaries_modern(dict1: dict[Any, Any], dict2: dict[Any, Any]) -> dict[Any, Any]:
    """
    Merges two dictionaries using the Union operator (|) introduced in Python 3.9.
    """
    return dict1 | dict2

# Test Run
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 4}

print("Merged (Classic):", merge_dictionaries_classic(d1, d2))  # Output: {'a': 1, 'b': 99, 'c': 4}
print("Merged (Modern):", merge_dictionaries_modern(d1, d2))   # Output: {'a': 1, 'b': 99, 'c': 4}
```

---

### Q2. Sum All Values in a Dictionary
*Write a function that calculates the sum of all numerical values in a dictionary.*

```python
from typing import Any

def sum_dict_values(data: dict[Any, float | int]) -> float | int:
    """
    Sums all numeric values stored in a dictionary.
    Handles empty dictionaries by returning 0.
    """
    return sum(data.values())

# Test Run
salaries = {"Alice": 5000, "Bob": 6000, "Charlie": 4500}
print("Total Salaries:", sum_dict_values(salaries))  # Output: 15500
print("Empty sum:", sum_dict_values({}))             # Output: 0
```

---

### Q3. Count Frequency of Elements (Frequency Map)
*Write a function that accepts an iterable (like a list or a string) and returns a frequency dictionary containing counts of each unique element.*

```python
from typing import Iterable, Hashable

def calculate_frequencies(elements: Iterable[Hashable]) -> dict[Hashable, int]:
    """
    Calculates the frequency of each element in an iterable.
    Returns a dictionary mapping elements to their occurrence count.
    """
    frequency_map = {}
    for element in elements:
        # If element is in map, increment; else initialize to 0 and add 1
        frequency_map[element] = frequency_map.get(element, 0) + 1
    return frequency_map

# Alternative: Using Python's built-in collections module
# from collections import Counter
# print(Counter("abracadabra"))

# Test Run
word = "mississippi"
print("Frequencies:", calculate_frequencies(word))
# Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

---

### Q4. Combine Dictionaries by Adding Values for Common Keys
*Write a function that merges two dictionaries. If a key is present in both, their numeric values should be summed up. If a key is exclusive to one dictionary, it should be kept as-is.*

```python
from typing import Any

def combine_dict_sums(dict1: dict[Any, float | int], dict2: dict[Any, float | int]) -> dict[Any, float | int]:
    """
    Combines two dictionaries by adding values for common keys.
    """
    combined = dict1.copy()
    for key, value in dict2.items():
        combined[key] = combined.get(key, 0) + value
    return combined

# Test Run
shop1 = {"Apples": 10, "Bananas": 20, "Oranges": 15}
shop2 = {"Bananas": 15, "Oranges": 10, "Grapes": 30}

print("Combined Inventory:", combine_dict_sums(shop1, shop2))
# Output: {'Apples': 10, 'Bananas': 35, 'Oranges': 25, 'Grapes': 30}
```
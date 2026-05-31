# Chapter 10.3: Sets in Python

> **Topic Index:** 10.3 | **Prerequisites:** Introduction to Data Structures & Chapter 10.1 (Lists)  
> **Original Concept Attribution:** Sheryians Coding School (Enhanced for DSA & Professional Development)

---

## 📌 Introduction to Sets

A **Set** is a fundamental built-in data structure in Python. Unlike lists and tuples, which are ordered sequences of elements, a set is an **unordered collection of unique elements**. 

Think of a set as a container where the order of items does not matter, but uniqueness does. It is modeled directly after mathematical set theory.

---

## ⚡ The "Powers" (Characteristics) of a Set

To understand sets, we must learn their four core characteristics:

1. **Mutable (Changeable):** The set itself is mutable. You can add new elements, remove existing elements, or empty the set. However, the individual elements stored inside a set **must be immutable** (hashable).
2. **Unordered:** Sets do not keep track of the insertion order of elements. Because there is no defined order, sets do not support indexing or slicing.
3. **No Duplicates (Strict Uniqueness):** A set cannot store duplicate values. If you try to add a duplicate element, Python will automatically ignore it.
4. **Semi-Heterogeneous Nature:** A set can store values of different data types (e.g., integers, floats, strings, booleans, and tuples) simultaneously. However, you **cannot** store mutable data structures (like lists, dictionaries, or other sets) inside a set.

### 💻 Code Demonstration of Set Characteristics
```python
# 1. Creation and Heterogeneous nature
demo_set = {10, "Python", 3.14, (1, 2)}
print("Set elements:", demo_set)  # Order is arbitrary

# 2. No duplicates allowed
duplicates_set = {10, 20, 10, 30, 20}
print("Unique elements only:", duplicates_set)  # Output: {10, 20, 30}

# 3. Unordered / No indexing check
try:
    print(demo_set[0])  # Trying to access via index
except TypeError as e:
    print(f"Error: {e}")  # Output: 'set' object is not subscriptable
```

---

## 🧠 How Sets Store Values: Hashing in Python

To understand why sets are unordered and require immutable elements, we look under the hood at how Python implements them:

* **Hashing Function:** Each element added to a set is passed through Python's built-in `hash()` function to compute a unique integer hash value.
* **Hash-Based Indexing:** This hash value is used as an index to store the element in a hash table in memory. This allows for extremely fast **O(1) average time complexity** for element lookup, addition, and removal.
* **Unordered Nature:** Because elements are stored in memory locations determined by their hash values rather than their insertion sequence, sets do not maintain order.
* **Hashability (Immutability):** For hashing to work, the value of an object must remain constant throughout its lifetime. 
  * **Hashable (Allowed):** Immutable types (strings, numbers, booleans, tuples) have a fixed hash value.
  * **Unhashable (Forbidden):** Mutable types (lists, dictionaries, sets) can be modified, which would alter their hash values and corrupt the hash table. Thus, Python raises a `TypeError` if you try to add them to a set.

```python
# Valid: Tuple inside a set (since tuples are immutable)
valid_set = {(1, 2, 3), "Hello"}

# Invalid: List inside a set (since lists are mutable)
try:
    invalid_set = {[1, 2, 3], "Hello"}
except TypeError as e:
    print(f"Error: {e}")  # Output: unhashable type: 'list'
```

---

## 📝 Set Basics: Creation & The Empty Set Gotcha

### 1️⃣ Creating a Set
Sets are defined by placing elements inside curly braces `{}` separated by commas.

```python
fruits = {"Apple", "Banana", "Cherry"}
print(type(fruits))  # <class 'set'>
```

> [!WARNING]  
> **The Empty Set Gotcha**  
> An empty set **cannot** be created using empty curly braces `{}` because Python reserves `{}` to initialize an empty dictionary. To create an empty set, you must use the `set()` constructor.
> ```python
> empty_dict = {}
> print(type(empty_dict))  # <class 'dict'>
> 
> empty_set = set()
> print(type(empty_set))   # <class 'set'>
> ```

---

## 🔄 Set Traversing

Since sets are unordered and do not support index-based lookups, you cannot use a `range(len(my_set))` loop to iterate through them. You must iterate through them **directly by value**.

```python
colors = {"Red", "Green", "Blue"}

# Direct Iteration (By Value)
for color in colors:
    print(color)
```

> [!NOTE]  
> The order of elements printed during iteration is arbitrary and may change across different script executions.

---

## 🛠️ Set Methods

Because sets do not have indexing, you cannot modify elements in-place using bracket assignment (e.g., `s[0] = 10` is invalid). Instead, Python provides built-in methods to modify sets.

### 1️⃣ Adding Elements
* **`.add(item)`**: Adds a single element to the set. If the element is already present, it has no effect.
* **`.update(iterable)`**: Adds multiple elements from an iterable (like a list, tuple, string, or another set).

```python
languages = {"Python", "JavaScript"}

# Add a single element
languages.add("Go")

# Add multiple elements
languages.update(["Rust", "C++", "Python"])  # "Python" is a duplicate and is ignored
print(languages)  # Output: {'Python', 'JavaScript', 'Go', 'Rust', 'C++'}
```

### 2️⃣ Removing Elements
* **`.remove(item)`**: Removes the specified element. **Raises a `KeyError`** if the element is not found.
* **`.discard(item)`**: Removes the specified element. **Does not raise an error** if the element is missing.
* **`.pop()`**: Removes and returns an **arbitrary** (random) element. Raises a `KeyError` if the set is empty.
* **`.clear()`**: Removes all elements, leaving the set empty.

```python
numbers = {1, 2, 3, 4, 5}

# remove() vs discard()
numbers.remove(3)     # Successfully removes 3
numbers.discard(10)   # Does nothing, no error raised

try:
    numbers.remove(10)  # Raises KeyError
except KeyError as e:
    print(f"KeyError: {e}")

# pop() removes an arbitrary element
popped_val = numbers.pop()
print(f"Removed: {popped_val}, Remaining: {numbers}")

# clear() empties the set
numbers.clear()
print(numbers)  # Output: set()
```

---

## 🧮 Mathematical Set Operations

One of the main strengths of sets in Python is their support for standard mathematical operations. These operations can be performed using either **methods** or **operators**.

| Operation | Method Syntax | Operator Syntax | Description |
| :--- | :--- | :--- | :--- |
| **Union** | `A.union(B)` | `A \| B` | Elements present in either set A or set B. |
| **Intersection** | `A.intersection(B)` | `A & B` | Elements present in both set A and set B. |
| **Difference** | `A.difference(B)` | `A - B` | Elements present in set A but not in set B. |
| **Symmetric Difference** | `A.symmetric_difference(B)` | `A ^ B` | Elements present in either set A or set B, but not both. |

### 💻 Code Demonstration of Set Operations
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 1. Union (|)
print("Union:", set_a | set_b)  # Output: {1, 2, 3, 4, 5, 6}

# 2. Intersection (&)
print("Intersection:", set_a & set_b)  # Output: {3, 4}

# 3. Difference (-)
print("Difference (A - B):", set_a - set_b)  # Output: {1, 2}
print("Difference (B - A):", set_b - set_a)  # Output: {5, 6}

# 4. Symmetric Difference (^)
print("Symmetric Difference:", set_a ^ set_b)  # Output: {1, 2, 5, 6}
```

### 🔍 Relationship Checks
* **`A.issubset(B)` (or `A <= B`)**: Returns `True` if all elements of set A are in set B.
* **`A.issuperset(B)` (or `A >= B`)**: Returns `True` if set A contains all elements of set B.
* **`A.isdisjoint(B)`**: Returns `True` if set A and set B have no common elements.

```python
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))     # True
print(y.issuperset(x))   # True
print(x.isdisjoint(y))   # False (they share elements 1 and 2)
```

---

> [!NOTE]  
> **Frequency of Use in Python**  
> While sets are not used as frequently as lists or dictionaries in everyday Python scripting, they are indispensable when dealing with duplicate removal, checking membership efficiently (lookups are $O(1)$ compared to $O(N)$ for lists), and performing mathematical set operations.

---

## 📝 Practice Labs & Solutions

Here are standard set-based interview and DSA problems, implemented with professional type hinting, clean structure, and documentation.

### Q1. Remove Duplicates from a List while Preserving Order
*Write a function that accepts a list of integers and returns a list containing only unique elements, maintaining the original order of their first occurrence.*

```python
from typing import Any

def remove_duplicates_preserve_order(items: list[Any]) -> list[Any]:
    """
    Removes duplicate elements from a list while preserving their original order.
    Uses a set for O(1) membership testing.
    """
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

# Test Run
numbers = [4, 5, 2, 4, 1, 2, 5, 9]
print("Unique list:", remove_duplicates_preserve_order(numbers))  # Output: [4, 5, 2, 1, 9]
```

---

### Q2. Find Elements in First List but Not in Second
*Write a function that takes two lists of integers and returns a set containing all elements that are present in the first list but not in the second list.*

```python
def find_exclusive_elements(list1: list[int], list2: list[int]) -> set[int]:
    """
    Finds elements in list1 that are not present in list2 using set difference.
    Time Complexity: O(N + M) where N and M are the sizes of the lists.
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1 - set2

# Test Run
l1 = [1, 2, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
print("Exclusive to l1:", find_exclusive_elements(l1, l2))  # Output: {1, 2}
```

---

### Q3. Subset Verification Without Built-in Methods
*Write a function to check if set `A` is a subset of set `B` without using the built-in `.issubset()` method or the `<=` operator.*

```python
from typing import Any

def is_custom_subset(set_a: set[Any], set_b: set[Any]) -> bool:
    """
    Verifies if set_a is a subset of set_b by manually checking element membership.
    """
    for element in set_a:
        if element not in set_b:
            return False
    return True

# Test Run
A = {1, 3, 5}
B = {1, 2, 3, 4, 5}
C = {1, 3, 6}

print("Is A subset of B?", is_custom_subset(A, B))  # Output: True
print("Is C subset of B?", is_custom_subset(C, B))  # Output: False
```

---

### Q4. Word Uniqueness Counter
*Write a function that accepts a sentence (string), cleans it of basic punctuation, and returns the number of unique words in a case-insensitive manner.*

```python
import string

def count_unique_words(sentence: str) -> int:
    """
    Cleans a sentence by removing punctuation and returns the count of unique words.
    """
    # Remove punctuation using translation table
    clean_sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    
    # Split into words and convert to lowercase
    words = clean_sentence.lower().split()
    
    # Convert to set to keep only unique words
    unique_words = set(words)
    
    return len(unique_words)

# Test Run
text = "Python is amazing, and python is fun! Isn't python fun?"
print("Count of unique words:", count_unique_words(text))  
# Output: 6
# Unique words: {'and', 'amazing', 'fun', 'is', 'isnt', 'python'}
```
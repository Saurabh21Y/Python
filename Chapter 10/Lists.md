# Chapter 10.1: Lists in Python

> **Topic Index:** 10.1 | **Prerequisites:** Introduction to Data Structures  
> **Original Concept Attribution:** Sheryians Coding School (Enhanced for DSA & Professional Development)

---

## 📌 Introduction to Lists

A **List** is one of the most versatile and widely used built-in data structures in Python. It acts as a dynamic container that stores an ordered collection of items.

---

## ⚡ The "Powers" (Characteristics) of a List

To understand lists, we must first learn their core characteristics:

1. **Mutable (Changeable):** Unlike strings, you can modify, add, or remove elements from a list after it has been created without generating a new list in memory.
2. **Ordered Sequence:** Lists maintain the exact insertion order of their elements. This means every element has a fixed position called its **index** (starting from `0`).
3. **Allows Duplicates:** A list can contain the same value multiple times.
4. **Heterogeneous Nature:** A single list can store elements of different data types (e.g., integers, floats, strings, booleans, and even other lists).

### 💻 Code Demonstration of List Characteristics
```python
# 1. Heterogeneous creation & ordered preservation
demo_list = [10, "Python", 3.14, True, 10]  # Note the duplicate '10'

# 2. Mutability in action
print("Original:", demo_list)
demo_list[1] = "DSA"  # Changing "Python" to "DSA"
print("Mutated: ", demo_list)  # Output: [10, "DSA", 3.14, True, 10]
```

---

## 📝 List Basics: Creation, Indexing & Slicing

### 1️⃣ Creating a List
Lists are created by placing elements inside square brackets `[]` separated by commas.
```python
empty_list = []
fruits = ["Apple", "Banana", "Cherry"]
```

### 2️⃣ Indexing & Slicing
List indexing and slicing work exactly like string indexing and slicing.
* **Positive Indexing:** Starts from `0` (left to right).
* **Negative Indexing:** Starts from `-1` (right to left).

```python
numbers = [10, 20, 30, 40, 50]

# Indexing
print(numbers[0])   # 10
print(numbers[-1])  # 50 (Last element)

# Slicing syntax: list[start:stop:step]
print(numbers[1:4])    # [20, 30, 40] (Index 4 is excluded)
print(numbers[::-1])   # [50, 40, 30, 20, 10] (Reverses the list)
```

> [!WARNING]  
> **The Mutability Contrast: String vs. List**  
> Strings are **immutable**. Trying to change a character in a string raises a `TypeError`.  
> Lists are **mutable**, meaning you can directly modify their elements.
> ```python
> text = "hello"
> # text[0] = "y"  # 🚫 Raises TypeError
> 
> lst = ["h", "e", "l", "l", "o"]
> lst[0] = "y"     # 👍 Valid! lst becomes ['y', 'e', 'l', 'l', 'o']
> ```

---

## 🔄 List Traversing

Traversing means visiting each element of the list one by one. There are two primary ways to traverse lists in Python:

### 1. Direct Iteration (By Value)
Best when you only need to read the elements.
```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)
```

### 2. Index-Based Iteration
Best when you need the index of the elements (e.g., to modify elements during iteration).
```python
for idx in range(len(names)):
    print(f"Index {idx}: {names[idx]}")
```

### 💡 Pro-Tip: Using `enumerate()`
You can get both the index and the value simultaneously:
```python
for idx, name in enumerate(names):
    print(f"Index {idx} holds value '{name}'")
```

---

## 🛠️ List Methods

A **Method** is a function associated with a specific object. For now, think of them as built-in helper tools you can call on lists using the dot (`.`) notation.

### Key List Methods:
* **`.append(item)`**: Adds an element to the end of the list.
* **`.insert(index, item)`**: Inserts an element at a specific index.
* **`.extend(iterable)`**: Appends multiple elements from another iterable.
* **`.pop(index)`**: Removes and returns the element at the given index (default is the last element).
* **`.remove(item)`**: Removes the first occurrence of the specified item.
* **`.sort()`**: Sorts the list in-place (ascending order).
* **`.reverse()`**: Reverses the elements of the list in-place.

```python
items = [3, 1, 4]

# Adding items
items.append(5)        # [3, 1, 4, 5]
items.insert(1, 9)     # [3, 9, 1, 4, 5]

# Removing items
popped_val = items.pop()  # Removes 5 (last element)
items.remove(9)        # Removes first occurrence of 9

# Ordering
items.sort()           # [1, 3, 4]
```

---

## 📝 Practice Labs & Solutions

Here are standard problems involving lists implemented with professional type hinting, clean structure, and documentation.

### Q1. Print Positive and Negative Elements of a List
*Write a function that separates and displays the positive and negative numbers from a given list.*

```python
def print_positive_negative(numbers: list[int]) -> None:
    """Separates and prints positive and negative elements of a list."""
    positives = [num for num in numbers if num >= 0]
    negatives = [num for num in numbers if num < 0]
    
    print(f"Original List: {numbers}")
    print(f"Positive Elements: {positives}")
    print(f"Negative Elements: {negatives}")

# Test Run
print_positive_negative([12, -7, 5, 64, -14, 0, -3])
```

---

### Q2. Mean of List Elements
*Write a function to compute the arithmetic mean (average) of all numeric elements in a list.*

```python
def calculate_mean(numbers: list[float]) -> float:
    """
    Calculates the mean of elements in a list.
    
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list.")
    return sum(numbers) / len(numbers)

# Test Run
print("Mean:", calculate_mean([10.5, 20.0, 30.5, 40.0]))  # Output: 25.25
```

---

### Q3. Find the Greatest Element and its Index
*Write a function to find the largest value in a list and retrieve its position (index) without using the built-in `max()` or `.index()` functions.*

```python
def find_greatest_with_index(numbers: list[int]) -> tuple[int, int]:
    """
    Finds the maximum value in a list and its index in O(N) time complexity.
    
    Returns:
        tuple[int, int]: (greatest_element, index)
    """
    if not numbers:
        raise ValueError("List is empty.")
        
    max_val = numbers[0]
    max_idx = 0
    
    for idx in range(1, len(numbers)):
        if numbers[idx] > max_val:
            max_val = numbers[idx]
            max_idx = idx
            
    return max_val, max_idx

# Test Run
val, index = find_greatest_with_index([12, 45, 2, 89, 34, 89, 7])
print(f"Greatest Element: {val} at Index: {index}")
```

---

### Q4. Find the Second Greatest Element
*Write a function to return the second largest distinct element in a list in a single traversal (O(N) time and O(1) space).*

```python
def find_second_greatest(numbers: list[int]) -> int | None:
    """
    Finds the second largest distinct element in a list.
    Returns None if no such element exists.
    """
    if len(numbers) < 2:
        return None
        
    first = second = float('-inf')
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return int(second) if second != float('-inf') else None

# Test Run
print("Second Greatest:", find_second_greatest([10, 20, 20, 15, 8]))  # Output: 15
print("Second Greatest:", find_second_greatest([10, 10]))            # Output: None
```

---

### Q5. Check if List is Sorted
*Write a function that checks if a list is sorted in non-decreasing (ascending) order.*

```python
def is_sorted(numbers: list[int]) -> bool:
    """
    Returns True if the list is sorted in ascending order, otherwise False.
    """
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

# Test Run
print("Is [1, 2, 3, 5, 8] sorted?", is_sorted([1, 2, 3, 5, 8]))    # Output: True
print("Is [1, 5, 3, 8] sorted?", is_sorted([1, 5, 3, 8]))          # Output: False
```
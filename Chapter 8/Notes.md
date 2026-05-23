# Chapter 08: Loops & Iterative Control Flow in Python

> **Topic Index:** 07 | **Prerequisites:** Conditional Statements & Control Flow  
> **Original Concept Attribution:** Sheryians Coding School (Enhanced for DSA & Professional Development)

---

## 📌 Introduction to Loops & Iterative Control Flow

By default, program execution is sequential. However, we frequently need to execute a specific block of code multiple times. For example, if you wanted to print `"Hello World"` 100 times in VS Code, writing 100 individual print statements would be tedious, repetitive, and hard to maintain.

Using **Loops**, we can achieve this in just **2 lines of code**. That is the core power of loops: automation, code reusability, and clean code structure.

---

## 🔍 The Loop Intuition: A Real-World Analogy

To understand loops, let's look at a simple analogy from *Sheryians Coding School*. 

Imagine you have a **filled water bucket**, an **empty bucket**, and a **mug**. Your goal is to transfer water from the filled bucket to the empty bucket.

```text
  [ Filled Bucket ]   === (Transfer via Mug) ===>   [ Empty Bucket ]
```

### Scenario 1: You must transfer exactly 4 mugs of water.
*   **Intuition:** You know the exact number of iterations beforehand (exactly 4 times).
*   **Programming Choice:** When the number of iterations is known in advance, we use a **`for` loop**.

### Scenario 2: You must transfer water until the source bucket is empty.
*   **Intuition:** You do not know how many mugs it will take (could be 10, 20, or 50), but you know the condition that determines when to stop (stop when the source bucket is empty).
*   **Programming Choice:** When the number of iterations is unknown but depends on a conditional expression, we use a **`while` loop**.

---

## 🔄 The `while` Loop: Condition-Driven Iteration

A `while` loop repeatedly executes a target statement or block of code as long as a given condition remains `True`.

### 📝 Syntax & Structure
```python
# 1. Initialization
variable = initial_value 

# 2. Condition evaluation
while condition:
    # 3. Code block to execute
    statement_1
    statement_2
    
    # 4. Update / Step (CRITICAL)
    variable_update 
```

### 💻 Standard Implementation: Counting 1 to 5
```python
i = 1 # Initialization
while i <= 5: # Condition Check
    print(i) # Action
    i += 1 # Update (Increment)
```

> [!WARNING]  
> **The Infinite Loop Trap:** If you forget to update the loop control variable (e.g., omitting `i += 1`), the condition `i <= 5` will always remain `True`. The program will enter an **infinite loop**, consuming CPU resources until it is manually terminated (e.g., via `Ctrl + C` in the terminal).

### 🤝 The `while-else` Architecture
Python has a unique feature: loops can have an optional `else` block. The code in the `else` block executes when the loop condition evaluates to `False` (i.e., the loop finishes naturally).

```python
count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop finished successfully without interruption.")
```
> [!NOTE]  
> If the loop is terminated prematurely by a `break` statement, the `else` block is **skipped**.

---

## 🔁 The `for` Loop: Sequence-Driven Iteration

The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, string, set, dictionary) or other iterable objects.

### 📝 Syntax & Structure
```python
for item in sequence:
    # Code block to execute
    statement(item)
```

### ⚡ The `range()` Function Deep-Dive
In Python, we often use the built-in `range()` function to generate a sequence of numbers.

$$\text{range}(\text{start}, \text{stop}, \text{step})$$

1.  **`range(stop)`**: Generates numbers from `0` up to (but not including) `stop`. Step defaults to `1`.
    *   `range(5)` $\rightarrow$ `0, 1, 2, 3, 4`
2.  **`range(start, stop)`**: Generates numbers from `start` up to (but not including) `stop`.
    *   `range(2, 6)` $\rightarrow$ `2, 3, 4, 5`
3.  **`range(start, stop, step)`**: Generates numbers from `start` up to `stop` (exclusive), incrementing by `step`.
    *   `range(1, 10, 2)` $\rightarrow$ `1, 3, 5, 7, 9`
4.  **Reverse Iteration (Negative Step)**: Generates numbers downwards.
    *   `range(5, 0, -1)` $\rightarrow$ `5, 4, 3, 2, 1`

```python
# Printing Hello World 100 times using a for loop
for _ in range(100):
    print("Hello World")
```
*(Note: We use `_` as a variable name if we do not need to use the loop index inside the block).*

### 📦 Iterating Through Sequences

```python
# 1. Iterating over a String
word = "Python"
for char in word:
    print(char, end="-")
# Output: P-y-t-h-o-n-

# 2. Iterating over a List
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

# 3. Iterating over a Dictionary
student = {"name": "Shery", "roll": 101, "course": "Python"}
for key, val in student.items():
    print(f"{key}: {val}")
```

### 🤝 The `for-else` Architecture
Just like `while-else`, the `else` block of a `for` loop executes when the loop finishes all its iterations naturally.

```python
for i in range(3):
    print(i)
else:
    print("Completed all iterations.")
```

---

## 🛑 Loop Control Statements

Loop control statements change the default execution flow of a loop. Python provides three key control statements:

| Statement | Behaviour | Use Case |
| :---: | :--- | :--- |
| **`break`** | Terminates the loop immediately and jumps to the code below the loop. | Stopping search once an item is found. |
| **`continue`** | Skips the remaining code inside the loop for the **current** iteration and goes to the next iteration. | Skipping specific values (e.g. odd numbers). |
| **`pass`** | A null statement. It acts as a syntactic placeholder doing absolutely nothing. | Defining empty loops, functions, or classes to implement later. |

### 🔍 Execution Visualization
```python
# Example of break
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output: 1, 2 (Stops completely when i is 3)

# Example of continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1, 2, 4, 5 (Skips printing 3)
```

---

## 🧠 Deep-Dive: Nested Loops

A **nested loop** is a loop inside another loop. For every single iteration of the outer loop, the inner loop executes completely.

```python
# Syntax
for outer_item in outer_sequence:
    for inner_item in inner_sequence:
        statement
```

### 📐 Pattern Printing Example (Right-Angled Triangle)
```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print() # Moves to the next line
```
**Output:**
```text
* 
* * 
* * * 
* * * * 
* * * * * 
```

> [!IMPORTANT]  
> **Time Complexity Warning:** Nested loops are common in grid traversals and sorting algorithms. A nested loop running $N$ times inside another loop running $N$ times has a time complexity of $\mathcal{O}(N^2)$. Keep this in mind when designing algorithms for large datasets.

---

## ⚡ Professional DSA Design Patterns & Best Practices

### Pattern 1: Sentinel Search (Using `for-else`)
In competitive programming, we often need to check if an element exists in a collection. Instead of using a Boolean flag variable (e.g. `found = False`), use Python's native `for-else` structure.

```python
def find_target(arr, target):
    for num in arr:
        if num == target:
            print("Element Found!")
            break
    else:
        # Runs only if the loop completed without breaking
        print("Element Not Found!")
```

### Pattern 2: Guard Clauses inside Loops
Use `continue` to filter out invalid elements early in the loop block. This keeps the indentation level low and makes the code cleaner.

```python
# Avoid deeply nested if-statements
for user in user_list:
    if not user.is_active:
        continue
    if not user.has_permission:
        continue
    # Process valid user
    process_user(user)
```

---

## 📝 Practice Labs & Solutions

Here are standard problems implemented with professional type hinting, documentation, and clean logic.

### Q1. Range Explorer
*Print numbers 1 to 10 using a `while` loop, and numbers 10 down to 1 using a `for` loop.*

```python
def print_forward() -> None:
    """Prints numbers 1 to 10 using a while loop."""
    print("Forward counting (1-10):")
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print()

def print_backward() -> None:
    """Prints numbers 10 down to 1 using a for loop."""
    print("Backward counting (10-1):")
    for i in range(10, 0, -1):
        print(i, end=" ")
    print()

# Run
print_forward()
print_backward()
```

---

### Q2. Sum of Natural Numbers (DSA Analysis)
*Calculate the sum of the first N natural numbers.*

```python
# Approach 1: Iterative approach O(N) time complexity
def sum_iterative(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Approach 2: Formula-based approach O(1) time complexity (Optimal)
def sum_formula(n: int) -> int:
    return (n * (n + 1)) // 2

# Test
print(f"Iterative Sum of 100: {sum_iterative(100)}")
print(f"Formula Sum of 100: {sum_formula(100)}")
```

---

### Q3. Multiplication Table generator
*Accept a number from the user and print its multiplication table.*

```python
def generate_table(number: int) -> None:
    """Generates the multiplication table of a given number up to 10."""
    print(f"--- Multiplication Table of {number} ---")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Run
generate_table(7)
```

---

### Q4. Factorial Calculator
*Compute the factorial of a given integer $N$ (e.g. $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$).*

```python
def factorial(n: int) -> int:
    """Calculates the factorial of non-negative integer n using loops."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test
print(f"Factorial of 5: {factorial(5)}") # Output: 120
```

---

### Q5. Fibonacci Sequence Generator
*Generate the Fibonacci sequence up to $N$ terms (0, 1, 1, 2, 3, 5, 8, 13, ...).*

```python
def generate_fibonacci(n_terms: int) -> list[int]:
    """Generates the first n Fibonacci numbers."""
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
        
    sequence = [0, 1]
    # We already have first 2 terms
    for _ in range(n_terms - 2):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

# Test
print(f"First 8 Fibonacci terms: {generate_fibonacci(8)}")
```

---

### Q6. Primality Verification (Optimized $\mathcal{O}(\sqrt{N})$)
*Verify if a given number is prime.*

> [!TIP]  
> **DSA Optimization:** A composite number must have a factor less than or equal to its square root. Instead of testing all numbers up to $N$, check up to $\sqrt{N}$ to save computational resources.

```python
import math

def is_prime(number: int) -> bool:
    """Verifies if a number is prime using optimized O(sqrt(N)) logic."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False  # Exclude even numbers greater than 2
        
    # Check odd divisors up to sqrt(N)
    limit = int(math.sqrt(number))
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    return True

# Test
print(f"Is 29 prime? {is_prime(29)}") # True
print(f"Is 35 prime? {is_prime(35)}") # False
```

---

### Q7. Pattern Printing (Pyramid Structure)
*Print a symmetric pyramid pattern of height $H$.*

```python
def print_pyramid(height: int) -> None:
    """Prints a symmetric asterisk pyramid of given height."""
    for i in range(1, height + 1):
        # Print leading spaces
        spaces = " " * (height - i)
        # Print asterisks
        asterisks = "*" * (2 * i - 1)
        print(spaces + asterisks)

# Run
print_pyramid(5)
```
**Output:**
```text
    *
   ***
  *****
 *******
*********
```

---
*Iterate, optimize, and build robust software!*  
⭐ **Crafted with care for Python Learners & DSA Aspirants.**
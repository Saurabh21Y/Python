# Chapter 07: Conditional Statements & Control Flow in Python

> **Topic Index:** 06 | **Prerequisites:** Python Operators  
> **Original Concept Attribution:** Sheryians Coding School (Enhanced for DSA & Professional Development)

---

## 📌 Introduction to Control Flow

By default, Python execution is **sequential**—it executes lines of code one after another from top to bottom. However, real-world applications require decision-making. We must execute specific blocks of code *only if* certain conditions are satisfied. 

These structures are called **Conditional Statements** or **Control Flow Statements** because they allow you to control the branching and execution path of your program.

### 🔍 Real-World Analogy
Suppose you are designing a system that accepts a number from a user:
- If the number is **greater than 10**, the system executes **Task A**.
- If the number is **10 or less**, the system executes **Task B**.

Here, the input value *controls* the execution branch:

```text
               [ User Input Number ]
                        |
                        v
              { Is Number > 10? }
                 /          \
         YES    /            \   NO
               v              v
          [ Task A ]      [ Task B ]
```

---

## 🛠️ Syntactic Architectures in Python

Python provides three primary syntactic structures to manage execution branches.

### 1. The Simple `if` Statement
Executes a block of code if and only if the underlying conditional expression evaluates to `True`.

```python
# Syntax
if condition:
    # Code block executed if condition is True
    statement_1
    statement_2
```

### 2. The Dual-Branch `if-else` Statement
Executes one block if the condition is `True`, and a fallback block if it evaluates to `False`.

```python
# Syntax
if condition:
    # Executed if condition is True
    statement_1
else:
    # Executed if condition is False
    statement_2
```

### 3. The Multi-Branch `if-elif-else` Ladder
Checks multiple conditions sequentially. The moment it encounters a condition that is `True`, it executes its associated block and exits the entire structure. If all conditions fail, the optional `else` block executes.

```python
# Syntax
if condition_A:
    # Executed if condition_A is True
    block_A
elif condition_B:
    # Executed if condition_A is False AND condition_B is True
    block_B
elif condition_C:
    # Executed if both A and B are False AND condition_C is True
    block_C
else:
    # Executed if ALL conditions are False
    fallback_block
```

> [!IMPORTANT]  
> **The Indentation Rule:** Python does not use curly braces `{}` to define code blocks. Instead, it relies strictly on whitespace indentation (typically 4 spaces). Inconsistent indentation will raise an `IndentationError`.

---

## 🚀 Deep-Dive: The Ternary Operator for DSA

In Data Structures and Algorithms (DSA) interviews and competitive programming, writing clean, highly optimized, and concise logic is paramount. The **Ternary Operator** (formally known as a **Conditional Expression** in Python) is one of the most powerful tools to achieve this.

### 📝 Syntax & Evaluation Semantics

Unlike C++ or Java which use the `? :` symbol, Python uses a highly readable, natural-language syntax:

$$\text{Result} = \text{Expression}_{\text{True}} \ \mathbf{if} \ \text{Condition} \ \mathbf{else} \ \text{Expression}_{\text{False}}$$

```python
# Example:
age = 20
status = "Voter" if age >= 18 else "Non-Voter"
```

### 🧠 Critical Difference: Expression vs. Statement

Understanding the computer science difference between statements and expressions is vital for advanced coding:

| Feature | `if-else` Statement | Ternary Expression |
| :--- | :--- | :--- |
| **Category** | Control Flow **Statement** | Inline **Expression** |
| **Return Value** | Does not return a value natively; must perform assignments or side-effects inside. | Evaluates directly to a single value, which can be returned, assigned, or passed as an argument. |
| **Usage Context** | Used to structure larger blocks of code, logical paths, and multi-line operations. | Used inside function calls, lambda expressions, list comprehensions, and inline returns. |
| **Nesting Cap** | Highly readable when nested (using `elif`). | Syntactically allowed to nest, but can quickly reduce readability ("Ternary Spaghetti"). |

---

### ⚡ Professional DSA Design Patterns with Ternaries

#### Pattern 1: Elegant Recursive Base Cases
When writing recursive algorithms (like Tree traversals or Binary Search), the base case typically returns a simple value. Using a ternary operator turns standard 4-line boilerplate into highly readable, elegant one-liners.

*Standard recursive depth calculation for a Binary Tree:*
```python
# Verbose Approach
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

*Elite DSA Ternary Approach:*
```python
# Clean, readable, and highly professional
def maxDepth(root):
    return 0 if not root else 1 + max(maxDepth(root.left), maxDepth(root.right))
```

#### Pattern 2: Dynamic Programming (DP) State Transitions
In DP tables (like the Knapsack problem, Longest Common Subsequence, or Grid Pathfinding), state updates often depend on a condition. An inline ternary prevents messy indentation.

```python
# LeetCode DP transition step
dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(dp[i-1][j], dp[i][j-1])
```

#### Pattern 3: Safe Attribute Evaluation via Short-Circuiting
Python’s ternary operator evaluates expressions **lazily**. That means if the condition is `True`, only the `Expression_True` is evaluated; the other branch is completely ignored (and vice-versa). This prevents runtime errors such as `AttributeError` when dealing with `None` pointers in linked lists and trees.

```python
# Prevents throwing an error if node is None
val = node.val if node else 0 
```

> [!WARNING]  
> **Avoid Nesting Ternaries Excessively:** While `a if cond1 else b if cond2 else c` is valid Python, it is incredibly difficult to read and debug. Use standard `if-elif-else` ladders if you have more than two distinct branches, unless doing simple inline dynamic programming states.

---

## 📝 Practice Labs & Solutions

Here are detailed implementations for each practice question, showcasing optimal Python structures.

### Q1. Greatest of Two Numbers
*Accept two numbers and print the greatest between them.*

```python
def print_greatest(num1: float, num2: float) -> None:
    # Standard conditional check
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("Both numbers are equal")

# --- DSA Ternary Version (For inline comparison/assignment) ---
def get_greatest(num1: float, num2: float) -> float:
    return num1 if num1 >= num2 else num2
```

---

### Q2. Greeting by Gender
*Accept gender from the user as a character and print the respective greeting.*

```python
def greet_user(gender_char: str) -> None:
    # Canonicalize the input to handle lower/uppercase variations safely
    gender = gender_char.strip().upper()
    
    if gender == 'M':
        print("Good Morning Sir!")
    elif gender == 'F':
        print("Good Morning Ma'am!")
    else:
        print("Good Morning! (Welcome)")
```

---

### Q3. Even or Odd Checker
*Accept an integer and check whether it is even or odd.*

```python
def check_even_odd(number: int) -> str:
    # A number is even if it leaves a remainder of 0 when divided by 2
    return "Even" if number % 2 == 0 else "Odd"

# Test example
print(f"Number 42 is: {check_even_odd(42)}")
```

---

### Q4. Voter Eligibility Checker
*Accept name and age from the user. Check if the user is a valid voter or not (Voter age >= 18).*

```python
def verify_voter(name: str, age: int) -> None:
    # Combine conditions safely using formatting
    status = "a valid voter" if age >= 18 else "not a valid voter yet"
    print(f"Hello {name}, you are {status}.")

# Execution Example
verify_voter("Shery", 19) # Output: Hello Shery, you are a valid voter.
```

---

### Q5. Leap Year Detection Algorithm
*Accept a year and check if it is a leap year.*

> [!NOTE]  
> **Leap Year Logic:**
> 1. If a year is evenly divisible by 4, it *might* be a leap year.
> 2. Except if it is divisible by 100, then it is *not* a leap year...
> 3. ...Unless it is also divisible by 400. Then it *is* a leap year.

```python
def is_leap_year(year: int) -> bool:
    # Combining conditions using logical operators
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Professional Ternary alternative for DSA
def is_leap_year_ternary(year: int) -> bool:
    return True if (year % 400 == 0) else (False if (year % 100 == 0) else (year % 4 == 0))
```

---

### Q6. Celsius Temperature Classifier
*Take Celsius temperature input and categorize it.*

* **Below 0°C** $\rightarrow$ "Freezing Cold"
* **0°C to 10°C** $\rightarrow$ "Very Cold"
* **10°C to 20°C** $\rightarrow$ "Cold"
* **20°C to 30°C** $\rightarrow$ "Pleasant"
* **30°C to 40°C** $\rightarrow$ "Hot"
* **Above 40°C** $\rightarrow$ "Very Hot"

```python
def classify_temperature(celsius: float) -> str:
    # if-elif ladder ensures exclusive ranges are evaluated in order
    if celsius < 0:
        return "Freezing Cold"
    elif celsius <= 10:
        return "Very Cold"
    elif celsius <= 20:
        return "Cold"
    elif celsius <= 30:
        return "Pleasant"
    elif celsius <= 40:
        return "Hot"
    else:
        return "Very Hot"

# Example Run
print(f"At 25°C, the weather is: {classify_temperature(25)}")
```

---
*Keep practicing and building robust logic!*  
⭐ **Crafted with care for Python Learners & DSA Aspirants.**
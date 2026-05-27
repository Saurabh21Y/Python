# Chapter 09: Functions & Modular Programming in Python

> **Topic Index:** 09 | **Prerequisites:** Loops & Iterative Control Flow  
> **Original Concept Attribution:** Sheryians Coding School (Enhanced for DSA & Professional Development)

---

## 📌 Introduction to Functions

In programming, we often need to execute a block of code multiple times with different inputs. Copying and pasting the same code violates the **DRY (Don't Repeat Yourself)** principle, making the program bloated, hard to debug, and difficult to maintain.

A **Function** is a self-contained block of reusable code designed to perform a specific task. By grouping code into functions, we make our programs modular, readable, and reusable.

### 🔄 Built-in vs. User-Defined Functions

Python categorizes functions into two main types:

1. **Built-in Functions:** Pre-defined functions available in Python's standard library.
   * Examples: `print()`, `input()`, `len()`, `range()`, `type()`, `sum()`, `max()`.
2. **User-Defined Functions (UDFs):** Functions created by developers to perform custom tasks.
   * Created using the `def` keyword.

---

## 📝 Syntax & Anatomy of a Python Function

To define and execute a function in Python, we use a specific syntax structure:

```python
# 1. Function Definition
def function_name(parameter1, parameter2):
    """
    Optional: Docstring explaining what the function does.
    """
    # Function Body (indented)
    result = parameter1 + parameter2
    return result # Optional: Returns a value to the caller

# 2. Function Call (Execution)
output = function_name(value1, value2)
```

### 🔍 Key Components:
* **`def` Keyword:** Signals the start of a function definition.
* **Function Name:** A descriptive name using `snake_case` naming conventions.
* **Parameters (inside parenthesis):** Placeholders for data that the function accepts.
* **Colon (`:`):** Marks the end of the signature and the start of the indented block.
* **Docstring:** A multi-line string used for documenting function behavior.
* **Function Body:** The actual logic that runs when the function is called.
* **`return` Statement:** Sends a result back to the caller. If omitted, Python returns `None` by default.

---

## ⚙️ Parameters vs. Arguments

Though often used interchangeably, **Parameters** and **Arguments** refer to distinct concepts:

| Concept | Definition | Where Defined | Analogy |
| :--- | :--- | :--- | :--- |
| **Parameters** | Variables listed inside the parentheses of a function's definition. | Function signature (`def`) | Blank placeholders / variables. |
| **Arguments** | The actual values passed to the function when it is called. | Function invocation (`name()`) | Real data assigned to those variables. |

### 💻 Code Illustration

```python
# 'name' is the PARAMETER (acting as a variable)
def greet(name):
    print(f"Hello, {name}!")

# 'Alice' and 'Bob' are the ARGUMENTS (the actual values assigned to 'name')
greet("Alice") # Output: Hello, Alice!
greet("Bob")   # Output: Hello, Bob!
```

> [!NOTE]  
> If a function is defined with a certain number of parameters, you must provide the exact same number of arguments when calling it, unless default values are specified. Otherwise, Python raises a `TypeError`.

---

## 🔀 Types of Arguments

Python provides flexible ways to pass arguments to parameters. The three primary types are:

### 1️⃣ Positional Arguments
By default, Python matches arguments to parameters based on their **position** (order). The first parameter captures the first argument, the second parameter captures the second argument, and so on.

```python
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Position matters: 'Alice' maps to 'name', 25 maps to 'age'
display_info("Alice", 25) # Output: Name: Alice, Age: 25

# Swapping the arguments alters the meaning
display_info(25, "Alice") # Output: Name: 25, Age: Alice
```

### 2️⃣ Default Arguments
You can assign default values to parameters during the function definition. If the caller does not pass an argument for that parameter, the default value is used automatically.

```python
# 'country' has a default value of "India"
def greet_user(name, country="India"):
    print(f"{name} is from {country}")

# Case A: Argument is omitted -> default is used
greet_user("Saurabh") # Output: Saurabh is from India

# Case B: Argument is provided -> default is overridden
greet_user("John", "USA") # Output: John is from USA
```

> [!WARNING]  
> **Syntax Rule:** In a function definition, all **positional (non-default) parameters must be placed before default parameters**.
> * `def func(a, b=10):` $\rightarrow$ **Valid**
> * `def func(a=10, b):` $\rightarrow$ **Invalid (Raises SyntaxError: non-default argument follows default argument)**

### 3️⃣ Keyword Arguments
Keyword arguments allow you to pass values by explicitly naming the parameters, using the `parameter_name = value` format. In this case, the **order of arguments does not matter**.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Passing arguments by name, allowing arbitrary ordering
describe_pet(pet_name="Bruno", animal_type="Dog") 
# Output: I have a Dog named Bruno.
```

---

## ⚡ Professional DSA Design Patterns & Best Practices

### Pattern 1: Type Hinting & Self-Documenting Code
In professional production systems, always specify input parameter types and the expected return type. This prevents type errors, helps IDE autocomplete, and clarifies code intent.

```python
def calculate_area(length: float, width: float) -> float:
    """
    Computes the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The calculated area.
    """
    return length * width
```

### Pattern 2: Return Values vs. Direct Printing
Avoid using `print()` inside core logical functions. Instead, **`return`** the result. This keeps your functions reusable for calculations, testing, and other workflows.

```python
# 🚫 POOR PRACTICE (Hard to reuse/test result)
def add_bad(a, b):
    print(a + b)

# 👍 GOOD PRACTICE (Result can be saved, formatted, or used in other operations)
def add_good(a: int, b: int) -> int:
    return a + b
```

### Pattern 3: Handling Multiple Returns (Tuples)
A function in Python can return multiple values separated by commas. Python automatically packages them into a single **tuple**, which can be easily unpacked by the caller.

```python
def get_min_max(numbers: list[int]) -> tuple[int, int]:
    """Returns both the minimum and maximum value in a list."""
    return min(numbers), max(numbers)

# Unpacking the returned tuple
minimum, maximum = get_min_max([23, 5, 89, 44, 12])
print(f"Min: {minimum}, Max: {maximum}")
```

---

## 📝 Practice Labs & Solutions

Here are standard problems implemented with professional type hinting, documentation, and clean logic.

### Q1. Dynamic Greeting Card Creator
*Write a function that takes a person's name and an optional event name (defaulting to "Birthday"). It should return a formatted greeting.*

```python
def create_greeting(name: str, event: str = "Birthday") -> str:
    """Generates a personalized celebration greeting card string."""
    return f"Dear {name}, Wishing you a fantastic and joyful {event}! Best regards."

# Test Cases
print(create_greeting("Saurabh"))
# Output: Dear Saurabh, Wishing you a fantastic and joyful Birthday! Best regards.

print(create_greeting("Rohit", "Graduation"))
# Output: Dear Rohit, Wishing you a fantastic and joyful Graduation! Best regards.
```

---

### Q2. Positional & Keyword Argument Validator
*Write a function representing a user profile builder that accepts username, email (required), role (default "Guest"), and status (default "Active"). Demonstrate how to call it using positional, default, and keyword arguments.*

```python
def build_profile(username: str, email: str, role: str = "Guest", status: str = "Active") -> dict[str, str]:
    """Creates a dictionary representation of a user profile."""
    return {
        "username": username,
        "email": email,
        "role": role,
        "status": status
    }

# Call using positional arguments only
p1 = build_profile("saurabh_21", "saurabh@example.com")

# Call combining positional, default, and keyword arguments
p2 = build_profile("admin_user", "admin@example.com", status="Inactive", role="Administrator")

print("Profile 1:", p1)
print("Profile 2:", p2)
```

---

### Q3. Modular Calculator (Single Responsibility Principle)
*Create a basic calculator function that takes two numbers and an operator (`+`, `-`, `*`, `/`) and returns the computed result. Use helper functions for mathematical operations.*

```python
def add(x: float, y: float) -> float: return x + y
def subtract(x: float, y: float) -> float: return x - y
def multiply(x: float, y: float) -> float: return x * y
def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def calculator(num1: float, num2: float, operator: str) -> float:
    """
    Performs arithmetic operations on two numbers based on operator.
    Demonstrates routing functions modularly.
    """
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
    if operator not in operations:
        raise ValueError(f"Invalid operator '{operator}'. Use +, -, *, or /.")
        
    # Execute the associated function
    return operations[operator](num1, num2)

# Test Runs
print(f"12 + 5 = {calculator(12, 5, '+')}")
print(f"8 * 9 = {calculator(8, 9, '*')}")
```

---

### Q4. Prime Range Searcher (Composition Pattern)
*Build a function `find_primes_in_range(start, end)` that uses a helper function `is_prime(n)` to find and return all prime numbers within a range.*

```python
import math

def is_prime(n: int) -> bool:
    """Helper function to verify prime numbers in O(sqrt(N)) time complexity."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for divisor in range(3, int(math.sqrt(n)) + 1, 2):
        if n % divisor == 0:
            return False
    return True

def find_primes_in_range(start: int, end: int) -> list[int]:
    """Finds all prime numbers inside a closed interval [start, end]."""
    primes = []
    for val in range(start, end + 1):
        if is_prime(val):
            primes.append(val)
    return primes

# Test Run
print("Primes between 10 and 50:", find_primes_in_range(10, 50))
# Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

### Q5. Temperature Converter (Multi-Value Return Pattern)
*Write a function that accepts a temperature value in Celsius and returns its converted value in both Fahrenheit and Kelvin.*

```python
def convert_celsius(celsius: float) -> tuple[float, float]:
    """
    Converts Celsius to Fahrenheit and Kelvin.
    
    Returns:
        tuple[float, float]: (Fahrenheit, Kelvin)
    """
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Test Case
c_temp = 25.0
f_temp, k_temp = convert_celsius(c_temp)
print(f"{c_temp}°C is equivalent to {f_temp}°F and {k_temp} K.")
```

---
*Write modular code, keep components focused, and minimize side effects!*  
⭐ **Crafted with care for Python Learners & DSA Aspirants.**
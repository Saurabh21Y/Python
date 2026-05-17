# Chapter 5: Input and Output in Python 🚀

In Python, interacting with the user is fundamental. We use the `print()` function to display data (Output) and the `input()` function to collect data (Input).

---

## 1. Output using `print()` 📤

The `print()` function is the primary way to display results on the terminal.

### Basic Usage
```python
print("Hello, World!")
name = "Saurabh"
print(name)
```

### Formatted Strings (f-strings)
F-strings provide a concise and convenient way to embed expressions inside string literals.
```python
age = 21
print(f"My name is {name} and I am {age} years old.")
```

### Advanced `print()` Parameters
- **`sep`**: Specifies the separator between objects. (Default is space `" "`)
- **`end`**: Specifies what to print at the end. (Default is newline `\n`)

```python
print("Python", "is", "fun", sep="-") # Output: Python-is-fun
print("Hello", end=" ")
print("World") # Output: Hello World (on the same line)
```

---

## 2. Input using `input()` 📥

To ask the user for information, we use the `input()` function.

### How it works
When `input()` is called, the program pauses and waits for the user to type something.
```python
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")
```

### The "String" Trap ⚠️
The `input()` function **always returns a string**, regardless of what the user types.
```python
age = input("Enter your age: ")
print(type(age)) # Output: <class 'str'>
```

---

## 3. Type Casting Input 🛠️

Since `input()` returns a string, we must manually convert (type cast) it if we need numbers.

### Accepting Integers
```python
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")
```

### Accepting Floats
```python
price = float(input("Enter the price: "))
print(f"Total with tax: {price * 1.18}")
```

---

## 4. Practice Questions 📝

1. **Accept numbers from a user**: Write a program to take two numbers and print their sum.
2. **Accept age from the user**: Take the user's age and check if they are eligible to vote (age >= 18).
3. **Multi-input**: Take name, age, and city in separate inputs and print them in a single formatted sentence.

---

> [!TIP]
> Always use descriptive prompts inside `input("Prompt here")` so the user knows what to type!



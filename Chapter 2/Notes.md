# 📝 Chapter 2: Comments & Variables

In this chapter, we explore how to document our code and how to store data using variables.

---

## 💬 Comments in Python

Comments are lines in your code that are ignored by the Python interpreter. They are used to explain what the code does, making it easier for humans to read.

### 1. Single-Line Comments
Use the `#` symbol to create a single-line comment.
```python
# This is a comment - Python will ignore this line
print("Hello Saurbh!") # You can also add comments after code
```

### 2. Multi-Line "Comments" (Docstrings)
Python doesn't have a specific syntax for multiline comments, but we use **Docstrings** (triple quotes) to achieve this.
```python
"""
This is a multiline string 
often used as a multiline comment 
to explain complex logic.
"""
```

---

## 📦 Variables in Python

A **Variable** is like a container or storage space where we can store data values. Think of it as a labeled box.

**Example:**
```python
name = "Saurbh Prakash"  # Storing a string
age = 22                 # Storing an integer
```

---

## 🚫 Variable Naming Rules

When naming your variables, follow these strict rules to avoid errors:

| Feature | Rule | Example (❌ Bad) | Example (✅ Good) |
| :--- | :--- | :--- | :--- |
| **Start** | Cannot start with a number. | `1name = "Saurbh"` | `name1 = "Saurbh"` |
| **Spaces** | No spaces allowed. | `user name = "Saurbh"` | `user_name = "Saurbh"` |
| **Characters** | Only alpha-numeric & underscores. | `name@ = "Saurbh"` | `name_val = "Saurbh"` |

> [!CAUTION]
> Avoid using Python keywords (like `print`, `if`, `else`) as variable names!

---

## 🏗️ Naming Conventions

To keep your code professional, follow these three common naming styles. We will use **Saurbh Prakash** as our example base:

### 1. 🐪 Camel Case
The first word is lowercase, and each subsequent word starts with an uppercase letter.
- **Example:** `saurbhPrakashCoding`

### 2. 📐 Pascal Case
Every word starts with an uppercase letter. Useful for Class names.
- **Example:** `SaurbhPrakashCoding`

### 3. 🐍 Snake Case
Words are separated by underscores. This is the **standard convention** for Python variables.
- **Example:** `saurbh_prakash_coding`

---

> [!TIP]
> **Pro Tip:** Always choose descriptive variable names. Instead of `a = 10`, use `user_age = 10`. It makes your code self-explanatory!


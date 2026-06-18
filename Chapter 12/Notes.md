# 📂 Chapter 12 — File Handling in Python

---

## 📌 What are Files?

Any name with an extension is a **file**.

For example:
- `notes.txt` → Text file
- `music.mp3` → Audio file
- `script.py` → Python file
- `photo.jpg` → Image file

When we want to work with these files through code (read, write, etc.), we use **File Handling**.

---

## 📌 What is File Handling?

**File Handling** refers to the **CRUD** operations we can perform on files:

| Operation | Meaning |
|-----------|---------|
| **C**reate | Create a new file |
| **R**ead | Read the contents of a file |
| **U**pdate | Modify/append content in a file |
| **D**elete | Delete a file |

---

## 📌 Opening a File — `open()`

To work with any file in Python, we first need to **open** it using the built-in `open()` function.

### Syntax

```python
file = open("filename.txt", "mode")
```

---

## 📌 File Modes

| Mode | Full Form | Description |
|------|-----------|-------------|
| `'r'` | Read | Opens file for reading *(default)*. File **must exist**. |
| `'w'` | Write | Opens file for writing. **Creates** file if not found, **overwrites** if exists. |
| `'a'` | Append | Opens file for appending. Adds content to the **end** of the file. |
| `'x'` | Create | Creates a new file. **Fails** if the file already exists. |
| `'rb'` | Read Binary | Reads file in binary mode (e.g., images, audio). |
| `'wb'` | Write Binary | Writes file in binary mode. |

---

## 📌 Reading a File

```python
# Open and read entire file
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```

### Reading Methods

| Method | Description |
|--------|-------------|
| `file.read()` | Reads the **entire** file as a string |
| `file.readline()` | Reads **one line** at a time |
| `file.readlines()` | Reads all lines and returns a **list** |

```python
file = open("notes.txt", "r")

# Read line by line
for line in file:
    print(line, end="")

file.close()
```

---

## 📌 Writing to a File

```python
# 'w' mode — overwrites the file
file = open("output.txt", "w")
file.write("Hello, World!\n")
file.write("Python is awesome!")
file.close()
```

> ⚠️ **Warning:** `'w'` mode deletes existing content and starts fresh. Use `'a'` to preserve old data.

---

## 📌 Appending to a File

```python
# 'a' mode — adds to the end without deleting existing content
file = open("output.txt", "a")
file.write("\nNew line added!")
file.close()
```

---

## 📌 The `with` Keyword (Recommended ✅)

Normally, after working with a file, you need to **manually close** it using `file.close()`.  
But Python provides the `with` keyword which **automatically closes** the file once the block is done — even if an error occurs!

### Syntax

```python
with open("filename.txt", "mode") as file:
    # work with the file here
    content = file.read()
    print(content)
# File is automatically closed here
```

### Example — Read with `with`

```python
with open("notes.txt", "r") as f:
    data = f.read()
    print(data)
```

### Example — Write with `with`

```python
with open("output.txt", "w") as f:
    f.write("This is written using 'with'!\n")
```

---

## 📌 Checking if File Exists (Safe Approach)

```python
import os

if os.path.exists("notes.txt"):
    with open("notes.txt", "r") as f:
        print(f.read())
else:
    print("File not found!")
```

---

## 📌 Deleting a File

```python
import os

os.remove("output.txt")  # Deletes the file
```

---

## 📌 Quick Summary

| Task | Code |
|------|------|
| Open file | `open("file.txt", "r")` |
| Read entire content | `file.read()` |
| Read one line | `file.readline()` |
| Read all lines as list | `file.readlines()` |
| Write to file | `open("file.txt", "w")` |
| Append to file | `open("file.txt", "a")` |
| Auto-close file | `with open(...) as f:` |
| Delete file | `os.remove("file.txt")` |

---

## 🧪 Practice Questions

1. Write a Python program to create a file `info.txt` and write your name and age in it.
2. Write a program to read and print each line of a file using a loop.
3. Append "Python is fun!" to an existing file without deleting its content.
4. Write a program that checks if a file exists before trying to open it.
5. Read a file and count the total number of lines in it.

---

> 💡 **Pro Tip:** Always use the `with` statement when working with files — it's cleaner, safer, and handles closing automatically!
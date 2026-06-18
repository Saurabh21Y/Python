# 🐍 Python Revision & Learning Repository

Welcome to the ultimate **Python Revision Repository**! This repo is a structured, chapter-wise learning log designed to master Python programming from the fundamentals up to data structures, algorithms, and practical application.

This repository tracks notes, hands-on code examples, interactive Jupyter Notebooks, and full-featured learning projects (games and tools) built along the way.

---

## 📂 Repository Structure & Directory Map

```text
Python/
├── Chapter 1/         # Intro to Python & PVM
├── Chapter 2/         # Comments & Variables
├── Chapter 3/         # Python Data Types
├── Chapter 4/         # String Data Type & Slicing
├── Chapter 5/         # Input & Output + Projects (Tip Calculator)
├── Chapter 6/         # Arithmetic, Assignment, Comparison & Logical Operators
├── Chapter 7/         # Conditional Statements + Projects (Treasure Island)
├── Chapter 8/         # Loops & Iterative Control Flow (Jupyter Notebooks)
├── Chapter 9/         # Functions & Modular Programming
├── Chapter 10/        # Data Structures (Lists, Tuples, Sets, Dictionaries)
└── pythonBOOK.pdf     # Reference Study Guide
```

---

## 🎮 Featured Learning Projects

Here are the interactive tools and games built as part of the hands-on learning process:

### 1. 🛠️ Tip Calculator (Chapter 5)
* **File:** [`Chapter 5/Tip_calc.py`](./Chapter%205/Tip_calc.py)
* **Objective:** A handy CLI utility to compute restaurant bills and splits. It takes the total bill amount, applies a custom tip percentage (e.g., 10%, 12%, 15%), and accurately calculates how much each person needs to pay when splitting the bill.

### 2. 🏰 Treasure Island Text Adventure Game (Chapter 7)
* **File:** [`Chapter 7/Treasure.py`](./Chapter%207/Treasure.py)
* **Objective:** A text-based role-playing game built using branching conditional logic (`if-elif-else`) and the `time` module to build suspense. It features:
  * Immersive storytelling and path choices (crossroads, dark forests, lake shores).
  * Inventory key tracking and dynamic ferryman riddles.
  * A 3-door castle final puzzle with secret trapdoor wins and multiple game-over conditions.

---

## 📚 Chapter-Wise Breakdown

| Chapter | Title & Focus | 📓 Notes | 💻 Code / Notebooks | Key Concepts Covered |
| :---: | :--- | :---: | :---: | :--- |
| **01** | **Introduction to Python** | [Notes.md](./Chapter%201/Notes.md) | — | Compiler vs. Interpreter, Python Virtual Machine (PVM), Origin of Python |
| **02** | **Comments & Variables** | [Notes.md](./Chapter%202/Notes.md) | [comments.py](./Chapter%202/comments.py)<br>[variable.py](./Chapter%202/variable.py) | Variable assignment, syntax, naming rules, Snake case convention, code documenting |
| **03** | **Python Data Types** | [Notes.md](./Chapter%203/Notes.md) | [Datatype.py](./Chapter%203/Datatype.py) | Numbers (`int`, `float`, `complex`), Strings (`str`), Booleans (`bool`), sequence preview |
| **04** | **Python String Data Type** | [Notes.md](./Chapter%204/Notes.md) | [String.py](./Chapter%204/String.py)<br>[TypeCasting.py](./Chapter%204/TypeCasting.py) | String indexing & slicing, string functions, Unicode (`ord`/`chr`), implicit/explicit type conversion |
| **05** | **Input and Output** | [Notes.md](./Chapter%205/Notes.md) | [I_O.py](./Chapter%205/I_O.py)<br>**[Tip_calc.py](./Chapter%205/Tip_calc.py)** | Formatted output (f-strings), `input()` handling, parsing values, **Tip Calculator Project** |
| **06** | **Python Operators** | [Notes.md](./Chapter%206/Notes.md) | [Arithimatic.py](./Chapter%206/Arithimatic.py)<br>[Assignment.py](./Chapter%206/Assignment.py)<br>[Comaprison.py](./Chapter%206/Comaprison.py)<br>[Logical.py](./Chapter%206/Logical.py) | Operators: Arithmetic, assignment shorthand, comparison logic, logical `and`/`or`/`not` |
| **07** | **Conditional Statements** | [Notes.md](./Chapter%207/Notes.md) | [Ternary.py](./Chapter%207/Ternary.py)<br>**[Treasure.py](./Chapter%207/Treasure.py)** | Control flow logic, `if-elif-else` architecture, ternary operator, **Treasure Island Game** |
| **08** | **Loops & Iterative Control** | [Notes.md](./Chapter%208/Notes.md) | [For_loop.ipynb](./Chapter%208/For_loop.ipynb)<br>[While_loop.ipynb](./Chapter%208/While_loop.ipynb) | Loop intuition, `while` condition loops, `for` sequence iterators, `break`/`continue`/`pass`, nested loops |
| **09** | **Functions & Modular Prep** | [Notes.md](./Chapter%209/Notes.md) | [User_fun.ipynb](./Chapter%209/User_fun.ipynb) | Custom functions, arguments vs parameters, default/keyword/positional args, single responsibility |
| **10** | **Built-in Data Structures** | [Notes.md](./Chapter%2010/Notes.md) | Detailed sub-chapters (below) | Overview of basic structures, classification (mutable vs. immutable, ordered vs. unordered) |

---

## 🗂️ Chapter 10: Deep-Dive into Data Structures

Chapter 10 contains comprehensive sub-modules for each built-in Python data structure:

* ### 📋 10.1 Lists
  * **Notes:** [`Chapter 10/Lists.md`](./Chapter%2010/Lists.md) | **Notebook:** [`Chapter 10/List.ipynb`](./Chapter%2010/List.ipynb)
  * **Topics:** Creation, indexing/slicing, list mutability, traversal, methods (`append`, `insert`, `pop`, `remove`, `sort`), and list practice labs.
* ### 🔒 10.2 Tuples
  * **Notes:** [`Chapter 10/Tuple.md`](./Chapter%2010/Tuple.md) | **Notebook:** [`Chapter 10/Tuple.ipynb`](./Chapter%2010/Tuple.ipynb)
  * **Topics:** Tuple immutability, creation patterns (single element gotcha), traversal, tuple packing/unpacking, list vs tuple comparisons, and tuple labs.
* ### ⚙️ 10.3 Sets
  * **Notes:** [`Chapter 10/Set.md`](./Chapter%2010/Set.md) | **Notebook:** [`Chapter 10/Set.ipynb`](./Chapter%2010/Set.ipynb)
  * **Topics:** Set uniqueness, unordered indexing, Python hashing mechanism, set methods (`add`, `discard`, `pop`), and mathematical operations (union, intersection, difference, symmetric difference).
* ### 📖 10.4 Dictionaries
  * **Notes:** [`Chapter 10/Dict.md`](./Chapter%2010/Dict.md) | **Notebook:** [`Chapter 10/Dict.ipynb`](./Chapter%2010/Dict.ipynb)
  * **Topics:** Key-value mappings, key uniqueness (hashability), Dictionary CRUD operations, traversal, dict methods (`keys`, `values`, `items`, `get`, `update`), and dictionary practice labs.

---

## 🛠️ Repository Utilities

* **`pythonBOOK.pdf`**: The master PDF book used as the reference material for standard study material.

---
*Happy coding! Keep practicing and updating your progress.* 🚀

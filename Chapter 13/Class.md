# 🐍 Python OOPs - Lecture 02: Understanding Classes, Attributes & Methods

Welcome back, class! 🎓

In today's lecture, we deep-dive into the building blocks of Object-Oriented Programming: **Classes**. Think of this as the architectural planning phase of your programming journey.

---

## 🏗️ What is a Class?

A **class** is a blueprint, template, or prototype for creating objects. 

> [!NOTE]
> **The House Analogy 🏠**
> Imagine an architect's blueprint for a house.
> *   **The Class** is the blueprint. It defines where the rooms, windows, doors, and pipes go, but you cannot live in it.
> *   **The Object** is the actual physical house built using that blueprint. You can build multiple distinct houses from that single blueprint!

---

## 🛠️ Syntax of a Class in Python

Creating a class in Python is straightforward. We use the `class` keyword followed by the class name, conventionally written in **PascalCase** (e.g., `MyClass`, `SmartCar`).

Here is the simplest class definition from today's blackboard:

```python
class Car:
    brand = "Toyota" # An attribute (variable)
```

---

## 🧬 Anatomy of a Class: Attributes and Methods

A class is essentially made of two types of members:

### 1. Attributes (Data)
*   **Definition:** Variables defined inside a class that hold data related to the class/object.
*   *Example:* The brand of a car, the name of a student, or the species of an animal.

### 2. Methods (Behavior)
*   **Definition:** Functions defined inside a class that describe what the class/object can do.
*   **The `self` parameter:** In Python, methods must take `self` as their first parameter. This refers to the specific object that is calling the method.

---

## 🐾 Classroom Code Examples

Let's look at the class code snippets captured during today's session:

### Example 1: The Cat Class (Direct Access Demonstration)
This snippet shows how to define attributes and methods, and how to access them directly using an on-the-fly instance.

```python
class Animal:
    type = "Cat" # Attribute

    def sound(self): # Method
        print("Meow!")

# Directly accessing attributes and calling methods using a temporary instance
print(Animal().type)       # Access attribute -> Output: Cat
Animal().sound()           # Call method      -> Output: Meow!
```

> [!WARNING]
> **Professor's Tip on `Animal()` vs Variable Instantiation:**
> Writing `Animal().type` creates a temporary object in memory, reads the attribute, and immediately discards it.
> Typically, in real-world code, you should instantiate the class to a variable first, like this:
> ```python
> my_cat = Animal()
> print(my_cat.type)
> my_cat.sound()
> ```

---

### Example 2: The Dog Class
Here is another example we discussed, modeling a dog:

```python
class Animal:
    species = "Dog" # Attribute

    def make_sound(self): # Method
        print("Bark!")
```

---

## 📊 Summary Comparison: Attributes vs. Methods

| Aspect | Attributes | Methods |
| :--- | :--- | :--- |
| **What it is** | Variable inside a class | Function inside a class |
| **Represents** | State/Properties (e.g., color, height, type) | Action/Behavior (e.g., fly, run, sound) |
| **Access Syntax** | `object.attribute_name` (no parentheses) | `object.method_name()` (needs parentheses) |

---

> [!TIP]
> **Recommended Reference:**
> To practice building classes, check out the classes section on **Sheryians Coding School** or the Python Documentation on classes.

---

## 📝 Professor's Homework Challenge
1. Create a class called `Book` with attributes `title` and `author`.
2. Add a method `read(self)` that prints `"You are reading [title] by [author]"`.
3. Create an instance of the `Book` class and call its method.

See you all in the next lecture! 🚀

---

# 🔥 Missing Pro-Level Concepts to Add

## Class Naming Rules
- Use `class` keyword.
- Follow **PascalCase** (`Student`, `BankAccount`).
- One file can contain **multiple classes**.

## What a Class Contains
1. Attributes (Data)
2. Methods (Behaviour)
3. Constructor (`__init__`)
4. Class Variables
5. Instance Variables

## Types of Attributes
### Class Attribute
Shared by every object.

### Instance Attribute
Unique for every object and usually created inside `__init__`.

## Types of Methods
- Instance Method (`self`)
- Class Method (`@classmethod`) *(later)*
- Static Method (`@staticmethod`) *(later)*

## Important Facts
- A class itself occupies memory only once.
- Objects occupy separate memory.
- Multiple objects can be created from a single class.
- Multiple classes can exist in one Python file.
- One object belongs to exactly one class.

## Frequently Asked Interview Questions
- Difference between class and object?
- Difference between class attribute and instance attribute?
- Why is `self` required?

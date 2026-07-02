# Python OOP: Abstraction, Abstract Base Classes (ABCs), & Interface Contracts

---

# 1. Definition

## Abstraction
**Abstraction** is the OOP concept of hiding complex implementation details from the user and exposing only the essential interface features. It allows developers to interact with a system at a higher level of comprehension without needing to know *how* it works under the hood.

## Abstract Base Class (ABC)
An **Abstract Base Class** is a class that cannot be instantiated directly and is designed to be used as a blueprint for other classes. It defines a set of **Abstract Methods** (methods declared but left unimplemented) that all concrete subclasses must implement.

![alt text](<mermaid-drawing (4).png>)

---

# 2. Why Do We Need It?

### The Problem of Missing Interface Enforcement
Without abstraction contracts, there is no compiler or interpreter-enforced rule requiring developers to implement specific methods in subclass definitions.

```python
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement make_sound")

class Dog(Animal):
    pass  # Forgot to implement make_sound

d = Dog()
d.make_sound()  # Crashes only at runtime during execution!
```
* **Explanation**: Demonstrates how standard class hierarchies fail to prevent instantiation of incomplete child classes.
* **Expected Output**: `NotImplementedError: Subclasses must implement make_sound`
* **Memory Explanation**: Instantiates the `Dog` object on the heap, but crashes when looking up the unimplemented method.
* **Time/Space Complexity**: $\mathcal{O}(1)$ runtime crash.
* **Common Mistakes**: Finding interface bugs only at runtime during system execution.
* **Best Practices**: Use Abstract Base Classes to catch interface compliance issues at instantiation time.

#### Issues:
1. **Late Crash Detection**: Failures occur only when the missing method is actually called during runtime execution.
2. **Inconsistent Interfaces**: Different developers might name identical behaviors differently (e.g., `make_sound()` vs `sound()` vs `bark()`).
3. **Weak System Architecture**: Large applications lose structural predictability, making automated pipelines brittle.

---

# 3. Real-Life Analogies

### Analogy: The Wall Socket
* **The Abstract Interface**: A standard electrical wall outlet. It defines a physical socket interface with specific dimensions and voltage levels (the abstract contract).
* **Concrete Implementations**: A television, a toaster, or a laptop charger. Each device implements the power plug differently, but they all conform to the exact layout of the wall socket.
* **The Abstraction**: You do not need to understand how the power plant generates electricity or how the grid distributes it; you only need to match your plug to the socket layout to draw power.

---

# 4. Syntax

```python
from abc import ABC, abstractmethod

# 1. Defining the Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass

# 2. Implementing a Concrete Subclass
class Car(Vehicle):
    def start_engine(self) -> None:
        print("Car engine started: Vroom!")
```
* **Explanation**: Illustrates importing the `abc` library, defining a template interface, and building a concrete class that implements it.
* **Expected Output**: Compiles and executes.
* **Memory Explanation**: Python registers `Vehicle` as abstract. Attempts to instantiate `Vehicle()` fail. `Car()` succeeds because it overrides `start_engine`.
* **Time Complexity**: $\mathcal{O}(1)$ lookup.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.
* **Common Mistakes**: Forgetting to inherit from `ABC` when defining an abstract class.
* **Best Practices**: Define abstract methods with no body (use `pass`).

---

# 5. Syntax Breakdown

Let's dissect the abstraction keywords:

* **`from abc import ABC, abstractmethod`**: Imports the **Abstract Base Classes** module infrastructure.
* **`class Vehicle(ABC)`**: Inheriting from `ABC` flags the class as an abstract base class.
* **`@abstractmethod`**: A decorator that flags the decorated method as abstract. The Python interpreter will refuse to instantiate any class that inherits this method without overriding it.

---

# 6. Memory Diagram

When you try to run `v = Vehicle()` vs `c = Car()`:

```
HEAP (Metaclass Instantiation Checks)
=========================================================
| Class Name | __abstractmethods__ set | Instantiable?  |
=========================================================
| Vehicle    | {'start_engine'}        | No (TypeError) |
| Car        | set() (Empty)           | Yes            |
=========================================================
```

* **Explanation**: The metaclass `ABCMeta` maintains a set of unimplemented method names. If the set is not empty, Python rejects calls to the constructor and raises a `TypeError`.

---

# 7. Internal Working (Behind the Scenes)

## The Metaclass `ABCMeta`
Under the hood:
1. When you define a class inheriting from `ABC`, Python sets its metaclass to `abc.ABCMeta`.
2. `ABCMeta` intercepts class creation. It checks all methods decorated with `@abstractmethod` and adds their names to the `__abstractmethods__` internal set attribute.
3. During class instantiation, the built-in `__new__` allocator inspects `__abstractmethods__`. If the set contains any elements, it prevents memory allocation and raises a `TypeError`.

---

# 8. Rules

### Abstraction Rules
1. **No Direct Instantiation**: You cannot instantiate an abstract base class directly.
2. **Complete Subclass Implementations**: A concrete subclass must implement **all** abstract methods defined in its parent chain to be instantiable.
3. **Concrete Methods in ABCs**: Abstract classes can contain normal, fully implemented concrete methods alongside abstract methods.

---

# 9. Naming Conventions (PEP 8)

* Use PascalCase for abstract class names.
* Use clear, descriptive action verbs for abstract method interfaces.

| Class Type | Bad Example | Good Example | Industry Standard |
| :--- | :--- | :--- | :--- |
| Abstract Class | `db_connector` | `DatabaseConnector` | `AbstractDatabaseAdapter` |

---

# 10. Common Mistakes & Bugs

### Mistake 1: Instantiating Abstract Classes Directly
```python
# BUGGY CODE
from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def connect(self):
        pass

db = DB()  # Raises TypeError!
```
* **Expected Output**: `TypeError: Can't instantiate abstract class DB with abstract method connect`
* **How to avoid**: Only instantiate concrete subclass objects.

---

### Mistake 2: Missing one of multiple abstract methods in subclasses
```python
# BUGGY CODE
class API(ABC):
    @abstractmethod
    def get(self): pass

    @abstractmethod
    def post(self): pass

class Client(API):
    def get(self):
        return "data"
    # Missing post() method override!

c = Client()  # Raises TypeError!
```
* **Why it happens**: Failing to implement *every* abstract method keeps the child class abstract.
* **How to avoid**: Override all abstract methods in the concrete child class.

---

# 11. Best Practices & Pythonic Code

* **Use Abstract Classes to Establish Strict System Boundaries**: Use them when defining plug-in architectures or adapter patterns.
```python
# Pythonic Interface Design
class MailGateway(ABC):
    @abstractmethod
    def send_mail(self, recipient: str, message: str) -> bool:
        pass
```

---

# 12. Interview Questions

### Q1. Can an abstract class in Python have a constructor (`__init__`)?
* **Answer**: Yes. An abstract class can define an `__init__` constructor. It cannot be used to instantiate the abstract class directly, but it is called from child classes via `super().__init__()` to initialize shared base attributes.

---

### Q2. What happens if a subclass does not implement a parent's abstract method?
* **Answer**: The subclass remains abstract itself. If you attempt to instantiate it, Python raises a `TypeError` indicating that the class cannot be instantiated because of the missing method implementation.

---

### Q3. Tricky Output Question
**What is the output of the following code?**
```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def show(self):
        print("Base Show")

class Derived(Base):
    def show(self):
        super().show()
        print("Derived Show")

d = Derived()
d.show()
```
* **Expected Output**:
  ```
  Base Show
  Derived Show
  ```
* **Explanation**: Abstract methods in Python can have an implementation in the base class. Concrete subclasses must still override them, but they can call the base implementation using `super()`.

---

# 13. Exam Points

* **`abc`**: The standard library module used to implement abstract classes.
* **`@abstractmethod`**: The decorator used to flag methods that must be overridden in subclasses.
* **`TypeError`**: The exception class raised when trying to instantiate abstract classes.

---

# 14. Real-World Examples

## Example 1: Database Adapter System
```python
from abc import ABC, abstractmethod

class DatabaseAdapter(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str) -> list:
        pass

class MySQLAdapter(DatabaseAdapter):
    def connect(self) -> None:
        print("Connecting to MySQL Database...")

    def execute_query(self, query: str) -> list:
        print(f"Executing MySQL query: {query}")
        return ["MySQL Row 1", "MySQL Row 2"]

# Execution
db: DatabaseAdapter = MySQLAdapter()
db.connect()
print(db.execute_query("SELECT * FROM users"))
```
* **Explanation**: Establishes a database interface that concrete adapters must implement.
* **Expected Output**:
  ```
  Connecting to MySQL Database...
  Executing MySQL query: SELECT * FROM users
  ['MySQL Row 1', 'MySQL Row 2']
  ```
* **Time Complexity**: $\mathcal{O}(1)$ dynamic dispatch.

---

# 15. Mini Practice

### Easy
Define an abstract class `Device` with an abstract method `turn_on()`. Subclass it as `Phone`.

### Medium
Create an abstract class `Shape` with abstract methods `area()` and `perimeter()`. Implement them in a concrete `Rectangle` subclass.

### Hard
Write an abstract class with a defined constructor, inherit it in a subclass, and demonstrate calling the base constructor while implementing the required abstract methods.

---

# 16. Summary Table

| Property | Abstract Class | Concrete Class |
| :--- | :--- | :--- |
| **Instantiable** | No | Yes |
| **Can contain abstract methods**| Yes | No |
| **Metaclass dependency** | `abc.ABCMeta` | Standard `type` |

---

# 17. Cheat Sheet

```python
# Setup Base
from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def action(self):
        pass

# Implement Child
class Concrete(Interface):
    def action(self):
        # Implementation
        pass
```

---

# 18. Flow Diagram

```mermaid
graph TD
    A[Instantiate Object: ClassName()] --> B{Are abstract methods missing implementation?}
    B -- Yes --> C[Raise TypeError]
    B -- No --> D[Allocate memory on Heap & run __init__]
```

---

# 19. Comparison Table

| Feature | Abstraction | Encapsulation |
| :--- | :--- | :--- |
| **Focus** | Design-level blueprints (what a class does) | Implementation-level safety (hiding class details) |
| **Mechanism**| Abstract Base Classes & methods | Private variables & public getter/setter properties |

---

# 20. Things to Remember

> [!IMPORTANT]
> **Key takeaways on Abstraction:**
> 1. **Inherit from ABC**: An abstract class must inherit from `ABC` and contain at least one `@abstractmethod` to prevent instantiation.
> 2. **Interfaces are contracts**: Use abstract base classes to enforce API consistency across your codebase.
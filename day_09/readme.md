
---

### Day_09 of 100 days of Mastering Agentic AI

# 🧱 Object-Oriented Programming (OOP) in Python

Welcome to your complete guide to **Object-Oriented Programming (OOP)** in Python — a powerful programming paradigm that helps you write **cleaner, reusable, and scalable code**.

In this guide, you’ll learn:
- What OOP is and why it matters
- How it compares to other approaches
- The core concepts: **Classes, Objects, Attributes, Methods**
- And how to use them in real programs

Let’s begin!

---

## 🔁 Programming Paradigms: A Quick Comparison

Before diving into OOP, let’s understand **how we’ve been writing code** so far — and why OOP is better for complex programs.

### 1. Imperative Approach (Basic Variables)

```python
a = 12
b = 12
print(a + b)  # Output: 24
```

> ❌ Problem: Need new variables every time you want to add different numbers.

---

### 2. Functional Approach (Using Functions)

```python
def add(a, b):
    return a + b

print(add(12, 12))  # 24
print(add(14, 12))  # 26
```

> ✅ Better: Reusable logic. No need to create new variables each time.

But still limited when dealing with **real-world entities** like users, cars, or bank accounts.

---

### 3. Object-Oriented Approach (OOP)

```python
class Addition:
    def __init__(self, a, b):
        print(a + b)

obj = Addition(14, 33)  # Output: 47
```

> ✅ Best: Organizes data and behavior together using **objects**.

---

## 🧩 What is OOP?

**OOP (Object-Oriented Programming)** is a programming paradigm based on the concept of **"objects"**, which are instances of **classes** that contain:

- **Data (attributes)** — like name, age, color
- **Code (methods)** — functions that operate on the data

> 💡 Think of an object as a **smart container** that holds both data and actions.

OOP makes it easier to model real-world things in code.

---

## 🏗️ Why Use OOP?

| Benefit | Description |
|--------|-------------|
| **Reusability** | Write once, use many times |
| **Modularity** | Break complex programs into manageable pieces |
| **Scalability** | Easy to extend and maintain |
| **Real-world modeling** | Represent people, cars, products, etc., naturally |

---

## 🏗️ Core Concepts of OOP

We’ll cover these in detail:
1. ✅ **Classes & Objects** ← This section
2. 🔐 Encapsulation
3. 🧬 Inheritance
4. 🔄 Polymorphism
5. 🧱 Abstraction

Let’s start with **Classes and Objects** — the foundation of OOP.

---

# 🏗️ Classes and Objects

### 🧱 What is a Class?

A **class** is a **blueprint** or **template** for creating objects.

> 🏡 Think of a class as the architectural plan of a house.  
> The house itself? That’s the **object**.

#### ✅ Syntax: Creating a Class

```python
class Car:
    brand = "Toyota"
```

- `class` → keyword to define a class
- `Car` → name of the class (PascalCase convention)
- `brand = "Toyota"` → an **attribute** (data)

---

### 🔩 What’s Inside a Class?

A class can contain two main things:

| Component | Description | Example |
|---------|-------------|--------|
| **Attributes** | Variables that hold data | `brand = "Toyota"` |
| **Methods** | Functions that define behavior | `def start_engine(self): ...` |

---

### 🧰 Example: Simple Class with Attribute and Method

```python
class Animal:
    species = "Dog"  # Attribute

    def make_sound(self):  # Method
        print("Bark!")
```

> 🔁 `self` refers to the instance (object) calling the method. We’ll explain it soon!

---

### 🚶‍♂️ Creating Objects (Instances)

An **object** is a real instance created from a class.

```python
dog = Animal()  # Create an object
```

Now you can access its attributes and methods:

```python
print(dog.species)      # Output: Dog
dog.make_sound()        # Output: Bark!
```

Each object is independent — you can create many:

```python
cat = Animal()
cat.species = "Cat"

print(cat.species)      # Output: Cat
cat.make_sound()        # Output: Bark! (still — behavior is shared)
```

---

### 🧱 Anatomy of a Class

```python
class Car:
    # 👇 Class Attribute (shared by all objects)
    wheels = 4

    # 👇 Constructor (called when object is created)
    def __init__(self, brand, color):
        self.brand = brand   # 👈 Instance Attribute
        self.color = color   # 👈 Instance Attribute

    # 👇 Instance Method
    def info(self):
        print(f"This car is a {self.color} {self.brand} with {self.wheels} wheels.")
```

#### ✅ Creating Objects

```python
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.info()  # This car is a Red Toyota with 4 wheels.
car2.info()  # This car is a Blue Honda with 4 wheels.
```

---

### 🔍 Understanding `__init__` and `self`

#### `__init__` – The Constructor

- A special method that runs **automatically** when an object is created.
- Used to initialize (set up) object attributes.

```python
def __init__(self, brand, color):
    self.brand = brand
    self.color = color
```

#### `self` – The Instance Reference

- Refers to the **current object** being created or used.
- Required as the **first parameter** in every method.

> 🧠 Without `self`, Python wouldn’t know which object’s data to use.

---

### 📥 Accessing Attributes and Methods

You access class members using the **dot notation** (`.`):

```python
obj.attribute
obj.method()
```

#### Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

# Create object
p = Person("Alice", 25)

# Access attributes and methods
print(p.name)     # Alice
print(p.age)      # 25
p.greet()         # Hello, I'm Alice and I'm 25 years old.
```

---

## 🎯 Real-World Example: Bank Account

Let’s build a simple `BankAccount` class:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance
```

#### ✅ Using the Class

```python
acc = BankAccount("Alice", 100)

acc.deposit(50)           # Deposited 50. New balance: 150
acc.withdraw(30)          # Withdrew 30. New balance: 120
print(acc.get_balance())  # 120
```

> ✅ This shows how OOP bundles **data (owner, balance)** and **actions (deposit, withdraw)** together.

---

## 🧩 Key Takeaways

| Concept | Meaning |
|-------|--------|
| **Class** | Blueprint for creating objects |
| **Object** | Instance of a class |
| **Attribute** | Data stored in an object (`self.name`) |
| **Method** | Function inside a class (`def greet()`) |
| `__init__` | Constructor — runs on object creation |
| `self` | Refers to the current object |

---

## 💡 Practice Questions

1. Create a `Student` class with `name`, `roll_no`, and `marks`. Add a method to display info.
2. Create a `Rectangle` class with `length` and `width`. Add methods to calculate area and perimeter.
3. Create a `Circle` class with `radius`. Add methods for area and circumference.
4. Modify the `BankAccount` class to prevent negative balance.
5. Create two objects of the same class and compare their attributes.

---

## 🏁 Summary

| Feature | Supported |
|-------|-----------|
| Bundles data and behavior | ✅ Yes |
| Reusable through classes | ✅ Yes |
| Models real-world entities | ✅ Yes |
| Uses `class`, `object`, `self`, `__init__` | ✅ Yes |

> OOP might feel abstract at first — but once you start building with classes, you’ll see how powerful and natural it is.

---

## 🚀 What’s Next?

Now that you understand **Classes and Objects**, we’ll dive into:
- 🔐 **Encapsulation** – Protecting data
- 🧬 **Inheritance** – Reusing and extending classes
- 🔄 **Polymorphism** – Same interface, different behavior
- 🧱 **Abstraction** – Hiding complex details

Each concept builds on this foundation.

---

## 🙌 Happy Coding!

> "OOP doesn’t just organize code — it organizes **thinking**."  
> You’re now on your way to writing professional-grade Python.

🐍 Keep practicing. Keep building.



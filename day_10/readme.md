
---

### Day_10 of leanning python

# 📝 Object-Oriented Programming (OOP) in Python – Notes

This document explains the core concepts of **Objects, Classes, Constructors, Attributes, and Methods** in Object-Oriented Programming using simple analogies and examples.

---

## 🧱 1. What is an Object?

An **object** is an instance of a **class**. Think of it like this:

> Imagine you have a **bag factory** that produces bags based on a blueprint.
>
> - The **blueprint** = **Class**
> - Each company (Reebok, Campus, etc.) gives their own specifications → creates their own **bag**
> - These **bags** = **Objects**

So, multiple objects can be created from a single class, each with its own data.

### ✅ Object Syntax

To create an object, simply call the class and assign it to a variable.

```python
class Fruit:
    name = "Apple"

# Creating an object
fruit = Fruit()

# Accessing attributes
print(fruit.name)  # Output: Apple
```

> 🔹 The object `fruit` now has access to all attributes and methods defined in the `Fruit` class.

---

## 🔧 2. Constructor (`__init__` method)

A **constructor** is a special method that runs automatically when an object is created.

It is used to initialize **instance attributes** (data specific to each object).

We use the `__init__(self, ...)` method for this.

### Why do we need a constructor?

Without a constructor, we can't pass values during object creation (like user input). Just like functions use parameters, classes use constructors to accept arguments.

```python
class Student:
    def __init__(self, name):
        self.name = name  # instance attribute

# Creating an object with value
student = Student("Ali")

# Accessing the attribute
print(student.name)  # Output: Ali
```

> 🔹 `self` refers to the current object being created. It ensures that data is stored in the correct object’s memory space.

> 🔹 Multiple objects will have their own separate copies of instance variables.

---

## 🏷️ 3. Types of Attributes

### 1. Class Attribute

- Belongs to the **class itself**, not any specific object.
- Shared across all instances.

```python
class Car:
    wheels = 4  # class attribute
```

> All cars have 4 wheels by default unless changed.

### 2. Instance Attribute

- Defined inside the constructor using `self`.
- Unique to each object.

```python
    def __init__(self, color):
        self.color = color  # instance attribute
```

### Example:

```python
class Car:
    wheels = 4  # class attribute

    def __init__(self, color):
        self.color = color  # instance attribute

car1 = Car("Red")
car2 = Car("Blue")

print(car1.wheels)   # Output: 4
print(car2.color)    # Output: Blue
```

> 🔹 `wheels` is shared; `color` is unique per object.

---

## ⚙️ 4. Types of Methods

### 1. Instance Method

- Operates on **instance data**.
- Can access and modify instance attributes.
- Takes `self` as the first parameter.

```python
class MyClass:
    def instance_method(self):
        print("This is an instance method")
```

#### Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.bark()  # Output: Buddy says Woof!
```

---

### 2. Class Method

- Works with the **class**, not individual objects.
- Uses `@classmethod` decorator.
- Takes `cls` as the first parameter (refers to the class).

```python
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")
```

#### Example:

```python
class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species

print(Person.get_species())  # Output: Human
```

> 🔹 Useful for alternative constructors or working with class-level data.

---

### 3. Static Method

- Does **not** access class or instance data.
- Behaves like a regular function but belongs to the class namespace.
- Uses `@staticmethod` decorator.
- No `self` or `cls` needed.

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")
```

#### Example:

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # Output: 8
```

> 🔹 Used for utility functions related to the class but not dependent on its state.

---

## 🧠 Summary Table

| Feature           | Belongs To     | Accesses       | Decorator       | First Param |
|-------------------|----------------|----------------|------------------|-------------|
| Instance Method   | Object         | Instance data  | None             | `self`      |
| Class Method      | Class          | Class data     | `@classmethod`   | `cls`       |
| Static Method     | Class (namespace) | Nothing     | `@staticmethod`  | None        |

---

## 🎯 Real-World Analogy: Bag Factory

Let’s tie it all together!

```python
class BagFactory:
    material_type = "Polyester"  # class attribute

    def __init__(self, company, zips, pockets):
        self.company = company  # instance attributes
        self.zips = zips
        self.pockets = pockets

    def describe(self):  # instance method
        print(f"{self.company} bag: {self.zips} zips, {self.pockets} pockets")

    @classmethod
    def get_material(cls):  # class method
        return cls.material_type

    @staticmethod
    def is_bag_valid(zips, pockets):  # static method
        return zips > 0 and pockets >= 0

# Creating objects
reebok_bag = BagFactory("Reebok", 3, 2)
campus_bag = BagFactory("Campus", 2, 1)

# Using instance method
reebok_bag.describe()  # Output: Reebok bag: 3 zips, 2 pockets

# Using class method
print(BagFactory.get_material())  # Output: Polyester

# Using static method
print(BagFactory.is_bag_valid(2, 1))  # Output: True
```

> ✅ Each company gets its own customized bag (object), but they share common traits (class attributes/methods).

---

## 📌 Key Takeaways

- **Class** → Blueprint
- **Object** → Instance made from the blueprint
- **Constructor (`__init__`)** → Initializes object-specific data
- **`self`** → Points to the current object
- **Class vs Instance Attributes** → Shared vs Unique data
- **Instance, Class, Static Methods** → Different ways to organize behavior

---

📘 *Now you're ready to build powerful, reusable code using OOP!*  
🎥 *For visual explanation, watch the linked video carefully — especially how `self` targets different object locations.*

---

**Created by**: [Your Name]  
📅 **Date**: April 2025  
🎯 **Topic**: Introduction to OOP in Python

---


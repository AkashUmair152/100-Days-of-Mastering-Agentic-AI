# Day 01: Python Setup & Basics

Welcome to Day 01 of **100 Days of Mastering Agentic AI**! Here’s a summary of what I learned today.

## Downloading Python

- Visit the [official Python website](https://www.python.org/downloads/) and download Python for your operating system.
- Install Python to get the Python Virtual Machine, which runs your code.

## Downloading an IDE

- **IDE** stands for *Integrated Development Environment*.
- You can write and run Python code directly, but using an IDE is recommended.
- Popular IDEs: VS Code, PyCharm, Jupyter.
- For this course, we’ll use **VS Code**.

## Setting Up & First Program

- In VS Code, install the **Python** and **Code Runner** extensions.
- Create your first Python program (not just "Hello World"!).

## Comments & Variables

### Comments

- Comments are ignored by the Python interpreter.
- Single-line comment: `# This is a comment`
- Multiline comments: Use docstrings (`""" Multiline comment """`).

### Variables

- Variables store data in Python.
- Example: `name = "Akash"`, `age = 12`
- Rules:
  - Cannot start with a number.
  - No spaces or special characters.
  - Naming styles: `sheryiansSchool`, `SheryiansSchool`, `sheryians_school`.

## Data Types in Python

- **Numbers**: `int`, `float`, `complex`
- **Strings**: Store text, use quotes (`"text"` or `'text'`)
- **Boolean**: `True` or `False`

## Strings & Type Conversion

- Strings use more space due to Unicode encoding.
- Use `ord()` to get Unicode value, `chr()` to convert back.
- String indexing: `a = "Hello"` → `a[0]` is `"H"`, `a[-1]` is `"o"`
- String slicing: `a[start:stop:step]`

## Type Conversion

- Convert between types using functions: `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, `bool()`
- **Implicit conversion**: Python automatically converts types (e.g., `print(12/2)` gives `6.0`).
- **Explicit conversion**: Use conversion functions manually.

### Truthy & Falsy Values

- Only 7 values are falsy: `0`, `0.0`, `False`, `""`, `[]`, `{}`, `None`
- Everything else is truthy.

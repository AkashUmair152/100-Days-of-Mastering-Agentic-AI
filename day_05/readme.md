# 📚 Python Functions – Beginner's Guide

## What Are Functions?

In Python, **functions** are blocks of reusable code designed to perform a specific task. They help you avoid repetition, make your code modular, and improve readability.

There are two types of functions:

- **Built-in functions**: Already available in Python (e.g., `print()`, `input()`, `len()`).
- **User-defined functions**: Created by you using the `def` keyword.

To define a function:

1. Use the `def` keyword.
2. Give it a name.
3. Add parentheses `()` — parameters go inside.
4. End with a colon `:`.
5. Indent the code block that follows.

To execute the function, simply **call it** using its name followed by parentheses.

---

### ✅ Example: Simple Function

```python
def hello_world():
    print("Hello World this is a function")

hello_world()
```

**Output:**

```
Hello World this is a function
```

> 🔁 This function runs only when called.

---

## Parameters and Arguments

### 🔹 Parameters

Parameters are **variables** listed inside the parentheses in the function definition.

```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")
```

### 🔹 Arguments

Arguments are the **actual values** passed to the function when it is called.

```python
greet("Akash")  # "Akash" is an argument
```

So:

- `name` → parameter (placeholder)
- `"Akash"` → argument (actual value)

---

### 📌 Rules

- Number of arguments must match the number of parameters unless defaults are used.
- Order matters in **positional arguments** — the first argument goes to the first parameter, and so on.

---

## Types of Arguments

Python supports three main types of arguments:

### 1. 🟢 Positional Arguments

Arguments passed in order. The position determines which parameter they assign to.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 30)
```

**Output:**

```
My name is Alice and I am 30 years old.
```

> ⚠️ If you switch the order: `introduce(30, "Alice")`, the output will be incorrect!

---

### 2. 🟡 Default Arguments

You can assign a default value to a parameter. If no argument is provided, the function uses the default.

```python
def greet(name="Akash"):
    print(f"Hello, {name}!")

greet()         # No argument → uses default
greet("Bob")
```

**Output:**

```
Hello, Akash!
Hello, Bob!
```

> ✅ Makes functions more flexible and prevents errors when arguments are missing.

---

### 3. 🔵 Keyword Arguments

You can pass arguments by specifying the parameter name. This allows **any order**.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="Charlie")   # Order doesn't matter
introduce(name="Diana", age=28)
```

**Output:**

```
My name is Charlie and I am 30 years old.
My name is Diana and I am 28 years old.
```

> ✅ Useful when functions have many parameters.

---

## Return Statement

Functions can return a value using `return`. This allows you to use the result elsewhere in your program.

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)  # Output: 15
```

> 💡 Without `return`, the function returns `None`.

---

## Complete Example Code

```python
# 1. Simple function
def hello_world():
    print("Hello World this is a function")

hello_world()

# 2. Function with parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 3. Function with return
def sum(a, b):
    return a + b

print(sum(3, 4))  # Output: 7

# 4. Multiple parameters (positional)
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 30)

# 5. Default argument
def greet(name="Akash"):
    print(f"Hello, {name}!")

greet()
greet("Bob")

# 6. Keyword arguments
introduce(age=30, name="Charlie")
introduce(name="Diana", age=28)
```

---

## ✅ Summary

| Type | Description | Example |
|------|-------------|--------|
| **Positional** | Based on order | `greet("Alice")` |
| **Default** | Uses fallback value | `def greet(name="Akash")` |
| **Keyword** | Passed by name | `introduce(name="Bob", age=25)` |

---

## 💡 Tips

- Always give meaningful names to functions (`calculate_area`, not `func1`).
- Use comments or docstrings to explain what the function does.
- Test your functions with different inputs.
- Avoid side effects — keep functions focused on one task.

---

## 🚀 Practice Ideas

- Write a function to check if a number is even.
- Create a function that returns the square of a number.
- Build a function that takes a list and returns the sum.

```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
```

---

## 🙌 Happy Coding

Functions are the building blocks of clean, efficient Python programs. Start small, practice often, and soon you'll write powerful, reusable code!

> *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."* – Martin Fowler


---

# 🧱 **Data Structures in Python**  

### A Complete Guide to Built-in Data Structures

Welcome to your comprehensive guide to **Python’s built-in data structures**:  
➡️ `List`, `Tuple`, `Dictionary`, and `Set`.

This guide is designed for beginners and learners who want to **understand not just the syntax**, but also the **purpose, use cases, and practical applications** of each structure.

> 💡 While custom data structures like Stack, Queue, and Linked List exist (part of DSA — Data Structures & Algorithms), this document focuses only on **Python’s built-in data types**.

---

## 📦 Why Use Data Structures?

Data structures help you:

- Store multiple values efficiently
- Organize data logically
- Perform operations like search, sort, and filter
- Write clean and scalable code

Python makes this easy with four powerful built-in tools:

| Structure | Ordered | Mutable | Duplicates | Syntax |
|---------|--------|--------|-----------|--------|
| `List` | ✅ Yes | ✅ Yes | ✅ Yes | `[1, 2]` |
| `Tuple` | ✅ Yes | ❌ No | ✅ Yes | `(1, 2)` |
| `Dictionary` | ✅ (since 3.7+) | ✅ Yes | ❌ Keys only | `{'a': 1}` |
| `Set` | ❌ No | ✅ Yes | ❌ No | `{1, 2}` |

Let’s dive into each one in detail.

---

# 📋 1. List – Ordered & Mutable Collection

A **list** is an ordered, changeable (mutable), and flexible collection that can store multiple items — even of different types.

## 🔑 Key Features

| Feature | Description |
|-------|-------------|
| **Ordered** | Maintains insertion order |
| **Mutable** | Can modify after creation |
| **Duplicates allowed** | Same value can appear multiple times |
| **Heterogeneous** | Mix integers, strings, booleans, etc. |

### ✅ Example

```python
mixed = [1, "apple", True, 3.14, [5, 6]]
print(mixed)  # Output: [1, 'apple', True, 3.14, [5, 6]]
```

---

### 🛠️ Creating a List

Use square brackets `[]`.

```python
fruits = ["Apple", "Banana", "Cherry"]
numbers = [1, 2, 3, 4, 5]
empty = []
```

---

### 🔢 Indexing & Slicing

Just like strings, lists support indexing and slicing.

```python
nums = [10, 20, 30, 40, 50]

print(nums[0])     # 10
print(nums[-1])    # 50
print(nums[1:4])   # [20, 30, 40]
print(nums[::-1])  # [50, 40, 30, 20, 10] ← Reverse
```

> ✅ Unlike strings, **lists are mutable** — you can change elements!

```python
nums[1] = 99
print(nums)  # [10, 99, 30, 40, 50]
```

---

### 🔁 Traversing a List

Two ways to loop:

#### 1. By Index

```python
for i in range(len(fruits)):
    print(fruits[i])
```

#### 2. Direct Iteration (Recommended)

```python
for fruit in fruits:
    print(fruit)
```

---

### 🧰 Common List Methods

```python
numbers = [1, 2, 3, 4, 5]

numbers.append(10)           # Add at end
numbers.insert(2, 15)        # Insert at index 2
numbers.extend([20, 25, 30]) # Add multiple items

numbers.remove(3)            # Remove first occurrence
popped = numbers.pop()       # Remove last item

idx = numbers.index(4)       # Get index of 4
cnt = numbers.count(2)       # Count occurrences

numbers.sort()               # Sort ascending
numbers.reverse()            # Reverse order

copy = numbers.copy()        # Shallow copy
numbers.clear()              # Remove all items
```

> ⚠️ `extend()` takes an iterable: `extend([20, 25, 30])`, not `extend(20,25,30)`.

---

### 💡 When to Use Lists?

- Store dynamic collections (e.g., user inputs, scores)
- Need to modify data later
- Maintain order and allow duplicates
- Use as stacks or queues (with `append()` and `pop()`)

---

### 🎯 Practice Questions

1. Print positive and negative numbers from a list.
2. Find the mean (average) of list elements.
3. Find the largest number and its index.
4. Check if a list is sorted.
5. Remove duplicates while preserving order.
6. Reverse a list without slicing.

---

# 📦 2. Tuple – Immutable Sequence

A **tuple** is an ordered, **immutable** (unchangeable) collection. Once created, it cannot be modified.

> Use tuples when you want to **protect data** — like coordinates, dates, or configuration values.

## 🔑 Key Features

| Feature | Description |
|-------|-------------|
| **Ordered** | Maintains order |
| **Immutable** | Cannot be changed after creation |
| **Duplicates allowed** | Yes |
| **Heterogeneous** | Supports mixed types |

### ✅ Example

```python
point = (3, 5)
colors = ("red", "green", "blue")
info = ("Alice", 25, "Engineer")
```

---

### 🛠️ Creating a Tuple

Use parentheses `()` — but they’re optional in many cases.

```python
empty = ()
single = (5,)               # ❗ Must have comma
named = "Bob", 30, "Dev"    # Parentheses optional
```

> ⚠️ `(5)` is just a number. `(5,)` is a tuple.

---

### 🔢 Indexing & Slicing

Same as lists:

```python
fruits = ("apple", "banana", "cherry")

print(fruits[0])      # apple
print(fruits[1:3])    # ('banana', 'cherry')
```

But **no modification allowed**:

```python
fruits[1] = "mango"   # ❌ TypeError
```

---

### 🔁 Traversing a Tuple

```python
for item in fruits:
    print(item)
```

---

### 🧰 Common Tuple Methods

```python
nums = (1, 2, 3, 2, 4, 2)

print(nums.count(2))   # 3 → count occurrences
print(nums.index(3))   # 2 → first index
```

> ❌ No `append`, `remove`, `sort`, etc.

---

### 💡 When to Use Tuples?

- Store fixed data: `resolution = (1920, 1080)`
- As dictionary keys (lists can’t be keys!)
- Return multiple values from functions:

  ```python
  def get_name_age():
      return "Alice", 30

  name, age = get_name_age()  # Tuple unpacking
  ```

- Swap variables:

  ```python
  a, b = b, a  # Magic!
  ```

---

# 🗂️ 3. Dictionary – Key-Value Mappings

A **dictionary** stores data as **key-value pairs**. Think of it like a real-world dictionary: look up a **key** to get its **value**.

> Use dictionaries for fast lookups, configurations, JSON-like data, and grouping related info.

## 🔑 Key Features

| Feature | Description |
|-------|-------------|
| **Ordered** | ✅ Since Python 3.7+ (insertion order preserved) |
| **Mutable** | ✅ Can add, update, delete |
| **Keys unique & immutable** | No duplicates; keys must be hashable (strings, numbers, tuples) |
| **Values any type** | Can be lists, dicts, etc. |

---

### 🛠️ Creating a Dictionary

Use curly braces `{}` with `key: value`.

```python
student = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "CS"],
    "graduated": False
}

empty = {}
```

---

### 🔍 Accessing Values

```python
print(student["name"])           # Alice
print(student.get("age"))        # 25
print(student.get("grade", "N/A"))  # N/A (safe fallback)
```

> ⚠️ `dict[key]` raises `KeyError` if missing. Use `.get()` for safety.

---

### ✏️ Adding & Modifying

```python
student["age"] = 26                    # Update
student["grade"] = "A"                 # Add new
student.update({"city": "NYC", "job": "Dev"})  # Add multiple
```

---

### 🗑️ Removing Items

```python
student.pop("graduated")     # Remove key and return value
del student["city"]          # Delete key
student.clear()              # Remove all
```

---

### 🔁 Traversing a Dictionary

```python
# Keys only
for key in student:
    print(key)

# Values only
for val in student.values():
    print(val)

# Key-value pairs
for key, val in student.items():
    print(f"{key}: {val}")
```

---

### 🧰 Common Dictionary Methods

| Method | Purpose |
|-------|--------|
| `.keys()` | All keys |
| `.values()` | All values |
| `.items()` | Key-value tuples |
| `.get(key, default)` | Safe access |
| `.pop(key)` | Remove and return |
| `.update(dict)` | Merge dictionaries |

---

### 💡 When to Use Dictionaries?

- User profiles, product info
- Count frequency of words/letters
- Configuration settings
- Representing JSON or API responses

---

### 🎯 Example: Word Frequency Counter

```python
text = "hello world hello python world hello"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)  # {'hello': 3, 'world': 2, 'python': 1}
```

---

# 🔁 4. Set – Unique, Unordered Collection

A **set** is an unordered collection of **unique** elements. It’s ideal for removing duplicates and performing math operations.

> Use sets when you care about **membership** and **uniqueness**, not order.

## 🔑 Key Features

| Feature | Description |
|-------|-------------|
| **Unordered** | No indexing or slicing |
| **Mutable** | Can add/remove items |
| **No duplicates** | Automatically removes duplicates |
| **Elements must be immutable** | No lists/dicts inside, but numbers, strings, tuples OK |

---

### 🛠️ Creating a Set

Use curly braces `{}` — but **no colons**!

```python
primes = {2, 3, 5, 7, 11}
empty_set = set()  # ❗ Not {} — that’s a dict!

# Remove duplicates from list
data = [1, 2, 2, 3, 3, 3]
unique = set(data)  # {1, 2, 3}
```

---

### ➕ Modifying Sets

```python
fruits = {"apple", "banana"}

fruits.add("cherry")             # Add one
fruits.update(["mango", "kiwi"]) # Add multiple
fruits.discard("grape")          # Remove (no error if missing)
fruits.remove("banana")          # Remove (raises error if missing)
fruits.clear()                   # Empty set
```

---

### 🔍 Set Operations (Mathematical!)

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection: {3, 4}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric diff: {1, 2, 5, 6}
```

Or use method names:

```python
A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)
```

---

### 🔁 Traversing a Set

```python
for item in fruits:
    print(item)
```

> ❌ No indexing: `fruits[0]` → Error

---

### 💡 When to Use Sets?

- Remove duplicates from a list
- Fast membership testing (`if x in set`)
- Find common elements (intersection)
- Filter data using logic

---

### 🎯 Example: Find Mutual Friends

```python
alice_friends = {"Bob", "Charlie", "David"}
bob_friends = {"Charlie", "Eve", "Frank"}

common = alice_friends & bob_friends
print("Mutual friends:", common)  # {'Charlie'}
```

---

## 💡 Practice Questions (All Structures)

### Lists

- Reverse a list manually.
- Find second largest number.
- Split list into even and odd.

### Tuples

- Unpack a tuple into variables.
- Return min and max of a list as a tuple.

### Dictionaries

- Build a phonebook (name → number).
- Count letter frequency in a string.
- Merge two dictionaries.

### Sets

- Remove duplicates from a list.
- Check if two strings are anagrams.
- Find common elements in two lists.

---

## 🧩 Real-World Examples

### 📞 Phonebook (Dictionary)

```python
phonebook = {}
while True:
    name = input("Name (or 'quit'): ")
    if name == 'quit': break
    phone = input("Phone: ")
    phonebook[name] = phone
print("Phonebook:", phonebook)
```

### 🔤 Anagram Checker (Set & Sorting)

```python
def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(is_anagram("listen", "silent"))  # True
```

### 🧮 Frequency Counter (Dictionary)

```python
from collections import Counter
text = "hello"
freq = Counter(text)
print(freq)  # {'l': 2, 'h': 1, 'e': 1, 'o': 1}
```

---

## 🏁 Summary Table

| Feature | List | Tuple | Dict | Set |
|-------|------|-------|------|-----|
| Ordered | ✅ | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ (keys) | ❌ |
| Indexing | ✅ | ✅ | ❌ (use keys) | ❌ |
| Use Case | Dynamic collection | Fixed data | Key-value lookup | Uniqueness, math |

---

## 🧠 Pro Tips

- Use `list` for dynamic, ordered data.
- Use `tuple` for fixed records and safe data.
- Use `dict` for labeled, structured data.
- Use `set` for uniqueness and fast lookups.
- Prefer `.get()` for safe dictionary access.
- Use `set()` to deduplicate lists.
- Empty set → `set()`, not `{}`.

---

## 🙌 Final Thoughts

You now know all **four built-in data structures in Python**:

- `List` → Ordered, mutable, duplicates OK
- `Tuple` → Ordered, immutable, fast
- `Dictionary` → Key-value, fast lookup
- `Set` → Unique, unordered, math operations

> 🚀 These are the **foundation of every Python program** — from simple scripts to complex applications.

---

## 📚 What’s Next?

- ✅ Practice with real problems
- 🧩 Learn **list and dict comprehensions**
- 🔄 Explore **nested structures** (list of dicts, dict of lists)
- 📊 Move to **DSA** (Stack, Queue, Linked List, etc.)
- 🌐 Work with **JSON, APIs, databases**

---

## 🙏 Happy Coding

> "The right data structure makes the impossible, possible."  
> Now you have the tools to write smarter, cleaner, and more powerful Python code.

🐍 Keep learning. Keep building.

---

> 📝 *This README is based on your original notes — fully combined, corrected, enhanced, and structured for clarity and GitHub readiness.*  
> 👨‍🏫 Perfect for personal study, teaching, or open-source projects.

---

Let me know when you'd like the **next part** — maybe **Comprehensions**, **Nested Structures**, or **DSA Fundamentals** — and I’ll create it instantly!

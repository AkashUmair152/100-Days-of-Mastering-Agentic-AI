
## Day 04 of 100 day Agentic AI mastering challage. 

# 🔄 Loops in Python

Loops in Python allow us to execute a block of code multiple times without rewriting it.

> **Example:** Imagine printing `"Hello World"` 100 times.  
> Manually, that would take 100 lines of code.  
> With loops? Just **2 lines** — that’s the power of loops!

---

## 🔁 Types of Loops in Python

There are two main types of loops in Python:

1. `for` loop
2. `while` loop

To understand the difference, consider this analogy:

### 🪣 Bucket & Mug Analogy

- **Scenario 1:** Transfer **4 mugs** of water from one bucket to another.  
  → You know the number of iterations → Use a **`for` loop**.

- **Scenario 2:** Transfer **all the water** using a mug until the first bucket is empty.  
  → You don’t know how many mugs it will take, but you know the **stopping condition** → Use a **`while` loop**.

---

## 🧠 Intuition Behind Loops

| Loop Type | When to Use |
|---------|-------------|
| `for` loop | When you **know the number of iterations** (e.g., loop 5 times). |
| `while` loop | When you **don’t know how many times**, but have a **condition to check** (e.g., keep going until something happens). |

---

## 🔁 For Loop

Before diving into `for` loops, let's understand the `range()` function.

### 📏 The `range()` Function

The `range()` function generates a sequence of numbers.

#### Syntax

```python
range(start, stop, step)
```

- `start`: Starting number (default = 0)
- `stop`: End number (**not included**)
- `step`: Increment/Decrement value (default = 1)

> ✅ You **must specify** the `stop` value.

#### Examples

```python
range(5)           → 0, 1, 2, 3, 4
range(1, 6)        → 1, 2, 3, 4, 5
range(1, 10, 2)    → 1, 3, 5, 7, 9
```

---

### 🔢 For Loop with Numbers

**Problem:** Print numbers from 1 to 5.

```python
for i in range(1, 6):
    print(i)
```

✅ Output:

```
1
2
3
4
5
```

---

### 🔤 For Loop with Strings

You can iterate over strings in two ways:

#### 1. Using Index Values

```python
a = 'Nature'

for i in range(len(a)):
    print(a[i])
```

#### 2. Direct Iteration (Simpler)

```python
a = 'Nature'

for char in a:
    print(char)
```

Both output:

```
N
a
t
u
r
e
```

---

## ⚙️ Break, Continue, and Else in Loops

These are control statements that alter loop behavior.

### 🔺 `break`

Exits the loop immediately when a condition is met.

> **Real-life example:** You're running 20 laps, but it starts raining on the 16th lap — you stop.

```python
for i in range(1, 21):
    if i == 16:
        print("It started raining! Stopping.")
        break
    print(f"Lap {i}")
```

### 🔁 `continue`

Skips the current iteration and continues with the next.

> You skip the 16th lap but complete all others.

```python
for i in range(1, 21):
    if i == 16:
        print("Skipping lap 16")
        continue
    print(f"Lap {i}")
```

### ✅ `else` with Loops

The `else` block runs **only if the loop completes without a `break`**.

```python
for i in range(5):
    if i == 10:  # This won't happen
        break
    print(i)
else:
    print("Loop completed successfully!")
```

> If `break` is triggered, `else` will **not** run.

---

## 💡 For Loop Practice Questions

Here are some coding problems to practice `for` loops.

1. **Accept an integer `n` and print `"Hello World"` `n` times.**
2. **Print natural numbers up to `n`.**
3. **Reverse for loop: Print from `n` down to `1`.**
4. **Take a number as input and print its multiplication table.**
5. **Sum of first `n` natural numbers.**
6. **Factorial of a number.**
7. **Print sum of all even and odd numbers in a range separately.**
8. **Print all factors of a number.**
9. **Check if a number is a perfect number.**  
   > A number where the sum of its factors (excluding itself) equals the number.  
   > Example: 6 → 1 + 2 + 3 = 6 ✅
10. **Check if a number is prime.**
11. **Reverse a string without built-in functions.**
12. **Check if a string is a palindrome.**
13. **Count letters, digits, and special symbols in a string.**

#### Example: Count Chars, Digits, Symbols

Given:

```python
str1 = "P@#yn26at^&i5ve"
```

Expected Output:

```
Chars = 8
Digits = 3
Symbols = 4
```

---

## 🔁 While Loop

The `while` loop executes a block of code **as long as** a condition is `True`.

#### Syntax

```python
while condition:
    # Code to run
```

Useful when the number of iterations is **unknown**.

Like `for` loops, `while` loops support:

- `break`
- `continue`
- `else`

---

### 💡 While Loop Practice Questions

1. **Separate each digit of a number and print it on a new line.**  
   Example: `1234` → `1`, `2`, `3`, `4`

2. **Accept a number and print its reverse.**  
   Example: `123` → `321`

3. **Check if a number is a palindrome.**  
   (Number == Reverse of number)

4. **Create a Random Number Guessing Game in Python.**  
   - Generate a random number between 1 and 100.
   - Let the user guess.
   - Give hints: "Too high" or "Too low".
   - End when guessed correctly.

---

## 🏁 Summary

| Feature | `for` Loop | `while` Loop |
|--------|-----------|-------------|
| Known iterations | ✅ Best choice | ❌ Not ideal |
| Unknown iterations / condition-based | ❌ Not ideal | ✅ Best choice |
| Uses `range()` | ✅ Often used | ❌ Not needed |
| Supports `break`, `continue`, `else` | ✅ Yes | ✅ Yes |

---


---

> ✅ **Loops are the foundation of automation in programming.**  
> Master them, and you'll write smarter, shorter, and more powerful code!

Happy Coding! 💻🐍  
— Your Python Guide

---


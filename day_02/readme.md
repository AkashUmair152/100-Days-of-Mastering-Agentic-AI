## Operators in Python

### What are Operators?
Operators are symbols that perform operations on variables and values. Python provides several types of operators for different tasks such as arithmetic, comparison, and logical operations.

---

### Arithmetic Operators
Arithmetic operators are used for mathematical calculations:

| Operator | Description           | Example      |
|----------|-----------------------|--------------|
| `+`      | Addition              | `a + b`      |
| `-`      | Subtraction           | `a - b`      |
| `*`      | Multiplication        | `a * b`      |
| `/`      | Division              | `a / b`      |
| `//`     | Floor Division        | `a // b`     |
| `%`      | Modulus (Remainder)   | `a % b`      |
| `**`     | Exponentiation        | `a ** b`     |

**Example:**
```python
a = 12
b = 8
print(a + b)  # Output: 20
```

---

### Assignment Operators
Assignment operators assign values to variables. The basic assignment operator is `=`.

#### Compound Assignment Operators
These combine arithmetic operations with assignment:

| Operator | Example      | Equivalent To      |
|----------|-------------|--------------------|
| `+=`     | `a += b`    | `a = a + b`        |
| `-=`     | `a -= b`    | `a = a - b`        |
| `*=`     | `a *= b`    | `a = a * b`        |
| `/=`     | `a /= b`    | `a = a / b`        |
| `//=`    | `a //= b`   | `a = a // b`       |
| `%=`     | `a %= b`    | `a = a % b`        |
| `**=`    | `a **= b`   | `a = a ** b`       |

---

### Comparison Operators
Comparison (relational) operators compare two values and return a Boolean (`True` or `False`):

| Operator | Description                  | Example      |
|----------|------------------------------|--------------|
| `==`     | Equal to                     | `a == b`     |
| `!=`     | Not equal to                 | `a != b`     |
| `>`      | Greater than                 | `a > b`      |
| `<`      | Less than                    | `a < b`      |
| `>=`     | Greater than or equal to     | `a >= b`     |
| `<=`     | Less than or equal to        | `a <= b`     |

These work with numbers and strings (using ASCII values for strings).

---

### Logical Operators
Logical operators combine multiple conditions:

| Operator | Description                                 | Example                |
|----------|---------------------------------------------|------------------------|
| `and`    | True if both conditions are True            | `a > 5 and b < 10`     |
| `or`     | True if at least one condition is True      | `a > 5 or b < 10`      |
| `not`    | Reverses the Boolean value                  | `not (a > 5)`          |

---

### Practice Questions

```python
print(126 > 130)  # False
print((456 == 456) != (235 == 236))  # True
print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)  # True
print(True and bool(0))  # False
```

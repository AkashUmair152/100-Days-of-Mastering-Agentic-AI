# Conditional Statements in Python

Conditional statements allow you to control the flow of your program by executing different blocks of code based on certain conditions. This is also known as decision making or control flow.

For example, if you receive a number from the user, you might want to do Task A if the number is greater than 10, or Task B if it is less than or equal to 10. Here, the number determines which task will be executed.

### Types of Conditional Statements 

There are three main types of conditional statements in Python:

1. **if** – Executes a block of code if the condition is `True`.
2. **if-else** – Executes one block if the condition is `True`, another if it is `False`.
3. **if-elif-else** – Checks multiple conditions in sequence.

#### Syntax Examples

```python
# if statement
if condition:
    # code to execute if condition is true

# if-else statement
if condition:
    # code if condition is true
else:
    # code if condition is false

# if-elif-else statement
if condition:
    # code if condition is true
elif another_condition:
    # code if another_condition is true
else:
    # code if both conditions are false
```

### Practice Questions

Try solving these problems to practice conditional statements:

1. Accept two numbers and print the greatest between them.
2. Accept the gender from the user as a character and print a respective greeting message (e.g., "Good Morning Sir").
3. Accept an integer and check whether it is even or odd.
4. Accept name and age from the user. Check if the user is a valid voter or not (e.g., "Hello Shery, you are a valid voter").
5. Accept a year and check if it is a leap year or not.

### The if-elif Ladder

You can use multiple `elif` statements to check several conditions in sequence. For example, to categorize temperature:

```python
temp = int(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing Cold")
elif temp <= 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Pleasant")
elif temp <= 40:
    print("Hot")
else:
    print("Very Hot")
```

Conditional statements are fundamental for making decisions in your programs!

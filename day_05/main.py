# Example 1: Simple Function
def hello_world():
    print("Hello World this is a function")

hello_world()


# Example 2: Function with a Parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")


# Example 3: Function with Return Value
def sum(a, b):
    return a + b

result = sum(5, 3)
print(result)


# Example 4: Function with Multiple Parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 30)
introduce("Bob", 25)


# Example 5: Default Arguments
def greet(name="Akash"):
    print(f"Hello, {name}!")

greet()
greet("Bob")


# Example 6: Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="Charlie")
introduce(name="Diana", age=28)


# Practice: Try It Yourself
def multiply(x, y):
    return x * y

def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")

def area(length=1, width=1):
    return length * width

print(multiply(4, 5))
greet_with_time("John")
greet_with_time("Jane", time="evening")
print(area(5, 3))
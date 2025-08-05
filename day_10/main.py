class Fruit:
    name = "Apple"

# Creating an object
fruit = Fruit()

# Accessing attributes
print(fruit.name)  # Output: Apple

class Student:
    def __init__(self, name):
        self.name = name  # instance attribute

# Creating an object with value
student = Student("Ali")

# Accessing the attribute
print(student.name)  # Output: Ali
class Car:
    wheels = 4  # class attribute
    
    def __init__(self, color):
        self.color = color  # instance attribute

class Car:
    wheels = 4  # class attribute

    def __init__(self, color):
        self.color = color  # instance attribute

car1 = Car("Red")
car2 = Car("Blue")

print(car1.wheels)   # Output: 4
print(car2.color)    # Output: Blue


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.bark()  # Output: Buddy says Woof!

class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species

print(Person.get_species())  # Output: Human

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # Output: 8
     
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
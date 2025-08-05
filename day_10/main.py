class Fruit:
    name= "Apple"
    
# creating an object 
fruit = Fruit()
# accessing the attributes 

print(fruit.name)

class Student:
    def __init__(self, name):
        self.name = name
        
# creating an object with a value 

student = Student("Ali")

# accessing the Attribute
print(student.name)


class Car:
    wheels = 4 # class attribute
    def __init__(self, color):
        self.color = color # instance attribute
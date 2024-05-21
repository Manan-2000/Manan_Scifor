#Abstraction
class Emp1:
    c_name = 'ABC'
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
    def show(self):
        print('Employee:', self.name, self.sal, self.c_name)
emp1 = Emp1("Harry", 12000)
emp1.show()
emp2 = Emp1("Emma", 10000)
emp2.show()

#Encapsulation 
class Emp2:
    def __init__(self, name, sal):
        self.name = name
        self.__sal = sal
    def show(self):
        print("Name is ", self.name, "and salary is", self.__sal)
emp = Emp2("Jessa", 40000)
emp.show()

#Polymorphism 
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of Rectangle :", self.length * self.width)
def area(shape):
    shape.area()
cir = Circle(5)
rect = Rectangle(10, 5)
area(cir)
area(rect)

#Inheritance
class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def info(self):
        print(self.name, self.color, self.price)
class Car(Vehicle):
    def change_gear(self, no):
        print(self.name, 'change gear to number', no)
car = Car('BMW X1', 'Black', 35000)
car.info()
car.change_gear(5)
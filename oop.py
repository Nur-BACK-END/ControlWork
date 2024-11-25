from abc import ABC, abstractmethod

# 1. Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Ошибка: возраст не может быть отрицательным.")

    def get_age(self):
        return self._age

# 2. Наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# 3. Полиморфизм
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

# 4. Абстракция
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        namber_pi = 3.14159
        return namber_pi * (self.radius ** 2)

if __name__ == "__main__":
# Инкапсуляция
    p = Person()
    p.set_age(68)
    print(f"Возраст человека: {p.get_age()}")
    p.set_age(-14)
# Наследование
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(f"{dog.name} говорит: {dog.speak()}")
    print(f"{cat.name} говорит: {cat.speak()}")
# Полиморфизм
    car = Car()
    bike = Bicycle()
    print(move(car))
    print(move(bike))
# Абстракция
    rect = Rectangle(15, 5)
    circle = Circle(9)
    print(f"Площадь прямоугольника: {rect.area()}")
    print(f"Площадь круга: {circle.area()}")
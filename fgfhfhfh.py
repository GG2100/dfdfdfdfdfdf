from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass
    def get_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")
class Dog(Animal):
    def make_sound(self):
        print("it's a dog: 'Гав-гав!'")

class Cat(Animal):
    def make_sound(self):
        print("it's a cat: 'Няв-няв!'")

class Parrot(Animal):
    def make_sound(self):
        print("it's a parrot: 'Привіт!'")

g=Dog("Каркаде", 5)
g.make_sound()
g.get_info()
d=Cat("Купрум", 75)
d.make_sound()
d.get_info()
s=Parrot("Карлсон", 47)
s.make_sound()
s.get_info()

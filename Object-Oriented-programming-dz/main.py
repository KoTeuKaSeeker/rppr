from abc import ABC, abstractmethod

#Интерфейс
class IRunable(ABC):
    @abstractmethod
    def run(self):
        pass

#Animal - абстрактный метод
class Animal(ABC):

    __name = ""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    @abstractmethod
    def say(self):
        pass

class Cat(Animal, IRunable):
    def say(self):
        return "Meow"

    def run(self):
        return "Cat is running"

class Dog(Animal, IRunable):
    def say(self):
        return "Woof"

    def run(self):
        return "Dog is running"

def to_run_animal(runnable):
    print(runnable.run())

#Полиморфизм
def polymorphism():
    animals = [Cat('murka'), Dog('sharik')]
    for a in animals:
        print(a.say())

#Инкапсуляция
def encapsulation():
    cat = Cat('murka')
    print(cat.get_name())
    cat.set_name('murka 2.0')
    print(cat.get_name())

#Интерфейс
def interface():
    cat = Cat('murka')
    dog = Dog('sharik')
    to_run_animal(cat)
    to_run_animal(dog)
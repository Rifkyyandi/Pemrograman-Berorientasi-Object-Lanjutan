from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    pass

c = Cat() # This will raise a NotImplementedError since 'sound' method has not been implemented in the 'Cat' class

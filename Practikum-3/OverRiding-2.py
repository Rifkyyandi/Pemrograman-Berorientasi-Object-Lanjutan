class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

# instantiate objects of each class
animal = Animal()
dog = Dog()
cat = Cat()

# call the make_sound() method for each object
animal.make_sound()
dog.make_sound()
cat.make_sound()

import weakref

class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person({self.name})"
    
person = Person("John")
weakref.ref(person)

del person
print(weakref.getweakrefcount(person)) # raises ReferenceError: weakly-referenced object no longer exists

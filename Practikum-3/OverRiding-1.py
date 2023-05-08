class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    pass

# instantiate objects of the Car and Bike classes
car = Car()
bike = Bike()

# call the start() method for each object
car.start()
bike.start()

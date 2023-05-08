class Calculator:
    def add(self, x=None, y=None, z=None):
        if x != None and y != None and z != None:
            return x + y + z
        elif x != None and y != None:
            return x + y
        else:
            return 0

# instantiate objects of the Calculator class
calc = Calculator()

# add three numbers
sum1 = calc.add(2, 4, 6)
print("Sum of three numbers is:", sum1)

# add two numbers
sum2 = calc.add(4, 5)
print("Sum of two numbers is:", sum2)

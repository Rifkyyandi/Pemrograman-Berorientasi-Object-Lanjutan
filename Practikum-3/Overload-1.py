class Shape:
    def area(self, x=None, y=None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0

# instantiate objects of the Shape class
shape = Shape()

# calculate area of a rectangle
area_rect = shape.area(4, 5)
print("Area of the rectangle is:", area_rect)

# calculate area of a square
area_square = shape.area(5)
print("Area of the square is:", area_square)

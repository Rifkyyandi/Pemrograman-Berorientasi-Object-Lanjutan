class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

class TwoDimensional(Shape):
    def __init__(self, name, color, sides):
        super().__init__(name, color)
        self.sides = sides
    
    def get_sides(self):
        return self.sides

class ThreeDimensional(Shape):
    def __init__(self, name, color, faces):
        super().__init__(name, color)
        self.faces = faces
    
    def get_faces(self):
        return self.faces

# Hierarchical Inheritance
class Sphere(ThreeDimensional):
    def __init__(self, name, color, faces, radius):
        super().__init__(name, color, faces)
        self.radius = radius
    
    def get_Detile(self):
        print(f"Nama = {self.name},\nWarna = {self.color},\nFaces = {self.faces},\nJarak = {self.radius}.")
        return self.radius

Adios = Sphere("Power Sphere","Kuning","Oval",100)
Adios.get_Detile()
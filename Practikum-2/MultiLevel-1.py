class Food:
    def __init__(self, name):
        self.name = name

class Ingredient(Food):
    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity

class Spice(Ingredient):
    def __init__(self, name, quantity, is_hot):
        super().__init__(name, quantity)
        self.is_hot = is_hot

# membuat objek Spice
cumin = Spice("Cumin", 50, True)

# mencetak atribut dari objek Spice
print(cumin.name)
print(cumin.quantity)
print(cumin.is_hot)

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

class Mammal(Animal):
    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur

    def get_fur(self):
        return self.fur

class Bird(Animal):
    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan

    def get_wingspan(self):
        print(f"Nama = {self.name},\n Warna = {self.color},\n Berbulu = {self.fur},\n Berumur = {self.scale} Tahun. " )
        return self.wingspan

# Hierarchical Inheritance
class Reptile(Mammal):
    def __init__(self, name, color, fur, umur):
        super().__init__(name, color, fur)
        self.umur = umur
    
    def get_detile(self):
        print(f"Nama = {self.name},\n Warna = {self.color},\n Berbulu = {self.fur},\n Berumur = {self.umur} Tahun. " )
        return self.umur

IOU = Reptile("Monyet","Kuning Emas","Berbulu Lebat",2 )
IOU.get_detile()


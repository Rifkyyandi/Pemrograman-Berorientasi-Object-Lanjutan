class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} Suka Berenang Dan Berjalan-jalan")
        
class Dog(Animal):
    def __init__(self, name, umur):
        super().__init__(name)
        self.umur = umur
        
    def Sound(self):
        print(f"{self.name} Si Anak Anjing Yang Berumur {self.umur} Tahun, Dan Bersuara Wupp.. Wupp")
        
class Bulldog(Dog):
    def __init__(self, name, umur, jenis_kelamin):
        super().__init__(name, umur)
        self.jenis_kelamin = jenis_kelamin
        
    def spill(self):
        print(f"{self.name} Memiliki Jenis Kelamin {self.jenis_kelamin} Dan Masih Berumur {self.umur} Tahun")

Bulldogy = Bulldog("Hoji", 7, "Jantan")
Bulldogy.Sound() 
Bulldogy.spill() 
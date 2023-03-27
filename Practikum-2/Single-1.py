class Komputer:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga

    def spesifikasi(self):
        print(f"Komputer merk {self.merk} dengan harga {self.harga}.")

class Laptop(Komputer):
    def __init__(self, merk, harga, ukuran_layar):
        super().__init__(merk, harga)
        self.ukuran_layar = ukuran_layar

    def spesifikasi(self):
        print(f"Laptop merk {self.merk} dengan harga {self.harga} dan ukuran layar {self.ukuran_layar} inci.")

laptop_acer = Laptop("Acer", 5000000, 15.6)
laptop_acer.spesifikasi() # output: "Laptop merk Acer dengan harga 5000000 dan ukuran layar 15.6 inci."

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

manusia = Manusia("Andi", 20)

try:
    print(manusia.alamat)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")

class Pekerja:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Perusahaan:
    def __init__(self, nama, pekerja):
        self.nama = nama
        self.pekerja = pekerja
    
    def daftar_pekerja(self):
        for pekerja in self.pekerja:
            print(pekerja.nama, pekerja.umur)

pekerja1 = Pekerja("Andi", 25)
pekerja2 = Pekerja("Budi", 30)

perusahaan = Perusahaan("ABC", [pekerja1, pekerja2])
perusahaan.daftar_pekerja()
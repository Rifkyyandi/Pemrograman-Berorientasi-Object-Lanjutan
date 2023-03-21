class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def belajar(self):
        print(self.nama, f"Memiliki Nim = {self.nim} Sedang Belajar Secara Online Karena Sakit")

class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    
    def bekerja(self):
        print(self.nama, "Sedang Bekerja Sebagai Seorang",self.pekerjaan)

class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    
    def bersosialisasi(self):
        print(self.nama, "Sedang Bersosialisasi Dengan Seorang",self.pekerjaan)

mhs_pekerja = MahasiswaPekerja("RIFKI YANDI", "210511156", "Programmer")
mhs_pekerja.belajar()
mhs_pekerja.bekerja()
mhs_pekerja.bersosialisasi() 
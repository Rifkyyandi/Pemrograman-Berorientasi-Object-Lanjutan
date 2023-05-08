class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
        
    def bergabung_kelompok_kkm(self, kelompok):
        self.kelompok = kelompok
        
class KelompokKKM:
    def __init__(self, nama):
        self.nama = nama
        self.mahasiswa = []
        
    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)

# Contoh penggunaan
mahasiswa1 = Mahasiswa("rifki yandi", "210511156")
kelompok_kkm1 = KelompokKKM("KKM A")

kelompok_kkm1.tambah_mahasiswa(mahasiswa1)
mahasiswa1.bergabung_kelompok_kkm(kelompok_kkm1)

print(mahasiswa1.kelompok.nama) # Output: KKM A
print(kelompok_kkm1.mahasiswa[0].nama) # Output: rifki yandi

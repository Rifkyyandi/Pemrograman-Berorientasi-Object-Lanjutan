class Peneliti:
    def __init__(self, nama):
        self.nama = nama
        self.jurnal = None
        
    def tambah_jurnal(self, jurnal):
        self.jurnal = jurnal
        
class Jurnal:
    def __init__(self, judul, tanggal):
        self.judul = judul
        self.tanggal = tanggal
        self.penulis = []
        
    def tambah_penulis(self, penulis):
        self.penulis.append(penulis)

# Contoh penggunaan
peneliti1 = Peneliti("rifki yandi")
jurnal1 = Jurnal("Jurnal A", "9 May 2023")

jurnal1.tambah_penulis(peneliti1)
peneliti1.tambah_jurnal(jurnal1)

print(peneliti1.jurnal.judul) # Output: Jurnal A
print(jurnal1.penulis[0].nama) # Output: rifki yandi

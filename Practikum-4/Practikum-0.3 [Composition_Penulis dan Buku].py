class Penulis:
    def __init__(self, nama):
        self.nama = nama
        
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        
    def tambah_penulis(self, penulis):
        self.penulis.append(penulis)

# Contoh penggunaan
penulis1 = Penulis("rifki yandi")
penulis2 = Penulis("rifki yandi")
buku1 = Buku("Buku A", [penulis1])

buku1.tambah_penulis(penulis2)

print(penulis1.nama) # Output: rifki yandi
print(buku1.penulis[1].nama) # Output: rifki yandi

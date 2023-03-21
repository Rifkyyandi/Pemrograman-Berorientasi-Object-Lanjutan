class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji

    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")

class Penulis:
    def __init__(self, buku, genre):
        self.buku = buku
        self.genre = genre
    
    def display_info(self):
        print(f"Buku: {self.buku}")
        print(f"Genre: {self.genre}")

class PenulisPekerja(Orang, Pekerja, Penulis):
    def __init__(self, nama, umur, pekerjaan, gaji, buku, genre):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Penulis.__init__(self, buku, genre)
    
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Buku: {self.buku}")
        print(f"Genre: {self.genre}")

# contoh penggunaan
penulis_pekerjaC = PenulisPekerja("Turtle Me", 23, "Penulis", "$5000", "The Beginning After The End", "Fiksi")
penulis_pekerjaC.display_info()
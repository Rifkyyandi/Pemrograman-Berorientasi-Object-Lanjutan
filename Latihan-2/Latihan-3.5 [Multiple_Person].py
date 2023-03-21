class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Mahasiswa(Person):
    def __init__(self, nama, umur, jurusan):
        self.jurusan = jurusan

    def display_info(self):
        super().display_info()
        print(f"Jurusan: {self.jurusan}")

class Alumni(Person):
    def __init__(self, nama, umur, tahun_lulus):
        super().__init__(nama, umur)
        self.tahun_lulus = tahun_lulus
    
    def display_info(self):
        super().display_info()
        print(f"Tahun lulus: {self.tahun_lulus}")

class MahasiswaAlumni(Mahasiswa, Alumni):
    def __init__(self, nama, umur, jurusan, tahun_lulus):
        Mahasiswa.__init__(self, nama, umur, jurusan)
        Alumni.__init__(self, nama, umur, tahun_lulus)
    
    def display_info(self):
        super().display_info()

# contoh penggunaan
mahasiswa_alumniA = MahasiswaAlumni("Rifki Yandi", 23, "Informatika", 2025)
mahasiswa_alumniA.display_info()

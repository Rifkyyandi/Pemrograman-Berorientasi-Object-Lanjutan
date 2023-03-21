class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna

    def berkendara(self):
        print(f"{self.jenis} Bermerk {self.merk} Dengan Warna {self.warna} ini sedang berjalan.")

class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc

    def belok(self):
        print(f"{self.jenis} ini sedang belok.")

motorA = SepedaMotor("Sepeda Motor", "Honda", "Merah", 150)
motorA.berkendara() # Output: Kendaraan ini sedang berjalan.
motorA.belok() # Output: Sepeda motor ini sedang belok.

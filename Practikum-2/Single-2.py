class UnsurAlam:
    def __init__(self, nama):
        self.nama = nama

    def get_info(self):
        print(f"Ini adalah unsur alam {self.nama}.")

class UnsurLogam(UnsurAlam):
    def __init__(self, nama, sifat):
        super().__init__(nama)
        self.sifat = sifat

    def get_info(self):
        print(f"Ini adalah unsur logam {self.nama} yang memiliki sifat {self.sifat}.")

unsur_1 = UnsurAlam("Oksigen")
unsur_2 = UnsurLogam("Emas", "Mudah ditempa")

unsur_1.get_info() # output: "Ini adalah unsur alam Oksigen."
unsur_2.get_info() # output: "Ini adalah unsur logam Emas yang memiliki sifat Mudah ditempa."

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
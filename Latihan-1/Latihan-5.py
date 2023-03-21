
class Warnet:
    def __init__(self, User, Paket):
        self.User = User
        self.Paket = Paket
        
    def info(self):
        print(f"Pengguna: {self.User}\nPaket: {self.Paket}")

Komputer1 = Warnet("Rifki Pramayandi Mahesa", "2 Jam(5000)")
Komputer1.info()
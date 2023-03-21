class Manga : 
    
    def __init__(self,judul,pengarang):
        self.judul = judul
        self.pengarang = pengarang
        
    def info(self) : 
        print(f"Judul : {self.judul}\nPengarang : {self.pengarang}")

Manga1 = Manga("The beginning afther The End","Turtle.Me")
Manga1.info()
        
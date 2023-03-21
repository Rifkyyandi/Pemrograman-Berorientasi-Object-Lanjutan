class Kulit : 
    
    def __init__(self,kategori,warna):
        self.kategori = kategori
        self.warna = warna 
        
    def info(self):
        print(f"Kulit {self.kategori} berwarna {self.warna}")
        
kulit1 = Kulit("Mulus","Putih")
kulit1.info() 
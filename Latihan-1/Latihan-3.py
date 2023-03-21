class lingkaran : 
    def __init__(self,r):
        self.r = r
        
    def luas(self): 
        return 3.14 * (self.r ** 2)
    
lingkaran1 = lingkaran(14)
print(f"Luas Lingkaran : {lingkaran1.luas()}")

class Pekerja :
    def __init__(self,nama,Job):
        self.nama = nama
        self.Job = Job
        
    def info(self): 
        print(f"Nama : {self.nama}\nJob : {self.Job}")
        
Pekerjaan1 = Pekerja ("Rifki Pramayandi Mahesa","Software Enginer")
Pekerjaan1.info()
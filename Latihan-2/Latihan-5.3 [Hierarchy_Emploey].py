class Employee:
    def __init__(self, name, age, jenis_kelamin):
        self.name = name
        self.age = age
        self.jenis_kelami = jenis_kelamin
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_umur(self):
        return self.jenis_kelamin

class Manager(Employee):
    def __init__(self, name, age, jenis_kelamin, department):
        super().__init__(name, age, jenis_kelamin)
        self.department = department
    
    def get_department(self):
        return self.department

class Programmer(Employee):
    def __init__(self, name, age, jenis_kelamin, language):
        super().__init__(name, age, jenis_kelamin)
        self.language = language
    
    def get_language(self):
        return self.language

# Hierarchical Inheritance
class SeniorProgrammer(Programmer):
    def __init__(self, name, age, jenis_kelamin, language, level):
        super().__init__(name, age, jenis_kelamin, language)
        self.level = level
    
    def get_Detile(self):
        print(f"Nama = {self.name},\nUmur = {self.age},\nJenis Kelamin = {self.jenis_kelami},\nBahasa = {self.language},\nLevel = {self.level}")

Senpai = SeniorProgrammer ("Rifki Yandi","23 Tahun","Laki-Laki","Bahasa Inggris","Exspert")   
Senpai.get_Detile()
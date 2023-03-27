class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Processor(Computer):
    def __init__(self, brand, model, cores):
        super().__init__(brand, model)
        self.cores = cores

class CPU(Processor):
    def __init__(self, brand, model, cores, frequency):
        super().__init__(brand, model, cores)
        self.frequency = frequency

    def print_specs(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nCores: {self.cores}\nFrequency: {self.frequency}")

# membuat objek CPU
my_cpu = CPU("Intel", "i7-10700K", 8, "3.8 GHz")

# mencetak spesifikasi dari objek CPU
my_cpu.print_specs()

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
# membuat class Configurate
class Configurate:
    def __init__(self, name, processor):
        self.name = name
        self.processor = processor
    
    def get_name(self):
        return self.name
    
    def get_processor(self):
        return self.processor

# membuat class Computing
class Computing:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
        
    def get_ram(self):
        return self.ram
    
    def get_storage(self):
        return self.storage

# membuat class Configurate Computing dengan menggunakan multiple inheritance
class ConfigurateComputing(Configurate, Computing):
    def __init__(self, name, processor, ram, storage, graphics_card):
        Configurate.__init__(self, name, processor)
        Computing.__init__(self, ram, storage)
        self.graphics_card = graphics_card
    
    def get_graphics_card(self):
        return self.graphics_card

# membuat objek dari class ConfigurateComputing
pc1 = ConfigurateComputing("Laptop", "Intel Core i5", "8 GB", "256 GB", "Nvidia GTX 1650")

# memanggil method yang dimiliki oleh class Configurate
print(pc1.get_name())       # Output: Laptop
print(pc1.get_processor())  # Output: Intel Core i5

# memanggil method yang dimiliki oleh class Computing
print(pc1.get_ram())        # Output: 8 GB
print(pc1.get_storage())    # Output: 256 GB

# memanggil method yang dimiliki oleh class ConfigurateComputing
print(pc1.get_graphics_card())  # Output: Nvidia GTX 1650

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
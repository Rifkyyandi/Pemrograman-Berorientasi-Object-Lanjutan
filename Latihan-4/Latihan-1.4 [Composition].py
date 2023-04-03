class RAM:
    def __init__(self, capacity):
        self.capacity = capacity

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

ram = RAM(8)
storage = Storage(500)
computer = Computer(ram, storage)
print(computer.ram.capacity) # output: 8
print(computer.storage.capacity) # output: 500
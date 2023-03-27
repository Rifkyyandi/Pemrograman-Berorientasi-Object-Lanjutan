class OutputDevice:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        self.connected = True
        
    def disconnect(self):
        self.connected = False

class Printer(OutputDevice):
    def __init__(self):
        super().__init__()
        self.print_queue = []
        
    def print(self, document):
        if self.connected:
            self.print_queue.append(document)
            print(f"Printing {document}")
        else:
            print("Printer is not connected.")
            
    def cancel_print(self, document):
        if document in self.print_queue:
            self.print_queue.remove(document)
            print(f"{document} has been removed from print queue.")
        else:
            print(f"{document} is not in print queue.")

class Scanner(OutputDevice):
    def __init__(self):
        super().__init__()
        
    def scan(self):
        if self.connected:
            print("Scanning document...")
        else:
            print("Scanner is not connected.")

# Membuat objek printer dan scanner
printer = Printer()
scanner = Scanner()

# Menghubungkan printer dan scanner
printer.connect()
scanner.connect()

# Mencetak dokumen dengan printer
printer.print("Sample Document")

# Membatalkan pencetakan dokumen dengan printer
printer.cancel_print("Sample Document")

# Melakukan scanning dokumen dengan scanner
scanner.scan()

# Memutuskan koneksi printer dan scanner
printer.disconnect()
scanner.disconnect()

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
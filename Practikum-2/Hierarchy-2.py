class Hardware:
    def __init__(self):
        self.powered_on = False
    
    def power_on(self):
        self.powered_on = True
        print("Hardware is now powered on.")
    
    def power_off(self):
        self.powered_on = False
        print("Hardware is now powered off.")

class InputDevice(Hardware):
    def __init__(self):
        super().__init__()

class OutputDevice(Hardware):
    def __init__(self):
        super().__init__()

class Keyboard(InputDevice):
    def __init__(self):
        super().__init__()
        
    def type(self, text):
        if self.powered_on:
            print(f"Typed: {text}")
        else:
            print("Keyboard is not powered on.")

class Monitor(OutputDevice):
    def __init__(self):
        super().__init__()
        
    def display(self, text):
        if self.powered_on:
            print(text)
        else:
            print("Monitor is not powered on.")

# Membuat objek keyboard dan monitor
keyboard = Keyboard()
monitor = Monitor()

# Menghidupkan keyboard dan monitor
keyboard.power_on()
monitor.power_on()

# Mengetikkan teks dengan keyboard
keyboard.type("Hello World")

# Menampilkan teks di monitor
monitor.display("Welcome to the world of Python")

# Mematikan keyboard dan monitor
keyboard.power_off()
monitor.power_off()

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
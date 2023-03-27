# membuat class Kernel
class Kernel:
    def __init__(self, name, version):
        self.name = name
        self.version = version
    
    def get_name(self):
        return self.name
    
    def get_version(self):
        return self.version

# membuat class User Interface
class UserInterface:
    def __init__(self, display_type, theme):
        self.display_type = display_type
        self.theme = theme
        
    def get_display_type(self):
        return self.display_type
    
    def get_theme(self):
        return self.theme

# membuat class Operating System dengan menggunakan multiple inheritance
class OperatingSystem(Kernel, UserInterface):
    def __init__(self, name, version, display_type, theme, default_browser):
        Kernel.__init__(self, name, version)
        UserInterface.__init__(self, display_type, theme)
        self.default_browser = default_browser
    
    def get_default_browser(self):
        return self.default_browser

# membuat objek dari class OperatingSystem
os1 = OperatingSystem("Windows", "10", "GUI", "Light", "Chrome")

# memanggil method yang dimiliki oleh class Kernel
print("Name OS :",os1.get_name())       # Output: Windows
print("Version :",os1.get_version())    # Output: 10

# memanggil method yang dimiliki oleh class UserInterface
print("Display Type :",os1.get_display_type())   # Output: GUI
print("Theme :",os1.get_theme())          # Output: Light

# memanggil method yang dimiliki oleh class OperatingSystem
print("Default Browser :",os1.get_default_browser())    # Output: Chrome

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
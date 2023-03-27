class WebPage:
    def __init__(self, url):
        self.url = url

    def open(self):
        print("Opening webpage:", self.url)


class OperatingSystem:
    def __init__(self, name):
        self.name = name

    def boot_up(self):
        print(self.name, "is booting up")


class Browser(WebPage, OperatingSystem):
    def __init__(self, url, name):
        WebPage.__init__(self, url)
        OperatingSystem.__init__(self, name)

    def display(self):
        self.boot_up()
        self.open()
        print("Browser is ready to use")


# Membuat objek dari kelas Browser
my_browser = Browser("https://www.google.com", "Windows 10")

# Memanggil metode display() pada objek my_browser
my_browser.display()

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
class Chef:
    def __init__(self, name):
        self.name = name
        
    def create_menu(self, *args):
        menu = []
        for item in args:
            menu.append(item)
        return MenuMakanan(menu)

class MenuMakanan:
    def __init__(self, menu):
        self.menu = menu
        
    def show_menu(self):
        print("Menu Makanan:")
        for item in self.menu:
            print("- " + item)

# Contoh penggunaan
chef = Chef("John")
menu = chef.create_menu("Nasi Goreng", "Mie Goreng", "Ayam Bakar")
menu.show_menu()

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()

class Item:
    def __init__(self, name):
        self.name = name

class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print(player)
    
    def remove_item(self, item):
        self.items.remove(item)
        
player = Player("John")
sword = Item("Sword")
shield = Item("Shield")
player.inventory.add_item(sword)
player.inventory.add_item(shield)
player.inventory.items # output: [sword, shield]
# Single Inheritance
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Single Inheritance
class Drawable:
    def draw(self):
        print("Drawing object at: ", self.x, self.y)

# Single Inheritance
class Moveable:
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Multiple Inheritance
class Player(GameObject, Drawable, Moveable):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def update(self):
        self.move(1, 1)
        self.draw()
        
GM = Player(2,3)
GM.update()
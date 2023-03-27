class Switchable:
    def switch_on(self):
        self.is_on = True
        print("Switched on")

    def switch_off(self):
        self.is_on = False
        print("Switched off")


class Dimmable:
    def set_brightness(self, brightness):
        self.brightness = brightness
        print("Brightness set to", brightness)


class Lampu(Switchable, Dimmable):
    def __init__(self):
        self.is_on = False
        self.brightness = 0

lampu1 = Lampu()
lampu1.switch_on()
lampu1.set_brightness(50)
print("Brightness:", lampu1.brightness)

lampu1.switch_off()
print("Is on:", lampu1.is_on)

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |\n") 
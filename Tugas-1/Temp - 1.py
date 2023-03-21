class Fahrenheit:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        return (self.temperature - 32) * 5 / 9

    def to_reamur(self):
        return (self.temperature - 32) * 4 / 9

    def to_kelvin(self):
        return (self.temperature + 459.67) * 5 / 9

# membuat objek Fahrenheit dengan nilai 7 derajat Fahrenheit
f = Fahrenheit(7)
print("|   CONVERTER  FAHRENHEIT   |") 

# konversi suhu Fahrenheit ke Celsius
c = f.to_celsius()
print("\nCelsius = ",c) 

# konversi suhu Fahrenheit ke Reamur
r = f.to_reamur()
print("Reamur = ",r)  

# konversi suhu Fahrenheit ke Kelvin
k = f.to_kelvin()
print("Kelvin = ",k) 
print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |") 
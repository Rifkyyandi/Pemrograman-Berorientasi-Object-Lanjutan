class Kelvin:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        return self.temperature - 273.15

    def to_fahrenheit(self):
        return self.temperature * 9 / 5 - 459.67

    def to_reamur(self):
        return (self.temperature - 273.15) * 4 / 5

# membuat objek Kelvin dengan nilai 14 derajat Kelvin
K = Kelvin(14)
print("|   CONVERTER  KELVIN   |") 

# konversi suhu Kelvin ke Celsius
c = K.to_celsius()
print("\nCelsius = ",c) 

# konversi suhu Kelvin ke Fahrenheit
f = K.to_fahrenheit()
print("Fahrenheit = ",f)

# konversi suhu Kelvin ke Reamur
r = K.to_reamur()
print("Reamur = ",r)
print("\n|RIFKI PRAMAYANDI MAHESA|") 
print("|      210511156        |") 
print("|       KELAS D         |") 
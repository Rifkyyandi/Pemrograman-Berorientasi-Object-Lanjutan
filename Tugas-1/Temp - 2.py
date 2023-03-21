class Reamur:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        return self.temperature * 5 / 4

    def to_fahrenheit(self):
        return self.temperature * 9 / 4 + 32

    def to_kelvin(self):
        return self.temperature * 5 / 4 + 273.15

# membuat objek Reamur dengan nilai 23 derajat Reamur
R = Reamur(23)
print("|   CONVERTER  REAMUR   |") 

# konversi suhu Reamur ke Celsius
c = R.to_celsius()
print("\nCelsius = ",c)

# konversi suhu Reamur ke Fahrenheit
f = R.to_fahrenheit()
print("Fahrenheit = ",f)

# konversi suhu Reamur ke Kelvin
k = R.to_kelvin()
print("Kelvin = ",k)
print("\n|RIFKI PRAMAYANDI MAHESA|") 
print("|      210511156        |") 
print("|       KELAS D         |") 
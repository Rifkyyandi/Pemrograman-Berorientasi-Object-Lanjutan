class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def to_kelvin(self):
        return self.temperature + 273

    def to_reamur(self):
        return self.temperature * 4/5

# membuat objek Celsius dengan nilai 14 derajat Celsius
C = Celsius(14)
print("|   CONVERTER  CELSIUS  |") 

# konversi suhu Celsius ke Fahrenheit
f = C.to_fahrenheit()
print("\nFahrenheit = ",f)

# konversi suhu Celsius ke Kelvin
k = C.to_kelvin()
print("Kelvin = ",k) 

# konversi suhu Celsius ke Reamur
r = C.to_reamur()
print("Reamur = ",r)
print("\n|RIFKI PRAMAYANDI MAHESA|") 
print("|      210511156        |") 
print("|       KELAS D         |") 
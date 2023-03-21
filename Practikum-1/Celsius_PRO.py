class Celsius :
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def to_reamur(celsius):
        return celsius * 4/5

    def to_kelvin(celsius):
        return celsius + 273.15

print("|   CONVERTER  CELSIUS_PRO  |\n") 

# Memanggil metode statis to_fahrenheit() di dalam class Celsius
print("Fahrenheit = ",Celsius.to_fahrenheit(13))

# Memanggil metode statis to_reamur() di dalam class Celsius
print("Reamur = ",Celsius.to_reamur(13))

# Memanggil metode statis to_kelvin() di dalam class Celsius
print("Kelvin = ",Celsius.to_kelvin(13))

print("\n|  RIFKI PRAMAYANDI MAHESA  |") 
print("|        210511156          |") 
print("|         KELAS D           |") 
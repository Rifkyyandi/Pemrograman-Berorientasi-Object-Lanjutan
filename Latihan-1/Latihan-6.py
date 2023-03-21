class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y

# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(7, 11)) # Output: 18
print(Kalkulator.subtract(2, 17)) # Output: -15

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(14, 17)) # Output: 238
print(Kalkulator.divide(1, 3)) # Output: 0.3333333333333333

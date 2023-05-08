# Contoh 1: Mengakses variabel lokal sebelum diinisialisasi
def my_function():
    print(x)
    x = 5

my_function()

# Output:
# UnboundLocalError: local variable 'x' referenced before assignment


# Contoh 2: Mengubah variabel lokal di luar lingkup variabel tersebut
def my_function():
    x = 5

    def inner_function():
        x += 10

    inner_function()

    print(x)

my_function()

# Output:
# UnboundLocalError: local variable 'x' referenced before assignment

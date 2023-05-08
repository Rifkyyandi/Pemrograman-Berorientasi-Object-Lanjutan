# Contoh 1: Ukuran stack melebihi batas
def recursive_function():
    recursive_function()

recursive_function()

# Output:
# SystemError: stack overflow


# Contoh 2: Terjadi kesalahan internal pada interpreter
print(2 ** 1000000000)

# Output:
# SystemError: error return without exception set

# Contoh 1: Menggunakan spasi dan tab untuk indentasi
def my_function():
    if True:
        print("Hello, world!")
          print("Indentasi tidak tepat")

my_function()

# Output:
# TabError: inconsistent use of tabs and spaces in indentation


# Contoh 2: Menggunakan jumlah spasi yang salah untuk indentasi
def my_function():
    if True:
        print("Hello, world!")
       print("Indentasi tidak tepat")

my_function()

# Output:
# IndentationError: unexpected indent

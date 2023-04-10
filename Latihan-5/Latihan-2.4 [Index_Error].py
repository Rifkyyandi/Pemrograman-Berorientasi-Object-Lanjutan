list_angka = [1, 2, 3]

try:
    value = list_angka[4]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")

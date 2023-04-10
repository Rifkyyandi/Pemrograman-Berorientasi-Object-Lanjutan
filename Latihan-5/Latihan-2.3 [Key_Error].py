dictionary = {"satu": 1, "dua": 2, "tiga": 3}

try:
    value = dictionary["empat"]
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")
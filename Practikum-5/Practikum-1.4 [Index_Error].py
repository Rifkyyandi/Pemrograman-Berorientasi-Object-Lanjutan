try:
    my_list = [1, 2, 3]
    value = my_list[3]
    print(value)

except IndexError:
    print("IndexError: Index out of range")

try:
    my_list = [0] * 10000000000000000000
    print(my_list)
    
except MemoryError:
    print("MemoryError: Not enough memory to create list")

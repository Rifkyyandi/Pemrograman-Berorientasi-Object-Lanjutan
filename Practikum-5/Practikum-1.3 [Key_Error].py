try:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    value = my_dict['d']
    print(value)
    
except KeyError:
    print("KeyError: Key not found in dictionary")

try:
    my_str = 'hello'
    value = int(my_str)
    print(value)
    
except ValueError:
    print("ValueError: Cannot convert 'hello' to int")

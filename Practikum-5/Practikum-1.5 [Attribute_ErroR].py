try:
    my_str = 'Hello, world!'
    value = my_str.uppercase()
    print(value)
    
except AttributeError:
    print("AttributeError: 'str' object has no attribute 'uppercase'")

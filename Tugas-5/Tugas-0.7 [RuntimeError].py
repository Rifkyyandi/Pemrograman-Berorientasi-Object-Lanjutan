def divide_numbers(a, b):
    if b == 0:
        raise RuntimeError("Cannot divide by zero!")
    return a / b

result = divide_numbers(10, 0) # raises RuntimeError: Cannot divide by zero!

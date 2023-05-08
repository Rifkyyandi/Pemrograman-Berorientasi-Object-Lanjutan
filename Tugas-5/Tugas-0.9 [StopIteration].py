my_list = [1, 2, 3]
my_iterator = iter(my_list)

while True:
    try:
        item = next(my_iterator)
        print(item)
    except StopIteration:
        break

# prints 1, 2, 3

try:
    with open('file.txt', 'r') as file:
        contents = file.read()
        print(contents)
        
except FileNotFoundError:
    print("FileNotFoundError: File not found")

try:
    with open('file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("File operation complete")
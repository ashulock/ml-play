try:
    with open('output.txt', 'w') as file:
        file.write(input("Enter text to save: "))
except IOError:
    print("Error: Could not write to file!")
word = input("Enter word to search: ")
line_num = 1
with open('multi.txt', 'r') as file:
    for line in file:
        if word in line:
            print(f"Found at line {line_num}")
        line_num += 1
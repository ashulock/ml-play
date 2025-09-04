word = input("Enter word to search: ")
line_num = 0
with open('multi.txt', 'r') as file:
    for line in file:
        line_num += 1
        if word.lower() in line.lower():
            print(f"Line {line_num}")
numbers = [10, 20, 30, 40, 50]
with open('numbers.txt', 'w') as file:
    for num in numbers:
        file.write(str(num) + '\n')

with open('numbers.txt', 'r') as file:
    num_list = [int(line.strip()) for line in file]
    print(num_list)
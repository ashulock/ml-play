
with open('multi.txt', 'w') as file:
    file.write("swayam\npravu\nturung")

with open('multi.txt', 'r') as file:
    for line in file:
        print(line.strip())
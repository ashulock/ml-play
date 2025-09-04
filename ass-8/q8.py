with open('multi.txt', 'r') as file:
    words = sum(len(line.split()) for line in file)
    print(f"Number of words: {words}")
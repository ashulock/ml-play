with open('multi.txt', 'r') as file:
    lines = file.readlines()
    words = sum(len(line.split()) for line in lines)
    chars = sum(len(line) for line in lines)
    print(f"Lines: {len(lines)}, Words: {words}, Chars: {chars}")
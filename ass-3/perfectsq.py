def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n

# Test
num = int(input("Enter a number: "))
print(is_perfect_square(num))
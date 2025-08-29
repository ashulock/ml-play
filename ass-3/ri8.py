def get_nth_digit(num, n):
    return (abs(num) // (10 ** (n - 1))) % 10

# Test
number = int(input("Enter a number: "))
n = int(input("Enter n: "))
print(get_nth_digit(number, n))
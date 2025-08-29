n = int(input("Enter n: "))
sum = 0
den = 1
for i in range(1, n + 1):
    sum += i / den
    den += 2
print(sum)
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
m = float(input("Enter m: "))
n = float(input("Enter n: "))

denominator = a*d - b*c
if denominator == 0:
    print("No unique solution (ad - bc = 0)")
else:
    x1 = (m*d - b*n) / denominator
    x2 = (n*a - m*c) / denominator
    print(f"x1 = {x1}, x2 = {x2}")
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers!")
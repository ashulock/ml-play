num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter choice (+, -, *, /): ")

if choice == '+':
    print(num1 + num2)
elif choice == '-':
    print(num1 - num2)
elif choice == '*':
    print(num1 * num2)
elif choice == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")